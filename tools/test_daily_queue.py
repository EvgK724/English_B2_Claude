"""Regressions for the text-only handoff and atomic multi-deck queue processing."""
import copy
import concurrent.futures
import contextlib
import datetime as dt
import json
import pathlib
import unittest
from unittest.mock import patch

import daily_deck as daily
import daily_queue as queue
import test_daily_deck as fixtures

NOW = dt.datetime(2026, 11, 2, 7, tzinfo=dt.timezone.utc)
LATER = NOW + dt.timedelta(days=1)


class DailyQueueTest(unittest.TestCase):
    setUp = fixtures.DailyDeckTest.setUp
    tearDown = fixtures.DailyDeckTest.tearDown
    write = fixtures.DailyDeckTest.write
    read = fixtures.DailyDeckTest.read
    snapshot = fixtures.DailyDeckTest.snapshot
    synthesize = fixtures.DailyDeckTest.synthesize
    builder = fixtures.DailyDeckTest.builder
    append = fixtures.DailyDeckTest.append

    def prepare(self, key="phrasal", batch=None, now=NOW):
        return queue.prepare_queue(self.root, key, batch or fixtures.batch(key), now=now)

    def process(self, **kwargs):
        options = {"synthesizer": self.synthesize, "validator": lambda path: 1.25,
                   "trimmer": lambda raw: (raw, 0.024), "builder": self.builder}
        options.update(kwargs.pop("append_options", {}))
        return queue.process_queue(self.root, now=kwargs.pop("now", NOW), append_options=options, **kwargs)

    def envelope_path(self, key="phrasal", date=fixtures.TODAY):
        return f"data/requests/{date}-{key}.json"

    def test_prepare_only_writes_json_and_same_request_is_immutable(self):
        before = self.snapshot()
        result = self.prepare()
        self.assertEqual(result["status"], "queued")
        after = self.snapshot()
        self.assertEqual(set(after) - set(before), {self.envelope_path()})
        self.assertEqual({key: after[key] for key in before}, before)
        self.assertEqual(self.generated, [])
        self.assertEqual(self.prepare(now=NOW + dt.timedelta(hours=1))["status"], "already-queued")
        self.assertEqual(self.snapshot(), after)
        different = fixtures.batch("phrasal")
        different["cards"][0]["sources"][0]["title"] = "Other evidence"
        with self.assertRaisesRegex(ValueError, "different immutable"):
            self.prepare(batch=different)
        self.assertEqual(self.snapshot(), after)
        report = queue.queue_status(self.root, "phrasal", now=NOW)
        self.assertEqual(report["state"], "queued")
        self.assertEqual(report["request"], self.envelope_path())

    def test_completed_daily_quota_does_not_queue_more_cards(self):
        self.append()
        before = self.snapshot()
        different = fixtures.batch("phrasal")
        different["cards"][0]["id"] = "another-new-card"
        different["cards"][0]["term"] = "Another phrasal verb"
        self.assertEqual(self.prepare(batch=different)["status"], "already-complete")
        self.assertEqual(before, self.snapshot())

    def test_concurrent_preparers_create_one_immutable_request(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            results = list(executor.map(lambda _: self.prepare(), range(2)))
        self.assertEqual(sorted(result["status"] for result in results), ["already-queued", "queued"])
        self.assertEqual(len(list((self.root / queue.REQUESTS).glob("*.json"))), 1)
        self.assertEqual(self.read(self.envelope_path())["batch"], fixtures.batch("phrasal"))
        self.assertEqual(self.generated, [])

    def test_midnight_while_waiting_for_lock_or_validating_cannot_backdate_submission(self):
        before = self.snapshot()
        with patch.object(queue, "clock", return_value=NOW) as fake_clock:
            @contextlib.contextmanager
            def delayed_lock(root):
                fake_clock.return_value = LATER
                yield
            with patch.object(daily, "repository_lock", delayed_lock):
                with self.assertRaisesRegex(ValueError, "today's date"):
                    queue.prepare_queue(self.root, "phrasal", fixtures.batch("phrasal"))
        with patch.object(queue, "clock", side_effect=[NOW, LATER]):
            with self.assertRaisesRegex(ValueError, "date changed"):
                queue.prepare_queue(self.root, "phrasal", fixtures.batch("phrasal"))
        self.assertEqual(before, self.snapshot())

    def test_top_level_symlink_is_rejected_before_synthesis(self):
        self.prepare()
        site = self.root / "site"
        moved = self.root / "site-target"
        site.rename(moved)
        site.symlink_to(moved, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Symlink not supported"):
            self.process()
        self.assertEqual(self.generated, [])

    def test_both_voices_are_processed_once_and_requests_remain(self):
        for key in daily.CONFIG:
            self.prepare(key)
        with self.assertRaisesRegex(ValueError, "remain queued"):
            queue.verify_queue(self.root, now=NOW, require_complete=True)
        original_requests = {key: self.read(self.envelope_path(key)) for key in daily.CONFIG}
        result = self.process()
        self.assertEqual(len(result["processed"]), 2)
        self.assertEqual({voice for clips, voice in self.generated},
                         {"en-GB-RyanNeural", "en-US-AndrewNeural"})
        self.assertEqual(queue.verify_queue(self.root, now=NOW, require_complete=True)["pending"], 0)
        for key in daily.CONFIG:
            self.assertEqual(self.read(self.envelope_path(key)), original_requests[key])
            self.assertEqual(self.read(f"data/daily/{fixtures.TODAY}-{key}.json")["batch_sha256"],
                             original_requests[key]["batch_sha256"])
        before = self.snapshot()
        self.assertEqual(self.process()["status"], "already-complete")
        self.assertEqual(before, self.snapshot())
        self.assertEqual(len(self.generated), 2)
        self.assertEqual(self.prepare()["status"], "already-complete")

    def test_late_delivery_retries_original_day_without_backfilling(self):
        self.prepare()
        report = queue.queue_status(self.root, "phrasal", now=LATER)
        self.assertEqual(report["state"], "queued")
        self.assertEqual(report["queued_date"], fixtures.TODAY)
        next_batch = fixtures.batch("phrasal")
        next_batch["date"] = "2026-11-03"
        next_batch["cards"][0]["added"] = "2026-11-03"
        with self.assertRaisesRegex(ValueError, "outstanding request"):
            self.prepare(batch=next_batch, now=LATER)
        result = self.process(now=LATER)
        self.assertEqual(result["processed"][0]["date"], fixtures.TODAY)
        self.assertEqual(daily.status(self.root, "phrasal", today="2026-11-03")["count_today"], 0)
        with self.assertRaisesRegex(ValueError, "today's date"):
            self.prepare(now=LATER)

    def test_all_requests_are_validated_before_any_synthesis(self):
        self.prepare("phrasal")
        self.prepare("bbapp")
        path = self.envelope_path("phrasal")
        request = self.read(path)
        request["batch"]["cards"][0]["term"] = "Original phrase."
        request["batch_sha256"] = daily.batch_digest(request["batch"])
        self.write(path, request)
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.process()
        self.assertEqual(self.generated, [])
        self.assertEqual(before, self.snapshot())

    def test_failure_after_first_deck_does_not_install_either_deck(self):
        for key in daily.CONFIG:
            self.prepare(key)
        calls = []
        def fail_second(clips, voice, directory):
            calls.append(voice)
            if len(calls) == 2:
                raise RuntimeError("speech unavailable")
            return self.synthesize(clips, voice, directory)
        before = self.snapshot()
        with self.assertRaisesRegex(RuntimeError, "speech unavailable"):
            self.process(append_options={"synthesizer": fail_second})
        self.assertEqual(len(calls), 2)
        self.assertEqual(before, self.snapshot())
        self.assertFalse(list(self.root.glob(".queue-stage-*")))

    def test_persistent_no_audio_keeps_original_requests_and_both_decks_unpublished(self):
        for key in daily.CONFIG:
            self.prepare(key)
        before = self.snapshot()
        # Queue order is bbapp then phrasal: finish Andrew, fail Ryan's first clip.
        outcomes = [fixtures.mp3(f"andrew-{i}") for i in range(4)]
        outcomes += [fixtures.NoAudioReceived("service returned no audio")] * 3
        with fixtures.fake_speech(outcomes) as speech:
            with self.assertRaisesRegex(RuntimeError, "voice=en-GB-RyanNeural.*attempt=3/3.*batch not published"):
                self.process(append_options={"synthesizer": daily.synthesize})
        self.assertEqual(speech.factory.call_count, 7)
        self.assertEqual(speech.sleep.await_count, 2)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(queue.verify_queue(self.root, now=NOW)["pending"], 2)
        self.assertFalse(list(self.root.glob(".queue-stage-*")))
        self.assertTrue(all(not path.exists() for path in speech.paths))

    def test_install_failure_rolls_back_the_complete_output_bundle(self):
        import ensure_ryan_audio
        self.prepare()
        before = self.snapshot()
        replace = ensure_ryan_audio.os.replace
        calls = []
        def fail_root_second(src, dst):
            relative = pathlib.Path(dst).resolve().relative_to(self.root.resolve())
            if not any(part.startswith(".queue-stage-") for part in relative.parts):
                calls.append(dst)
                if len(calls) == 2:
                    raise OSError("disk unavailable")
            return replace(src, dst)
        with patch.object(ensure_ryan_audio.os, "replace", side_effect=fail_root_second):
            with self.assertRaisesRegex(OSError, "disk unavailable"):
                self.process()
        self.assertEqual(len(calls), 2)
        self.assertEqual(before, self.snapshot())

    def test_uncooperative_concurrent_change_is_not_overwritten(self):
        self.prepare()
        before = self.snapshot()
        def changed_input(*args, **kwargs):
            result = daily.append_batch(*args, **kwargs)
            (self.root / "site/index.html").write_text("concurrent new content")
            return result
        with self.assertRaisesRegex(ValueError, "inputs changed"):
            self.process(appender=changed_input)
        after = self.snapshot()
        self.assertEqual(after.pop("site/index.html"), b"concurrent new content")
        before.pop("site/index.html")
        self.assertEqual(after, before)

    def test_tampered_or_missing_receipt_fails_completed_verification(self):
        self.prepare()
        self.process()
        path = self.envelope_path()
        original = self.read(path)
        changed = copy.deepcopy(original)
        changed["batch"]["cards"][0]["sources"][0]["title"] = "Rewritten evidence"
        changed["batch_sha256"] = daily.batch_digest(changed["batch"])
        self.write(path, changed)
        self.assertEqual(queue.queue_status(self.root, "phrasal", now=NOW)["state"], "conflict")
        with self.assertRaisesRegex(ValueError, "differs from completed"):
            queue.verify_queue(self.root, now=NOW)
        self.write(path, original)
        (self.root / f"data/daily/{fixtures.TODAY}-phrasal.json").unlink()
        with self.assertRaisesRegex(ValueError, "matching daily ledger"):
            queue.verify_queue(self.root, now=NOW)

    def test_invalid_request_dates_hashes_paths_and_submission_are_rejected(self):
        self.prepare()
        path = self.envelope_path()
        original = self.read(path)
        variations = []
        for field, value in (("batch_sha256", "wrong"), ("schema", True),
                             ("deck", "../phrasal"), ("submitted_at", "2026-11-04T07:00:00Z"),
                             ("submitted_at", "2026-11-01T07:00:00Z"),
                             ("submitted_at", "2026-11-02T07:00:00")):
            changed = copy.deepcopy(original); changed[field] = value; variations.append(changed)
        changed = copy.deepcopy(original); changed["batch"]["date"] = "2026-02-30"; variations.append(changed)
        for changed in variations:
            self.write(path, changed)
            with self.subTest(changed=changed), self.assertRaises((ValueError, TypeError)):
                self.process()
            self.assertEqual(self.generated, [])
        self.write(path, original)
        (self.root / path).rename(self.root / "data/requests/wrong-name.json")
        with self.assertRaisesRegex(ValueError, "filename"):
            self.process()

    def test_multiple_outstanding_requests_for_same_deck_fail_closed(self):
        self.prepare()
        original = self.read(self.envelope_path())
        request = copy.deepcopy(original)
        request["batch"]["date"] = "2026-11-01"
        request["batch"]["cards"][0].update(added="2026-11-01", id="older-queued", term="Different term")
        request["submitted_at"] = "2026-11-01T07:00:00Z"
        request["batch_sha256"] = daily.batch_digest(request["batch"])
        self.write("data/requests/2026-11-01-phrasal.json", request)
        with self.assertRaisesRegex(ValueError, "More than one outstanding"):
            self.process()
        self.assertEqual(self.generated, [])

    def test_duplicate_source_invalid_number_and_symlink_are_rejected_without_tts(self):
        value = fixtures.batch("phrasal")
        value["cards"][0]["term"] = "ORIGINAL phrase!"
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.prepare(batch=value)
        value = fixtures.batch("phrasal")
        value["cards"][0]["sources"][0]["extra"] = float("nan")
        with self.assertRaises(ValueError):
            self.prepare(batch=value)
        self.prepare()
        path = self.root / self.envelope_path()
        outside = self.root / "request-copy.json"
        path.rename(outside)
        path.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "regular JSON"):
            self.process()
        self.assertEqual(self.generated, [])


if __name__ == "__main__":
    unittest.main()
