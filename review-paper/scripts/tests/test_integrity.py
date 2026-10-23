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
        # Replay recreates the unscreened 13 October pilot. Later identification sources may add rows and
        # screening may fill decision fields; every replayed identification value must still be preserved.
        screening = {"Reviewer 1", "TA Decision R1", "Reviewer 2", "TA Decision R2", "TA Final", "TA Reason Code",
                     "Full text sought?", "Retrieval Result", "FT Decision R1", "FT Decision R2", "FT Final",
                     "FT Exclusion Code", "Decision Rationale", "Decision Date", "Adjudicator", "Study ID",
                     "Included in synthesis?", "Decision Integrity"}
        for generated in output.iterdir():
            saved = self.corpus / generated.name
            if generated.suffix == ".csv":
                header = generated.read_text(encoding="utf-8").splitlines()[0]
                fields = ["Event ID"] if "Event ID" in header else ["Run ID", "Search ID"] if "Run ID" in header else ["Paper ID"]
                key = lambda row: tuple(row[f] for f in fields)
                with saved.open(encoding="utf-8", newline="") as stream:
                    current = {key(row): row for row in csv.DictReader(stream)}
                with generated.open(encoding="utf-8", newline="") as stream:
                    for row in csv.DictReader(stream):
                        kept = current[key(row)]
                        identity = {k: v for k, v in row.items() if k not in screening and not (generated.name == "corpus.csv")}
                        self.assertEqual(identity, {k: kept[k] for k in identity}, generated.name + " " + str(key(row)))
            elif generated.name == "identity-registry.json":
                registry = json.loads(saved.read_text(encoding="utf-8"))
                for key, value in json.loads(generated.read_text(encoding="utf-8")).items():
                    self.assertEqual(registry[key], value)
            elif generated.name == "scope-counts.json":
                pilot = json.loads(generated.read_text(encoding="utf-8")); now = json.loads(saved.read_text(encoding="utf-8"))
                for key in ["crossref_occurrences", "seed_occurrences"]:
                    self.assertEqual(pilot[key], now[key])
            elif generated.name == "references-draft.bib":
                self.assertEqual(generated.read_text(encoding="utf-8"), saved.read_text(encoding="utf-8"))
        self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)
        command[-1] = str(self.corpus)
        self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)

if __name__ == "__main__":
    unittest.main()
