"""Derive current review progress without confusing identified and assessed reports."""
import collections
import csv
import json

def read(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))

def derive_flow(counts, ledger, status, linkage):
    ta = collections.Counter(row["TA Final"] for row in ledger)
    assessed = [row for row in ledger if row["FT Final"] != "Pending"]
    exclusions = collections.Counter(row["FT Exclusion Code"] for row in assessed if row["FT Final"] == "Exclude")
    eligible = {r["Paper ID"] for r in ledger if r["TA Final"] in {"Retrieve full text", "Unclear"}}
    supplementary = [r for r in status if r["Paper ID"] not in eligible]
    outcomes = {r["Paper ID"]: r for r in status if r["Paper ID"] in eligible}
    retrieved = {pid for pid, row in outcomes.items() if row["Outcome"].startswith("Retrieved")}
    members = collections.defaultdict(set)
    for row in linkage: members[row["Study ID"]].add(row["Paper ID"])
    study = {pid: sid for sid, group in members.items() for pid in group}
    included = {row["Paper ID"] for row in assessed if row["FT Final"] == "Include"}
    secondary = {row["Paper ID"] for row in assessed if row["FT Exclusion Code"] == "FT04"
                 and members.get(study.get(row["Paper ID"], ""), set()) & included}
    flow = {"identified": counts["retrieval_occurrences"], "openalex": counts.get("openalex_occurrences", 0),
            "crossref": counts["crossref_occurrences"], "seeds": counts["seed_occurrences"],
            "duplicates": counts["duplicate_occurrences"], "unique_reports": len(ledger),
            "screened": sum(row["TA Final"] != "Pending" for row in ledger), "pending_ta": ta["Pending"],
            "ta_excluded": ta["Exclude"], "ta_background": ta["Background/supporting"],
            "eligible_for_retrieval": len(eligible), "awaiting_retrieval": len(eligible - outcomes.keys()),
            "supplementary_retrievals": len(supplementary),
            "supplementary_retrieved": sum(r["Outcome"].startswith("Retrieved") for r in supplementary),
            "sought": len(outcomes), "not_retrieved": len(outcomes) - len(retrieved), "retrieved": len(retrieved),
            "assessed": len(assessed), "awaiting_ft_assessment": len(retrieved - {row["Paper ID"] for row in assessed}),
            "ft_excluded": dict(sorted(exclusions.items())),
            "ft_background": sum(row["FT Final"] == "Background/supporting" for row in assessed),
            "included_studies": len({study.get(pid, pid) for pid in included}),
            "primary_included_reports": len(included), "secondary_reports_of_included": len(secondary),
            "included_reports": len(included) + len(secondary)}
    if flow["identified"] - flow["duplicates"] != flow["unique_reports"]:
        raise ValueError("Identification flow does not reconcile")
    if flow["screened"] + flow["pending_ta"] != flow["unique_reports"]:
        raise ValueError("Screened and pending reports do not reconcile")
    if flow["screened"] != flow["ta_excluded"] + flow["ta_background"] + flow["eligible_for_retrieval"]:
        raise ValueError("Title/abstract dispositions do not reconcile")
    if not {row["Paper ID"] for row in assessed} <= retrieved:
        raise ValueError("Full-text assessment has no retrieved report")
    if flow["assessed"] != flow["primary_included_reports"] + sum(exclusions.values()) + flow["ft_background"]:
        raise ValueError("Full-text dispositions do not reconcile")
    return flow

def flow_counts(review_root):
    return derive_flow(json.loads((review_root / "corpus/scope-counts.json").read_text(encoding="utf-8")),
                       read(review_root / "corpus/records-ledger.csv"),
                       read(review_root / "fulltext/retrieval-status.csv"),
                       read(review_root / "corpus/study-linkage.csv"))
