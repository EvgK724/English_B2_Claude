"""Append one reviewed daily batch with verified speech and no partial publication.

python3 tools/daily_deck.py status phrasal
python3 tools/daily_deck.py append phrasal /path/to/batch.json

Batch: {"date":"YYYY-MM-DD","cards":[{...card fields...,"sources":[
  {"url":"https://...","title":"Checked source", ...optional evidence...}]}]}.
Only today's Asia/Yekaterinburg date is accepted. Sources are saved in the ledger,
not rendered as card fields. Fetch the current main branch before preparing a batch.
This command never commits, pushes, changes schedules, or repairs historical cards.
"""
from __future__ import annotations

import argparse
import asyncio
import contextlib
import datetime as dt
import fcntl
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo

import deck_sync
from ensure_ryan_audio import (STATE_FILE, build_shell, digest, install_changes,
                               json_bytes, load_json, record, slice_bytes)

ROOT = pathlib.Path(__file__).resolve().parent.parent
TIMEZONE = "Asia/Yekaterinburg"
VERSION = "7.3.1"
RATE = "-5%"
# Three attempts in total, only for the service returning no audio.
TTS_RETRY_DELAYS = (2, 4)
CONFIG = {
    "phrasal": {"count": 1, "voice": "en-GB-RyanNeural", "label": "Ryan",
                "fields": ("id", "au", "added", "term", "ipa", "pos", "ru", "note", "ex", "exru")},
    "bbapp": {"count": 2, "voice": "en-US-AndrewNeural", "label": "Andrew",
              "fields": ("id", "au", "added", "term", "who", "reg", "ru", "note", "ex", "exru")},
}


def local_date(now=None):
    return (now or dt.datetime.now(dt.timezone.utc)).astimezone(ZoneInfo(TIMEZONE)).date().isoformat()


def normalized_term(text):
    text = unicodedata.normalize("NFKC", text).casefold()
    text = text.translate(str.maketrans("", "", "'’‘ʼ"))
    return " ".join(re.findall(r"[^\W_]+", text, flags=re.UNICODE))


def batch_digest(batch):
    return digest(json.dumps(batch, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode())


def parse_cards(html):
    if html.count("const CARDS = [") != 1 or html.count(deck_sync.MARK) != 1:
        raise ValueError("Expected one card array and one append marker")
    try:
        deck_sync.check_parsed(html, "current deck")
    except SystemExit as error:
        raise ValueError(str(error)) from error
    cards = [deck_sync.card_object(block) for _, block in deck_sync.card_blocks(html)]
    if len({card["id"] for card in cards}) != len(cards):
        raise ValueError("Current deck contains duplicate card IDs")
    return cards


def card_block(card, key):
    def literal(value):
        # Keep inline JavaScript data safe, even if a source uses HTML-like text.
        return (json.dumps(value, ensure_ascii=False).replace("<", "\\u003c")
                .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))
    lines = [f"    {field}: {literal(card[field])}" for field in CONFIG[key]["fields"]]
    return "  {\n" + ",\n".join(lines) + "\n  },\n"


def validate_batch(key, batch, today):
    if key not in CONFIG:
        raise ValueError("Choose phrasal or bbapp")
    if not isinstance(batch, dict) or set(batch) != {"date", "cards"}:
        raise ValueError("Batch must contain date and cards only")
    if batch["date"] != today:
        raise ValueError(f"Only today's date is allowed: {today} ({TIMEZONE})")
    incoming = batch["cards"]
    if not isinstance(incoming, list) or len(incoming) != CONFIG[key]["count"]:
        raise ValueError(f"{key} requires exactly {CONFIG[key]['count']} cards")
    cards, evidence, ids, terms = [], {}, set(), set()
    required = set(CONFIG[key]["fields"])
    for item in incoming:
        if not isinstance(item, dict) or set(item) != required | {"sources"}:
            raise ValueError(f"Each {key} card must contain {sorted(required)} and sources")
        card = {field: item[field] for field in CONFIG[key]["fields"]}
        for field, value in card.items():
            if field == "au":
                if type(value) is not int or value != 1:
                    raise ValueError("Every new card must have au: 1 and verified recordings")
            elif not isinstance(value, str) or not value.strip() or any(ord(c) < 32 for c in value):
                raise ValueError(f"Card field {field} must be nonempty single-line text")
        cid = card["id"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", cid) or cid in ids:
            raise ValueError(f"Invalid or duplicate card ID: {cid}")
        if card["added"] != today:
            raise ValueError(f"{cid}: added must equal today's date")
        for field in ("term", "ex"):
            if not re.search(r"[A-Za-z]", card[field]) or re.search(r"[А-Яа-яЁё]", card[field]):
                raise ValueError(f"{cid}/{field}: English speech text is required")
        term = normalized_term(card["term"])
        if not term or term in terms:
            raise ValueError(f"Duplicate normalized term: {card['term']}")
        sources = item["sources"]
        if not isinstance(sources, list) or not sources:
            raise ValueError(f"{cid}: at least one checked source is required")
        for source in sources:
            if not isinstance(source, dict) or not isinstance(source.get("url"), str):
                raise ValueError(f"{cid}: source URL is required")
            parsed = urlsplit(source["url"])
            if (parsed.scheme not in ("http", "https") or not parsed.hostname
                    or parsed.username or parsed.password):
                raise ValueError(f"{cid}: source URL must be HTTP(S) without credentials")
            if not isinstance(source.get("title"), str) or not source["title"].strip():
                raise ValueError(f"{cid}: source title is required")
        # Fail before synthesis if optional evidence cannot be serialized.
        json_bytes(sources)
        cards.append(card)
        evidence[cid] = sources
        ids.add(cid)
        terms.add(term)
    return cards, evidence


@contextlib.contextmanager
def repository_lock(root):
    gitdir = root / ".git"
    if not gitdir.is_dir():
        output = subprocess.run(["git", "rev-parse", "--git-common-dir"], cwd=root,
                                check=True, capture_output=True, text=True).stdout.strip()
        gitdir = (root / output).resolve()
    with (gitdir / "daily-deck.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


def status(root, key, *, today=None):
    root = pathlib.Path(root)
    today = today or local_date()
    cards = parse_cards((root / f"site/apps/{key}.html").read_text(encoding="utf-8"))
    current = [card for card in cards if card.get("added") == today]
    ledger_rel = pathlib.Path(f"data/daily/{today}-{key}.json")
    state, problem = "pending", None
    if len(current) == CONFIG[key]["count"]:
        try:
            verify_completed(root, key, current, ledger_rel)
            state = "complete"
        except (OSError, ValueError, KeyError, StopIteration) as error:
            state, problem = "conflict", str(error)
    elif current or (root / ledger_rel).exists():
        state, problem = "conflict", "Partial daily cards or a ledger without matching cards"
    return {"deck": key, "date": today, "timezone": TIMEZONE,
            "state": state, "problem": problem, "ledger_present": (root / ledger_rel).exists(),
            "expected_count": CONFIG[key]["count"], "count_today": len(current),
            "cards_today": current, "existing_terms": [card["term"] for card in cards],
            "latest_added": max((card.get("added", "") for card in cards), default="")}


def synthesize(clips, voice, directory):
    import edge_tts
    if edge_tts.__version__ != VERSION:
        raise RuntimeError(f"edge-tts {VERSION} is required (tools/requirements-audio.txt)")
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is required to verify speech before publication")
    directory.mkdir(parents=True)

    async def generate():
        generated = {}
        for clip in clips:
            path = directory / (clip["key"] + ".part.mp3")
            attempts = len(TTS_RETRY_DELAYS) + 1
            try:
                for attempt in range(1, attempts + 1):
                    # Never let a partial result from one attempt enter the next.
                    path.unlink(missing_ok=True)
                    try:
                        # Communicate instances cannot be reused after streaming.
                        await edge_tts.Communicate(clip["text"], voice, rate=clip["rate"],
                                                   pitch="+0Hz", volume="+0%").save(str(path))
                        if not path.is_file() or not path.stat().st_size:
                            raise edge_tts.exceptions.NoAudioReceived("No audio file was produced")
                        generated[clip["key"]] = path.read_bytes()
                        break
                    except edge_tts.exceptions.NoAudioReceived as error:
                        path.unlink(missing_ok=True)
                        context = (f"clip={clip['key']} voice={voice} rate={clip['rate']} "
                                   f"attempt={attempt}/{attempts} edge-tts={VERSION}")
                        if attempt == attempts:
                            raise RuntimeError(f"Daily speech: {context}: NoAudioReceived; "
                                               "retry limit reached, batch not published") from error
                        delay = TTS_RETRY_DELAYS[attempt - 1]
                        print(f"Daily speech: {context}: NoAudioReceived; retrying in {delay}s",
                              file=sys.stderr, flush=True)
                        await asyncio.sleep(delay)
            finally:
                path.unlink(missing_ok=True)
        return generated

    return asyncio.run(generate())


def validate_audio(path):
    from ryan_tts import validate_audio as validate
    return validate(path)


def verify_completed(root, key, cards, ledger_rel):
    """A retry must not hide a partial/externally damaged prior publication."""
    index = load_json(root / "tools/packs.json")[key]
    pack = (root / f"site/packs/{key}.mp3").read_bytes()
    ledger = load_json(root / ledger_rel) if (root / ledger_rel).exists() else None
    if ledger is not None:
        saved_cards = [{field: card[field] for field in CONFIG[key]["fields"]} for card in ledger["cards"]]
        if ({c["id"]: c for c in saved_cards} != {c["id"]: c for c in cards}
                or ledger.get("deck") != key or ledger.get("voice") != CONFIG[key]["voice"]
                or ledger.get("date") != cards[0]["added"]
                or ledger.get("batch_sha256") != batch_digest({"date": ledger["date"], "cards": ledger["cards"]})):
            raise ValueError("Completed daily content differs from its ledger")
    catalog = load_json(root / "tools/catalog.json")
    app = next(a for a in catalog["apps"] if a["key"] == key)
    for card in cards:
        if app["ids"].count(card["id"]) != 1:
            raise ValueError("Completed daily cards are missing from the catalog")
        for suffix in ("t", "x"):
            clip_key = f"{card['id']}-{suffix}"
            if clip_key not in index:
                raise ValueError("Completed daily cards have missing audio")
            packed = slice_bytes(pack, index[clip_key], clip_key)
            if ledger is not None:
                metadata = ledger.get("clips", {}).get(clip_key, {})
                if (metadata.get("packed_sha256") != digest(packed)
                        or metadata.get("location") != index[clip_key]):
                    raise ValueError("Completed daily audio differs from its ledger")


def append_batch(root, key, batch, *, today=None, synthesizer=synthesize,
                 validator=validate_audio, trimmer=deck_sync.trim_clip,
                 builder=build_shell):
    root = pathlib.Path(root).resolve()
    today = today or local_date()
    cards, evidence = validate_batch(key, batch, today)
    with repository_lock(root):
        app_rel = pathlib.Path(f"site/apps/{key}.html")
        html = (root / app_rel).read_text(encoding="utf-8")
        old_cards = parse_cards(html)
        current = [card for card in old_cards if card.get("added") == today]
        ledger_rel = pathlib.Path(f"data/daily/{today}-{key}.json")
        if current:
            if (len(current) == CONFIG[key]["count"]
                    and {c["id"]: c for c in current} == {c["id"]: c for c in cards}):
                verify_completed(root, key, cards, ledger_rel)
                return {"deck": key, "date": today, "status": "already-complete", "changed": []}
            raise ValueError(f"{key}/{today}: partial or conflicting existing daily content; no changes written")
        if (root / ledger_rel).exists():
            raise ValueError("Daily ledger exists without matching cards; inspect before retrying")
        old_ids = {card["id"] for card in old_cards}
        old_terms = {normalized_term(card["term"]) for card in old_cards}
        if any(card["id"] in old_ids or normalized_term(card["term"]) in old_terms for card in cards):
            raise ValueError("A proposed ID or normalized term already exists")
        packs = load_json(root / "tools/packs.json")
        catalog = load_json(root / "tools/catalog.json")
        matching = [a for a in catalog["apps"] if a["key"] == key]
        if len(matching) != 1:
            raise ValueError("Expected one catalog entry")
        app = matching[0]
        if app["ids"] != [c["id"] for c in old_cards] or [c["id"] for c in app["items"]] != app["ids"]:
            raise ValueError("Existing deck and catalog IDs disagree")
        if app.get("voice") != CONFIG[key]["label"]:
            raise ValueError("Existing catalog voice differs from the approved daily voice")
        pack_rel = pathlib.Path(f"site/packs/{key}.mp3")
        pack = (root / pack_rel).read_bytes()
        for clip_key, location in packs[key].items():
            slice_bytes(pack, location, f"{key}/{clip_key}")
        clips = [{"key": f"{card['id']}-{suffix}", "text": card[field], "rate": RATE}
                 for card in cards for suffix, field in (("t", "term"), ("x", "ex"))]
        if any(clip["key"] in packs[key] for clip in clips):
            raise ValueError("Proposed audio key already exists")
        state = None
        if key == "phrasal":
            state = load_json(root / STATE_FILE)
            if (state.get("schema") != 1 or state.get("voice") != CONFIG[key]["voice"]
                    or not isinstance(state.get("apps", {}).get(key, {}).get("clips"), dict)):
                raise ValueError("Valid existing Ryan audio state is required")
            if any(clip["key"] in state["apps"][key]["clips"] for clip in clips):
                raise ValueError("Proposed audio key already exists in Ryan state")
        changes = {}
        ledger = {"schema": 1, "date": today, "timezone": TIMEZONE, "deck": key,
                  "voice": CONFIG[key]["voice"], "rate": RATE, "edge_tts": VERSION,
                  "cards": [{**card, "sources": evidence[card["id"]]} for card in cards],
                  "batch_sha256": batch_digest(batch), "clips": {}}
        with tempfile.TemporaryDirectory(prefix=".daily-stage-", dir=root) as temporary:
            stage = pathlib.Path(temporary)
            generated = synthesizer(clips, CONFIG[key]["voice"], stage / "generated")
            if set(generated) != {clip["key"] for clip in clips}:
                raise ValueError("Generator returned an incomplete or unexpected set of recordings")
            for clip in clips:
                raw = generated[clip["key"]]
                if not isinstance(raw, bytes) or not raw:
                    raise ValueError(f"Missing recording: {clip['key']}")
                validation_path = stage / "validate.mp3"
                validation_path.write_bytes(raw)
                validator(validation_path)
                packed, lead = trimmer(raw)
                validation_path.write_bytes(packed)
                duration = validator(validation_path)
                slice_bytes(packed, [0, len(packed), lead], clip["key"])
                packs[key][clip["key"]] = [len(pack), len(packed), lead]
                pack += packed
                metadata = {"voice": CONFIG[key]["voice"], **clip, "pitch": "+0Hz", "volume": "+0%",
                            "text_sha256": digest(clip["text"].encode()),
                            "raw_sha256": digest(raw), "packed_sha256": digest(packed),
                            "duration": duration, "location": packs[key][clip["key"]]}
                ledger["clips"][clip["key"]] = metadata
                if state is not None:
                    state["apps"][key]["clips"][clip["key"]] = record(
                        clip, packed, source="Microsoft-Edge-TTS", raw=raw, duration=duration)
            addition = "".join(card_block(card, key) for card in cards)
            updated = html.replace(deck_sync.MARK, addition + deck_sync.MARK, 1)
            if parse_cards(updated) != old_cards + cards:
                raise ValueError("Final card preservation check failed")
            for card in cards:
                app["ids"].append(card["id"])
                app["items"].append({"id": card["id"], "term": card["term"],
                                     "ru": deck_sync.short_ru(card["ru"]), "added": today})
                app["kw"] = (app.get("kw", "") + " · " + card["term"]).strip(" ·")
            app["size"] = len(updated.encode())
            changes.update({app_rel: updated.encode(), pack_rel: pack,
                            pathlib.Path("tools/packs.json"): json_bytes(packs),
                            pathlib.Path("tools/catalog.json"): json_bytes(catalog),
                            ledger_rel: json_bytes(ledger, pretty=True)})
            if state is not None:
                changes[STATE_FILE] = json_bytes(state, pretty=True)
            builder(root, stage, changes)
            install_changes(root, changes, stage)
        return {"deck": key, "date": today, "status": "appended", "cards": [c["id"] for c in cards],
                "voice": CONFIG[key]["voice"], "changed": [str(path) for path in changes]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("status", "append"):
        command = commands.add_parser(name)
        command.add_argument("key", choices=CONFIG)
        if name == "append":
            command.add_argument("batch", type=pathlib.Path)
    args = parser.parse_args()
    try:
        if args.command == "status":
            result = status(args.root, args.key)
        else:
            result = append_batch(args.root, args.key, load_json(args.batch))
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if result.get("state") == "conflict":
            parser.exit(1)
    except Exception as error:
        parser.exit(1, f"Daily deck: {error}\n")


if __name__ == "__main__":
    main()
