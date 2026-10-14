"""Validate human provenance, stage progression, audit gates and derived counts."""
import copy
import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from validate_screening import validate_ledger, validate_evidence

REASONS = {"TA02": "Title abstract", "FT02": "Full text", "NR01": "Retrieval"}

def evidence(stage="TA", decision="Retrieve full text"):
    return {"Paper ID": "P01", "Stage": stage, "Decision": decision, "Reviewer": "Daniel Oyewale",
            "Review Basis": "Human assessment", "Decision Date": "2026-10-14", "Protocol Version": "0.3",
            "Evidence Locator": "source URI; abstract paragraph 1", "Rationale": "Human recorded rationale",
            "Reason Code": "", "Audit Status": "Pending", "Auditor": "", "Audit Date": "", "Audit Outcome": "",
            "Audit Rationale": "", "Resolution By": "", "Resolution Rationale": ""}

def ledger():
    return {"Paper ID": "P01", "TA Final": "Retrieve full text", "FT Final": "Pending", "Reviewer 1": "Daniel Oyewale",
            "TA Reason Code": "", "FT Exclusion Code": "", "Decision Rationale": "Human recorded rationale",
            "Decision Date": "2026-10-14", "TA Decision R1": "Retrieve full text", "FT Decision R1": "Not started",
            "Adjudicator": "", "Retrieval Result": "Not started", "Included in synthesis?": "Pending", "Study ID": "Not linked"}

class ScreeningTests(unittest.TestCase):
    def test_primary_human_decision_with_pending_audit_is_recordable(self):
        result = validate_ledger([ledger()], {"formal_screened": 1, "formal_included": 0}, [evidence()], REASONS)
        self.assertEqual(result["formal_screened"], 1)

    def test_missing_evidence_or_count_mismatch_rejected(self):
        with self.assertRaisesRegex(ValueError, "human decision evidence"):
            validate_ledger([ledger()], {"formal_screened": 1, "formal_included": 0}, [], REASONS)
        with self.assertRaisesRegex(ValueError, "count mismatch"):
            validate_ledger([ledger()], {"formal_screened": 0, "formal_included": 0}, [evidence()], REASONS)

    def test_missing_reviewer_date_locator_or_human_basis_rejected(self):
        for field in ["Reviewer", "Decision Date", "Evidence Locator", "Review Basis", "Protocol Version", "Rationale"]:
            row = evidence(); row[field] = ""
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_evidence([row], {"P01"}, REASONS)

    def test_retrieval_failure_is_not_exclusion_reason(self):
        row = evidence(decision="Exclude"); row["Reason Code"] = "NR01"
        with self.assertRaisesRegex(ValueError, "Invalid exclusion reason"):
            validate_evidence([row], {"P01"}, REASONS)

    def test_full_text_inclusion_requires_retrieved_text(self):
        row = ledger(); row.update({"FT Final": "Include", "FT Decision R1": "Include"})
        with self.assertRaisesRegex(ValueError, "retrieved full text"):
            validate_ledger([row], {"formal_screened": 1, "formal_included": 1}, [evidence(), evidence("FT", "Include")], REASONS)

    def test_synthesis_requires_a_different_named_auditor(self):
        row = ledger(); row.update({"FT Final": "Include", "FT Decision R1": "Include", "Retrieval Result": "Retrieved", "Included in synthesis?": "Yes", "Study ID": "STUDY-001"})
        proof = evidence("FT", "Include")
        with self.assertRaisesRegex(ValueError, "before documented audit"):
            validate_ledger([row], {"formal_screened": 1, "formal_included": 1}, [evidence(), proof], REASONS)
        proof.update({"Audit Status": "Complete", "Auditor": "Daniel Oyewale", "Audit Date": "2026-10-14", "Audit Outcome": "Agree", "Audit Rationale": "Audit evidence checked"})
        with self.assertRaisesRegex(ValueError, "different human"):
            validate_evidence([proof], {"P01"}, REASONS)
        proof["Auditor"] = "Synthetic test auditor"
        validate_ledger([row], {"formal_screened": 1, "formal_included": 1}, [evidence(), proof], REASONS)

    def test_unresolved_conflict_cannot_be_complete(self):
        row = evidence(); row.update({"Audit Status": "Complete", "Auditor": "Synthetic test auditor", "Audit Date": "2026-10-14", "Audit Outcome": "Disagree", "Audit Rationale": "Synthetic discrepancy"})
        with self.assertRaisesRegex(ValueError, "cannot be complete"):
            validate_evidence([row], {"P01"}, REASONS)

if __name__ == "__main__": unittest.main()
