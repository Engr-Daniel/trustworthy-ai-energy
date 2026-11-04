"""Evaluate frozen referral thresholds on saved predictions; does not train a model."""
import argparse
import csv
import json
import math
from pathlib import Path

ROLES = {"train", "tune", "test_id", "test_shift"}


def validate(rows):
    seen, groups = set(), {}
    for row in rows:
        identity, group, role = row["sample_id"], row["group_id"], row["split"]
        if not identity or identity in seen:
            raise ValueError("Missing or repeated sample identity")
        seen.add(identity)
        if not group or role not in ROLES:
            raise ValueError("Missing group or invalid split role")
        if group in groups and groups[group] != role:
            raise ValueError("Group leakage across split roles: " + group)
        groups[group] = role
        if row["label"] not in {"0", "1"} or row["prediction"] not in {"0", "1"}:
            raise ValueError("Labels and predictions must be 0 or 1")
        if not math.isfinite(float(row["uncertainty"])):
            raise ValueError("Uncertainty must be finite")


def threshold_for_budget(tuning, budget):
    if not 0 <= budget <= 1 or not tuning:
        raise ValueError("A source tuning set and budget in [0, 1] are required")
    values = sorted(float(r["uncertainty"]) for r in tuning)
    referred = math.floor(budget * len(values))
    if referred == 0:
        return math.inf
    if referred == len(values):
        return -math.inf
    # Accept ties at the cutoff: source referral never exceeds the requested cap.
    return values[len(values) - referred - 1]


def metrics(rows, threshold):
    accepted = [r for r in rows if float(r["uncertainty"]) <= threshold]
    positive = sum(r["label"] == "1" for r in rows)
    accepted_positive = sum(r["label"] == "1" for r in accepted)
    errors = sum(r["label"] != r["prediction"] for r in accepted)
    misses = sum(r["label"] == "1" and r["prediction"] == "0" for r in accepted)
    def ratio(n, d):
        return n / d if d else None
    return {
        "images": len(rows), "accepted": len(accepted),
        "referred": len(rows) - len(accepted), "positives": positive,
        "accepted_positives": accepted_positive, "accepted_errors": errors,
        "accepted_false_negatives": misses,
        "coverage": ratio(len(accepted), len(rows)),
        "review_fraction": ratio(len(rows) - len(accepted), len(rows)),
        "accepted_error_rate": ratio(errors, len(accepted)),
        "accepted_misses_per_all_positives": ratio(misses, positive),
        "false_negative_rate_among_accepted_positives": ratio(misses, accepted_positive),
    }


def evaluate(rows, budgets):
    validate(rows)
    tuning = [r for r in rows if r["split"] == "tune"]
    result = []
    for budget in budgets:
        threshold = threshold_for_budget(tuning, budget)
        for role in ["test_id", "test_shift"]:
            selected = [r for r in rows if r["split"] == role]
            if not selected:
                continue
            domains = sorted({r["domain"] for r in selected})
            for domain in [None] + domains:
                subset = selected if domain is None else [r for r in selected if r["domain"] == domain]
                result.append({
                    "requested_source_review_budget": budget, "split": role,
                    "domain": domain, "threshold": threshold if math.isfinite(threshold) else None,
                    "threshold_boundary": "finite" if math.isfinite(threshold) else "accept_all" if threshold > 0 else "refer_all",
                    **metrics(subset, threshold),
                })
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("predictions", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--budgets", type=float, nargs="+", default=[0, .05, .10, .20, .40, 1])
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Choose a new output file; preserve earlier runs")
    with args.predictions.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    report = {
        "status": "Retrospective prediction evaluation; no certification or post-human performance claim",
        "policy": "Source tuning threshold frozen before held-out evaluation; achieved target workload may differ",
        "results": evaluate(rows, args.budgets),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(report, stream, indent=2, allow_nan=False)
        stream.write("\n")


if __name__ == "__main__":
    main()
