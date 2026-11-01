"""Verify Breaking Bad separately from Ryan and repair only approved missing clips.

The committed baseline fingerprints the existing Andrew corpus without claiming
that its historical synthesis parameters were independently recovered. Eight
explicitly approved missing clips are marked pending. New daily recordings are
adopted only from a matching, fully verified daily ledger. Unknown or damaged
recordings stop publication instead of being silently trusted or replaced.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import pathlib
import re
import tempfile

import daily_deck as daily
from ensure_ryan_audio import (build_shell, digest, install_changes, json_bytes,
                               load_json, phrasal_html, slice_bytes)

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATE_FILE = pathlib.Path("tools/andrew-audio-state.json")
KEY = "bbapp"
VOICE = "en-US-AndrewNeural"
RATE = "-5%"
SCHEMA = 1


def identity(clip):
    return {"voice": VOICE, "text": clip["text"], "rate": RATE,
            "pitch": "+0Hz", "volume": "+0%"}


def signature(clip):
    return digest(json.dumps(identity(clip), sort_keys=True, ensure_ascii=False).encode())


def clip_specs(cards):
    return [{"key": f"{card['id']}-{suffix}", "text": card[field], "rate": RATE}
            for card in cards for suffix, field in (("t", "term"), ("x", "ex"))]


def read_deck(root):
    html = (root / "site/apps/bbapp.html").read_text(encoding="utf-8")
    cards = daily.parse_cards(html)
    catalog = load_json(root / "tools/catalog.json")
    entries = [app for app in catalog["apps"] if app["key"] == KEY]
    if len(entries) != 1:
        raise ValueError("Expected one Breaking Bad catalog entry")
    app = entries[0]
    ids = [card["id"] for card in cards]
    if (app.get("voice") != "Andrew" or app["ids"] != ids
            or [item["id"] for item in app["items"]] != ids):
        raise ValueError("Breaking Bad catalog voice or card IDs disagree")
    clips = clip_specs(cards)
    if len({clip["key"] for clip in clips}) != len(clips):
        raise ValueError("Duplicate Breaking Bad audio keys")
    packs = load_json(root / "tools/packs.json")
    pack = (root / "site/packs/bbapp.mp3").read_bytes()
    for key, location in packs[KEY].items():
        slice_bytes(pack, location, f"{KEY}/{key}")
    return html, cards, clips, catalog, app, packs, pack


def ledger_records(root, cards, clips, index, pack):
    """Trust new recordings only when content, identity and byte hashes agree."""
    by_id = {card["id"]: card for card in cards}
    specs = {clip["key"]: clip for clip in clips}
    records = {}
    for path in sorted((root / "data/daily").glob("*-bbapp.json")):
        ledger = load_json(path)
        date = ledger.get("date")
        if (ledger.get("schema") != 1 or not isinstance(date, str)
                or path.name != f"{date}-bbapp.json"
                or ledger.get("timezone") != daily.TIMEZONE
                or ledger.get("edge_tts") != daily.VERSION
                or ledger.get("rate") != RATE
                or ledger.get("voice") != VOICE):
            raise ValueError(f"Invalid Andrew daily ledger: {path.name}")
        saved = ledger.get("cards")
        if not isinstance(saved, list) or len(saved) != daily.CONFIG[KEY]["count"]:
            raise ValueError(f"Invalid Andrew daily card count: {path.name}")
        daily.validate_batch(KEY, {"date": date, "cards": saved}, date)
        actual = [by_id.get(card.get("id")) for card in saved]
        if any(card is None for card in actual):
            raise ValueError(f"Andrew ledger contains absent cards: {path.name}")
        daily.verify_completed(root, KEY, actual, path.relative_to(root))
        expected_keys = {clip["key"] for clip in clip_specs(actual)}
        if set(ledger.get("clips", {})) != expected_keys:
            raise ValueError(f"Incomplete Andrew ledger clips: {path.name}")
        for key, metadata in ledger["clips"].items():
            clip = specs[key]
            packed = slice_bytes(pack, index[key], key)
            if (key in records or any(metadata.get(k) != v for k, v in identity(clip).items())
                    or metadata.get("key") != key
                    or metadata.get("text_sha256") != digest(clip["text"].encode())
                    or metadata.get("packed_sha256") != digest(packed)
                    or metadata.get("location") != index[key]
                    or not isinstance(metadata.get("duration"), (int, float))
                    or not math.isfinite(metadata["duration"]) or metadata["duration"] < 0.1
                    or not re.fullmatch(r"[0-9a-f]{64}", str(metadata.get("raw_sha256", "")))):
                raise ValueError(f"Andrew ledger identity or audio mismatch: {key}")
            records[key] = {**metadata, "signature": signature(clip),
                            "source": "Microsoft-Edge-TTS", "edge_tts": daily.VERSION,
                            "ledger": str(path.relative_to(root))}
    return records


def reviewed_baseline(root, approved_missing, *, source_commit):
    """Build the one-time reviewed baseline; never called by ordinary CI."""
    root = pathlib.Path(root)
    _, cards, clips, _, _, packs, pack = read_deck(root)
    specs = {clip["key"]: clip for clip in clips}
    index = packs[KEY]
    missing = set(specs) - set(index)
    if missing != set(approved_missing) or set(index) - set(specs):
        raise ValueError("Reviewed baseline gaps differ from the explicitly approved repair")
    ledgers = ledger_records(root, cards, clips, index, pack)
    state = {"schema": SCHEMA, "voice": VOICE, "deck": KEY,
             "baseline_source_commit": source_commit,
             "baseline_note": "Existing Andrew bytes are preserved. Historical synthesis parameters and exact voice variant were not independently recovered.",
             "clips": {}}
    for clip in clips:
        key = clip["key"]
        if key in ledgers:
            state["clips"][key] = ledgers[key]
        elif key in missing:
            state["clips"][key] = {**identity(clip), "signature": signature(clip),
                                   "source": "approved-missing-recording", "pending": True}
        else:
            state["clips"][key] = {**identity(clip), "signature": signature(clip),
                                   "text_sha256": digest(clip["text"].encode()),
                                   "packed_sha256": digest(slice_bytes(pack, index[key], key)),
                                   "location": index[key],
                                   "source": "reviewed-existing-Andrew-baseline",
                                   "baseline_parameters_verified": False}
    return state


def ensure_audio(root, *, check=False, synthesizer=daily.synthesize,
                 validator=daily.validate_audio, trimmer=daily.deck_sync.trim_clip,
                 builder=build_shell):
    root = pathlib.Path(root).resolve()
    with daily.repository_lock(root):
        html, cards, clips, catalog, app, packs, pack = read_deck(root)
        state = load_json(root / STATE_FILE)
        if (state.get("schema") != SCHEMA or state.get("voice") != VOICE
                or state.get("deck") != KEY or not isinstance(state.get("clips"), dict)):
            raise ValueError("Valid reviewed Andrew state is required")
        state = copy.deepcopy(state)
        original_state = copy.deepcopy(state)
        specs = {clip["key"]: clip for clip in clips}
        if set(state["clips"]) - set(specs) or set(packs[KEY]) - set(specs):
            raise ValueError("Unexpected Andrew state or audio keys; inspect before publication")
        ledgers = ledger_records(root, cards, clips, packs[KEY], pack)
        jobs, adopted = [], []
        for clip in clips:
            key = clip["key"]
            saved = state["clips"].get(key)
            if saved is None:
                if key not in ledgers:
                    raise ValueError(f"Unreviewed Andrew recording: {key}")
                saved = state["clips"][key] = ledgers[key]
                adopted.append(key)
            if (not isinstance(saved, dict) or saved.get("signature") != signature(clip)
                    or any(saved.get(k) != v for k, v in identity(clip).items())):
                raise ValueError(f"Andrew text or voice differs from its approved state: {key}")
            if saved.get("pending") is True:
                if saved.get("source") != "approved-missing-recording" or key in packs[KEY]:
                    raise ValueError(f"Approved Andrew repair is inconsistent: {key}")
                jobs.append(clip)
                continue
            if key not in packs[KEY]:
                raise ValueError(f"Previously verified Andrew recording is missing: {key}")
            if saved.get("source") == "Microsoft-Edge-TTS":
                if (not isinstance(saved.get("duration"), (int, float))
                        or not math.isfinite(saved["duration"]) or saved["duration"] < 0.1
                        or saved.get("edge_tts") != daily.VERSION
                        or not re.fullmatch(r"[0-9a-f]{64}", str(saved.get("raw_sha256", "")))):
                    raise ValueError(f"Incomplete Andrew synthesis provenance: {key}")
            elif (saved.get("source") != "reviewed-existing-Andrew-baseline"
                    or saved.get("baseline_parameters_verified") is not False):
                raise ValueError(f"Unknown Andrew recording provenance: {key}")
            packed = slice_bytes(pack, packs[KEY][key], key)
            if (saved.get("packed_sha256") != digest(packed)
                    or saved.get("location") != packs[KEY][key]
                    or saved.get("text_sha256") != digest(clip["text"].encode())):
                raise ValueError(f"Andrew audio differs from its approved state: {key}")
            if key in ledgers and any(saved.get(field) != ledgers[key].get(field)
                                      for field in ("packed_sha256", "location", "signature")):
                raise ValueError(f"Andrew state differs from its daily ledger: {key}")
        flags = sum(card.get("au") != 1 for card in cards)
        report = {"deck": KEY, "voice": VOICE, "cards": len(cards), "clips": len(clips),
                  "generate": len(jobs), "adopt": len(adopted), "audio_flags": flags}
        if check:
            if jobs or flags or adopted:
                raise ValueError(f"Andrew audio is not ready: {len(jobs)} approved missing clips, "
                                 f"{flags} pending flags, {len(adopted)} ledger records to adopt")
            return {**report, "changed": []}
        changes = {}
        with tempfile.TemporaryDirectory(prefix=".andrew-stage-", dir=root) as temporary:
            stage = pathlib.Path(temporary)
            generated = synthesizer(jobs, VOICE, stage / "generated") if jobs else {}
            if set(generated) != {clip["key"] for clip in jobs}:
                raise ValueError("Andrew generator returned incomplete or unexpected recordings")
            for clip in jobs:
                key, raw = clip["key"], generated[clip["key"]]
                if not isinstance(raw, bytes) or not raw:
                    raise ValueError(f"Missing Andrew recording: {key}")
                validation_path = stage / "validate.mp3"
                validation_path.write_bytes(raw)
                validator(validation_path)
                packed, lead = trimmer(raw)
                validation_path.write_bytes(packed)
                duration = validator(validation_path)
                slice_bytes(packed, [0, len(packed), lead], key)
                location = [len(pack), len(packed), lead]
                packs[KEY][key] = location
                pack += packed
                state["clips"][key] = {**identity(clip), "key": key,
                    "signature": signature(clip), "text_sha256": digest(clip["text"].encode()),
                    "raw_sha256": digest(raw), "packed_sha256": digest(packed),
                    "location": location, "duration": duration, "edge_tts": daily.VERSION,
                    "source": "Microsoft-Edge-TTS"}
            for clip in clips:
                key = clip["key"]
                if (state["clips"][key].get("pending")
                        or state["clips"][key]["packed_sha256"] != digest(slice_bytes(pack, packs[KEY][key], key))):
                    raise ValueError(f"Final Andrew coverage check failed: {key}")
            updated = phrasal_html(root, KEY, {"audio_flags": cards}, packs[KEY])
            if updated is not None:
                expected = [{**card, "au": 1} for card in cards]
                if daily.parse_cards(updated.decode()) != expected:
                    raise ValueError("Andrew repair changed card content beyond audio flags")
                changes[pathlib.Path("site/apps/bbapp.html")] = updated
                app["size"] = len(updated)
                changes[pathlib.Path("tools/catalog.json")] = json_bytes(catalog)
            if jobs:
                changes[pathlib.Path("site/packs/bbapp.mp3")] = pack
                changes[pathlib.Path("tools/packs.json")] = json_bytes(packs)
            if state != original_state:
                changes[STATE_FILE] = json_bytes(state, pretty=True)
            if changes:
                builder(root, stage, changes)
            install_changes(root, changes, stage)
        return {**report, "changed": [str(path) for path in changes]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        print(json.dumps(ensure_audio(args.root, check=args.check), ensure_ascii=False))
    except Exception as error:
        parser.exit(1, f"Andrew audio: {error}\n")


if __name__ == "__main__":
    main()
