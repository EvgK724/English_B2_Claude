"""Keep every published lesson's audio in sync with its text, using Microsoft Ryan.

Run after changing site/apps/*.html and before publishing. Breaking Bad is excluded.
The first, explicitly reviewed baseline uses --bootstrap; ordinary runs regenerate
unknown or externally replaced recordings instead of trusting their voice. --check is read-only and fails if publication is not ready.
"""
from __future__ import annotations

import argparse
import asyncio
import copy
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

from ryan_manifest import VOICE, digest, identity, signature

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATE_FILE = pathlib.Path("tools/ryan-audio-state.json")
EXCLUDED = "bbapp"
SCHEMA = 1


def json_bytes(value, *, pretty=False):
    return (json.dumps(value, ensure_ascii=False, sort_keys=pretty,
                       indent=2 if pretty else None,
                       separators=None if pretty else (",", ":")) + "\n").encode()


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def safe_key(value, label):
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+", value) or value in (".", ".."):
        raise ValueError(f"Unsafe {label}: {value!r}")
    return value


def read_manifest(value):
    """Accept extractor output, optionally wrapped in an `apps` object."""
    apps = value.get("apps", value)
    if not isinstance(apps, dict) or not apps:
        raise ValueError("Audio manifest must contain an app mapping")
    result = {}
    for app, spec in apps.items():
        safe_key(app, "app key")
        if app == EXCLUDED:
            continue
        if not isinstance(spec, dict) or not isinstance(spec.get("clips"), list):
            raise ValueError(f"{app}: clips array is required")
        clips, seen = [], set()
        for original in spec["clips"]:
            key = safe_key(original.get("key"), "clip key")
            text, rate = original.get("text"), original.get("rate", "-5%")
            if key in seen or not isinstance(text, str) or not text.strip():
                raise ValueError(f"{app}/{key}: duplicate key or empty text")
            if not isinstance(rate, str) or not re.fullmatch(r"[+-]\d+%", rate):
                raise ValueError(f"{app}/{key}: invalid speech rate")
            clips.append({"key": key, "text": text, "rate": rate})
            seen.add(key)
        if not clips:
            raise ValueError(f"{app}: no speech clips extracted; refusing an incomplete audit")
        result[app] = {**spec, "clips": clips}
    if not result:
        raise ValueError("No Ryan lessons found")
    return result


def slice_bytes(pack, location, label):
    if (not isinstance(location, list) or len(location) != 3
            or type(location[0]) is not int or type(location[1]) is not int
            or not isinstance(location[2], (int, float))
            or location[0] < 0 or location[1] <= 0 or location[2] < 0
            or location[0] + location[1] > len(pack)):
        raise ValueError(f"Invalid packed audio range: {label}")
    data = pack[location[0]:location[0] + location[1]]
    if data[:2] not in (b"\xff\xf3", b"\xff\xf2", b"\xff\xfb"):
        raise ValueError(f"Invalid MP3 header: {label}")
    return data


def record(clip, packed, *, source, raw=None, duration=None):
    normalized = " ".join(unicodedata.normalize("NFC", clip["text"]).split())
    result = {**identity(clip), "signature": signature(clip),
              "text_sha256": digest(clip["text"].encode()),
              "normalized_text_sha256": digest(normalized.encode()),
              "packed_sha256": digest(packed), "source": source}
    if raw is not None:
        result.update(raw_sha256=digest(raw), edge_tts="7.3.1", duration=duration)
    else:
        # This identity fingerprints today's extracted request; it does not claim
        # that historical punctuation/rate were independently recovered from audio.
        result["baseline_parameters_verified"] = False
    return result


def synthesize_recordings(jobs, directory):
    """Generate into an isolated directory; no source pack is mutated here."""
    from ryan_tts import generate
    inputs, paths = [], {}
    for app in sorted({app for app, _ in jobs}):
        clips = [clip for key, clip in jobs if key == app]
        out = directory / app
        out.mkdir(parents=True)
        manifest = out / "clips.json"
        manifest.write_bytes(json_bytes(clips))
        inputs.append((manifest, out))
        paths.update({(app, clip["key"]): out / (clip["key"] + ".mp3") for clip in clips})
    asyncio.run(generate(inputs))
    return {key: path.read_bytes() for key, path in paths.items()}


def trim_recording(data):
    from deck_sync import trim_clip
    return trim_clip(data)


def validate_recording(path):
    from ryan_tts import validate_audio
    return validate_audio(path)


def phrasal_html(root, app, spec, pack_index):
    """Enable audio only after both verified clips exist; preserve all card fields."""
    flags = spec.get("audio_flags", [])
    pending = [row["id"] for row in flags if row.get("au") != 1]
    if not pending:
        return None
    path = root / "site/apps" / (app + ".html")
    html = path.read_text(encoding="utf-8")
    # Use the established deck parser so unexpected source formatting fails safely.
    from deck_sync import card_blocks
    blocks = dict(card_blocks(html))
    for cid in pending:
        if not all(f"{cid}-{suffix}" in pack_index for suffix in ("t", "x")):
            raise ValueError(f"{app}/{cid}: both term and example audio are required")
        if cid not in blocks:
            raise ValueError(f"Cannot locate {app} card {cid}; no changes written")
        before = blocks[cid]
        if re.search(r"^\s*au\s*:", before, re.M):
            after, count = re.subn(r"(^\s*au\s*:\s*)\d+", r"\g<1>1", before, count=1, flags=re.M)
        else:
            after, count = re.subn(r'(^[ \t]*)id:\s*"[^"\n]+",',
                                   r'\g<0>\n\g<1>au: 1,', before, count=1, flags=re.M)
        if count != 1 or html.count(before) != 1:
            raise ValueError(f"Cannot safely update audio flag for {app}/{cid}")
        html = html.replace(before, after, 1)
    return html.encode()


def build_shell(root, stage, changes):
    """Build against staged packs; a failed build cannot affect the working tree."""
    shadow = stage / "build"
    (shadow / "tools").mkdir(parents=True)
    shutil.copytree(root / "site", shadow / "site", copy_function=os.symlink)
    for name in ("mk_shell.py", "shell.html", "head.html", "sw.js", "packs.json", "catalog.json", "silent.mp3"):
        shutil.copyfile(root / "tools" / name, shadow / "tools" / name)
    for rel, data in changes.items():
        target = shadow / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.unlink(missing_ok=True)
        target.write_bytes(data)
    for name in ("index.html", "sw.js"):
        (shadow / "site" / name).unlink(missing_ok=True)
    subprocess.run([sys.executable, str(shadow / "tools/mk_shell.py")], cwd=shadow, check=True)
    for rel in (pathlib.Path("site/index.html"), pathlib.Path("site/sw.js")):
        changes[rel] = (shadow / rel).read_bytes()


def install_changes(root, changes, stage):
    """Replace only validated files; restore originals on a caught write failure."""
    originals, installed = {}, []
    prepared = stage / "install"
    prepared.mkdir()
    for i, (rel, data) in enumerate(changes.items()):
        destination = root / rel
        originals[rel] = destination.read_bytes() if destination.exists() else None
        (prepared / str(i)).write_bytes(data)
    try:
        for i, rel in enumerate(changes):
            destination = root / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            os.replace(prepared / str(i), destination)
            installed.append(rel)
    except BaseException:
        for rel in reversed(installed):
            if originals[rel] is None:
                (root / rel).unlink(missing_ok=True)
            else:
                (root / rel).write_bytes(originals[rel])
        raise


def ensure_audio(root, manifest, *, bootstrap=False, check=False, build=True,
                 synthesize=synthesize_recordings, trim=trim_recording,
                 validate=validate_recording, builder=build_shell):
    root = pathlib.Path(root).resolve()
    apps = read_manifest(manifest)
    packs = load_json(root / "tools/packs.json")
    catalog = load_json(root / "tools/catalog.json")
    entries = {a["key"]: a for a in catalog["apps"]}
    missing_apps = set(entries) - {EXCLUDED} - set(apps)
    if missing_apps or set(apps) - set(entries):
        raise ValueError(f"Manifest/catalog app mismatch: {sorted(missing_apps | (set(apps) - set(entries)))}")
    state_path = root / STATE_FILE
    if bootstrap:
        if state_path.exists():
            raise ValueError("State already exists; --bootstrap cannot overwrite trusted history")
        state = {"schema": SCHEMA, "voice": VOICE, "apps": {}}
    else:
        if not state_path.exists():
            raise ValueError("Ryan state missing; review the corpus and explicitly run --bootstrap once")
        state = load_json(state_path)
        if state.get("schema") != SCHEMA or state.get("voice") != VOICE or not isinstance(state.get("apps"), dict):
            raise ValueError("Unrecognized Ryan state; no existing recordings will be trusted")
    state = copy.deepcopy(state)
    original_state = copy.deepcopy(state)
    buffers, jobs, removed_invalid = {}, [], []
    for app, spec in apps.items():
        if bootstrap and entries[app].get("voice") != "Ryan":
            raise ValueError(f"{app}: bootstrap requires an explicitly confirmed Ryan catalog entry")
        pack_file = root / "site/packs" / (app + ".mp3")
        buffers[app] = pack_file.read_bytes() if pack_file.exists() else b""
        app_index = packs.setdefault(app, {})
        required = {clip["key"] for clip in spec["clips"]}
        # A vanished pack can leave legacy indexes behind. Keep valid unused
        # recordings, but never retain a dangling index into the rebuilt pack.
        for key, location in list(app_index.items()):
            if key in required:
                continue
            try:
                slice_bytes(buffers[app], location, f"{app}/{key}")
            except ValueError:
                if bootstrap:
                    raise
                del app_index[key]
                removed_invalid.append(f"{app}/{key}")
        saved = state["apps"].setdefault(app, {"clips": {}})
        if not isinstance(saved, dict) or not isinstance(saved.get("clips"), dict):
            raise ValueError(f"{app}: invalid saved state")
        for clip in spec["clips"]:
            key, previous = clip["key"], saved["clips"].get(clip["key"])
            try:
                data = slice_bytes(buffers[app], app_index[key], f"{app}/{key}") if key in app_index else None
            except ValueError:
                if bootstrap:
                    raise
                data = None  # Repair a missing pack or invalid required slice with Ryan.
            if bootstrap:
                if data is None:
                    raise ValueError(f"{app}/{key}: bootstrap requires complete existing audio")
                saved["clips"][key] = record(clip, data, source="reviewed-existing-Ryan-baseline")
                continue
            if data is not None:
                if (isinstance(previous, dict) and previous.get("voice") == VOICE
                        and previous.get("packed_sha256") == digest(data)
                        and previous.get("signature") == signature(clip)):
                    continue
            jobs.append((app, clip))
    pending_flags = sum(row.get("au") != 1 for spec in apps.values() for row in spec.get("audio_flags", []))
    report = {"apps": len(apps), "clips": sum(len(s["clips"]) for s in apps.values()),
              "generate": len(jobs), "audio_flags": pending_flags, "bootstrap": bootstrap,
              "removed_invalid_index_entries": removed_invalid}
    if check:
        if bootstrap:
            raise ValueError("--bootstrap and --check are mutually exclusive")
        if jobs or pending_flags or removed_invalid or any(entries[a].get("voice") != "Ryan" for a in apps):
            raise ValueError(f"Ryan audio is not ready: {len(jobs)} missing/changed clips, "
                             f"{pending_flags} pending flags, {len(removed_invalid)} invalid unused index entries")
        return {**report, "changed": []}
    changes = {}
    with tempfile.TemporaryDirectory(prefix=".ryan-stage-", dir=root) as temporary:
        stage = pathlib.Path(temporary)
        generated = synthesize(jobs, stage / "generated") if jobs else {}
        for app, clip in jobs:
            key = clip["key"]
            raw = generated.get((app, key))
            if not isinstance(raw, bytes) or not raw:
                raise ValueError(f"Generator returned no recording for {app}/{key}")
            raw_path = stage / "validate.mp3"
            raw_path.write_bytes(raw)
            validate(raw_path)
            data, lead = trim(raw)
            raw_path.write_bytes(data)
            duration = validate(raw_path)
            slice_bytes(data, [0, len(data), lead], f"{app}/{key}")
            # Append-only updates retain every previously published byte and offset.
            packs[app][key] = [len(buffers[app]), len(data), lead]
            buffers[app] += data
            state["apps"][app]["clips"][key] = record(
                clip, data, source="Microsoft-Edge-TTS", raw=raw, duration=duration)
        for app, spec in apps.items():
            # Recheck complete coverage after synthesis, before writing any output.
            for clip in spec["clips"]:
                data = slice_bytes(buffers[app], packs[app][clip["key"]], f"{app}/{clip['key']}")
                saved = state["apps"][app]["clips"][clip["key"]]
                if saved["signature"] != signature(clip) or saved["packed_sha256"] != digest(data):
                    raise ValueError(f"Final Ryan coverage check failed: {app}/{clip['key']}")
            entries[app]["voice"] = "Ryan"
            if spec.get("kind") == "phrasal" or spec.get("audio_flags"):
                updated = phrasal_html(root, app, spec, packs[app])
                if updated is not None:
                    changes[pathlib.Path("site/apps") / (app + ".html")] = updated
                    entries[app]["size"] = len(updated)
        for app in {app for app, _ in jobs}:
            changes[pathlib.Path("site/packs") / (app + ".mp3")] = buffers[app]
        if jobs or removed_invalid:
            changes[pathlib.Path("tools/packs.json")] = json_bytes(packs)
        if catalog != load_json(root / "tools/catalog.json"):
            changes[pathlib.Path("tools/catalog.json")] = json_bytes(catalog)
        if bootstrap or state != original_state:
            changes[STATE_FILE] = json_bytes(state, pretty=True)
        if build:
            builder(root, stage, changes)
        changes = {rel: data for rel, data in changes.items()
                   if not (root / rel).exists() or (root / rel).read_bytes() != data}
        install_changes(root, changes, stage)
    return {**report, "changed": [str(p) for p in changes]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=ROOT)
    parser.add_argument("--manifest", type=pathlib.Path, help="Use an already extracted JSON clip manifest")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--bootstrap", action="store_true", help="Trust the reviewed complete current Ryan corpus once")
    group.add_argument("--check", action="store_true", help="Read-only publication gate; fail if audio needs updating")
    parser.add_argument("--no-build", action="store_true", help="Skip shell generation (focused tests only)")
    args = parser.parse_args()
    try:
        if args.manifest:
            manifest = load_json(args.manifest)
        else:
            extracted = subprocess.run(["node", str(args.root / "tools/audio_clips.mjs"), "--root", str(args.root)],
                                       check=True, capture_output=True, text=True)
            manifest = json.loads(extracted.stdout)
        result = ensure_audio(args.root, manifest, bootstrap=args.bootstrap, check=args.check, build=not args.no_build)
        print(json.dumps(result, ensure_ascii=False))
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Ryan audio: {error}\n")


if __name__ == "__main__":
    main()
