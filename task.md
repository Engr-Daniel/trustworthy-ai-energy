# Research task ledger
Updated 14 October 2026.

## Done in this session
- [x] Clarify PRISMA-ScR, PRISMA-S and review design.
- [x] Draft PCC scope, eligibility, search layers and charting plan.
- [x] Capture 16 pilot query families with raw responses, failures, retries and hashes.
- [x] Expand reading queue while retaining all identified records.
- [x] Preserve user tracker columns and add provenance/screening/reliability fields.
- [x] Add memory.md, AGENTS.md and agent.md.

## Current delivery tasks
- [x] Verify updated workbook, flow counts and evidence matrix.
- [x] Save the revised archive and log as new versions.
- [x] Import the workbook to native Google Sheets in the requested Drive folder and verify it.

- [x] Prepare a separate 20-record eligibility calibration packet (human assessment pending).
- [x] Initialise the user-created GitHub repository with the prepared workspace.

## Next research tasks
- [ ] Pilot eligibility on 20 diverse records with documented reviewers.
- [ ] Finalise and register/version the protocol prospectively.
- [ ] Validate database-specific Boolean strings and known-item retrieval.
- [ ] Execute subject-database searches and retain complete exports.
- [ ] Trace citations from core benchmarks, reviews and reliability studies.
- [ ] Link preprint/journal reports into Study IDs without double-counting.
- [ ] Screen title/abstract and full text with reasons and retrieval outcomes.
- [ ] Pilot charting on 10 diverse papers and refine the taxonomy codebook.
- [ ] Extract evidence, map field coverage and test review contribution.
- [ ] Draft synthesis and verify all citations before manuscript writing.
- [ ] Evaluate candidate original projects only after evidence mapping.

## Open decisions
Human reviewers and adjudicator; database access; publication-status policy; final date/language restrictions; final taxonomy; focused review angle.
No fixed paper-count target substitutes for search coverage or rigorous screening.

## Repository review - 14 October 2026
- [x] Strengthen saved-pilot validation and protect replay from overwriting research.
- [x] Verify raw metadata checksums and preserve capture bytes across platforms.
- [x] Add regression checks, contributor guidance and progression acceptance criteria.
- [x] Migrate validation for human screening decisions with provenance, stage progression, counts and audit checks.
- [x] Establish workbook/Sheet reconciliation and release procedure; audit saved XLSX and inspect live headers.
- [ ] Capture full live snapshot, reconcile any differences and verify a complete workbook/Sheet round trip.
- [ ] Choose reuse terms for original repository material.

See docs/progression-plan.md for acceptance criteria; this ledger remains the active work plan.

## Publication and calibration handoff - 14 October 2026
- [x] Publish reviewed improvements in 090f5db and verify all four hosted CI jobs.
- [x] Prepare separate abstract evidence and retrieval log for the 20-record pilot (14 available, six unresolved).
- [ ] Resolve remaining abstract retrievals and audit source identity/completeness.
- [ ] Complete human calibration decisions and the secondary audit.

- [x] Confirm primary reviewer arrangement: Daniel, with a documented secondary audit.
- [ ] Name the secondary auditor and agree/record the audit procedure before calibration screening.

## Calibration readiness continuation - 14 October 2026
- [x] Retry six unresolved abstracts through primary sources and log exact discovery queries/captures.
- [x] Recover C0028 matching-title arXiv abstract (candidate linkage only): 15 available, five unresolved.
- [x] Add pending 20-record human decision template and screening workflow.
- [ ] Resolve five remaining abstract captures, verify source/version identity and complete Daniel's calibration decisions.
- [ ] Confirm auditor identity/coverage and amend eligibility rules after calibration.

## Calibration reading handoff - 15 October 2026
- [x] Recover P04 from preserved IEEE embedded metadata and test the parser.
- [x] Prepare a new dated, readable 20-record calibration packet and pending decision template.
- [x] Retry the remaining four primary-source captures and preserve failures.
- [ ] Resolve P05, P10, R02 and C0032 captures; verify source/version identity for the available evidence.
- [ ] Daniel records actual calibration decisions; name secondary auditor and agree audit coverage.

## IEEE manuscript scaffold - 15 October 2026
- [x] Create an IEEE journal LaTeX writing guide with main.tex, refrence.bib and figures/.
- [x] Add methods/results/discussion reporting guides and empty figure/table placeholders.
- [x] Package an Overleaf upload ZIP and verify its contents and LaTeX structure.
- [ ] Compile and inspect the scaffold in Overleaf; select a journal-specific template before submission.

## Review pipeline under protocol v0.4 - 16 October 2026
Daniel asked to finish the review: run the pipeline, with screening/charting delegated to the AI assistant under documented rationale (see protocol v0.4 amendment).
- [x] Record Daniel's calibration judgment (all 20 pass) with AI-assisted resolution: 11 retrieve full text, 7 background/supporting, 2 excluded (calibration-20261016/decisions.csv).
- [x] Protocol v0.4 amendment: delegation, refined eligibility (R1-R8), TA05/FT06, OpenAlex sources; validator and tests updated.
- [x] OpenAlex collector/integrator with checksummed raw pages; search development runs -01 (failed), -02 (superseded after known-item test), -03 (rate-limited) logged.
- [x] Activate OpenAlex API key and run the definitive OpenAlex search; integrate (runs OPENALEX-20261022-01/-02, 6,250 occurrences; 5,585 reports).
- [x] Title/abstract screening of all 5,585 records with rationale (packets 01-18; 785 F, 2 U, 406 B, 4,392 X).
- [x] Version linkage verified by metadata: 144 links, 104 multi-report studies; 787 FT reports = 766 studies.
- [x] Open-access full-text retrieval: 219/787 reports retrieved; 568 listed in fulltext/not-retrieved.csv.
- [x] Full-text eligibility of all 219 retrieved reports (packets ft-01, ft-02): 157 include, 11 background, 51 excluded.
- [ ] Daniel: optionally obtain non-retrieved PDFs (institutional access) into review-paper/fulltext/manual/<Paper ID>.pdf; then run --stage ingest and assess.
- [x] Pilot charting on 10 studies; form v0.2; all 157 included studies charted (charting/charting.csv).
- [x] Descriptive synthesis, PRISMA-ScR flow and figures; manuscript draft v1 with generated counts, tables and verified bibliography.
- [x] Audit sample prepared (screening/audit-20261023/).
- [ ] Daniel: complete audit-sample.csv (groups A and B required); then record resolutions and update manuscript.
- [ ] Abstract-level tier for NR01 reports (or manual retrieval first).
- [ ] Citation tracing of included studies (families defined; run CT01 failed 403 key_not_activated - Daniel to re-activate OpenAlex key), then final search update.
- [ ] Author inputs in main.tex (affiliations, funding, conflicts, release DOI, PRISMA-ScR checklist pages); first Overleaf compile.
- [ ] Resolve linked-study TA conflicts at full text: S0001 (B04/O4549), P05/O3428.
- [ ] Known-item gap: P03, P07, P09 not returned by OpenAlex (full texts retrieved via arXiv IDs); report as recall limitation; citation tracing pending.
- [ ] Citation tracing of core studies; final search update.
- [x] Synthesis, PRISMA-ScR flow, figures/tables, manuscript draft v1, title-level citation verification (see Session 13).
- [ ] Daniel's verification audit (all FT includes + 10% random TA exclusions) before submission - packet ready.

## Active finalisation plan - 2 November 2026
This dated plan supersedes older open-task summaries; historical entries above are retained.
- [x] Compare local and remote: both began at 3405d41; preserve the later CT02 working files.
- [x] Reconcile 664 saved 26 October decisions with original attribution; retain 186 unsupported title-only exclusion proposals Pending.
- [x] Assess 20 more complete abstracts under OpenAI delegation with dated rationales (8 full text, 1 background, 11 excluded).
- [x] Regenerate count/figure/table outputs and fix identified-versus-screened and supplementary-retrieval counting errors.
- [x] Add Daniel's supplied author details/no-funding declaration; retain conflicts and audit reconciliation as open.
- [x] Compile provisional 14-page PDF; fix math escaping and author-name typography against the primary source; no missing glyphs, overfull boxes or unresolved citations.
- [x] Build dated workbook and verify mapped tables against CSV; preserve the original pilot workbook and live Sheet.
- [ ] Complete 701 pending TA records and initiate retrieval for the 66 newly routed reports using retrieval-plan-20261102.csv.
- [ ] Assess/chart eligible new full texts, resolve version conflicts, update the audit sample and determine the final search cutoff.
- [ ] Locate Daniel's completed audit: current local CSV has 658 blank auditor decisions; reconcile disagreements before claiming completion.
- [ ] Confirm conflicts of interest/acknowledgments, finalise checklist and journal formatting, then remove provisional banner.
