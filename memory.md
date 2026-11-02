# Project memory
Updated 14 October 2026. Owner: Daniel Oyewale.

## Current objective
Scope literature broadly and reproducibly before finalising taxonomy, review angle or original projects.
The programme is Trustworthy AI for Energy and Industrial Systems, focused on image-based industrial inspection.
Daniel requested memory, agent and task files, PRISMA-style records, an adapted corpus tracker, a screening ledger, evidence matrix and synthesis prompts.

## Decisions to preserve
- Use a systematic scoping review and evidence map now. PRISMA-ScR reports the review; PRISMA-S reports the searches; JBI informs conduct.
- Broad scoping precedes confirmed clusters, taxonomy and research opportunities.
- Keep uncertainty, shift, multimodal sensing, human review and grounding in discovery. Do not force all papers into the previous selective-prediction question.
- Preserve stable IDs, primary-source metadata, raw exports, exact searches and failed attempts.
- Metadata matches, reading-queue flags and reading stages are different from eligibility decisions.
- No technical project has passed the novelty and data-feasibility gate.
- Original/resized dataset images are not independent samples.
- Never treat image evidence as direct wall-thickness or fitness-for-service ground truth.

## Snapshot
Pilot: 400 Crossref retrieval occurrences across 16 scalar, ranked query families, plus 33 seed occurrences.
After identity deduplication: 360 report records. The reading queue contains 230 records, including supporting methodology.
All formal screening is pending. Subject-database searches, human reviewer assignment, study/version linkage and full charting remain incomplete.
The pilot is capped and supplementary, not a completed exhaustive search.
Some bibliographic records have incomplete or ambiguous metadata; do not fill missing fields by guessing.

## Files to read on restart
AGENTS.md, task.md, review-paper/protocol.md, docs/research-story.md.
Then review-paper/corpus/scope-counts.json and the current corpus/screening records.
Historical log sessions remain historical. This snapshot supersedes earlier narrower working angles.

## Shared location
Drive folder: https://drive.google.com/drive/folders/15KlOofeUQ7soHwr26TbkoSw-7ppkw9eD
GitHub repository: https://github.com/Engr-Daniel/trustworthy-ai-energy
Default branch: master. Daniel authorised publishing the prepared foundation on 14 October 2026.

Native tracker: https://docs.google.com/spreadsheets/d/14NW5z6UziqVTzN2ZsmPbhT8Nmjo-ZQzQo0YaLDvNHTw/edit

## Latest continuation
The 20-record eligibility calibration packet is in review-paper/screening/pilot-20261013/. It contains title/metadata-only AI route suggestions and draft, unexecuted arXiv searches. Human decisions remain pending. Do not count those suggestions as formal screening.

## Repository maintenance - 14 October 2026
The repo is flattened into Personal/trustworthy-ai-energy. Replay now requires --output-dir pointing to a separate empty directory and never updates source records. Stronger validation checks metadata hashes, duplicate links, stable identity and workbook JSON/CSV agreement. Raw capture line endings are preserved through .gitattributes. Read CONTRIBUTING.md and docs/progression-plan.md for maintenance and milestone criteria. Live GitHub state and shared Sheet were not verified during this review.

## Verified publication and handoff - 14 October 2026
Published improvements in 090f5dbcb6ab365fd6f4325258d7e60e365ad0d4; GitHub run 38629633313 passed all four platform/Python jobs. See docs/workbook-synchronisation.md and review-paper/synchronisation/ for version relationships and archived-XLSX audit; live Sheet data equivalence remains unverified and no Sheet edits were made. Separate abstract evidence for the 20-record pilot is in review-paper/screening/abstracts-20261014/: 14 available, six unresolved; reviewer arrangement and all eligibility decisions remain pending. Counts remain snapshot counts.

Reviewer arrangement confirmed by Daniel on 14 October 2026: Daniel performs primary human screening with a documented secondary audit. Auditor identity and audit procedure remain pending; report single-human screening with audit, not independent dual review. Formal decisions are still pending.

## Calibration readiness continuation - 14 October 2026
Abstract availability is now 15/20: C0028 has a matching-title arXiv:2107.10880 candidate; OSF linkage remains unverified. P04, P05, P10, R02 and C0032 captures remain unresolved. Human-decisions-template.csv is pending, with Daniel as primary reviewer. validate_scope.py now supports human decisions with confirmed-decisions.csv provenance, stage/coverage/count checks and synthesis audit/linkage gates. See docs/screening-workflow.md. Auditor and human decisions remain pending; snapshot records/counts, workbook and Sheet were not changed.

## Current handoff - 15 October 2026
Use review-paper/screening/abstracts-20261015/reading-packet.md and human-decisions-template.csv. Availability is 16/20: P04 recovered from embedded IEEE JSON in the saved capture; P05, P10, R02 and C0032 remain unresolved. Earlier dated packets are preserved. All human decisions/audits remain pending. Daniel is primary screener; secondary auditor not yet named. Canonical records/counts, archived workbook and live Sheet were not changed. Local validator/template checks and 17 regression tests passed.

## Manuscript scaffold - 15 October 2026
Daniel requested a template only, with expected IEEE/Overleaf headings and guidance rather than synthesis. Sources are review-paper/manuscript/main.tex, refrence.bib and figures/. Local upload bundle: review-paper/manuscript-overleaf.zip. IEEEtran journal layout, visible writing instructions, empty tables/figures, no filled findings or bibliography entries. Bibliography is disabled until verified entries are cited. Static structural/ZIP checks passed; local TeX compiler is unavailable, so no PDF compilation is claimed.

## Current handoff - 22 October 2026
Protocol v0.5 governs. Daniel delegated screening/eligibility to the AI assistant (v0.4); every decision needs a defensible rationale, recall matters, Q1/PRISMA-ScR target. Title/abstract screening is complete: confirmed-decisions.csv has 5,585 rows (785 F, 2 U, 406 B, 4,392 X); consistency rules are in screening/ta-ai-20261022/screening-notes.md. Studies come from corpus/study-linkage.csv (verified links only); report records are never merged. Full text uses open-access copies only, via fulltext/retrieval-plan.csv, scripts/retrieve_fulltext.py (locate, then download) and logs/hashes in fulltext/. PDFs and text are git-ignored. The OpenAlex key lives outside the repo (OPENALEX_API_KEY env var only). Daniel's audit (all FT includes plus 10% of TA exclusions) is pending before submission. Do not commit or push without asking Daniel.

## Current handoff - 23 October 2026
Charting is complete for the 157 included studies (charting/charting.csv, form v0.2). Manuscript draft v1 is in manuscript/main.tex. Regenerate it after any record change: make_figures.py, then make_bib.py, then make_tables.py. Open items:
- Daniel's audit (screening/audit-20261023/audit-sample.csv).
- Optional manual retrieval of the 568 unretrieved reports into fulltext/manual/, then `retrieve_fulltext.py --stage ingest --supplier "..."`.
- The abstract-level tier.
- Citation tracing.
- Author inputs marked [Author input required] in main.tex.
Nothing has been committed since ca19572; ask Daniel before committing or pushing.

## Current handoff - 2 November 2026
Latest user request authorises checking/updating local and remote and progressing the paper. Both repos began at 3405d41. CT02 had added 1,385 pending reports. Reconciled 664 saved prior decisions (original Claude/date retained), held 186 unsupported title-only exclusions, and assessed 20 further complete abstracts as OpenAI-assisted under delegation. Current totals: 8,626 occurrences, 6,970 reports, 6,269 TA dispositions, 701 pending; 853 routed/unclear, 787 attempted, 66 await retrieval initiation; 219 core full texts assessed, 157 provisionally included/charted studies. Fourteen background retrievals (eight retrieved) are separate from core flow.

main.tex is updated and compiles locally to a 14-page provisional main.pdf with regenerated inputs. Added supplied author details: Daniel Oyewale, Ormedian Research Institute, corresponding email, no funding. Conflicts remain pending. User says audit completed, but reread local audit CSV still has all 658 auditor entries blank; requested its location and do not invent agreement. New Review_Tracker_20261102.xlsx reflects CSVs; original workbook/live Sheet were not overwritten. Current completion gates are in reporting-status.md and the dated active task plan.
