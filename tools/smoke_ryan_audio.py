"""Exercise real missing-audio recovery in an isolated copy, never the live lessons.

Requires the same Node, edge-tts and ffmpeg dependencies as the publish workflow.
"""
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def fingerprint(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for folder in ("site", "tools") for p in (root / folder).rglob("*")
            if p.is_file() and "__pycache__" not in p.parts}


def main():
    original = fingerprint(ROOT)
    with tempfile.TemporaryDirectory(prefix="english-ryan-smoke-") as temporary:
        root = pathlib.Path(temporary)
        for folder in ("site", "tools"):
            shutil.copytree(ROOT / folder, root / folder, ignore=shutil.ignore_patterns("__pycache__"))
        state = read_json(root / "tools/ryan-audio-state.json")
        app = "whatfor"
        key = next(iter(state["apps"][app]["clips"]))
        before_pack = (root / f"site/packs/{app}.mp3").read_bytes()
        packs = read_json(root / "tools/packs.json")
        bb_index = packs["bbapp"]
        bb_catalog = next(a for a in read_json(root / "tools/catalog.json")["apps"] if a["key"] == "bbapp")
        del packs[app][key]
        (root / "tools/packs.json").write_text(json.dumps(packs), encoding="utf-8")
        # Simulate the daily importer adding a new card without any audio files.
        from deck_sync import MARK, card_blocks, card_object
        new_id = "smoke-test-keep-going"
        new_card = '''  {
    id: "smoke-test-keep-going",
    term: "keep going",
    ru: "продолжать",
    ex: "Keep going. You are making progress.",
    exru: "Продолжайте. Вы делаете успехи."
  },
'''
        phrasal = root / "site/apps/phrasal.html"
        source = phrasal.read_text(encoding="utf-8")
        assert source.count(MARK) == 1 and new_id not in source
        phrasal.write_text(source.replace(MARK, new_card + MARK), encoding="utf-8")
        catalog = read_json(root / "tools/catalog.json")
        deck = next(a for a in catalog["apps"] if a["key"] == "phrasal")
        deck["ids"].append(new_id)
        deck["items"].append({"id": new_id, "term": "keep going", "ru": "продолжать", "added": ""})
        (root / "tools/catalog.json").write_text(json.dumps(catalog, ensure_ascii=False), encoding="utf-8")
        result = subprocess.run([sys.executable, str(root / "tools/ensure_ryan_audio.py")],
                                check=True, capture_output=True, text=True)
        print(result.stdout, end="")
        report = json.loads(result.stdout.strip().splitlines()[-1])
        assert report["generate"] == 3 and report["audio_flags"] == 1, report
        subprocess.run([sys.executable, str(root / "tools/ensure_ryan_audio.py"), "--check"], check=True)
        after_pack = (root / f"site/packs/{app}.mp3").read_bytes()
        assert after_pack.startswith(before_pack), "Existing recordings were altered"
        meta = read_json(root / "tools/ryan-audio-state.json")["apps"][app]["clips"][key]
        assert meta["voice"] == "en-GB-RyanNeural" and meta["source"] == "Microsoft-Edge-TTS"
        assert meta["duration"] > 0.1
        new_state = read_json(root / "tools/ryan-audio-state.json")["apps"]["phrasal"]["clips"]
        for suffix in ("t", "x"):
            assert new_state[f"{new_id}-{suffix}"]["source"] == "Microsoft-Edge-TTS"
        assert card_object(dict(card_blocks(phrasal.read_text(encoding="utf-8")))[new_id])["au"] == 1
        assert read_json(root / "tools/packs.json")["bbapp"] == bb_index
        assert next(a for a in read_json(root / "tools/catalog.json")["apps"] if a["key"] == "bbapp") == bb_catalog
        for filename in ("site/apps/bbapp.html", "site/packs/bbapp.mp3"):
            assert (root / filename).read_bytes() == (ROOT / filename).read_bytes()
        assert fingerprint(ROOT) == original, "Smoke test changed the real project"
        print(json.dumps({"real_synthesis": "passed", "voice": meta["voice"],
                          "recovered_clip": f"{app}/{key}", "duration": meta["duration"],
                          "new_card_with_term_and_example": "passed",
                          "breaking_bad_unchanged": True, "source_tree_unchanged": True}))


if __name__ == "__main__":
    main()
