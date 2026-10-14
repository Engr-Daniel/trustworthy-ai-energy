#!/usr/bin/env python3
"""Validate IDs, occurrence accounting, CSV links and preserved raw hashes."""
import csv,hashlib,json,pathlib

def require(condition, message="Validation failed"):
 if not condition: raise ValueError(message)

root=pathlib.Path(__file__).resolve().parents[2];c=root/"review-paper/corpus"
read=lambda n:list(csv.DictReader((c/n).open(encoding="utf-8")))
corpus=read("corpus.csv");ledger=read("records-ledger.csv");events=read("identification-events.csv")
counts=json.loads((c/"scope-counts.json").read_text())
ids=[r["Paper ID"] for r in ledger]
require(len(ids)==len(set(ids)),"Duplicate persistent paper IDs")
require(set(r["Paper ID"] for r in corpus)<=set(ids),"Corpus ID not in screening ledger")
require(set(r["Paper ID"] for r in events)<=set(ids),"Event ID not mapped to report")
require(len(events)==counts["retrieval_occurrences"])
require(len(ledger)==counts["unique_reports"])
require(len(corpus)==counts["reading_queue"])
require(sum(bool(e["Duplicate of"]) for e in events)==counts["duplicate_occurrences"])
require(counts["retrieval_occurrences"]-counts["duplicate_occurrences"]==counts["unique_reports"])
require(all(r["TA Final"]=="Pending" and r["FT Final"]=="Pending" for r in ledger),"Update counts after screening")
for run in (root/"review-paper/search-strategy/runs").glob("PILOT-*"):
 m=json.loads((run/"search_manifest.json").read_text())
 for s in m["searches"]:
  if s["status"]=="completed":require(hashlib.sha256((run/s["raw_file"]).read_bytes()).hexdigest()==s["sha256"])
# Verify stable identity mappings and duplicate targets, not only totals.
registry=json.loads((c/"identity-registry.json").read_text(encoding="utf-8"))
require(all(registry.get(e["Identity"])==e["Paper ID"] for e in events),"Identity registry mismatch")
event_ids=[e["Event ID"] for e in events]
require(all(event_ids) and len(event_ids)==len(set(event_ids)),"Empty or duplicate event IDs")
require(all(ids),"Empty report ID")
require(len(corpus)==len({r["Paper ID"] for r in corpus}),"Duplicate queue IDs")
require({e["Paper ID"] for e in events}==set(ids),"Report without identification event")
first={};by_event={}
for e in events:
 require(bool(e["Identity"]),"Empty event identity")
 require(e["Duplicate of"]==first.get(e["Identity"],""),"Incorrect duplicate target: "+e["Event ID"])
 if e["Duplicate of"]:
  require(by_event[e["Duplicate of"]]["Paper ID"]==e["Paper ID"],"Duplicate report mismatch")
 else:first[e["Identity"]]=e["Event ID"]
 by_event[e["Event ID"]]=e
require(len(first)==len(ledger),"Identity/report count mismatch")
for key,source in [("crossref_occurrences","Crossref pilot"),("seed_occurrences","Seed register")]:
 require(counts[key]==sum(e["Source"]==source for e in events),"Source count mismatch: "+key)
require(counts["formal_screened"]==counts["formal_included"]==0,"Pilot must remain formally unscreened")
expected=[{k:e[k] for k in ["Event ID","Paper ID","Duplicate of","Identity"]} for e in events if e["Duplicate of"]]
require(read("deduplication.csv")==expected,"Deduplication export mismatch")
payload=json.loads((c/"workbook-data.json").read_text(encoding="utf-8"))
for key,rows in [("corpus",corpus),("ledger",ledger),("events",events),("searches",read("search-runs.csv"))]:
 normalized=[{k:"" if v is None else str(v) for k,v in row.items()} for row in payload[key]]
 require(normalized==rows,"Workbook JSON/CSV mismatch: "+key)
require(payload["counts"]==counts,"Workbook JSON count mismatch")
metadata_hashes=0
for manifest in (root/"review-paper/search-strategy/runs").glob("*/metadata_manifest.json"):
 for entry in json.loads(manifest.read_text(encoding="utf-8"))["attempts"]:
  if entry["status"]!="completed":continue
  path=(manifest.parent/entry["file"]).resolve()
  require(path.is_relative_to(manifest.parent.resolve()),"Metadata path outside run")
  require(hashlib.sha256(path.read_bytes()).hexdigest()==entry["sha256"],"Metadata hash mismatch: "+str(path))
  metadata_hashes+=1
print("Verified",metadata_hashes,"seed/baseline metadata checksums.")
print("Validated",len(events),"occurrences,",len(ledger),"unique reports,",len(corpus),"reading-queue records.")
