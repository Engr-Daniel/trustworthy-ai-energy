#!/usr/bin/env python3
"""Verify same-title version-linkage candidates against bibliographic metadata and assign Study IDs.

No network required. Reads version-linkage-candidates.csv (left unchanged) and compares each pair's
authors, year, record type, venue and identifiers from corpus.csv. Writes
version-linkage-verification.csv (evidence and outcome per pair) and study-linkage.csv (Study ID per
report for verified links only). Verification uses metadata, not full text: a link means the records
describe one study, it does not merge report records or delete identification events. Pairs without
author metadata are linked only when one side is a seed record with no identifiers and an identical
full title; otherwise they stay unverified. Screening decisions inside each linked study are listed so
conflicts are resolved explicitly at full text.
"""
import argparse, collections, csv, pathlib, re, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
C = ROOT / "review-paper/corpus"
DECISIONS = ROOT / "review-paper/screening/confirmed-decisions.csv"

def read(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def write(p, rows, headers):
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers, extrasaction="ignore"); w.writeheader(); w.writerows(rows)

def ascii_lower(s):
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()

def author_tokens(authors):
    # One token set per author, so name order ("Gibbons Tom" / "Tom Gibbons") does not matter.
    # Names with no ASCII transliteration (e.g. CJK script) are compared as written.
    out = []
    for a in (authors or "").split(";"):
        t = {w for w in re.findall(r"[a-z]{2,}", ascii_lower(a))} or ({a.strip().lower()} if a.strip() else set())
        if t:
            out.append(t)
    return out

def author_overlap(ta, tb):
    # Relative to the shorter list: one source often truncates or omits co-authors.
    shared = sum(any(x & y for y in tb) for x in ta)
    return shared, shared / min(len(ta), len(tb))

def venue(s):
    return re.sub(r"[^a-z0-9]", "", ascii_lower(s))

def classify(a, b):
    if not re.sub(r"[^a-z0-9]", "", ascii_lower(a["Full Title"])) or not re.sub(r"[^a-z0-9]", "", ascii_lower(b["Full Title"])):
        return "Not linked - spurious candidate", "Title empty or in non-Latin script, so the normalised title is empty; no title identity exists", 0.0, ""
    sa, sb = author_tokens(a["Full Authors"]), author_tokens(b["Full Authors"])
    if not sa or not sb:
        seed = a if not a["Paper ID"].startswith(("O", "C")) else b if not b["Paper ID"].startswith(("O", "C")) else None
        if seed and not (seed["DOI"] or seed["arXiv ID"] or seed["Full Authors"]):
            return "Linked - same study", "Seed record has no identifiers or authors; identical full title; bibliographic metadata taken from the retrieved record", 0.0, ""
        return "Unverified - insufficient metadata", "Author list missing on at least one record", 0.0, ""
    shared, overlap = author_overlap(sa, sb)
    first = "yes" if sa[0] & sb[0] else "no"
    if shared == 0:
        return "Not linked - distinct works", "Identical title but no author overlap", overlap, first
    if overlap < 0.5 or (first == "no" and shared < 2):
        return "Unverified - partial author overlap", "Too few shared authors to verify one study", overlap, first
    same_record = (a["Record Type"] == b["Record Type"] and venue(a["Venue / Journal"]) == venue(b["Venue / Journal"])
                   and a["Year"] == b["Year"])
    if same_record:
        basis = "Same authors, type, venue and year under different identifiers (duplicate records of one report)"
    else:
        basis = "Same authors; differing type/venue/year ({} {} {} vs {} {} {}) indicates preprint/proceedings/journal versions".format(
            a["Record Type"], a["Year"], a["Venue / Journal"][:40] or "no venue", b["Record Type"], b["Year"], b["Venue / Journal"][:40] or "no venue")
    return "Linked - same study", basis, overlap, first

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--corpus-dir", type=pathlib.Path, default=C, help="Override only for tests on a copy")
    ap.add_argument("--decisions", type=pathlib.Path, default=DECISIONS)
    ap.add_argument("--date", required=True)
    args = ap.parse_args()
    meta = {r["Paper ID"]: r for r in read(args.corpus_dir / "corpus.csv")}
    for r in read(args.corpus_dir / "records-ledger.csv"):
        meta.setdefault(r["Paper ID"], {"Paper ID": r["Paper ID"], "Full Title": r["Full Title"], "DOI": r["DOI"], "arXiv ID": r["arXiv ID"],
                                        "Record Type": r["Record Type"], "Full Authors": "", "Year": "", "Venue / Journal": ""})
    dec = {r["Paper ID"]: r["Decision"] for r in read(args.decisions)} if args.decisions.exists() else {}
    out, parent = [], {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for c in read(args.corpus_dir / "version-linkage-candidates.csv"):
        a, b = meta[c["Paper ID"]], meta[c["Candidate Paper ID"]]
        outcome, basis, overlap, first = classify(a, b)
        if outcome.startswith("Linked"):
            parent[find(a["Paper ID"])] = find(b["Paper ID"])
        out.append({"Paper ID": a["Paper ID"], "Candidate Paper ID": b["Paper ID"], "Outcome": outcome, "Basis": basis,
                    "Author overlap": f"{overlap:.2f}", "First author match": first or "unknown",
                    "Years": f"{a['Year'] or '?'} / {b['Year'] or '?'}", "Record Types": f"{a['Record Type']} / {b['Record Type']}",
                    "Identifiers": f"{a['DOI'] or a['arXiv ID'] or 'none'} / {b['DOI'] or b['arXiv ID'] or 'none'}",
                    "TA Decisions": f"{dec.get(a['Paper ID'], 'none')} / {dec.get(b['Paper ID'], 'none')}",
                    "Verified By": "Claude (AI assistant, delegated by Daniel Oyewale); metadata comparison", "Verification Date": args.date})
    groups = collections.defaultdict(list)
    for pid in list(parent):
        groups[find(pid)].append(pid)
    rank = {"Retrieve full text": 0, "Unclear": 1, "Background/supporting": 2, "Exclude": 3}
    study_rows = []
    for n, members in enumerate(sorted((sorted(m) for m in groups.values()), key=lambda m: m[0]), 1):
        decisions = sorted({dec.get(p, "none") for p in members})
        primary = min(members, key=lambda p: (meta[p]["Record Type"] == "preprint", not meta[p]["DOI"], rank.get(dec.get(p), 9), p))
        for p in members:
            study_rows.append({"Study ID": f"S{n:04d}", "Paper ID": p, "Primary report": "yes" if p == primary else "no",
                               "Record Type": meta[p]["Record Type"], "TA Decision": dec.get(p, "none"),
                               "Decision conflict": "yes - resolve at full text" if len(decisions) > 1 else "no",
                               "Linkage basis": "version-linkage-verification.csv", "Linkage Date": args.date})
    write(args.corpus_dir / "version-linkage-verification.csv", out, list(out[0]))
    write(args.corpus_dir / "study-linkage.csv", study_rows, list(study_rows[0]) if study_rows else ["Study ID", "Paper ID"])
    tally = collections.Counter(r["Outcome"] for r in out)
    conflicts = len({r["Study ID"] for r in study_rows if r["Decision conflict"].startswith("yes")})
    print(dict(tally), f"studies={len(groups)} conflicts={conflicts}")

if __name__ == "__main__":
    main()
