"""Selection figures must distinguish identified, reviewed and pending reports."""
import copy
import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from review_progress import derive_flow

class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.counts = {"retrieval_occurrences": 6, "duplicate_occurrences": 1,
                       "crossref_occurrences": 1, "seed_occurrences": 1, "openalex_occurrences": 4}
        def row(pid, ta, ft="Pending"):
            return {"Paper ID": pid, "TA Final": ta, "FT Final": ft, "FT Exclusion Code": ""}
        self.ledger = [row("A", "Retrieve full text", "Include"), row("B", "Pending"),
                       row("C", "Exclude"), row("D", "Background/supporting"), row("E", "Retrieve full text")]
        self.status = [{"Paper ID": "A", "Outcome": "Retrieved - original"},
                       {"Paper ID": "D", "Outcome": "Retrieved - review for context"}]

    def test_identified_are_not_all_screened(self):
        result = derive_flow(self.counts, self.ledger, self.status, [])
        self.assertEqual(result["unique_reports"], 5)
        self.assertEqual(result["screened"], 4)
        self.assertEqual(result["pending_ta"], 1)

    def test_new_full_text_candidates_are_not_claimed_as_attempted(self):
        result = derive_flow(self.counts, self.ledger, self.status, [])
        self.assertEqual(result["eligible_for_retrieval"], 2)
        self.assertEqual(result["sought"], 1)
        self.assertEqual(result["awaiting_retrieval"], 1)

    def test_background_retrieval_is_not_core_full_text_assessment(self):
        result = derive_flow(self.counts, self.ledger, self.status, [])
        self.assertEqual(result["retrieved"], 1)
        self.assertEqual(result["assessed"], 1)
        self.assertEqual(result["supplementary_retrieved"], 1)

    def test_missing_retrieved_source_rejected(self):
        with self.assertRaisesRegex(ValueError, "no retrieved report"):
            derive_flow(self.counts, self.ledger, [], [])

    def test_study_count_is_not_report_count(self):
        self.ledger[-1]["FT Final"] = "Include"
        self.status.append({"Paper ID": "E", "Outcome": "Retrieved - preprint"})
        linkage = [{"Paper ID": "A", "Study ID": "S1"}, {"Paper ID": "E", "Study ID": "S1"}]
        result = derive_flow(self.counts, self.ledger, self.status, linkage)
        self.assertEqual(result["primary_included_reports"], 2)
        self.assertEqual(result["included_studies"], 1)

if __name__ == "__main__": unittest.main()
