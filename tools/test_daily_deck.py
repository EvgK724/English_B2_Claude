"""Daily publication regressions: idempotence, preservation and failure safety."""
import copy
import datetime as dt
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch

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


if __name__ == "__main__":
    unittest.main()
