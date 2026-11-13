"""Correction publication regressions; all speech and Git history are local fixtures."""
import datetime as dt
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import build_publication as publication
import daily_deck as daily
import daily_queue as queue
import test_daily_deck as fixtures


TOOLS = pathlib.Path(__file__).resolve().parent
NOW = dt.datetime(2026, 11, 2, 7, tzinfo=dt.timezone.utc)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def files(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*")
            if p.is_file() and ".git" not in p.relative_to(root).parts
            and "__pycache__" not in p.relative_to(root).parts}


class PublicationTest(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.DailyDeckTest("test_timezone_boundary_and_status")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        outputs = tempfile.TemporaryDirectory()
        self.addCleanup(outputs.cleanup)
        self.outputs = pathlib.Path(outputs.name)
        batch = fixtures.batch("bbapp")
        batch["cards"][0]["ru"] = "Я\u00a0весь внимание. Готов выслушать."
        queue.prepare_queue(self.root, "bbapp", batch, now=NOW)
        self.process(now=NOW)
        self.card = batch["cards"][0]
        # Use the production shell builder, with both fixture decks and their
        # small fake MP3 packs. No browser, speech client or network is involved.
        catalog = self.fixture.read("tools/catalog.json")
        for app in catalog["apps"]:
            app.update(title=app["key"], group="vocab", desc="Fixture", en="fixture", deck=True)
        self.fixture.write("tools/catalog.json", catalog)
        for name in ("mk_shell.py", "shell.html", "head.html", "sw.js", "silent.mp3"):
            shutil.copyfile(TOOLS / name, self.root / "tools" / name)
        (self.root / "site/theme.css").write_text("body{color:white}")
        (self.root / "site/fonts").mkdir()
        for name in ("manifest.webmanifest", "apple-touch-icon.png", "favicon.png", "icon-192.png", "icon-512.png"):
            (self.root / "site" / name).write_bytes(b"fixture")
        (self.root / "index.html").write_text('<meta http-equiv="refresh" content="0;url=site/">')
        (self.root / ".nojekyll").write_bytes(b"")
        self.rebuild_source()

    def process(self, *, now):
        return queue.process_queue(self.root, now=now, append_options={
            "synthesizer": self.fixture.synthesize,
            "validator": lambda path: 1.25,
            "trimmer": lambda raw: (raw, 0.024),
            "builder": self.fixture.builder,
        })

    def rebuild_source(self):
        subprocess.run([sys.executable, str(self.root / "tools/mk_shell.py")],
                       cwd=self.root, check=True, capture_output=True)

    def correction(self, **updates):
        value = {
            "schema": 1,
            "deck": "bbapp",
            "card_id": self.card["id"],
            "ledger_date": fixtures.TODAY,
            "request_sha256": sha((self.root / f"data/requests/{fixtures.TODAY}-bbapp.json").read_bytes()),
            "ledger_sha256": sha((self.root / f"data/daily/{fixtures.TODAY}-bbapp.json").read_bytes()),
            "revision": 1,
            "previous_sha256": None,
            "changes": {
                "ru": {"from": self.card["ru"], "to": "Внимательно слушаю. Готов выслушать."},
                "exru": {"from": self.card["exru"], "to": "Нам понадобится ещё немного времени."},
            },
            "reason": "Исправлен русский перевод.",
        }
        value.update(updates)
        return value

    def write_correction(self, value=None, *, name=None):
        value = value or self.correction()
        directory = self.root / "data/corrections"
        directory.mkdir(parents=True, exist_ok=True)
        name = name or f"{value['deck']}-{value['card_id']}-{value['revision']:04d}.json"
        path = directory / name
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
        return path

    def build(self, name="published"):
        output = self.outputs / name
        report = publication.build_publication(self.root, output, check_history=False)
        return output, report

    def test_empty_overlay_reproduces_source_site_and_does_not_write_source(self):
        before = files(self.root)
        output, report = self.build()
        self.assertEqual(report["corrections"], 0)
        expected = {p: b for p, b in before.items() if p.startswith("site/") or p in ("index.html", ".nojekyll")}
        self.assertEqual(files(output), expected)
        self.assertEqual(files(self.root), before)

    def test_corrected_artifact_preserves_history_srs_english_and_all_audio(self):
        value = self.correction()
        self.write_correction(value)
        before = files(self.root)
        with patch.object(daily, "synthesize", side_effect=AssertionError("Publication must not synthesize")):
            output, report = self.build()
        self.assertEqual(report["corrections"], 1)
        self.assertEqual(files(self.root), before)
        expected_cards = daily.parse_cards(before["site/apps/bbapp.html"].decode())
        expected = next(c for c in expected_cards if c["id"] == self.card["id"])
        expected.update({field: change["to"] for field, change in value["changes"].items()})
        actual_html = (output / "site/apps/bbapp.html").read_text()
        self.assertEqual(daily.parse_cards(actual_html), expected_cards)
        self.assertIn('const LS_STATE = "preserve-this";', actual_html)
        for path, data in before.items():
            if path.startswith("site/") and path not in ("site/apps/bbapp.html", "site/index.html", "site/sw.js"):
                self.assertEqual((output / path).read_bytes(), data, path)
        self.assertFalse((output / "tools").exists())
        self.assertFalse((output / "data").exists())
        self.assertEqual(queue.verify_queue(self.root, now=NOW, require_complete=True)["pending"], 0)

    def test_effective_catalog_app_hash_and_sw_agree_pack_hash_stays_the_same(self):
        value = self.correction()
        self.write_correction(value)
        output, _ = self.build()
        source_shell = (self.root / "site/index.html").read_text()
        shell = (output / "site/index.html").read_text()
        def constant(text, name):
            return json.loads(re.search(r"^const " + name + r" = (.*);$", text, re.M).group(1))
        catalog, versions = constant(shell, "CAT"), constant(shell, "VER")
        source_versions = constant(source_shell, "VER")
        app = next(a for a in catalog["apps"] if a["key"] == "bbapp")
        item = next(c for c in app["items"] if c["id"] == self.card["id"])
        self.assertEqual(item["ru"], "Внимательно слушаю")
        self.assertEqual(versions["a"]["bbapp"], sha((output / "site/apps/bbapp.html").read_bytes())[:8])
        self.assertNotEqual(versions["a"]["bbapp"], source_versions["a"]["bbapp"])
        self.assertEqual(versions["p"], source_versions["p"])
        self.assertEqual(constant(shell, "PACKS"), constant(source_shell, "PACKS"))
        sw = (output / "site/sw.js").read_text()
        self.assertIn(f'apps/bbapp.html?v={versions["a"]["bbapp"]}', sw)
        self.assertNotEqual(sw, (self.root / "site/sw.js").read_text())

    def test_repeated_build_is_byte_identical_without_reapplying_into_source(self):
        self.write_correction()
        before = files(self.root)
        first, _ = self.build("first")
        second, _ = self.build("second")
        self.assertEqual(files(first), files(second))
        self.assertEqual(files(self.root), before)

    def test_successive_correction_uses_prior_effective_text_and_hash(self):
        first = self.correction()
        path = self.write_correction(first)
        second = self.correction(revision=2, previous_sha256=sha(path.read_bytes()), changes={
            "ru": {"from": first["changes"]["ru"]["to"], "to": "Я внимательно слушаю."},
        })
        self.write_correction(second)
        output, report = self.build()
        actual = next(c for c in daily.parse_cards((output / "site/apps/bbapp.html").read_text())
                      if c["id"] == self.card["id"])
        self.assertEqual(report["corrections"], 2)
        self.assertEqual(actual["ru"], "Я внимательно слушаю.")
        self.assertEqual(actual["exru"], first["changes"]["exru"]["to"])

    def test_future_daily_batch_keeps_correction_and_preexisting_recordings(self):
        self.write_correction()
        old_pack = (self.root / "site/packs/bbapp.mp3").read_bytes()
        next_day = NOW + dt.timedelta(days=1)
        batch = fixtures.batch("bbapp")
        batch["date"] = next_day.date().isoformat()
        for i, card in enumerate(batch["cards"]):
            card.update(id=f"tomorrow-{i}", term=f"Another useful example number {i}.", added=batch["date"])
        queue.prepare_queue(self.root, "bbapp", batch, now=next_day)
        self.process(now=next_day)
        self.rebuild_source()
        before = files(self.root)
        output, _ = self.build()
        self.assertEqual(files(self.root), before)
        pack = (output / "site/packs/bbapp.mp3").read_bytes()
        self.assertTrue(pack.startswith(old_pack))
        self.assertEqual(pack, (self.root / "site/packs/bbapp.mp3").read_bytes())
        cards = daily.parse_cards((output / "site/apps/bbapp.html").read_text())
        self.assertEqual([c["id"] for c in cards[-2:]], ["tomorrow-0", "tomorrow-1"])
        self.assertEqual(next(c for c in cards if c["id"] == self.card["id"])["ru"],
                         "Внимательно слушаю. Готов выслушать.")
        self.assertEqual(queue.verify_queue(self.root, now=next_day, require_complete=True)["pending"], 0)

    def test_preflight_allows_unrelated_pending_request_but_build_blocks_it(self):
        self.write_correction()
        queue.prepare_queue(self.root, "phrasal", fixtures.batch("phrasal"), now=NOW)
        self.assertEqual(publication.check_corrections(self.root, check_history=False)["corrections"], 1)
        with self.assertRaises(ValueError):
            self.build()
        self.assertFalse((self.outputs / "published").exists())

    def test_invalid_record_shapes_and_forbidden_fields_fail_closed(self):
        base = self.correction()
        invalid = [
            {**base, "schema": True}, {**base, "schema": 2}, {**base, "unknown": "value"},
            {**base, "revision": True}, {**base, "revision": 0}, {**base, "revision": 1.5},
            {**base, "previous_sha256": "a" * 64}, {**base, "reason": ""},
            {**base, "request_sha256": "0" * 64}, {**base, "ledger_sha256": "0" * 64},
            {**base, "changes": {}}, {**base, "changes": []},
            {**base, "changes": {"term": {"from": self.card["term"], "to": "Changed English."}}},
            {**base, "changes": {"id": {"from": self.card["id"], "to": "another-id"}}},
            {**base, "changes": {"note": {"from": self.card["note"], "to": "Другое пояснение."}}},
            {**base, "changes": {"ru": {"from": self.card["ru"], "to": self.card["ru"]}}},
            {**base, "changes": {"ru": {"from": self.card["ru"], "to": ""}}},
            {**base, "changes": {"ru": {"from": self.card["ru"], "to": "Две\nстроки"}}},
            {**base, "changes": {"ru": {"from": self.card["ru"], "to": "Текст </script>"}}},
            {**base, "changes": {"ru": {"from": self.card["ru"], "to": "Две\u2028строки"}}},
            {**base, "changes": {"ru": {"from": self.card["ru"], "to": "Текст", "extra": True}}},
        ]
        path = self.write_correction(base)
        for value in invalid:
            with self.subTest(value=value):
                path.write_text(json.dumps(value, ensure_ascii=False))
                before = files(self.root)
                with self.assertRaises(ValueError):
                    publication.check_corrections(self.root, check_history=False)
                self.assertEqual(files(self.root), before)

    def test_from_value_must_match_exactly_including_nonbreaking_spaces(self):
        value = self.correction()
        value["changes"]["ru"]["from"] = self.card["ru"].replace("\u00a0", " ")
        self.write_correction(value)
        with self.assertRaises(ValueError):
            publication.check_corrections(self.root, check_history=False)

    def test_unknown_target_and_uncompleted_card_are_rejected(self):
        for card_id in ("absent", "original"):
            with self.subTest(card_id=card_id):
                path = self.write_correction(self.correction(card_id=card_id))
                with self.assertRaises(ValueError):
                    publication.check_corrections(self.root, check_history=False)
                path.unlink()

    def test_revision_gap_bad_link_and_conflicting_sequence_are_rejected(self):
        first = self.correction()
        path = self.write_correction(first)
        second = self.correction(revision=2, previous_sha256=sha(path.read_bytes()), changes={
            "ru": {"from": first["changes"]["ru"]["to"], "to": "Следующий перевод."},
        })
        for updates in ({"revision": 3}, {"previous_sha256": "0" * 64},
                        {"changes": first["changes"]}):
            with self.subTest(updates=updates):
                candidate = self.write_correction({**second, **updates})
                with self.assertRaises(ValueError):
                    publication.check_corrections(self.root, check_history=False)
                candidate.unlink()

    def test_duplicate_keys_malformed_json_and_wrong_filename_are_rejected(self):
        path = self.write_correction()
        original = path.read_text()
        for data in ('{"schema":1,"schema":1}', '{"schema": NaN}', '{"schema":',
                     original.replace('"schema": 1,', '"schema": 1, "schema": 1,')):
            with self.subTest(data=data[:60]):
                path.write_text(data)
                with self.assertRaises(ValueError):
                    publication.check_corrections(self.root, check_history=False)
        path.write_text(original)
        path.rename(path.with_name("wrong-name.json"))
        with self.assertRaises(ValueError):
            publication.check_corrections(self.root, check_history=False)

    def test_correction_symlinks_and_nested_files_are_rejected(self):
        path = self.write_correction()
        target = self.outputs / "record.json"
        target.write_bytes(path.read_bytes())
        path.unlink()
        path.symlink_to(target)
        with self.assertRaises(ValueError):
            publication.check_corrections(self.root, check_history=False)
        path.unlink()
        nested = path.parent / "nested"
        nested.mkdir()
        shutil.copyfile(target, nested / path.name)
        with self.assertRaises(ValueError):
            publication.check_corrections(self.root, check_history=False)

    def test_correction_cannot_bless_mutated_request_history(self):
        request_path = self.root / f"data/requests/{fixtures.TODAY}-bbapp.json"
        request = json.loads(request_path.read_text())
        request["batch"]["cards"][0]["ru"] = "Изменённая история"
        request["batch_sha256"] = daily.batch_digest(request["batch"])
        request_path.write_text(json.dumps(request, ensure_ascii=False))
        self.write_correction()  # Even an updated anchor cannot replace the old equality gate.
        with self.assertRaises(ValueError):
            publication.check_corrections(self.root, check_history=False)

    def test_existing_destination_and_source_destination_are_not_overwritten(self):
        self.write_correction()
        output = self.outputs / "existing"
        output.mkdir()
        (output / "keep").write_bytes(b"keep")
        before = files(self.root)
        for destination in (output, self.root, self.root / "site", self.root / "site/new-output"):
            with self.subTest(destination=destination):
                with self.assertRaises((ValueError, FileExistsError)):
                    publication.build_publication(self.root, destination, check_history=False)
        self.assertEqual((output / "keep").read_bytes(), b"keep")
        self.assertEqual(files(self.root), before)

    def test_invalid_correction_leaves_no_partial_artifact(self):
        self.write_correction(self.correction(request_sha256="0" * 64))
        before = files(self.root)
        with self.assertRaises(ValueError):
            self.build()
        self.assertFalse((self.outputs / "published").exists())
        self.assertEqual(files(self.root), before)

    def test_shell_failure_leaves_no_partial_artifact_or_source_changes(self):
        self.write_correction()
        before = files(self.root)
        with patch.object(publication, "build_shell", side_effect=RuntimeError("Build failed")):
            with self.assertRaisesRegex(RuntimeError, "Build failed"):
                self.build()
        self.assertFalse((self.outputs / "published").exists())
        self.assertEqual(list(self.outputs.iterdir()), [])
        self.assertEqual(files(self.root), before)

    def test_concurrent_source_change_stops_publication(self):
        self.write_correction()
        path = self.root / "site/theme.css"
        original = path.read_bytes()
        builder = publication.build_shell
        def concurrent_change(*args):
            builder(*args)
            path.write_bytes(original + b"\n/* Another writer changed the source. */")
        try:
            with patch.object(publication, "build_shell", side_effect=concurrent_change):
                with self.assertRaises(ValueError):
                    self.build()
            self.assertFalse((self.outputs / "published").exists())
            # The builder detects another writer; it must not undo their edit.
            self.assertNotEqual(path.read_bytes(), original)
        finally:
            path.write_bytes(original)

    def test_shell_builder_cannot_change_or_extend_verified_projection(self):
        self.write_correction()
        before = files(self.root)
        builder = publication.build_shell
        target = pathlib.Path("site/apps/bbapp.html")
        for mode in ("mutate", "remove", "add-other-deck"):
            with self.subTest(mode=mode):
                def unsafe_builder(root, stage, changes):
                    builder(root, stage, changes)
                    if mode == "mutate":
                        changes[target] += b"\n<script>unreviewedCode()</script>"
                    elif mode == "remove":
                        del changes[target]
                    else:
                        changes[pathlib.Path("site/apps/phrasal.html")] = b"Unexpected app replacement"
                with patch.object(publication, "build_shell", side_effect=unsafe_builder):
                    with self.assertRaisesRegex(ValueError, "verified card projection"):
                        self.build(mode)
                self.assertFalse((self.outputs / mode).exists())
                self.assertEqual(files(self.root), before)

    def test_destination_created_during_exclusive_reservation_is_never_overwritten(self):
        self.write_correction()
        before = files(self.root)
        output = self.outputs / "published"
        mkdir = pathlib.Path.mkdir
        injected = False
        def competing_writer(path, *args, **kwargs):
            nonlocal injected
            if path == output and not injected:
                injected = True
                mkdir(path)
                (path / "other-writer").write_bytes(b"Do not overwrite")
            return mkdir(path, *args, **kwargs)
        with patch.object(pathlib.Path, "mkdir", competing_writer):
            with self.assertRaises(FileExistsError):
                self.build()
        self.assertTrue(injected)
        self.assertEqual(files(output), {"other-writer": b"Do not overwrite"})
        self.assertEqual(files(self.root), before)

    def test_install_failure_cleans_only_its_empty_reservation(self):
        self.write_correction()
        before = files(self.root)
        with patch.object(publication.os, "rename", side_effect=OSError("Install failed")):
            with self.assertRaisesRegex(OSError, "Install failed"):
                self.build()
        self.assertFalse((self.outputs / "published").exists())
        self.assertEqual(list(self.outputs.iterdir()), [])
        self.assertEqual(files(self.root), before)


class CorrectionHistoryTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = pathlib.Path(temporary.name)
        self.root = self.base / "repo"
        self.root.mkdir()
        self.git("init", "-q")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "commit", "--allow-empty", "-qm", "Initial fixture")
        self.directory = self.root / "data/corrections"
        self.directory.mkdir(parents=True)
        self.path = self.directory / "bbapp-phrase-0001.json"

    def git(self, *args, root=None):
        return subprocess.run(["git", *args], cwd=root or self.root, check=True,
                              capture_output=True, text=True).stdout.strip()

    def commit(self, message):
        self.git("add", "-A")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "commit", "-qm", message)

    def baseline(self):
        self.path.write_text('{"fixture":1}\n')
        self.commit("Add first correction")

    def test_additions_and_new_uncommitted_records_are_allowed(self):
        publication.verify_history(self.root)
        self.baseline()
        publication.verify_history(self.root)
        second = self.directory / "bbapp-phrase-0002.json"
        second.write_text('{"fixture":2}\n')
        publication.verify_history(self.root)
        self.commit("Append another correction")
        publication.verify_history(self.root)

    def test_modified_or_missing_committed_record_is_rejected_before_commit(self):
        self.baseline()
        original = self.path.read_bytes()
        self.path.write_text('{"fixture":2}\n')
        with self.assertRaises(ValueError):
            publication.verify_history(self.root)
        self.path.write_bytes(original)
        self.path.unlink()
        with self.assertRaises(ValueError):
            publication.verify_history(self.root)

    def test_modification_followed_by_restoration_still_violates_history(self):
        self.baseline()
        original = self.path.read_bytes()
        self.path.write_text('{"fixture":2}\n')
        self.commit("Modify old correction")
        self.path.write_bytes(original)
        self.commit("Restore old correction")
        with self.assertRaises(ValueError):
            publication.verify_history(self.root)

    def test_committed_deletion_or_rename_is_rejected(self):
        for action in ("delete", "rename"):
            with self.subTest(action=action):
                # Separate repositories keep each history case independent.
                original_root = self.root
                candidate = self.base / action
                self.git("clone", "-q", str(original_root), str(candidate))
                self.root = candidate
                path = candidate / "data/corrections/bbapp-phrase-0001.json"
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('{"fixture":1}\n')
                self.commit("Add correction")
                if action == "delete":
                    path.unlink()
                else:
                    path.rename(path.with_name("bbapp-phrase-0002.json"))
                self.commit("Remove or rename correction")
                with self.assertRaises(ValueError):
                    publication.verify_history(candidate)
                self.root = original_root

    def test_shallow_history_is_not_sufficient_evidence(self):
        self.baseline()
        clone = self.base / "shallow"
        self.git("clone", "--depth=1", "-q", self.root.as_uri(), str(clone))
        with self.assertRaises(ValueError):
            publication.verify_history(clone)

    def test_merge_that_rewrites_existing_correction_is_rejected(self):
        self.baseline()
        main_branch = self.git("branch", "--show-current")
        self.git("checkout", "-qb", "rewrite-correction")
        self.path.write_text('{"fixture":2}\n')
        self.commit("Rewrite old correction on a branch")
        self.git("checkout", "-q", main_branch)
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "merge", "--no-ff", "-qm", "Merge rewritten correction", "rewrite-correction")
        with self.assertRaises(ValueError):
            publication.verify_history(self.root)


if __name__ == "__main__":
    unittest.main()
