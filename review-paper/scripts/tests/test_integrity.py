"""Regression checks for corruption detection and non-destructive replay."""
import csv
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]

class IntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)
        shutil.copytree(ROOT / "review-paper", self.root / "review-paper")
        self.corpus = self.root / "review-paper/corpus"

    def validate(self, optimized=False):
        return subprocess.run([sys.executable, *(["-O"] if optimized else []),
            str(self.root / "review-paper/scripts/validate_scope.py")], capture_output=True, text=True)

    def test_saved_snapshot_passes(self):
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_metadata_corruption_rejected(self):
        path = self.root / "review-paper/search-strategy/runs/BASELINE-METADATA-20261013/B03.xml"
        path.write_bytes(path.read_bytes() + b"corruption")
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Metadata hash mismatch", result.stderr)

    def test_count_corruption_rejected_even_when_optimized(self):
        path = self.corpus / "scope-counts.json"
        counts = json.loads(path.read_text())
        counts["unique_reports"] += 1
        path.write_text(json.dumps(counts))
        self.assertNotEqual(self.validate(optimized=True).returncode, 0)

    def test_duplicate_target_corruption_rejected(self):
        path = self.corpus / "identification-events.csv"
        with path.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            fields = reader.fieldnames
            rows = list(reader)
        next(row for row in rows if row["Duplicate of"])["Duplicate of"] = "NONEXISTENT"
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Incorrect duplicate target", result.stderr)

    def test_replay_matches_snapshot_and_rejects_overwrite(self):
        output = self.root / "replay"
        command = [sys.executable, str(self.root / "review-paper/scripts/build_corpus.py"), "--output-dir", str(output)]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        for generated in output.iterdir():
            saved = self.corpus / generated.name
            self.assertEqual(generated.read_text(encoding="utf-8"), saved.read_text(encoding="utf-8"), generated.name)
        self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)
        command[-1] = str(self.corpus)
        self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)

if __name__ == "__main__":
    unittest.main()
