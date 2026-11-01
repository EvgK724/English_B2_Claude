"""Prepare reviewed daily JSON without TTS; process it only in the publishing job.

status/prepare use only the Python standard library and never alter published files.
process stages every queued batch before installing one validated output bundle.
Requests are immutable receipts: keep them after their matching daily ledger exists.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import shutil
import tempfile

import daily_deck as daily

REQUESTS = pathlib.Path("data/requests")
FIELDS = {"schema", "deck", "submitted_at", "batch", "batch_sha256"}
NAME = re.compile(r"(\d{4}-\d{2}-\d{2})-(phrasal|bbapp)\.json")


def date_value(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("Expected an ISO date YYYY-MM-DD")
    if dt.date.fromisoformat(value).isoformat() != value:
        raise ValueError("Noncanonical date")
    return value


def clock(now=None, today=None):
    if now is None:
        now = (dt.datetime.combine(dt.date.fromisoformat(date_value(today)), dt.time(12), dt.timezone.utc)
               if today is not None else dt.datetime.now(dt.timezone.utc))
    if now.tzinfo is None or now.utcoffset() is None:
        raise ValueError("An aware timestamp is required")
    now = now.astimezone(dt.timezone.utc)
    if today is not None and date_value(today) != daily.local_date(now):
        raise ValueError("Timestamp and local date disagree")
    return now


def read_json(path):
    def invalid(value):
        raise ValueError(f"Non-finite JSON number: {value}")
    if path.is_symlink():
        raise ValueError(f"Symlink not allowed: {path.name}")
    return json.loads(path.read_text(encoding="utf-8"), parse_constant=invalid)


def request_path(key, date):
    if key not in daily.CONFIG:
        raise ValueError("Choose phrasal or bbapp")
    return REQUESTS / f"{date_value(date)}-{key}.json"


def request_files(root):
    directory = root / REQUESTS
    if (root / "data").is_symlink() or directory.is_symlink():
        raise ValueError("Request directory must not be a symlink")
    if not directory.exists():
        return []
    files = sorted(directory.rglob("*.json"))
    if any(path.parent != directory or path.is_symlink() for path in files):
        raise ValueError("Requests must be regular JSON files directly in data/requests")
    return files


def validate_request(path, value, now):
    if not isinstance(value, dict) or set(value) != FIELDS or type(value["schema"]) is not int or value["schema"] != 1:
        raise ValueError(f"Invalid request envelope: {path.name}")
    # JSON validation also rejects NaN/Infinity in optional source evidence.
    json.dumps(value, allow_nan=False)
    key, batch = value["deck"], value["batch"]
    if not isinstance(batch, dict):
        raise ValueError("Request batch must be an object")
    date = date_value(batch.get("date"))
    if path.name != request_path(key, date).name or not NAME.fullmatch(path.name):
        raise ValueError("Request filename, deck and date disagree")
    submitted = value["submitted_at"]
    if not isinstance(submitted, str) or not submitted.endswith("Z"):
        raise ValueError("submitted_at must be an explicit UTC timestamp ending in Z")
    submitted = dt.datetime.fromisoformat(submitted[:-1] + "+00:00")
    if submitted.utcoffset() != dt.timedelta(0) or submitted > now:
        raise ValueError("Request submission is not UTC or is in the future")
    if daily.local_date(submitted) != date or date > daily.local_date(now):
        raise ValueError("A request must be submitted on its own Yekaterinburg date")
    cards, _ = daily.validate_batch(key, batch, date)
    if value["batch_sha256"] != daily.batch_digest(batch):
        raise ValueError("Request batch hash differs from its content")
    return cards


def new_cards(root, key, cards):
    old = daily.parse_cards((root / f"site/apps/{key}.html").read_text(encoding="utf-8"))
    ids = {card["id"] for card in old}
    terms = {daily.normalized_term(card["term"]) for card in old}
    if any(card["id"] in ids or daily.normalized_term(card["term"]) in terms for card in cards):
        raise ValueError("A proposed ID or normalized term already exists")
    catalog = daily.load_json(root / "tools/catalog.json")
    entries = [app for app in catalog["apps"] if app["key"] == key]
    if (len(entries) != 1 or entries[0]["ids"] != [card["id"] for card in old]
            or [card["id"] for card in entries[0]["items"]] != entries[0]["ids"]
            or entries[0].get("voice") != daily.CONFIG[key]["label"]):
        raise ValueError("Published deck, catalog IDs or voice disagree")


def verify_ledgers(root, now):
    directory = root / "data/daily"
    if (root / "data").is_symlink() or directory.is_symlink():
        raise ValueError("Daily ledger directory must not be a symlink")
    count = 0
    for path in sorted(directory.glob("*.json")):
        match = NAME.fullmatch(path.name)
        if not match:
            raise ValueError(f"Unexpected daily ledger filename: {path.name}")
        date, key = match.groups()
        date_value(date)
        if date > daily.local_date(now):
            raise ValueError("A daily ledger is dated in the future")
        ledger = read_json(path)
        cards, _ = daily.validate_batch(key, {"date": date, "cards": ledger["cards"]}, date)
        if ledger.get("date") != date or ledger.get("deck") != key:
            raise ValueError("Ledger filename and identity disagree")
        result = daily.status(root, key, today=date)
        if result["state"] != "complete" or result["cards_today"] != cards:
            raise ValueError(f"Invalid daily ledger {path.name}: {result.get('problem') or 'card mismatch'}")
        count += 1
    return count


def inspect_queue(root, now):
    records, pending = [], {}
    for path in request_files(root):
        request = read_json(path)
        cards = validate_request(path, request, now)
        key, date = request["deck"], request["batch"]["date"]
        result = daily.status(root, key, today=date)
        if result["state"] == "conflict":
            raise ValueError(f"{path.name}: {result['problem']}")
        if result["state"] == "complete":
            ledger_path = root / f"data/daily/{date}-{key}.json"
            if not ledger_path.exists():
                raise ValueError(f"{path.name}: queued content needs its matching daily ledger")
            ledger = read_json(ledger_path)
            if (ledger.get("batch_sha256") != request["batch_sha256"]
                    or ledger.get("cards") != request["batch"]["cards"]):
                raise ValueError(f"{path.name}: immutable request differs from completed ledger")
            state = "complete"
        else:
            new_cards(root, key, cards)
            if key in pending:
                raise ValueError(f"More than one outstanding request for {key}; inspect instead of backfilling")
            pending[key] = request
            state = "queued"
        records.append({"path": str(path.relative_to(root)), "deck": key, "date": date,
                        "state": state, "batch_sha256": request["batch_sha256"], "request": request})
    return records


def verify_queue(root, *, now=None, today=None, require_complete=False):
    root, now = pathlib.Path(root).resolve(), clock(now, today)
    ledgers = verify_ledgers(root, now)
    records = inspect_queue(root, now)
    pending = [row for row in records if row["state"] == "queued"]
    if require_complete and pending:
        raise ValueError("Publication blocked: daily requests remain queued")
    return {"status": "ready" if not pending else "queued", "ledgers": ledgers,
            "requests": [{k: v for k, v in row.items() if k != "request"} for row in records],
            "pending": len(pending)}


def queue_status(root, key, *, now=None):
    root, now = pathlib.Path(root).resolve(), clock(now)
    if key not in daily.CONFIG:
        raise ValueError("Choose phrasal or bbapp")
    result = daily.status(root, key, today=daily.local_date(now))
    try:
        verification = verify_queue(root, now=now)
        outstanding = [row for row in verification["requests"] if row["deck"] == key and row["state"] == "queued"]
        result["requests"] = [row for row in verification["requests"] if row["deck"] == key]
        if outstanding and result["state"] != "conflict":
            result.update(state="queued", queued_date=outstanding[0]["date"], request=outstanding[0]["path"])
    except (OSError, ValueError, KeyError, TypeError, StopIteration) as error:
        result.update(state="conflict", problem=str(error))
    return result


def prepare_queue(root, key, batch, *, now=None):
    root, fixed_now = pathlib.Path(root).resolve(), now
    json.dumps(batch, allow_nan=False)
    with daily.repository_lock(root):
        # A long-running audio job can hold this lock across local midnight.
        # Submission time is measured after acquiring it, not before waiting.
        now = clock(fixed_now)
        date = daily.local_date(now)
        cards, _ = daily.validate_batch(key, batch, date)
        rel = request_path(key, date)
        records = inspect_queue(root, now)
        verify_ledgers(root, now)
        existing = next((row for row in records if row["path"] == str(rel)), None)
        if existing:
            if existing["request"]["batch"] != batch:
                raise ValueError("A different immutable request already exists for this deck and date")
            return {"status": "already-complete" if existing["state"] == "complete" else "already-queued",
                    "deck": key, "date": date, "request": str(rel), "changed": []}
        outstanding = [row for row in records if row["deck"] == key and row["state"] == "queued"]
        if outstanding:
            raise ValueError(f"{key} already has an outstanding request for {outstanding[0]['date']}; wait for it")
        result = daily.status(root, key, today=date)
        if result["state"] == "complete":
            return {"status": "already-complete", "deck": key, "date": date, "changed": []}
        if result["state"] != "pending":
            raise ValueError(f"Cannot queue partial or conflicting daily content: {result['problem']}")
        new_cards(root, key, cards)
        submitted = clock(fixed_now)
        if daily.local_date(submitted) != date:
            raise ValueError("Local date changed during preparation; prepare a new current-day batch")
        envelope = {"schema": 1, "deck": key, "submitted_at": submitted.isoformat().replace("+00:00", "Z"),
                    "batch": batch, "batch_sha256": daily.batch_digest(batch)}
        destination = root / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        # Linking the completely written file is atomic and exclusive, including
        # against an unrelated writer that ignores our lock. Never expose half JSON.
        with tempfile.TemporaryDirectory(prefix=".request-stage-", dir=root) as temporary:
            prepared = pathlib.Path(temporary) / "request.json"
            prepared.write_text(json.dumps(envelope, ensure_ascii=False, sort_keys=True,
                                            indent=2, allow_nan=False) + "\n", encoding="utf-8")
            if daily.local_date(clock(fixed_now)) != date:
                raise ValueError("Local date changed before submission; prepare a new current-day batch")
            os.link(prepared, destination)
        return {"status": "queued", "deck": key, "date": date, "request": str(rel), "changed": [str(rel)]}


def tree_hashes(root):
    result = {}
    for folder in ("site", "tools", "data"):
        if (root / folder).is_symlink():
            raise ValueError(f"Symlink not supported in publication inputs: {folder}")
        for path in (root / folder).rglob("*"):
            rel = path.relative_to(root)
            if "__pycache__" in rel.parts:
                continue
            if path.is_symlink():
                raise ValueError(f"Symlink not supported in publication inputs: {rel}")
            if path.is_file():
                result[rel] = daily.digest(path.read_bytes())
    return result


def process_queue(root, *, now=None, today=None, appender=daily.append_batch, append_options=None):
    root, fixed_now = pathlib.Path(root).resolve(), now
    with daily.repository_lock(root):
        now = clock(fixed_now, today)
        verify_queue(root, now=now)
        records = inspect_queue(root, now)
        pending = [row for row in records if row["state"] == "queued"]
        if not pending:
            return {"status": "already-complete", "processed": [], "changed": []}
        before = tree_hashes(root)
        with tempfile.TemporaryDirectory(prefix=".queue-stage-", dir=root) as temporary:
            stage = pathlib.Path(temporary)
            shadow = stage / "repo"
            shadow.mkdir()
            (shadow / ".git").mkdir()
            for folder in ("site", "tools", "data"):
                if (root / folder).exists():
                    shutil.copytree(root / folder, shadow / folder, ignore=shutil.ignore_patterns("__pycache__"))
            processed = []
            for row in pending:
                result = appender(shadow, row["deck"], row["request"]["batch"],
                                  today=row["date"], **(append_options or {}))
                processed.append({"deck": row["deck"], "date": row["date"], "status": result["status"]})
            verify_queue(shadow, now=now, require_complete=True)
            after = tree_hashes(shadow)
            if set(before) - set(after):
                raise ValueError("Queue processing unexpectedly deleted existing files")
            allowed = {pathlib.Path(name) for name in (
                "tools/packs.json", "tools/catalog.json", str(daily.STATE_FILE),
                "site/index.html", "site/sw.js", "site/apps/phrasal.html", "site/apps/bbapp.html",
                "site/packs/phrasal.mp3", "site/packs/bbapp.mp3")}
            allowed.update(pathlib.Path(f"data/daily/{row['date']}-{row['deck']}.json") for row in pending)
            changed = {rel for rel in after if before.get(rel) != after[rel]}
            if changed - allowed:
                raise ValueError(f"Queue processing changed unexpected files: {sorted(map(str, changed - allowed))}")
            if tree_hashes(root) != before:
                raise ValueError("Publication inputs changed during queue processing; retry from a fresh checkout")
            daily.install_changes(root, {rel: (shadow / rel).read_bytes() for rel in sorted(changed)}, stage)
        return {"status": "processed", "processed": processed, "changed": sorted(map(str, changed))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=daily.ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("status", "prepare"):
        command = commands.add_parser(name)
        command.add_argument("key", choices=daily.CONFIG)
        if name == "prepare":
            command.add_argument("batch", type=pathlib.Path)
    for name in ("process", "check", "verify"):
        commands.add_parser(name)
    args = parser.parse_args()
    try:
        if args.command == "status":
            result = queue_status(args.root, args.key)
        elif args.command == "prepare":
            result = prepare_queue(args.root, args.key, read_json(args.batch))
        elif args.command == "process":
            result = process_queue(args.root)
        else:
            result = verify_queue(args.root, require_complete=args.command == "check")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if result.get("state") == "conflict":
            parser.exit(1)
    except Exception as error:
        parser.exit(1, f"Daily queue: {error}\n")


if __name__ == "__main__":
    main()
