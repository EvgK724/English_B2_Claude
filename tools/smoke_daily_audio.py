"""Verify the complete daily queue with fresh Ryan and Andrew in an isolated copy.

Run in GitHub Actions only. Successful evidence is reused until speech/queue code
changes; --force repeats the live test. Synthetic cards never enter site/ in the
real checkout. No credentials, new endpoints, proxy changes or TLS overrides.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import pathlib
import re
import shutil
import tempfile
from zoneinfo import ZoneInfo

import daily_deck as daily
import daily_queue as queue
from ensure_ryan_audio import digest, json_bytes, load_json, slice_bytes

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATE = pathlib.Path("tools/speech-smoke-state.json")
SOURCES = (
    "tools/daily_deck.py", "tools/daily_queue.py", "tools/ensure_andrew_audio.py",
    "tools/ensure_ryan_audio.py", "tools/ryan_tts.py", "tools/ryan_manifest.py",
    "tools/audio_clips.mjs", "tools/deck_sync.py", "tools/requirements-audio.txt",
    "tools/mk_shell.py", "tools/reference/lossless.py", "tools/reference/audio.py",
    "tools/smoke_daily_audio.py", ".github/workflows/ryan-pages.yml",
)


def source_digest(root):
    return digest(json_bytes({name: digest((root / name).read_bytes()) for name in SOURCES}))


def fingerprint(root):
    return {str(p.relative_to(root)): digest(p.read_bytes())
            for folder in ("site", "tools", "data") for p in (root / folder).rglob("*")
            if p.is_file() and "__pycache__" not in p.parts and p.relative_to(root) != STATE}


def valid_evidence(value, source_sha):
    if not isinstance(value, dict) or value.get("schema") != 1 or value.get("source_sha256") != source_sha:
        return False
    if value.get("executor") != "GitHub Actions" or not str(value.get("run_id", "")).isdigit():
        return False
    if (value.get("queue_roundtrip") != "passed" or value.get("retry") != "no-op"
            or value.get("source_tree_unchanged") is not True):
        return False
    decks = value.get("decks")
    if not isinstance(decks, dict) or set(decks) != set(daily.CONFIG):
        return False
    for key, config in daily.CONFIG.items():
        deck = decks[key]
        if not isinstance(deck, dict) or deck.get("voice") != config["voice"]:
            return False
        clips = deck.get("clips")
        if not isinstance(clips, dict) or len(clips) != config["count"] * 2:
            return False
        for clip in clips.values():
            if not isinstance(clip, dict):
                return False
            duration = clip.get("duration")
            if (clip.get("voice") != config["voice"] or type(duration) not in (int, float)
                    or not math.isfinite(duration) or duration <= 0.1
                    or any(not re.fullmatch(r"[0-9a-f]{64}", str(clip.get(field, "")))
                           for field in ("packed_sha256", "raw_sha256"))):
                return False
    return True


def smoke_batch(key, date):
    cards = []
    for number in range(daily.CONFIG[key]["count"]):
        card = {"id": f"ci-unpublished-{key}-{number}", "au": 1, "added": date,
                "term": f"This is unpublished speech test number {number + 1} for {key}.",
                "ru": "Непубликуемая тестовая карточка", "note": "Техническая проверка в изолированной копии.",
                "ex": "Let's go over the plan before we start.", "exru": "Обсудим план перед началом.",
                "sources": [{"url": "https://github.com/EvgK724/English_B2_Claude",
                             "title": "Original CI fixture, not a quotation or teaching material"}]}
        card.update({"ipa": "/test/", "pos": "CI fixture"} if key == "phrasal"
                    else {"who": "Original test fixture, not Breaking Bad dialogue", "reg": "CI fixture"})
        cards.append(card)
    return {"date": date, "cards": cards}


def run(root=ROOT, *, force=False, check=False):
    root = pathlib.Path(root).resolve()
    source_sha = source_digest(root)
    previous = load_json(root / STATE) if (root / STATE).exists() else None
    if valid_evidence(previous, source_sha) and not force:
        return {"status": "verified-evidence-current", "run_id": previous["run_id"], "source_sha256": source_sha}
    if check:
        raise ValueError("Fresh GitHub Actions speech/queue verification is required for this code")
    if os.environ.get("GITHUB_ACTIONS") != "true" or not os.environ.get("GITHUB_RUN_ID", "").isdigit():
        raise ValueError("Real daily speech verification runs only in the authorized GitHub Actions workflow")
    before = fingerprint(root)
    evidence = {"schema": 1, "executor": "GitHub Actions", "run_id": os.environ["GITHUB_RUN_ID"],
                "verified_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                "source_sha256": source_sha, "decks": {}}
    with tempfile.TemporaryDirectory(prefix="english-daily-smoke-") as temporary:
        shadow = pathlib.Path(temporary)
        for folder in ("site", "tools", "data"):
            if (root / folder).exists():
                shutil.copytree(root / folder, shadow / folder,
                                ignore=shutil.ignore_patterns("__pycache__"))
        (shadow / ".git").mkdir()
        # Test requests are isolated from any genuine outstanding requests. Their
        # original counterpart and every production file are fingerprinted above.
        shutil.rmtree(shadow / "data/requests", ignore_errors=True)
        latest = max([daily.local_date()] + [card.get("added", "")
                     for key in daily.CONFIG for card in daily.parse_cards(
                         (shadow / f"site/apps/{key}.html").read_text())])
        future = dt.date.fromisoformat(latest) + dt.timedelta(days=1)
        now = dt.datetime.combine(future, dt.time(12), tzinfo=ZoneInfo(daily.TIMEZONE))
        for key in daily.CONFIG:
            queue.prepare_queue(shadow, key, smoke_batch(key, future.isoformat()), now=now)
        queue.process_queue(shadow, now=now)
        queue.verify_queue(shadow, now=now, require_complete=True)
        for key in daily.CONFIG:
            ledger = load_json(shadow / f"data/daily/{future}-{key}.json")
            pack = (shadow / f"site/packs/{key}.mp3").read_bytes()
            for clip_key, metadata in ledger["clips"].items():
                data = slice_bytes(pack, metadata["location"], clip_key)
                path = shadow / f"{clip_key}.mp3"
                path.write_bytes(data)
                duration = daily.validate_audio(path)
                if duration <= 0.1 or digest(data) != metadata["packed_sha256"]:
                    raise ValueError("Smoke recording differs from its verified ledger")
            evidence["decks"][key] = {"voice": daily.CONFIG[key]["voice"], "clips": ledger["clips"]}
        ready = fingerprint(shadow)
        queue.process_queue(shadow, now=now)
        if fingerprint(shadow) != ready:
            raise ValueError("Queue retry changed already-complete daily content")
    if fingerprint(root) != before:
        raise ValueError("Isolated speech test changed production files")
    evidence.update(queue_roundtrip="passed", retry="no-op", source_tree_unchanged=True)
    if not valid_evidence(evidence, source_sha):
        raise ValueError("Incomplete speech verification evidence")
    (root / STATE).write_bytes(json_bytes(evidence, pretty=True))
    return {"status": "fresh-speech-queue-passed", "run_id": evidence["run_id"],
            "voices": {key: cfg["voice"] for key, cfg in daily.CONFIG.items()},
            "new_recordings": 6, "source_sha256": source_sha,
            "queue_roundtrip": "passed", "retry": "no-op", "source_tree_unchanged": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        print(json.dumps(run(force=args.force, check=args.check), ensure_ascii=False))
    except Exception as error:
        parser.exit(1, f"Daily speech smoke: {error}\n")


if __name__ == "__main__":
    main()
