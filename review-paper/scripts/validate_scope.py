#!/usr/bin/env python3
"""Validate IDs, occurrence accounting, CSV links and preserved raw hashes."""
import csv,hashlib,json,pathlib
root=pathlib.Path(__file__).resolve().parents[2];c=root/"review-paper/corpus"
read=lambda n:list(csv.DictReader((c/n).open(encoding="utf-8")))
corpus=read("corpus.csv");ledger=read("records-ledger.csv");events=read("identification-events.csv")
counts=json.loads((c/"scope-counts.json").read_text())
ids=[r["Paper ID"] for r in ledger]
assert len(ids)==len(set(ids)),"Duplicate persistent paper IDs"
assert set(r["Paper ID"] for r in corpus)<=set(ids),"Corpus ID not in screening ledger"
assert set(r["Paper ID"] for r in events)<=set(ids),"Event ID not mapped to report"
assert len(events)==counts["retrieval_occurrences"]
assert len(ledger)==counts["unique_reports"]
assert len(corpus)==counts["reading_queue"]
assert sum(bool(e["Duplicate of"]) for e in events)==counts["duplicate_occurrences"]
assert counts["retrieval_occurrences"]-counts["duplicate_occurrences"]==counts["unique_reports"]
assert all(r["TA Final"]=="Pending" and r["FT Final"]=="Pending" for r in ledger),"Update counts after screening"
for run in (root/"review-paper/search-strategy/runs").glob("PILOT-*"):
 m=json.loads((run/"search_manifest.json").read_text())
 for s in m["searches"]:
  if s["status"]=="completed":assert hashlib.sha256((run/s["raw_file"]).read_bytes()).hexdigest()==s["sha256"]
print("Validated",len(events),"occurrences,",len(ledger),"unique reports,",len(corpus),"reading-queue records.")
