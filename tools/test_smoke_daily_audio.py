"""Exercise live-smoke orchestration with a mock speech provider, never a network call."""
import copy
import os
import unittest
from unittest.mock import patch

import daily_queue as queue
import smoke_daily_audio as smoke
import test_daily_deck as daily_fixture


class SpeechSmokeTest(unittest.TestCase):
    def setUp(self):
        self.fixture = daily_fixture.DailyDeckTest("test_timezone_boundary_and_status")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.actual_process = queue.process_queue

    def mock_process(self, root, **kwargs):
        return self.actual_process(root, **kwargs, append_options={
            "synthesizer": self.fixture.synthesize,
            "validator": lambda path: 1.25,
            "trimmer": lambda raw: (raw, 0.024),
            "builder": self.fixture.builder,
        })

    def run_mock_smoke(self):
        with patch.dict(os.environ, {"GITHUB_ACTIONS": "true", "GITHUB_RUN_ID": "123456"}), \
                patch.object(smoke, "source_digest", return_value="a" * 64), \
                patch.object(queue, "process_queue", side_effect=self.mock_process), \
                patch.object(smoke.daily, "validate_audio", return_value=1.25):
            return smoke.run(self.root)

    def test_roundtrip_covers_both_voices_preserves_source_and_retry_uses_evidence(self):
        before = smoke.fingerprint(self.root)
        result = self.run_mock_smoke()
        self.assertEqual(result["status"], "fresh-speech-queue-passed")
        self.assertEqual(result["new_recordings"], 6)
        self.assertEqual({voice for _, voice in self.fixture.generated},
                         {"en-GB-RyanNeural", "en-US-AndrewNeural"})
        self.assertEqual(len(self.fixture.generated), 2)
        self.assertEqual(smoke.fingerprint(self.root), before)
        self.assertEqual(self.run_mock_smoke()["status"], "verified-evidence-current")
        self.assertEqual(len(self.fixture.generated), 2)

    def test_corrupt_evidence_is_not_trusted(self):
        self.run_mock_smoke()
        evidence = smoke.load_json(self.root / smoke.STATE)
        self.assertTrue(smoke.valid_evidence(evidence, "a" * 64))
        for change in (float("nan"), float("inf"), "1.25", True, 0):
            broken = copy.deepcopy(evidence)
            next(iter(broken["decks"]["bbapp"]["clips"].values()))["duration"] = change
            self.assertFalse(smoke.valid_evidence(broken, "a" * 64))
        broken = copy.deepcopy(evidence)
        next(iter(broken["decks"]["phrasal"]["clips"].values()))["packed_sha256"] = "z" * 64
        self.assertFalse(smoke.valid_evidence(broken, "a" * 64))
        self.assertFalse(smoke.valid_evidence(evidence, "b" * 64))
        broken["decks"] = []
        self.assertFalse(smoke.valid_evidence(broken, "a" * 64))

    def test_new_live_test_is_refused_outside_authorized_actions_executor(self):
        with patch.dict(os.environ, {"GITHUB_ACTIONS": "false"}), \
                patch.object(smoke, "source_digest", return_value="a" * 64):
            with self.assertRaisesRegex(ValueError, "authorized GitHub Actions"):
                smoke.run(self.root)
        self.assertEqual(self.fixture.generated, [])
        self.assertFalse((self.root / smoke.STATE).exists())


if __name__ == "__main__":
    unittest.main()
