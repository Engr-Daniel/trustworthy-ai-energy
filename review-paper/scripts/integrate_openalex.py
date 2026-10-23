#!/usr/bin/env python3
"""Append a completed, checksum-verified OpenAlex run to the identification and report records.

No network required. Every returned work becomes an identification event. Identity is DOI, with
arXiv DataCite DOIs (10.48550/arxiv.N) normalised to arxiv:N so they meet existing arXiv records;
works without a DOI use openalex:W. Different identifiers are never merged on title: same-title pairs
are written to version-linkage-candidates.csv for explicit verification. Abstracts are saved for
screening. Re-running on an already integrated run is refused.
"""
import argparse, csv, hashlib, json, pathlib, re, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
C = ROOT / "review-paper/corpus"
RUNS = ROOT / "review-paper/search-strategy/runs"
SCREEN = ROOT / "review-paper/screening"

def read(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def write(p, rows, headers):
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers, extrasaction="ignore"); w.writeheader(); w.writerows(rows)

def norm(s):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower())

def abstract(inv):
    if not inv:
        return ""
    return " ".join(w for _, w in sorted((p, w) for w, ps in inv.items() for p in ps))

def identity(w):
    doi = (w.get("doi") or "").lower().replace("https://doi.org/", "")
    m = re.fullmatch(r"10\.48550/arxiv\.(.+)", doi)
    if m:
        return "arxiv:" + re.sub(r"v\d+$", "", m.group(1)), "", re.sub(r"v\d+$", "", m.group(1))
    if doi:
        return "doi:" + doi, doi, ""
    return "openalex:" + w["id"].rsplit("/", 1)[-1], "", ""

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--corpus-dir", type=pathlib.Path, default=C, help="Override only for tests on a copy")
    args = ap.parse_args()
    cdir = args.corpus_dir
    run = RUNS / args.run_id
    manifest = json.loads((run / "search_manifest.json").read_text(encoding="utf-8"))
    if any(s["status"] != "completed" for s in manifest["searches"]):
        ap.error("Only fully completed runs are integrated")
    events = read(cdir / "identification-events.csv"); ev_headers = list(events[0])
    if any(e["Run ID"] == args.run_id for e in events):
        ap.error("Run already integrated")
    ledger = read(cdir / "records-ledger.csv"); led_headers = list(ledger[0])
    corpus = read(cdir / "corpus.csv"); cor_headers = list(corpus[0])
    registry = json.loads((cdir / "identity-registry.json").read_text(encoding="utf-8"))
    first = {}
    for e in events:
        first.setdefault(e["Identity"], e["Event ID"])
    known_titles = {}
    for r in ledger:
        known_titles.setdefault(norm(r["Full Title"]), []).append(r["Paper ID"])
    counter = max([int(v[1:]) for v in registry.values() if re.fullmatch(r"O\d+", v)] + [0])
    new_records, abstracts, searches_by_id = {}, [], {}
    for s in manifest["searches"]:
        rank = 0
        for page in s["pages"]:
            blob = (run / page["file"]).read_bytes()
            if hashlib.sha256(blob).hexdigest() != page["sha256"]:
                raise ValueError("Raw hash mismatch: " + page["file"])
            for w in json.loads(blob)["results"]:
                rank += 1
                key, doi, arxiv = identity(w)
                title = w.get("title") or w.get("display_name") or ""
                if key not in registry:
                    counter += 1
                    registry[key] = f"O{counter:04d}"
                    new_records[key] = (w, doi, arxiv)
                pid = registry[key]
                searches_by_id.setdefault(pid, set()).add(s["search_id"])
                eid = f"{args.run_id}-{s['search_id']}-{rank:04d}"
                events.append({"Event ID": eid, "Source": "OpenAlex", "Run ID": args.run_id, "Search ID": s["search_id"],
                               "Rank": rank, "Identity": key, "Title": title, "DOI": doi,
                               "Duplicate of": first.get(key, ""), "Paper ID": pid})
                first.setdefault(key, eid)
    linkage = []
    for key, (w, doi, arxiv) in new_records.items():
        pid = registry[key]
        title = w.get("title") or w.get("display_name") or ""
        loc = w.get("primary_location") or {}
        src = (loc.get("source") or {})
        authors = [a["author"]["display_name"] for a in w.get("authorships", []) if a.get("author")]
        rtype = w.get("type") or ""
        pub = "Preprint / repository record" if arxiv or rtype == "preprint" else "Journal / conference record; peer review not audited" if rtype in {"article", "book-chapter"} else "Publication status unverified"
        oa = (w.get("best_oa_location") or {})
        sid = "; ".join(sorted(searches_by_id[pid]))
        ledger.append({**{h: "" for h in led_headers}, "Paper ID": pid, "Full Title": title, "DOI": doi, "arXiv ID": arxiv,
                       "Record Type": rtype, "Source / Search IDs": sid, "Queue": "OpenAlex Boolean search",
                       "Reviewer 1": "Not assigned", "TA Decision R1": "Not started", "Reviewer 2": "Not assigned",
                       "TA Decision R2": "Not started", "TA Final": "Pending", "Full text sought?": "Not started",
                       "Retrieval Result": "Not started", "FT Decision R1": "Not started", "FT Decision R2": "Not started",
                       "FT Final": "Pending", "Study ID": "Not linked", "Included in synthesis?": "Pending"})
        first_author = authors[0] if authors else ""
        surname = norm(first_author.split()[-1]) if first_author else "unknown"
        corpus.append({**{h: "" for h in cor_headers}, "Paper ID": pid, "Cluster ID": "Unassigned", "Cluster": "Unassigned",
                       "Secondary Cluster": "Unassigned", "Pillar": "Unassigned", "Full Authors": "; ".join(authors),
                       "First Author": first_author, "Year": w.get("publication_year") or "", "Full Title": title,
                       "Venue / Journal": src.get("display_name") or "", "DOI": doi, "arXiv ID": arxiv,
                       "Publisher URL": loc.get("landing_page_url") or "", "URL (Paper Access)": oa.get("pdf_url") or oa.get("landing_page_url") or "",
                       "Modality": "Not extracted", "Task": "Not extracted", "Shift Type": "Not extracted",
                       "Dataset / Benchmark": "Not extracted", "Method Family": "Unassigned", "Paper Type": "Unassigned",
                       "Evaluation Type": "Not extracted", "Inclusion Rationale": "Pending eligibility screening",
                       "BibTeX Key": f"{surname}{w.get('publication_year') or 'nd'}_{pid}",
                       "BibTeX Status": "Generated; needs verification" if authors else "Incomplete metadata",
                       "Cited in Main Text?": "No manuscript yet", "Citation Verified?": "No",
                       "Accessible?": "Open-access location listed by OpenAlex; not checked" if oa else "Not checked",
                       "Status": "Unscreened", "Study ID": "Not linked", "Search IDs": sid, "Source Platform": "OpenAlex REST API",
                       "Publication Status": pub, "Reading Stage": "Metadata only",
                       "Metadata Status": "OpenAlex metadata; publisher citation check pending", "Record Type": rtype,
                       "Automated Queue": "OpenAlex Boolean search", "Evidence Locator": f"{run.relative_to(ROOT).as_posix()} {w['id']}",
                       "Last Checked": manifest["searches"][0]["started_utc"][:10]})
        abstracts.append({"Paper ID": pid, "OpenAlex ID": w["id"], "Title": title, "Year": w.get("publication_year") or "",
                          "Venue": src.get("display_name") or "", "Type": rtype, "Language": w.get("language") or "",
                          "Abstract": abstract(w.get("abstract_inverted_index")),
                          "Abstract Status": "OpenAlex abstract" if w.get("abstract_inverted_index") else "No abstract in OpenAlex",
                          "OA URL": oa.get("pdf_url") or oa.get("landing_page_url") or ""})
        for other in known_titles.get(norm(title), []):
            if other != pid:
                linkage.append({"Paper ID": pid, "Candidate Paper ID": other, "Basis": "Identical normalised title, different identifier",
                                "Status": "Unverified - do not merge"})
        known_titles.setdefault(norm(title), []).append(pid)
    write(cdir / "identification-events.csv", events, ev_headers)
    write(cdir / "records-ledger.csv", ledger, led_headers)
    write(cdir / "corpus.csv", corpus, cor_headers)
    (cdir / "identity-registry.json").write_text(json.dumps(registry, indent=2), encoding="utf-8")
    write(cdir / "deduplication.csv", [{k: e[k] for k in ["Event ID", "Paper ID", "Duplicate of", "Identity"]} for e in events if e["Duplicate of"]],
          ["Event ID", "Paper ID", "Duplicate of", "Identity"])
    out = SCREEN / f"openalex-{args.run_id}" if cdir == C else cdir
    out.mkdir(exist_ok=True)
    write(out / "abstracts.csv", abstracts, list(abstracts[0]) if abstracts else ["Paper ID"])
    lpath = cdir / "version-linkage-candidates.csv"
    old = read(lpath) if lpath.exists() else []
    write(lpath, old + linkage, ["Paper ID", "Candidate Paper ID", "Basis", "Status"])
    runs = read(cdir / "search-runs.csv"); run_headers = list(runs[0])
    for m_path in sorted(RUNS.glob("OPENALEX-*/search_manifest.json")):
        m = json.loads(m_path.read_text(encoding="utf-8"))
        if any(r["Run ID"] == m["run_id"] for r in runs):
            continue
        for s in m["searches"]:
            runs.append({"Run ID": m["run_id"], "Search ID": s["search_id"], "Source/platform": m["platform"],
                         "Search purpose": s["theme"], "Exact query": s["exact_query"], "Field": s["filter"].split(":", 1)[0],
                         "Filters": s["filter"].rsplit(")", 1)[-1].lstrip(","), "Run status": s["status"],
                         "Returned records": s.get("records_returned", 0), "API fuzzy hit count": s.get("api_count", ""),
                         "Capture limit": "All results (page pagination, per-page 200)", "Pagination": m.get("pagination", "cursor"),
                         "Search time UTC": s["started_utc"], "Raw file": (m_path.parent.relative_to(ROOT)).as_posix(),
                         "SHA256": "per-page in search_manifest.json",
                         "Notes": ("Integrated: " if m["run_id"] == args.run_id else "Not integrated (search development or failed attempt): ") + s.get("error", "")[:200]})
    for r in runs:
        if r["Run ID"] == args.run_id and r["Notes"].startswith("Not integrated"):
            r["Notes"] = "Integrated: " + r["Notes"].split(": ", 1)[1]
    write(cdir / "search-runs.csv", runs, run_headers)
    counts = json.loads((cdir / "scope-counts.json").read_text(encoding="utf-8"))
    counts.update({"retrieval_occurrences": len(events), "openalex_occurrences": sum(e["Source"] == "OpenAlex" for e in events),
                   "duplicate_occurrences": sum(bool(e["Duplicate of"]) for e in events), "unique_reports": len(ledger),
                   "reading_queue": len(corpus), "status": "Identification includes OpenAlex run " + args.run_id + "; screening in progress"})
    (cdir / "scope-counts.json").write_text(json.dumps(counts, indent=2), encoding="utf-8")
    payload = json.loads((cdir / "workbook-data.json").read_text(encoding="utf-8"))
    payload.update({"corpus": corpus, "ledger": ledger, "events": events, "searches": runs, "counts": counts})
    payload = json.loads(json.dumps(payload, ensure_ascii=False, default=str))
    for key in ["corpus", "ledger", "events", "searches"]:
        payload[key] = read(cdir / {"corpus": "corpus.csv", "ledger": "records-ledger.csv", "events": "identification-events.csv", "searches": "search-runs.csv"}[key])
    (cdir / "workbook-data.json").write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"new_reports": len(new_records), "linkage_candidates": len(linkage), **counts}))

if __name__ == "__main__":
    main()
