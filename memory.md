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

## Current handoff - 2 November 2026 (audit pass and reference check)
Claude completed an AI second pass over the 658-row audit sample (screening/audit-20261023/ai-audit-pass-20261102.csv; human columns still blank) and applied five revisions plus one code fix (resolution-packet-20261102.csv). Included studies: 155. The ledger Audit Status stays Pending: the protocol's human audit needs Daniel or another named human. References were checked against DOI/arXiv records (manuscript/citation-check-20261102/), and metadata corrections are in metadata-overrides.csv. Two publisher-printed DOIs are unregistered (O1478, O1522). Not committed or pushed; ask Daniel before any commit or push.

## Local snapshot synchronisation - 2 November 2026
After the later Claude audit resolutions, current flow is 854 routed/unclear, 788 core retrieval attempts, 569 not retrieved, 219 assessed, 155 provisional included studies and 167 bibliography entries. Still 701 TA pending and 66 retrievals not initiated. README/reporting status are refreshed; the new Review_Tracker_20261102_post-audit.xlsx preserves earlier workbooks. A separate post-audit manifest identifies uncommitted working files by hashes; the earlier release manifest remains historical. Human audit entries remain blank. This continuation does not authorise publication; no commit/push or live Sheet update.

## Human audit confirmation - 2 November 2026

Daniel explicitly confirmed in chat: "I completed the human audit of all 658 sampled records and agreed with every current decision." Recorded 658 agreements with current post-resolution decisions, including all 155 current full-text inclusions. The original sample is archived as audit-sample-before-human-confirmation-20261102.csv; human-confirmation-20261102.csv preserves original versus current decisions and the attestation basis. The date is the confirmation date; individual reading dates were not supplied. This is human verification of AI-assisted single-reviewer decisions, not independent dual human screening. Remaining screening (701), retrieval initiation (66), linkage and author declarations stay open; refresh audit coverage for later decisions. No commit, push or live Sheet write.

## Remote update authorised - 3 November 2026
Daniel explicitly requested pushing the necessary updates. Prepared the current manuscript, DOI/arXiv checks, AI resolution history, human confirmation of 658 sampled decisions, CSV-backed workbooks and synchronisation reports for publication. Local TeX logs, source-paper downloads and compiler files are excluded. Research selection remains incomplete (701 TA pending, 66 retrieval initiations); no live Sheet update. Hosted CI is to be checked for the resulting commit.

## Selection completed - 3 November 2026
All 6,970 reports now have title/abstract dispositions (701 screened in screening/ta-ai-20261103/; 292 on title/metadata only after Crossref/Semantic Scholar abstract capture ABSTRACT-CAPTURE-20261103-01). Retrieval was attempted for all 985 routed/unclear reports (197 initiated in FULLTEXT-LOCATE-20261103-01): 255 retrieved and assessed, 730 not retrieved (never excluded). The 36 new full texts gave 18 inclusions (charted in charting/compact/chart-003.txt), 1 background, 17 exclusions; included studies 173. Retrieved Unclear records must first be progressed to Retrieve full text in a dated TA packet (validator rule). Refreshed audit sample screening/audit-20261103/ (A2 18, B2 52, C2 18, D2 148) awaits Daniel. Open: O5989 SoftPatch FT04 versus SoftPatch+ O4487 linkage; author declarations. 185 bib entries, 165 OK/16 explained Check/4 no identifier. Manuscript 15 pages, 35 tests pass, workbook Review_Tracker_20261103.xlsx audited. No commit or push for this work yet.

## Publication review - 3 November 2026
Reviewed the new selection work for the requested push. Validators report 0 pending TA and 0 retrieval initiations; 255 full texts assessed, 173 provisional inclusions. This does not verify substantive eligibility: 168 exclusions rely on title/metadata alone and require scrutiny under AGENTS.md rule 8; the refreshed human audit is pending. O5989 SoftPatch FT04 linkage to O4487 remains unresolved. Updated current status pages, corrected workbook snapshot dating and added the refreshed audit tab. Preserved all earlier workbooks and dated decisions. No source-paper PDFs or local compiler files are included.

## Author declarations confirmed - 4 November 2026
Daniel explicitly confirmed no funding and no conflict of interest, and requested the necessary acknowledgments. Updated the manuscript to state both declarations, acknowledge researchers and dataset/software maintainers, and retain the documented Claude/OpenAI assistance disclosure and author responsibility. No named personal contribution, institutional support or independent review was invented. Refreshed human audit remains separate and is not completed by this declaration. Other pre-existing local research edits are preserved.

## Publication verification - 4 November 2026
Daniel requested review and push. Verified the SoftPatch+ preliminary-version statement in local O4487 full text, preserving the recorded AI provenance and refreshed human-audit gate. Current map remains 173 studies, with 14 associated secondary reports. Fixed a replay risk in verify_version_linkage.py: preserve existing Study IDs and linkage dates, reject merges/splits of established IDs, and allocate new IDs after the existing maximum. Isolated replay preserved all 229 current memberships; 19 additional proposals remained temporary and were not applied. Added regression coverage. The unfinished ABSTRACT-CAPTURE-20261103-02 run has no manifest and remains local. Author declarations and manuscript compile checks pass; refreshed human audit and title-only exclusion evidence remain open.
