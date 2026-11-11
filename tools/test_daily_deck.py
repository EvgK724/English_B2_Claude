"""Daily publication regressions: idempotence, preservation and failure safety."""
import copy
import contextlib
import datetime as dt
import io
import json
import pathlib
import sys
import tempfile
import types
import unittest
from unittest.mock import AsyncMock, Mock, call, patch

import daily_deck as daily

TODAY = "2026-11-02"


def mp3(text):
    return b"\xff\xf3" + text.encode() * 40


def card(key, cid, term, added=TODAY):
    result = {"id": cid, "au": 1, "added": added, "term": term,
              "ru": "Перевод", "note": "Пояснение и типичная ошибка.",
              "ex": "We need a little more time.", "exru": "Нам нужно ещё немного времени."}
    result.update({"ipa": "/test/", "pos": "phrasal verb"} if key == "phrasal"
                  else {"who": "Персонаж", "reg": "разговорное"})
    return result


def batch(key):
    terms = ["Check in"] if key == "phrasal" else ["This is a new phrase.", "That is another phrase."]
    cards = [card(key, f"new-{i}", term) for i, term in enumerate(terms)]
    for value in cards:
        value["sources"] = [{"url": "https://example.org/source", "title": "Verified example",
                              "episode": "S01E01", "checked_quote": value["term"]}]
    return {"date": TODAY, "cards": cards}


class NoAudioReceived(Exception):
    """Offline equivalent of edge_tts.exceptions.NoAudioReceived."""


@contextlib.contextmanager
def fake_speech(outcomes):
    """Exercise the real retry loop without networking, ffmpeg or real waits."""
    outcomes = iter(outcomes)
    paths = []

    class Communicate:
        async def save(self, filename):
            path = pathlib.Path(filename)
            paths.append(path)
            if path.exists():
                raise AssertionError("Partial audio survived into the next attempt")
            outcome = next(outcomes)
            if isinstance(outcome, BaseException):
                path.write_bytes(b"partial audio that must not be published")
                raise outcome
            if outcome is not None:
                path.write_bytes(outcome)

    factory = Mock(side_effect=lambda *args, **kwargs: Communicate())
    module = types.SimpleNamespace(__version__=daily.VERSION, Communicate=factory,
                                   exceptions=types.SimpleNamespace(NoAudioReceived=NoAudioReceived))
    with patch.dict(sys.modules, {"edge_tts": module}), \
            patch.object(daily.shutil, "which", return_value="/fake/ffmpeg"), \
            patch.object(daily.asyncio, "sleep", new_callable=AsyncMock) as sleep, \
            contextlib.redirect_stderr(io.StringIO()) as stderr:
        yield types.SimpleNamespace(factory=factory, sleep=sleep, stderr=stderr, paths=paths)


class DailyDeckTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temporary.name)
        for directory in (".git", "tools", "site/apps", "site/packs"):
            (self.root / directory).mkdir(parents=True)
        catalog, indexes = {"apps": [], "groups": []}, {}
        state = {"schema": 1, "voice": "en-GB-RyanNeural", "apps": {"phrasal": {"clips": {}}}}
        self.old = {}
        for key in daily.CONFIG:
            previous = card(key, "original", "Original phrase.", "2026-10-28")
            self.old[key] = previous
            html = ("const CARDS = [\n" + daily.card_block(previous, key) + daily.deck_sync.MARK
                    + '\n];\nconst LS_STATE = "preserve-this";\n')
            (self.root / f"site/apps/{key}.html").write_text(html)
            raw = mp3(key)
            (self.root / f"site/packs/{key}.mp3").write_bytes(raw + raw)
            indexes[key] = {"original-t": [0, len(raw), 0.024], "original-x": [len(raw), len(raw), 0.024]}
            catalog["apps"].append({"key": key, "voice": daily.CONFIG[key]["label"], "ids": ["original"],
                                    "items": [{"id": "original", "term": previous["term"], "ru": "Перевод"}],
                                    "kw": "original", "ls": "preserve-this", "size": len(html.encode())})
        self.write("tools/catalog.json", catalog)
        self.write("tools/packs.json", indexes)
        self.write(daily.STATE_FILE, state)
        (self.root / "site/index.html").write_text("old shell")
        (self.root / "site/sw.js").write_text("old cache")
        self.generated = []

    def tearDown(self):
        self.temporary.cleanup()

    def write(self, path, value):
        (self.root / path).write_text(json.dumps(value))

    def read(self, path):
        return json.loads((self.root / path).read_text())

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*")
                if p.is_file() and ".git" not in p.relative_to(self.root).parts}

    def synthesize(self, clips, voice, directory):
        self.generated.append((copy.deepcopy(clips), voice))
        return {clip["key"]: mp3(clip["text"]) for clip in clips}

    def builder(self, root, stage, changes):
        # The real shell builder is already covered by its existing test suite.
        changes[pathlib.Path("site/index.html")] = b"new shell"
        changes[pathlib.Path("site/sw.js")] = b"new cache"

    def append(self, key="phrasal", value=None, **kwargs):
        return daily.append_batch(self.root, key, value or batch(key), today=TODAY,
                                  synthesizer=kwargs.pop("synthesizer", self.synthesize),
                                  validator=kwargs.pop("validator", lambda path: 1.25),
                                  trimmer=lambda raw: (raw, 0.024),
                                  builder=kwargs.pop("builder", self.builder), **kwargs)

    def test_timezone_boundary_and_status(self):
        self.assertEqual(daily.local_date(dt.datetime(2026, 11, 1, 20, 0, tzinfo=dt.timezone.utc)), TODAY)
        report = daily.status(self.root, "phrasal", today=TODAY)
        self.assertEqual(report["count_today"], 0)
        self.assertEqual(report["state"], "pending")
        self.assertEqual(report["existing_terms"], ["Original phrase."])

    def test_append_preserves_history_and_is_noop_on_retry(self):
        before = self.snapshot()
        old_index = self.read("tools/packs.json")
        result = self.append()
        self.assertEqual(result["status"], "appended")
        self.assertEqual(len(self.generated[0][0]), 2)
        self.assertEqual(self.generated[0][1], "en-GB-RyanNeural")
        after = self.snapshot()
        self.assertTrue(after["site/packs/phrasal.mp3"].startswith(before["site/packs/phrasal.mp3"]))
        self.assertEqual(before["site/packs/bbapp.mp3"], after["site/packs/bbapp.mp3"])
        self.assertEqual(before["site/apps/bbapp.html"], after["site/apps/bbapp.html"])
        html = after["site/apps/phrasal.html"].decode()
        self.assertEqual(daily.parse_cards(html)[0], self.old["phrasal"])
        self.assertIn('const LS_STATE = "preserve-this";', html)
        for name, location in old_index["phrasal"].items():
            self.assertEqual(self.read("tools/packs.json")["phrasal"][name], location)
        ledger = self.read(f"data/daily/{TODAY}-phrasal.json")
        self.assertEqual(ledger["cards"], batch("phrasal")["cards"])
        self.assertNotIn("sources:", html)
        clip = self.read(daily.STATE_FILE)["apps"]["phrasal"]["clips"]["new-0-t"]
        self.assertEqual(clip["rate"], "-5%")
        self.assertEqual(clip["packed_sha256"], ledger["clips"]["new-0-t"]["packed_sha256"])
        self.assertEqual(self.append()["status"], "already-complete")
        self.assertEqual(daily.status(self.root, "phrasal", today=TODAY)["state"], "complete")
        self.assertEqual(len(self.generated), 1)
        self.assertEqual(after, self.snapshot())

    def test_bb_batch_uses_andrew_and_does_not_touch_ryan_state(self):
        before = self.snapshot()
        self.append("bbapp")
        self.assertEqual(self.generated[0][1], "en-US-AndrewNeural")
        self.assertEqual(len(self.generated[0][0]), 4)
        self.assertEqual(before[str(daily.STATE_FILE)], self.snapshot()[str(daily.STATE_FILE)])
        self.assertEqual(self.append("bbapp")["status"], "already-complete")
        self.assertEqual(len(self.generated), 1)

    def test_wrong_date_count_sources_and_duplicate_terms_are_rejected_before_speech(self):
        cases = []
        wrong_date = batch("phrasal"); wrong_date["date"] = "2026-11-01"; cases.append(wrong_date)
        wrong_count = batch("phrasal"); wrong_count["cards"] *= 2; cases.append(wrong_count)
        missing_source = batch("phrasal"); missing_source["cards"][0]["sources"] = []; cases.append(missing_source)
        bad_source = batch("phrasal"); bad_source["cards"][0]["sources"][0]["url"] = "file:///secret"; cases.append(bad_source)
        duplicate = batch("phrasal"); duplicate["cards"][0]["term"] = "ORIGINAL   PHRASE!"; cases.append(duplicate)
        duplicate_id = batch("phrasal"); duplicate_id["cards"][0]["id"] = "original"; cases.append(duplicate_id)
        for value in cases:
            with self.subTest(value=value), self.assertRaises(ValueError):
                before = self.snapshot()
                self.append(value=value)
            self.assertEqual(before, self.snapshot())
        self.assertEqual(self.generated, [])

    def test_partial_and_conflicting_current_date_stop(self):
        self.append("bbapp")
        before = self.snapshot()
        different = batch("bbapp"); different["cards"][0]["note"] = "Другое пояснение"
        with self.assertRaisesRegex(ValueError, "partial or conflicting"):
            self.append("bbapp", different)
        self.assertEqual(before, self.snapshot())
        app = self.root / "site/apps/bbapp.html"
        html = app.read_text().replace(daily.card_block({k:v for k,v in batch("bbapp")["cards"][1].items()
                                                       if k != "sources"}, "bbapp"), "")
        app.write_text(html)
        partial = self.snapshot()
        with self.assertRaisesRegex(ValueError, "partial or conflicting"):
            self.append("bbapp")
        self.assertEqual(partial, self.snapshot())
        self.assertEqual(daily.status(self.root, "bbapp", today=TODAY)["state"], "conflict")
        self.assertEqual(len(self.generated), 1)

    def test_speech_validation_and_build_failures_leave_no_partial_changes(self):
        def failure(*args):
            raise RuntimeError("intentional failure")
        cases = [{"synthesizer": failure}, {"validator": failure}, {"builder": failure},
                 {"synthesizer": lambda clips, voice, directory: {}},
                 {"synthesizer": lambda clips, voice, directory: {c["key"]: b"broken" for c in clips}}]
        for kwargs in cases:
            before = self.snapshot()
            with self.subTest(kwargs=kwargs), self.assertRaises((ValueError, RuntimeError)):
                self.append(**kwargs)
            self.assertEqual(before, self.snapshot())
            self.assertFalse(list(self.root.glob(".daily-stage-*")))

    def test_install_failure_rolls_back_all_written_files(self):
        import ensure_ryan_audio
        replace = ensure_ryan_audio.os.replace
        calls = 0
        def fail_third(src, dst):
            nonlocal calls
            calls += 1
            if calls == 3:
                raise OSError("disk full")
            return replace(src, dst)
        before = self.snapshot()
        with patch.object(ensure_ryan_audio.os, "replace", side_effect=fail_third):
            with self.assertRaisesRegex(OSError, "disk full"):
                self.append()
        self.assertEqual(before, self.snapshot())

    def test_retry_detects_corrupt_completed_audio_without_regenerating(self):
        self.append()
        index = self.read("tools/packs.json")["phrasal"]["new-0-t"]
        path = self.root / "site/packs/phrasal.mp3"
        data = bytearray(path.read_bytes()); data[index[0] + 2] ^= 1; path.write_bytes(data)
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "differs from its ledger"):
            self.append()
        self.assertEqual(daily.status(self.root, "phrasal", today=TODAY)["state"], "conflict")
        self.assertEqual(before, self.snapshot())
        self.assertEqual(len(self.generated), 1)

    def test_status_detects_missing_audio_and_changed_source_evidence(self):
        self.append()
        ledger_path = f"data/daily/{TODAY}-phrasal.json"
        ledger = self.read(ledger_path)
        ledger["cards"][0]["sources"][0]["title"] = "Changed after publication"
        self.write(ledger_path, ledger)
        self.assertEqual(daily.status(self.root, "phrasal", today=TODAY)["state"], "conflict")
        ledger["cards"][0]["sources"][0]["title"] = "Verified example"
        self.write(ledger_path, ledger)
        index = self.read("tools/packs.json")
        del index["phrasal"]["new-0-x"]
        self.write("tools/packs.json", index)
        report = daily.status(self.root, "phrasal", today=TODAY)
        self.assertEqual(report["state"], "conflict")
        self.assertIn("missing audio", report["problem"])

    def test_no_audio_retries_then_preserves_voices_history_and_completed_clips(self):
        for key in daily.CONFIG:
            with self.subTest(key=key):
                before = self.snapshot()
                recordings = [mp3(f"clip-{i}") for i in range(daily.CONFIG[key]["count"] * 2)]
                # The first clip succeeds once; the second succeeds on its last attempt.
                outcomes = [recordings[0], NoAudioReceived("temporary"),
                            NoAudioReceived("temporary"), *recordings[1:]]
                with fake_speech(outcomes) as speech:
                    result = self.append(key, synthesizer=daily.synthesize)
                self.assertEqual(result["status"], "appended")
                self.assertEqual(speech.sleep.await_args_list, [call(2), call(4)])
                self.assertEqual(speech.factory.call_count, len(recordings) + 2)
                clips = [(c[field], daily.CONFIG[key]["voice"])
                         for c in batch(key)["cards"] for field in ("term", "ex")]
                expected = [clips[0], clips[1], clips[1], *clips[1:]]
                self.assertEqual(speech.factory.call_args_list,
                                 [call(*args, rate="-5%", pitch="+0Hz", volume="+0%")
                                  for args in expected])
                after = self.snapshot()
                pack_path = f"site/packs/{key}.mp3"
                self.assertEqual(after[pack_path], before[pack_path] + b"".join(recordings))
                other = "phrasal" if key == "bbapp" else "bbapp"
                for rel in (f"site/apps/{other}.html", f"site/packs/{other}.mp3"):
                    self.assertEqual(after[rel], before[rel])
                html = after[f"site/apps/{key}.html"].decode()
                self.assertEqual(daily.parse_cards(html)[0], self.old[key])
                self.assertIn('const LS_STATE = "preserve-this";', html)
                self.assertFalse(list(self.root.glob(".daily-stage-*")))
                self.assertTrue(all(not path.exists() for path in speech.paths))
                self.assertIn("clip=new-0-x", speech.stderr.getvalue())
                self.assertIn("attempt=2/3", speech.stderr.getvalue())
                self.assertNotIn(clips[1][0], speech.stderr.getvalue())
                # An idempotent append neither synthesizes again nor changes a byte.
                with fake_speech([]) as retry:
                    self.assertEqual(self.append(key, synthesizer=daily.synthesize)["status"], "already-complete")
                retry.factory.assert_not_called()
                self.assertEqual(self.snapshot(), after)

    def test_persistent_no_audio_fails_closed_after_three_attempts(self):
        before = self.snapshot()
        with fake_speech([mp3("first"), *[NoAudioReceived("no audio")] * 3]) as speech:
            with self.assertRaisesRegex(RuntimeError, "clip=new-0-x voice=en-US-AndrewNeural.*attempt=3/3.*batch not published"):
                self.append("bbapp", synthesizer=daily.synthesize)
        self.assertEqual(speech.factory.call_count, 4)
        self.assertEqual(speech.sleep.await_args_list, [call(2), call(4)])
        self.assertEqual(self.snapshot(), before)
        self.assertFalse(list(self.root.glob(".daily-stage-*")))
        self.assertTrue(all(not path.exists() for path in speech.paths))

    def test_missing_and_empty_audio_retry_and_success_has_no_staging_files(self):
        directory = self.root / "generated"
        clip = {"key": "short-term", "text": "Come again?", "rate": "-5%"}
        with fake_speech([None, b"", mp3("valid")]) as speech:
            result = daily.synthesize([clip], "en-US-AndrewNeural", directory)
        self.assertEqual(result, {clip["key"]: mp3("valid")})
        self.assertEqual(speech.sleep.await_args_list, [call(2), call(4)])
        self.assertEqual(list(directory.iterdir()), [])

    def test_success_needs_no_retry_or_wait_for_either_voice(self):
        for voice in (config["voice"] for config in daily.CONFIG.values()):
            directory = self.root / voice
            with fake_speech([mp3("valid")]) as speech:
                self.assertEqual(daily.synthesize([{"key": "one", "text": "Hello.", "rate": "-5%"}],
                                                 voice, directory), {"one": mp3("valid")})
            speech.factory.assert_called_once_with("Hello.", voice, rate="-5%", pitch="+0Hz", volume="+0%")
            speech.sleep.assert_not_awaited()
            self.assertEqual(speech.stderr.getvalue(), "")
            self.assertEqual(list(directory.iterdir()), [])

    def test_persistent_empty_output_is_bounded_and_cancellation_during_wait_stops(self):
        clip = {"key": "one", "text": "Hello.", "rate": "-5%"}
        for number, outcomes in enumerate(([None] * 3, [b""] * 3)):
            directory = self.root / f"empty-{number}"
            with fake_speech(outcomes) as speech:
                with self.assertRaisesRegex(RuntimeError, "attempt=3/3.*retry limit reached"):
                    daily.synthesize([clip], "en-US-AndrewNeural", directory)
            self.assertEqual(speech.factory.call_count, 3)
            self.assertEqual(speech.sleep.await_args_list, [call(2), call(4)])
            self.assertEqual(list(directory.iterdir()), [])
        directory = self.root / "cancelled-wait"
        with fake_speech([NoAudioReceived("temporary")]) as speech:
            speech.sleep.side_effect = daily.asyncio.CancelledError()
            with self.assertRaises(daily.asyncio.CancelledError):
                daily.synthesize([clip], "en-US-AndrewNeural", directory)
        self.assertEqual(speech.factory.call_count, 1)
        self.assertEqual(speech.sleep.await_args_list, [call(2)])
        self.assertEqual(list(directory.iterdir()), [])

    def test_other_failures_and_cancellation_are_not_retried_and_remove_partial_audio(self):
        for number, error in enumerate((RuntimeError("service denied"), ValueError("invalid voice"),
                                        PermissionError("disk denied"), daily.asyncio.CancelledError())):
            with self.subTest(error=type(error).__name__):
                directory = self.root / f"failure-{number}"
                with fake_speech([error]) as speech:
                    with self.assertRaises(type(error)):
                        daily.synthesize([{"key": "one", "text": "Hello.", "rate": "-5%"}],
                                         "en-US-AndrewNeural", directory)
                self.assertEqual(speech.factory.call_count, 1)
                speech.sleep.assert_not_awaited()
                self.assertEqual(list(directory.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
