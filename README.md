# Trustworthy AI for Energy and Industrial Systems
Research programme investigating reliability of image-based industrial inspection.

## Current review workspace
Read memory.md, AGENTS.md and task.md on restart.
The current scope is review-paper/protocol.md (v0.3): a systematic scoping review and evidence map.
The earlier narrower scope draft and closest-work memo are historical pilot records.

Shared Google Sheet: https://docs.google.com/spreadsheets/d/14NW5z6UziqVTzN2ZsmPbhT8Nmjo-ZQzQo0YaLDvNHTw/edit
Drive folder: https://drive.google.com/drive/folders/15KlOofeUQ7soHwr26TbkoSw-7ppkw9eD

The pilot captured 433 occurrences, 360 unique reports and a 230-record reading queue.
All formal eligibility screening is pending. The reading queue is not an included-study set.
The workbook contains Overview, Corpus, Screening, Identification, Searches, Evidence matrix, Synthesis, Data audit and Decisions.

The user's 30 corpus fields are preserved, with 10 added provenance/workflow fields.
Definitions: review-paper/corpus/data-dictionary.csv.
Replay: review-paper/scripts/build_corpus.py and validate_scope.py.
Exact pilot queries, manifests and raw snapshots: review-paper/search-strategy/.
Subject-database search specification: review-paper/search-strategy/database-searches.md.

Current XLSX is an archive snapshot. Read fresh shared-sheet changes before editing or synchronising back to CSV; do not overwrite collaborator changes with a replay.

**Current stage:** review scoping and novelty assessment.
**Technical projects:** candidates only; implementation has not started.

## Start here
- docs/programme-charter.md: purpose and workstreams.
- docs/research-story.md: dated research log and decision history.
- review-paper/protocol.md: current draft protocol (v0.3).
- review-paper/screening/pilot-20261013/: 20-record eligibility calibration packet.
- review-paper/scope-and-protocol-draft.md: historical earlier scope.
- review-paper/closest-work-comparison.md: evidence, novelty threats and data audit.
- review-paper/corpus/Industrial_Inspection_Corpus_Tracker.xlsx: editable tracker.
- review-paper/corpus/*.csv: text records suitable for git diffs.
- research/candidate-branches/: three branch briefs.
- docs/novelty-gate.md: conditions for moving into implementation.

The seed corpus is not a completed systematic search. Screening decisions remain unscreened. Retrieved full text is not equivalent to completed critical extraction.

## Updating the record
Keep source and decision IDs stable. Update the Excel tracker and corresponding CSV files together.
Append dated sessions to the research story. Record sources, version, access level, findings, interpretations and rejected directions.
Keep dataset bytes and third-party paper PDFs outside git. Cite primary records and preserve relevant licences.

## Reproduce the saved pilot
Run from the repository root with Python 3.10 or later (standard library only):
```bash
python review-paper/scripts/validate_scope.py
python -m unittest discover -s review-paper/scripts/tests -v
python review-paper/scripts/build_corpus.py --output-dir replay-output
```
Replay uses preserved snapshots and requires a separate, new or empty output directory. It does not run a fresh search, modify the source corpus or rebuild the XLSX. Review generated diffs before applying changes. The validator supports confirmed human decisions only with reconciled provenance, ledger, JSON and derived counts; see docs/screening-workflow.md. The saved pilot itself remains unscreened.

## Current handoff
GitHub workspace initialised 14 October 2026. The shared Sheet remains the collaboration surface; repository CSVs and XLSX are the saved scoping snapshot. Session 04 pilot suggestions are separate from formal decisions. Next: abstract retrieval and reviewer calibration, followed by validated multi-source searches.

## Contributor workflow and next milestones

- [Contributor guide](CONTRIBUTING.md): validation, safe replay, evidence preservation and synchronisation.
- [Progression milestones](docs/progression-plan.md): acceptance criteria for the active task ledger.
- [Repository review, 14 October 2026](docs/repository-review-20261014.md): findings, fixes and remaining limits.

Raw search captures retain exact bytes across platforms. The root `manifest.json` records the initial delivery snapshot; search-run manifests verify the preserved captures. Reuse licensing is not yet declared.

- [Workbook synchronisation procedure](docs/workbook-synchronisation.md): version relationships, keyed reconciliation and release checks.
- [Pilot abstract evidence](review-paper/screening/abstracts-20261014/README.md): 15 abstracts available; five unresolved; human decisions pending.

- [Human screening workflow](docs/screening-workflow.md): pending decision template and provenance checks; no automated eligibility decisions.
