"""Full-text decisions need retrieved text; charting rows need full-text inclusion and controlled vocabulary."""
import csv
import pathlib
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = pathlib.Path(__file__).resolve().parents[1]
ROOT = SCRIPTS.parents[1]

def run(script, *args):
    return subprocess.run([sys.executable, str(SCRIPTS / script), *args], capture_output=True, text=True)

class FullTextTests(unittest.TestCase):
    def test_ft_decision_without_retrieved_text_is_rejected(self):
        with open(ROOT / "review-paper/fulltext/retrieval-status.csv", encoding="utf-8") as f:
            missing = next(r["Paper ID"] for r in csv.DictReader(f) if not r["Outcome"].startswith("Retrieved"))
        with tempfile.TemporaryDirectory() as d:
            src, out = pathlib.Path(d) / "in.txt", pathlib.Path(d) / "out.csv"
            src.write_text(f"{missing};I;;p.1;test\n", encoding="utf-8")
            r = run("expand_ft_decisions.py", "--input", str(src), "--output", str(out), "--date", "2026-10-23")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("No retrieved full text", r.stderr)

    def test_charting_rejects_bad_vocabulary_without_writing(self):
        chart = ROOT / "review-paper/charting/charting.csv"
        before = chart.read_bytes()
        with tempfile.TemporaryDirectory() as d:
            src = pathlib.Path(d) / "c.txt"
            fields = ["XNOTINCLUDED"] + ["x"] * 20
            src.write_text(" | ".join(fields) + "\n", encoding="utf-8")
            r = run("expand_charting.py", "--input", str(src), "--date", "2026-10-23")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("not a full-text Include", r.stderr)
        self.assertEqual(chart.read_bytes(), before)

if __name__ == "__main__":
    unittest.main()
