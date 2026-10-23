"""Focused regression tests for incremental publication and failure safety."""
import copy
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch

import ensure_ryan_audio as audio


def mp3(label):
    return b"\xff\xf3" + label.encode() * 40


class IncrementalAudioTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temporary.name)
        (self.root / "tools").mkdir()
        (self.root / "site/packs").mkdir(parents=True)
        (self.root / "site/apps").mkdir()
        self.original = mp3("existing-Ryan")
        self.bb = mp3("Breaking-Bad-Andrew")
        self.catalog = {"groups": [], "apps": [
            {"key": "lesson", "voice": "Ryan", "ids": ["old"], "ls": "lesson:state"},
            {"key": "bbapp", "voice": "Andrew", "ids": ["original"], "ls": "bbapp:state"}]}
        self.write_json("tools/catalog.json", self.catalog)
        self.write_json("tools/packs.json", {
            "lesson": {"old": [0, len(self.original), 0.048]},
            "bbapp": {"original": [0, len(self.bb), 0.048]}})
        (self.root / "site/packs/lesson.mp3").write_bytes(self.original)
        (self.root / "site/packs/bbapp.mp3").write_bytes(self.bb)
        (self.root / "site/apps/bbapp.html").write_bytes(b"Original Breaking Bad content")
        self.manifest = {"lesson": {"clips": [{"key": "old", "text": "Existing phrase.", "rate": "-5%"}]}}
        self.generated = []
        self.run_audio(bootstrap=True)

    def tearDown(self):
        self.temporary.cleanup()

    def write_json(self, rel, value):
        (self.root / rel).write_text(json.dumps(value))

    def read_json(self, rel):
        return json.loads((self.root / rel).read_text())

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}

    def fake_generate(self, jobs, directory):
        self.generated.extend(copy.deepcopy(jobs))
        return {(app, clip["key"]): mp3(clip["text"] + clip["rate"]) for app, clip in jobs}

    def run_audio(self, manifest=None, **kwargs):
        return audio.ensure_audio(self.root, manifest or self.manifest, build=kwargs.pop("build", False),
                                  synthesize=kwargs.pop("synthesize", self.fake_generate),
                                  validate=lambda path: 1.25, trim=lambda data: (data, 0.024), **kwargs)

    def add_clip(self, key="new", text="A newly added phrase."):
        self.manifest["lesson"]["clips"].append({"key": key, "text": text, "rate": "-5%"})

    def test_baseline_and_idempotence_do_not_generate_or_change_existing_audio(self):
        before = self.snapshot()
        self.assertEqual(self.run_audio()["changed"], [])
        self.assertEqual(self.run_audio(check=True)["generate"], 0)
        self.assertEqual(self.generated, [])
        self.assertEqual(before, self.snapshot())
        record = self.read_json(audio.STATE_FILE)["apps"]["lesson"]["clips"]["old"]
        self.assertEqual(record["packed_sha256"], audio.digest(self.original))
        self.assertEqual(record["source"], "reviewed-existing-Ryan-baseline")
        self.assertFalse(record["baseline_parameters_verified"])

    def test_missing_audio_is_generated_once_and_preserves_existing_slice(self):
        self.add_clip()
        with self.assertRaisesRegex(ValueError, "1 missing/changed"):
            self.run_audio(check=True)
        result = self.run_audio()
        self.assertEqual(result["generate"], 1)
        self.assertEqual(self.generated[0][1]["key"], "new")
        pack = (self.root / "site/packs/lesson.mp3").read_bytes()
        index = self.read_json("tools/packs.json")["lesson"]
        self.assertEqual(pack[:len(self.original)], self.original)
        self.assertEqual(index["old"], [0, len(self.original), 0.048])
        self.assertEqual(index["new"][0], len(self.original))
        state = self.read_json(audio.STATE_FILE)["apps"]["lesson"]["clips"]["new"]
        self.assertEqual(state["voice"], "en-GB-RyanNeural")
        self.assertEqual(state["packed_sha256"], audio.digest(audio.slice_bytes(pack, index["new"], "new")))
        before = self.snapshot()
        self.assertEqual(self.run_audio()["generate"], 0)
        self.assertEqual(before, self.snapshot())

    def test_text_and_rate_edits_replace_only_matching_key(self):
        self.add_clip()
        self.run_audio()
        old_pack = (self.root / "site/packs/lesson.mp3").read_bytes()
        old_index = self.read_json("tools/packs.json")["lesson"]
        self.manifest["lesson"]["clips"][0]["text"] = "The corrected phrase."
        self.assertEqual(self.run_audio()["generate"], 1)
        index = self.read_json("tools/packs.json")["lesson"]
        self.assertEqual(index["new"], old_index["new"])
        self.assertEqual(index["old"][0], len(old_pack))
        self.assertEqual((self.root / "site/packs/lesson.mp3").read_bytes()[:len(old_pack)], old_pack)
        self.manifest["lesson"]["clips"][0]["rate"] = "-10%"
        self.assertEqual(self.run_audio()["generate"], 1)
        self.assertEqual(self.run_audio(check=True)["generate"], 0)

    def test_unknown_imported_and_replaced_audio_is_regenerated_as_ryan(self):
        self.add_clip()
        imported = mp3("source voice unconfirmed")
        (self.root / "site/packs/lesson.mp3").write_bytes(self.original + imported)
        packs = self.read_json("tools/packs.json")
        packs["lesson"]["new"] = [len(self.original), len(imported), 0]
        self.write_json("tools/packs.json", packs)
        self.assertEqual(self.run_audio()["generate"], 1)
        # A later importer overwrites the existing slice with different valid MP3 bytes.
        data = (self.root / "site/packs/lesson.mp3").read_bytes()
        (self.root / "site/packs/lesson.mp3").write_bytes(data[:2] + b"x" + data[3:])
        self.assertEqual(self.run_audio()["generate"], 1)
        self.assertEqual(self.generated[-1][1]["key"], "old")

    def test_missing_recorded_clip_is_restored(self):
        packs = self.read_json("tools/packs.json")
        del packs["lesson"]["old"]
        self.write_json("tools/packs.json", packs)
        self.assertEqual(self.run_audio()["generate"], 1)

    def test_missing_pack_is_rebuilt_without_dangling_unused_indexes(self):
        packs = self.read_json("tools/packs.json")
        packs["lesson"]["legacy-unused"] = packs["lesson"]["old"].copy()
        self.write_json("tools/packs.json", packs)
        (self.root / "site/packs/lesson.mp3").unlink()
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "1 missing/changed"):
            self.run_audio(check=True)
        self.assertEqual(before, self.snapshot())
        result = self.run_audio()
        self.assertEqual(result["generate"], 1)
        self.assertEqual(result["removed_invalid_index_entries"], ["lesson/legacy-unused"])
        self.assertEqual(set(self.read_json("tools/packs.json")["lesson"]), {"old"})
        self.assertEqual(self.run_audio(check=True)["generate"], 0)

    def test_invalid_required_range_or_header_is_repaired_and_valid_extras_retained(self):
        packs = self.read_json("tools/packs.json")
        packs["lesson"]["legacy-unused"] = packs["lesson"]["old"].copy()
        packs["lesson"]["old"] = [len(self.original), 100, 0]
        self.write_json("tools/packs.json", packs)
        self.assertEqual(self.run_audio()["generate"], 1)
        self.assertEqual(self.read_json("tools/packs.json")["lesson"]["legacy-unused"],
                         [0, len(self.original), 0.048])
        packs = self.read_json("tools/packs.json")
        data = bytearray((self.root / "site/packs/lesson.mp3").read_bytes())
        data[packs["lesson"]["old"][0]] = 0
        (self.root / "site/packs/lesson.mp3").write_bytes(data)
        self.assertEqual(self.run_audio()["generate"], 1)
        self.assertEqual(self.run_audio(check=True)["generate"], 0)

    def test_generator_failure_does_not_publish_partial_work(self):
        self.add_clip("new-1")
        self.add_clip("new-2")
        before = self.snapshot()
        def fail(jobs, directory):
            directory.mkdir()
            (directory / "first.mp3").write_bytes(mp3("first completed"))
            raise RuntimeError("service unavailable during second clip")
        with self.assertRaisesRegex(RuntimeError, "service unavailable"):
            self.run_audio(synthesize=fail)
        self.assertEqual(before, self.snapshot())
        self.assertFalse(list(self.root.glob(".ryan-stage-*")))

    def test_invalid_generated_audio_and_build_failure_do_not_write(self):
        self.add_clip()
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "Invalid MP3 header"):
            self.run_audio(synthesize=lambda jobs, directory: {("lesson", "new"): b"bad audio"})
        self.assertEqual(before, self.snapshot())
        def failed_build(root, stage, changes):
            raise ValueError("broken shell template")
        with self.assertRaisesRegex(ValueError, "broken shell"):
            self.run_audio(build=True, builder=failed_build)
        self.assertEqual(before, self.snapshot())

    def test_breaking_bad_is_excluded_even_if_manifest_contains_it(self):
        before_pack = (self.root / "site/packs/bbapp.mp3").read_bytes()
        before_html = (self.root / "site/apps/bbapp.html").read_bytes()
        before_index = self.read_json("tools/packs.json")["bbapp"]
        before_entry = self.read_json("tools/catalog.json")["apps"][1]
        self.manifest["bbapp"] = {"clips": [{"key": "new", "text": "Do not generate"}]}
        self.add_clip()
        self.run_audio()
        self.assertEqual((self.root / "site/packs/bbapp.mp3").read_bytes(), before_pack)
        self.assertEqual((self.root / "site/apps/bbapp.html").read_bytes(), before_html)
        self.assertEqual(self.read_json("tools/packs.json")["bbapp"], before_index)
        self.assertEqual(self.read_json("tools/catalog.json")["apps"][1], before_entry)
        self.assertNotIn("bbapp", self.read_json(audio.STATE_FILE)["apps"])
        self.assertEqual([job[0] for job in self.generated], ["lesson"])

    def test_bootstrap_cannot_be_used_to_bless_edited_text(self):
        before = self.snapshot()
        self.manifest["lesson"]["clips"][0]["text"] = "Changed"
        with self.assertRaisesRegex(ValueError, "cannot overwrite"):
            self.run_audio(bootstrap=True)
        self.assertEqual(before, self.snapshot())

    def test_missing_state_requires_explicit_review(self):
        (self.root / audio.STATE_FILE).unlink()
        with self.assertRaisesRegex(ValueError, "state missing"):
            self.run_audio()
        self.assertEqual(self.generated, [])

    def test_incomplete_extractor_output_and_duplicate_keys_fail_safely(self):
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "Manifest/catalog app mismatch"):
            self.run_audio({"other": {"clips": [{"key": "x", "text": "Wrong app"}]}})
        self.manifest["lesson"]["clips"].append(self.manifest["lesson"]["clips"][0].copy())
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.run_audio()
        self.assertEqual(before, self.snapshot())

    def test_install_error_rolls_back_every_replaced_file(self):
        self.add_clip()
        before = self.snapshot()
        real_replace = audio.os.replace
        calls = 0
        def fail_second(source, destination):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated disk write failure")
            real_replace(source, destination)
        with patch.object(audio.os, "replace", side_effect=fail_second):
            with self.assertRaisesRegex(OSError, "disk write"):
                self.run_audio()
        self.assertEqual(before, self.snapshot())

    def test_new_trainer_audio_and_catalog_become_ryan(self):
        catalog = self.read_json("tools/catalog.json")
        catalog["apps"].append({"key": "new-lesson", "voice": "System"})
        self.write_json("tools/catalog.json", catalog)
        self.manifest["new-lesson"] = {"clips": [{"key": "first", "text": "New trainer."}]}
        result = self.run_audio()
        self.assertEqual(result["generate"], 1)
        self.assertEqual(self.read_json("tools/catalog.json")["apps"][-1]["voice"], "Ryan")
        self.assertEqual(self.run_audio(check=True)["generate"], 0)

    def test_new_phrasal_style_deck_without_audio_flag_is_enabled(self):
        catalog = self.read_json("tools/catalog.json")
        catalog["apps"].append({"key": "new-deck", "voice": "Ryan", "ids": ["carry-on"]})
        self.write_json("tools/catalog.json", catalog)
        html = '''const CARDS = [
  {
    id: "carry-on",
    term: "carry on",
    ex: "Carry on working."
  },
  // НОВАЯ КАРТОЧКА ВСТАВЛЯЕТСЯ ВЫШЕ ЭТОЙ СТРОКИ
];'''
        (self.root / "site/apps/new-deck.html").write_text(html)
        self.manifest["new-deck"] = {"kind": "phrasal", "audio_flags": [{"id": "carry-on", "au": 0}], "clips": [
            {"key": "carry-on-t", "text": "carry on"}, {"key": "carry-on-x", "text": "Carry on working."}]}
        result = self.run_audio()
        self.assertEqual(result["generate"], 2)
        self.assertEqual((self.root / "site/apps/new-deck.html").read_text(),
                         html.replace('id: "carry-on",', 'id: "carry-on",\n    au: 1,'))
        self.assertFalse((self.root / "site/apps/phrasal.html").exists())
        self.manifest["new-deck"]["audio_flags"][0]["au"] = 1
        self.assertEqual(self.run_audio(check=True)["generate"], 0)

    def test_phrasal_flag_is_enabled_after_both_clips_are_validated(self):
        catalog = self.read_json("tools/catalog.json")
        catalog["apps"].append({"key": "phrasal", "voice": "Ryan", "ids": ["carry-on"]})
        self.write_json("tools/catalog.json", catalog)
        html = '''const CARDS = [
  {
    id: "carry-on",
    au: 0,
    term: "carry on",
    ex: "Carry on working."
  },
  // НОВАЯ КАРТОЧКА ВСТАВЛЯЕТСЯ ВЫШЕ ЭТОЙ СТРОКИ
];'''
        (self.root / "site/apps/phrasal.html").write_text(html)
        self.manifest["phrasal"] = {"audio_flags": [{"id": "carry-on", "au": 0}], "clips": [
            {"key": "carry-on-t", "text": "carry on"}, {"key": "carry-on-x", "text": "Carry on working."}]}
        result = self.run_audio()
        self.assertEqual(result["generate"], 2)
        self.assertEqual((self.root / "site/apps/phrasal.html").read_text(), html.replace("au: 0", "au: 1"))
        self.manifest["phrasal"]["audio_flags"][0]["au"] = 1
        self.assertEqual(self.run_audio(check=True)["generate"], 0)


if __name__ == "__main__":
    unittest.main()
