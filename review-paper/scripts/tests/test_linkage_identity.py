"""Protect established study identities across later discovery and replay."""
import csv
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]

class LinkageIdentityTests(unittest.TestCase):
    def test_new_candidates_preserve_existing_ids_and_replay_is_stable(self):
        source = ROOT / "review-paper/corpus"
        def read(path):
            with path.open(encoding="utf-8", newline="") as stream:
                return list(csv.DictReader(stream))
        with tempfile.TemporaryDirectory() as directory:
            target = pathlib.Path(directory)
            for name in ["corpus.csv", "records-ledger.csv", "version-linkage-candidates.csv", "fulltext-linkage.csv", "study-linkage.csv"]:
                shutil.copyfile(source / name, target / name)
            before = {r["Paper ID"]: r for r in read(target / "study-linkage.csv")}
            command = [sys.executable, str(ROOT / "review-paper/scripts/verify_version_linkage.py"), "--corpus-dir", str(target), "--date", "2026-11-04"]
            first = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            rows = read(target / "study-linkage.csv")
            after = {r["Paper ID"]: r for r in rows}
            for paper, old in before.items():
                self.assertIn(paper, after)
                self.assertEqual(after[paper]["Study ID"], old["Study ID"])
                self.assertEqual(after[paper]["Linkage Date"], old["Linkage Date"])
            second = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(read(target / "study-linkage.csv"), rows)
