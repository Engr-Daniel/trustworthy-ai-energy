#!/usr/bin/env python3
"""Validate human screening provenance without producing eligibility decisions."""
import argparse
import csv
import datetime
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
TA = {"Pending", "Retrieve full text", "Exclude", "Background/supporting", "Unclear"}
FT = {"Pending", "Include", "Exclude", "Background/supporting", "Unclear"}
PLACEHOLDERS = {"", "pending", "not assigned", "not started", "unknown"}

def require(condition, message):
    if not condition: raise ValueError(message)

def assigned(value):
    return value.strip().lower() not in PLACEHOLDERS

def read(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))

def valid_date(value, message):
    require(bool(value), message)
    require(datetime.date.fromisoformat(value).isoformat() == value, "Date must be YYYY-MM-DD")

def validate_evidence(rows, known_ids, reasons):
    indexed = {}
    for row in rows:
        ident, stage = row["Paper ID"], row["Stage"]
        require(ident in known_ids, "Unknown screening Paper ID: " + ident)
        require(stage in {"TA", "FT"}, "Unknown screening stage")
        key = (ident, stage)
        require(key not in indexed, "Duplicate current screening evidence: " + str(key))
        indexed[key] = row
        decision = row["Decision"]
        require(decision in (TA if stage == "TA" else FT), "Unknown screening decision: " + decision)
        audit = row["Audit Status"]
        require(audit in {"Pending", "Complete", "Discrepancy unresolved"}, "Unknown audit status")
        if decision != "Pending":
            require(assigned(row["Reviewer"]), "Missing human reviewer: " + ident)
            require(row["Review Basis"] == "Human assessment", "Decision is not documented as human assessment: " + ident)
            valid_date(row["Decision Date"], "Missing decision date: " + ident)
            require(assigned(row["Protocol Version"]), "Missing protocol version: " + ident)
            require(assigned(row["Evidence Locator"]), "Missing screening evidence locator: " + ident)
            require(assigned(row["Rationale"]), "Missing screening rationale: " + ident)
            if decision == "Exclude":
                code = row["Reason Code"]
                require(code in reasons and reasons[code] == ("Title abstract" if stage == "TA" else "Full text"),
                        "Invalid exclusion reason for stage: " + ident)
            else:
                require(not row["Reason Code"], "Exclusion code on a non-exclusion: " + ident)
        if audit == "Complete":
            require(decision != "Pending", "Cannot audit a pending decision")
            require(assigned(row["Auditor"]) and row["Auditor"].strip().casefold() != row["Reviewer"].strip().casefold(),
                    "Secondary auditor must be a named different human")
            valid_date(row["Audit Date"], "Missing audit date")
            require(row["Audit Date"] >= row["Decision Date"], "Audit precedes primary decision")
            require(assigned(row["Audit Rationale"]), "Missing audit rationale")
            require(row["Audit Outcome"] in {"Agree", "Resolved discrepancy"}, "Unresolved audit cannot be complete")
            if row["Audit Outcome"] == "Resolved discrepancy":
                require(assigned(row["Resolution By"]) and assigned(row["Resolution Rationale"]), "Missing discrepancy resolution")
        elif audit == "Discrepancy unresolved":
            require(assigned(row["Auditor"]) and assigned(row["Audit Rationale"]), "Missing audit discrepancy evidence")
    return indexed

def validate_ledger(ledger, counts, evidence, reasons):
    indexed = validate_evidence(evidence, {r["Paper ID"] for r in ledger}, reasons)
    for row in ledger:
        ident = row["Paper ID"]
        require(row["TA Final"] in TA and row["FT Final"] in FT, "Unknown ledger decision: " + ident)
        for stage, field, reason_field in [("TA", "TA Final", "TA Reason Code"), ("FT", "FT Final", "FT Exclusion Code")]:
            decision = row[field]
            proof = indexed.get((ident, stage))
            if decision == "Pending":
                require(proof is None or proof["Decision"] == "Pending", "Evidence not reconciled to ledger: " + ident)
                require(not row[reason_field], "Exclusion reason on pending decision: " + ident)
                continue
            require(proof is not None and proof["Decision"] == decision, "Missing/mismatched human decision evidence: " + ident)
            require(row["Reviewer 1"] == proof["Reviewer"], "Ledger/evidence reviewer mismatch: " + ident)
            require(row[reason_field] == proof["Reason Code"], "Ledger/evidence exclusion reason mismatch: " + ident)
            require(assigned(row["Decision Rationale"]) and bool(row["Decision Date"]), "Missing ledger rationale/date: " + ident)
            valid_date(row["Decision Date"], "Missing ledger date")
            original = row["TA Decision R1" if stage == "TA" else "FT Decision R1"]
            require(original in (TA if stage == "TA" else FT) and original != "Pending", "Missing primary decision: " + ident)
            if original != decision:
                require(assigned(row["Adjudicator"]), "Missing resolver for changed primary decision: " + ident)
            if stage == "FT":
                require(row["TA Final"] == "Retrieve full text", "Full-text decision without progression: " + ident)
                require(row["Retrieval Result"] == "Retrieved", "Full-text decision without retrieved full text: " + ident)
        dated=[indexed[(ident,stage)]["Decision Date"] for stage in ["TA","FT"] if (ident,stage) in indexed and indexed[(ident,stage)]["Decision"] != "Pending"]
        if dated:
            require(row["Decision Date"] == max(dated), "Ledger date does not match latest stage decision: " + ident)
        if row["Included in synthesis?"] == "Yes":
            require(row["FT Final"] == "Include" and assigned(row["Study ID"]) and row["Study ID"] != "Not linked", "Synthesis inclusion without eligible linked study: " + ident)
            proof = indexed.get((ident, "FT"))
            require(proof is not None and proof["Audit Status"] == "Complete", "Synthesis inclusion before documented audit: " + ident)
    observed = {"formal_screened": sum(r["TA Final"] != "Pending" for r in ledger),
                "formal_included": sum(r["FT Final"] == "Include" for r in ledger)}
    for key, value in observed.items():
        require(counts[key] == value, "Screening count mismatch: " + key)
    return observed

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=pathlib.Path, help="Decision evidence/template CSV; validation does not promote decisions")
    args = parser.parse_args()
    reasons = {r["Code"]: r["Stage"] for r in read(ROOT / "review-paper/screening/reason-codes.csv")}
    ids = {r["Paper ID"] for r in read(ROOT / "review-paper/corpus/records-ledger.csv")}
    rows = read(args.input); validate_evidence(rows, ids, reasons)
    print("Validated", len(rows), "screening evidence rows; no decisions entered or promoted.")
