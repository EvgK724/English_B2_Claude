"""Build Pages with reviewed Russian corrections over immutable daily history.

Only the separate publication directory receives corrected cards. Requests,
ledgers, canonical HTML, audio and their existing validators stay unchanged.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import pathlib
import re
import shutil
import subprocess
import tempfile

import daily_deck as daily
import daily_queue as queue
from ensure_ryan_audio import build_shell, digest, json_bytes

ROOT = pathlib.Path(__file__).resolve().parent.parent
CORRECTIONS = pathlib.Path("data/corrections")
FIELDS = {"schema", "deck", "card_id", "ledger_date", "request_sha256",
          "ledger_sha256", "revision", "previous_sha256", "changes", "reason"}
ALLOWED_FIELDS = {"ru", "exru"}
SHA = re.compile(r"[0-9a-f]{64}")
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def git(root, *args):
    return subprocess.run(["git", *args], cwd=root, check=True,
                          capture_output=True).stdout


def correction_files(root):
    directory = root / CORRECTIONS
    if (root / "data").is_symlink() or directory.is_symlink():
        raise ValueError("Correction directory must not be a symlink")
    if not directory.exists():
        return []
    files = sorted(directory.iterdir())
    if any(path.is_symlink() or not path.is_file() or path.suffix != ".json" for path in files):
        raise ValueError("Corrections must be regular JSON files directly in data/corrections")
    return files


def verify_history(root):
    """Check every mainline transition, including changes later reverted.

New, not-yet-committed files are allowed for local review. Files already in HEAD
must remain byte-identical, and a complete history is required even in cron runs.
    """
    root = pathlib.Path(root).resolve()
    files = correction_files(root)
    if git(root, "rev-parse", "--is-shallow-repository").strip() != b"false":
        raise ValueError("Append-only correction verification requires complete Git history")
    history = git(root, "log", "--first-parent", "--format=", "--name-status",
                  "--diff-merges=first-parent", "--no-renames", "--", str(CORRECTIONS)).decode()
    seen = set()
    for line in history.splitlines():
        if not line:
            continue
        status, separator, name = line.partition("\t")
        if not separator or status != "A" or name in seen:
            raise ValueError("Correction history is append-only: edits, deletions and renames are forbidden")
        seen.add(name)
    entries = git(root, "ls-tree", "-r", "-z", "HEAD", "--", str(CORRECTIONS)).split(b"\0")
    current = {str(path.relative_to(root)): path for path in files}
    for entry in filter(None, entries):
        metadata, name = entry.split(b"\t", 1)
        mode, kind, oid = metadata.decode().split()
        name = name.decode()
        if mode != "100644" or kind != "blob" or name not in current:
            raise ValueError("Committed correction was deleted, renamed or is not a regular file")
        if current[name].read_bytes() != git(root, "cat-file", "blob", oid):
            raise ValueError("Committed correction is immutable; add a new revision instead")


def read_record(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key in {path.name}: {key}")
            result[key] = value
        return result

    def invalid(value):
        raise ValueError(f"Non-finite JSON value: {value}")

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique,
                      parse_constant=invalid)


def plain_text(value):
    # The existing shell embeds its catalog in an inline script. Corrections are
    # plain text, never HTML; reject delimiters instead of changing that builder.
    return (isinstance(value, str) and bool(value.strip())
            and not any(ord(c) < 32 or c in "<>\u2028\u2029" for c in value))


def validate_record(path, value):
    if (not isinstance(value, dict) or set(value) != FIELDS
            or type(value["schema"]) is not int or value["schema"] != 1):
        raise ValueError(f"Invalid correction schema: {path.name}")
    key, cid, revision = value["deck"], value["card_id"], value["revision"]
    if (not isinstance(key, str) or key not in daily.CONFIG
            or not isinstance(cid, str) or not SLUG.fullmatch(cid)
            or type(revision) is not int or not 1 <= revision <= 9999
            or path.name != f"{key}-{cid}-{revision:04d}.json"):
        raise ValueError(f"Correction filename and identity disagree: {path.name}")
    queue.date_value(value["ledger_date"])
    for field in ("request_sha256", "ledger_sha256"):
        if not isinstance(value[field], str) or not SHA.fullmatch(value[field]):
            raise ValueError(f"Invalid correction anchor: {field}")
    previous = value["previous_sha256"]
    if previous is not None and (not isinstance(previous, str) or not SHA.fullmatch(previous)):
        raise ValueError("Invalid previous correction hash")
    changes = value["changes"]
    if not isinstance(changes, dict) or not changes or set(changes) - ALLOWED_FIELDS:
        raise ValueError("Corrections may change only ru and exru")
    for field, change in changes.items():
        if (not isinstance(change, dict) or set(change) != {"from", "to"}
                or not all(plain_text(change[k]) for k in ("from", "to"))
                or change["from"] == change["to"]):
            raise ValueError(f"Invalid or no-op plain-text correction: {field}")
    if not plain_text(value["reason"]):
        raise ValueError("Correction reason must be nonempty plain text")


def correction_changes(root, *, check_history=True):
    root = pathlib.Path(root).resolve()
    # Pending requests for other cards are valid here: CI checks corrections
    # before completing those requests. Every correction target must be complete.
    verification = queue.verify_queue(root)
    records = correction_files(root)
    if check_history:
        verify_history(root)
    completed = {(r["deck"], r["date"]) for r in verification["requests"] if r["state"] == "complete"}
    catalog = daily.load_json(root / "tools/catalog.json")
    original_catalog = copy.deepcopy(catalog)
    decks, chains, anchors = {}, {}, {}
    hashes = {}
    for path in records:
        value = read_record(path)
        validate_record(path, value)
        key, cid, date = value["deck"], value["card_id"], value["ledger_date"]
        if (key, date) not in completed:
            raise ValueError("Correction target must have a completed immutable request and ledger")
        for kind, field in (("requests", "request_sha256"), ("daily", "ledger_sha256")):
            source = root / f"data/{kind}/{date}-{key}.json"
            if source.is_symlink() or digest(source.read_bytes()) != value[field]:
                raise ValueError(f"Correction {kind} anchor mismatch: {path.name}")
        identity = (key, cid)
        previous_revision, previous_hash = chains.get(identity, (0, None))
        if value["revision"] != previous_revision + 1 or value["previous_sha256"] != previous_hash:
            raise ValueError(f"Broken correction revision chain: {path.name}")
        anchor = (date, value["request_sha256"], value["ledger_sha256"])
        if identity in anchors and anchors[identity] != anchor:
            raise ValueError("Correction chain changed its original history anchors")
        anchors[identity] = anchor
        if key not in decks:
            html = (root / f"site/apps/{key}.html").read_text(encoding="utf-8")
            cards = daily.parse_cards(html)
            decks[key] = {"html": html, "cards": cards, "effective": copy.deepcopy(cards)}
        deck = decks[key]
        matching = [card for card in deck["effective"] if card["id"] == cid]
        if len(matching) != 1 or matching[0].get("added") != date:
            raise ValueError("Correction target card/date is absent or ambiguous")
        card = matching[0]
        for field, change in value["changes"].items():
            if card.get(field) != change["from"]:
                raise ValueError(f"Correction from value differs from current text: {cid}/{field}")
            card[field] = change["to"]
        hashes[path.name] = digest(path.read_bytes())
        chains[identity] = (value["revision"], hashes[path.name])
    changes = {}
    for key, deck in decks.items():
        html = deck["html"]
        blocks = dict(daily.deck_sync.card_blocks(html))
        app = next(app for app in catalog["apps"] if app["key"] == key)
        for before, after in zip(deck["cards"], deck["effective"]):
            if before == after:
                continue
            if {k for k in before.keys() | after.keys() if before.get(k) != after.get(k)} - ALLOWED_FIELDS:
                raise ValueError("Projection changed protected card fields")
            block = blocks[before["id"]]
            updated = block
            for field in ALLOWED_FIELDS:
                if before[field] == after[field]:
                    continue
                pattern = re.compile(r'(^[ \t]*' + field + r':[ \t]*)"(?:[^"\\]|\\.)*"', re.M)
                literal = json.dumps(after[field], ensure_ascii=False)
                updated, count = pattern.subn(lambda m: m.group(1) + literal, updated)
                if count != 1:
                    raise ValueError("Expected exactly one correction field literal")
            if html.count(block) != 1:
                raise ValueError("Ambiguous card block")
            html = html.replace(block, updated, 1)
            items = [item for item in app["items"] if item["id"] == before["id"]]
            if (len(items) != 1 or items[0]["term"] != before["term"]
                    or items[0]["ru"] != daily.deck_sync.short_ru(before["ru"])):
                raise ValueError("Canonical catalog disagrees with the correction target")
            items[0]["ru"] = daily.deck_sync.short_ru(after["ru"])
        if daily.parse_cards(html) != deck["effective"]:
            raise ValueError("Published card projection differs from verified corrections")
        if html != deck["html"]:
            changes[pathlib.Path(f"site/apps/{key}.html")] = html.encode()
            app["size"] = len(html.encode())
    if catalog != original_catalog:
        changes[pathlib.Path("tools/catalog.json")] = json_bytes(catalog)
    return changes, {"corrections": len(records), "cards": len(chains),
                     "corrections_sha256": digest(json_bytes(hashes))}


def check_corrections(root, *, check_history=True):
    _, report = correction_changes(root, check_history=check_history)
    return {"status": "verified", **report}


def source_hashes(root):
    hashes = {str(k): v for k, v in queue.tree_hashes(root).items()}
    for name in ("index.html", ".nojekyll"):
        path = root / name
        if path.is_symlink():
            raise ValueError("Publication input must not be a symlink")
        hashes[name] = digest(path.read_bytes())
    return hashes


def output_hashes(output):
    return {str(p.relative_to(output)): digest(p.read_bytes())
            for p in output.rglob("*") if p.is_file()}


def build_publication(root, output, *, check_history=True):
    root = pathlib.Path(root).resolve()
    requested = pathlib.Path(output)
    output = requested.resolve()
    if (requested.is_symlink() or output == root or root in output.parents
            or output in root.parents or output.exists()):
        raise ValueError("Publication output must be a new directory outside the source repository")
    before = source_hashes(root)
    queue.verify_queue(root, require_complete=True)
    changes, report = correction_changes(root, check_history=check_history)
    with tempfile.TemporaryDirectory(prefix=".publication-", dir=output.parent) as temporary:
        stage = pathlib.Path(temporary)
        projection = dict(changes)
        build_shell(root, stage, changes)
        generated = {pathlib.Path("site/index.html"), pathlib.Path("site/sw.js")}
        if (set(changes) != set(projection) | generated
                or any(changes.get(path) != data for path, data in projection.items())):
            raise ValueError("Shell builder changed the verified card projection")
        bundle = stage / "output"
        bundle.mkdir()
        shutil.copytree(root / "site", bundle / "site")
        for name in ("index.html", ".nojekyll"):
            shutil.copyfile(root / name, bundle / name)
        expected = {name: sha for name, sha in before.items()
                    if name.startswith("site/") or name in {"index.html", ".nojekyll"}}
        for rel, data in changes.items():
            if rel.parts[0] == "site":
                (bundle / rel).write_bytes(data)
                expected[str(rel)] = digest(data)
        if output_hashes(bundle) != expected:
            raise ValueError("Publication changed files outside the verified projection")
        if source_hashes(root) != before:
            raise ValueError("Source files changed during publication build")
        if output.exists() or requested.is_symlink():
            raise ValueError("Publication output appeared during build")
        # Atomically reserve the destination: never replace a directory created
        # by another build between validation and installation. Rename only our
        # own empty reservation, so the complete bundle appears in one step.
        output.mkdir()
        reservation = output.stat()
        try:
            os.rename(bundle, output)
        except BaseException:
            try:
                current = output.lstat()
                if (current.st_dev, current.st_ino) == (reservation.st_dev, reservation.st_ino):
                    output.rmdir()  # refuses to remove a nonempty directory
            except OSError:
                pass
            raise
    return {"status": "built", **report, "output": str(output),
            "changed": sorted(str(p) for p, data in changes.items()
                              if p.parts[0] == "site" and before.get(str(p)) != digest(data)),
            "index_sha256": digest((output / "site/index.html").read_bytes()),
            "sw_sha256": digest((output / "site/sw.js").read_bytes())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check")
    build = commands.add_parser("build")
    build.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    try:
        result = (check_corrections(args.root) if args.command == "check"
                  else build_publication(args.root, args.output))
        print(json.dumps(result, ensure_ascii=False))
    except Exception as error:
        parser.exit(1, f"Publication corrections: {error}\n")


if __name__ == "__main__":
    main()
