"""Andrew coverage: approved repairs, provenance, preservation and failure safety."""
import copy
import pathlib
import unittest
from unittest.mock import patch

import daily_deck as daily
import ensure_andrew_audio as andrew
import test_daily_deck as fixtures


class AndrewAudioTest(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.DailyDeckTest()
        self.fixture.setUp()
        self.root = self.fixture.root
        self.addCleanup(self.fixture.tearDown)
        self.gap = fixtures.card("bbapp", "approved-gap", "An approved old phrase.", "2026-10-12")
        app = self.root / "site/apps/bbapp.html"
        text = daily.card_block(self.gap, "bbapp").replace('    au: 1,\n', '')
        app.write_text(app.read_text().replace(daily.deck_sync.MARK, text + daily.deck_sync.MARK))
        self.gap.pop("au")
        catalog = self.read("tools/catalog.json")
        entry = next(a for a in catalog["apps"] if a["key"] == "bbapp")
        entry["ids"].append(self.gap["id"])
        entry["items"].append({"id": self.gap["id"], "term": self.gap["term"], "ru": self.gap["ru"]})
        self.write("tools/catalog.json", catalog)
        self.write(andrew.STATE_FILE, andrew.reviewed_baseline(
            self.root, {"approved-gap-t", "approved-gap-x"}, source_commit="test-reviewed-source"))

    def read(self, path):
        return self.fixture.read(path)

    def write(self, path, value):
        return self.fixture.write(path, value)

    def snapshot(self):
        return self.fixture.snapshot()

    def ensure(self, **kwargs):
        return andrew.ensure_audio(
            self.root, synthesizer=kwargs.pop("synthesizer", self.fixture.synthesize),
            validator=kwargs.pop("validator", lambda path: 1.25),
            trimmer=kwargs.pop("trimmer", lambda raw: (raw, 0.024)),
            builder=kwargs.pop("builder", self.fixture.builder), **kwargs)

    def test_check_refuses_approved_missing_recordings_without_mutation(self):
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "2 approved missing clips"):
            self.ensure(check=True)
        self.assertEqual(before, self.snapshot())
        self.assertEqual(self.fixture.generated, [])

    def test_repair_preserves_audio_content_ids_and_other_deck_then_is_idempotent(self):
        before = self.snapshot()
        indexes = self.read("tools/packs.json")
        result = self.ensure()
        self.assertEqual(result["generate"], 2)
        self.assertEqual(result["audio_flags"], 1)
        self.assertEqual(self.fixture.generated[0][1], "en-US-AndrewNeural")
        self.assertEqual({c["key"] for c in self.fixture.generated[0][0]}, {"approved-gap-t", "approved-gap-x"})
        after = self.snapshot()
        self.assertTrue(after["site/packs/bbapp.mp3"].startswith(before["site/packs/bbapp.mp3"]))
        for key, value in indexes["bbapp"].items():
            self.assertEqual(self.read("tools/packs.json")["bbapp"][key], value)
        for path in ("site/apps/phrasal.html", "site/packs/phrasal.mp3", str(daily.STATE_FILE)):
            self.assertEqual(before[path], after[path])
        parsed = daily.parse_cards(after["site/apps/bbapp.html"].decode())
        self.assertEqual(parsed, [self.fixture.old["bbapp"], {**self.gap, "au": 1}])
        self.assertIn('const LS_STATE = "preserve-this";', after["site/apps/bbapp.html"].decode())
        state = self.read(andrew.STATE_FILE)
        self.assertEqual(state["clips"]["approved-gap-t"]["source"], "Microsoft-Edge-TTS")
        self.assertFalse(state["clips"]["original-t"]["baseline_parameters_verified"])
        self.assertEqual(self.ensure(check=True)["generate"], 0)
        self.assertEqual(self.ensure()["changed"], [])
        self.assertEqual(after, self.snapshot())
        self.assertEqual(len(self.fixture.generated), 1)

    def test_wrong_voice_changed_text_and_corruption_fail_before_speech(self):
        baseline = self.snapshot()
        state = self.read(andrew.STATE_FILE)
        for mutate in (
            lambda: self.write(andrew.STATE_FILE, {**state, "voice": "en-GB-RyanNeural"}),
            lambda: (self.root / "site/apps/bbapp.html").write_text(
                baseline["site/apps/bbapp.html"].decode().replace("Original phrase.", "Changed phrase.")),
            lambda: (self.root / "site/packs/bbapp.mp3").write_bytes(
                baseline["site/packs/bbapp.mp3"][:2] + b"bad" + baseline["site/packs/bbapp.mp3"][5:]),
        ):
            for path, data in baseline.items():
                (self.root / path).write_bytes(data)
            mutate()
            before = self.snapshot()
            with self.assertRaises(ValueError):
                self.ensure()
            self.assertEqual(before, self.snapshot())
        self.assertEqual(self.fixture.generated, [])

    def test_unknown_audio_and_inconsistent_repair_are_not_adopted(self):
        state = self.read(andrew.STATE_FILE)
        del state["clips"]["original-t"]
        self.write(andrew.STATE_FILE, state)
        with self.assertRaisesRegex(ValueError, "Unreviewed"):
            self.ensure()
        self.assertEqual(self.fixture.generated, [])

    def test_deleted_verified_clip_requires_inspection_instead_of_silent_repair(self):
        indexes = self.read("tools/packs.json")
        del indexes["bbapp"]["original-t"]
        self.write("tools/packs.json", indexes)
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "Previously verified Andrew recording is missing"):
            self.ensure()
        self.assertEqual(before, self.snapshot())
        self.assertEqual(self.fixture.generated, [])

    def test_unexpected_audio_for_pending_repair_is_not_trusted_or_overwritten(self):
        indexes = self.read("tools/packs.json")
        indexes["bbapp"]["approved-gap-t"] = indexes["bbapp"]["original-t"]
        self.write("tools/packs.json", indexes)
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "Approved Andrew repair is inconsistent"):
            self.ensure()
        self.assertEqual(before, self.snapshot())
        self.assertEqual(self.fixture.generated, [])

    def test_synthesis_validation_and_build_failure_leave_no_partial_repairs(self):
        def failure(*args):
            raise RuntimeError("intentional failure")
        cases = [{"synthesizer": failure}, {"validator": failure}, {"builder": failure},
                 {"synthesizer": lambda clips, voice, directory: {}},
                 {"synthesizer": lambda clips, voice, directory: {c["key"]: b"broken" for c in clips}}]
        for kwargs in cases:
            before = self.snapshot()
            with self.subTest(kwargs=kwargs), self.assertRaises((ValueError, RuntimeError)):
                self.ensure(**kwargs)
            self.assertEqual(before, self.snapshot())
            self.assertFalse(list(self.root.glob(".andrew-stage-*")))

    def test_install_failure_rolls_back_pack_flags_and_state(self):
        import ensure_ryan_audio
        replace = ensure_ryan_audio.os.replace
        calls = 0
        def fail_third(source, destination):
            nonlocal calls
            calls += 1
            if calls == 3:
                raise OSError("disk full")
            return replace(source, destination)
        before = self.snapshot()
        with patch.object(ensure_ryan_audio.os, "replace", side_effect=fail_third):
            with self.assertRaisesRegex(OSError, "disk full"):
                self.ensure()
        self.assertEqual(before, self.snapshot())

    def test_daily_ledger_records_are_adopted_without_another_tts_request(self):
        self.ensure()
        self.fixture.append("bbapp")
        before = self.snapshot()
        calls = len(self.fixture.generated)
        with self.assertRaisesRegex(ValueError, "4 ledger records to adopt"):
            self.ensure(check=True)
        result = self.ensure()
        self.assertEqual(result["adopt"], 4)
        self.assertEqual(result["generate"], 0)
        self.assertEqual(len(self.fixture.generated), calls)
        for path in ("site/packs/bbapp.mp3", "site/apps/bbapp.html", "data/daily/2026-11-02-bbapp.json"):
            self.assertEqual(before[path], self.snapshot()[path])
        self.assertEqual(self.ensure(check=True)["generate"], 0)
        self.assertEqual(daily.status(self.root, "bbapp", today="2026-11-02")["state"], "complete")

    def test_tampered_daily_voice_or_audio_metadata_cannot_be_imported(self):
        self.ensure()
        self.fixture.append("bbapp")
        ledger_path = "data/daily/2026-11-02-bbapp.json"
        original = self.read(ledger_path)
        for field, value in (("voice", "en-GB-RyanNeural"), ("text", "Wrong spoken text."),
                             ("duration", 0), ("raw_sha256", "unknown")):
            ledger = copy.deepcopy(original)
            ledger["clips"]["new-0-t"][field] = value
            self.write(ledger_path, ledger)
            before = self.snapshot()
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.ensure()
            self.assertEqual(before, self.snapshot())

    def test_baseline_cannot_silently_accept_additional_missing_audio(self):
        with self.assertRaisesRegex(ValueError, "explicitly approved"):
            andrew.reviewed_baseline(self.root, {"approved-gap-t"}, source_commit="test")


if __name__ == "__main__":
    unittest.main()
