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

## Audit pass and reference check - 2 November 2026 (later session)
Daniel asked to complete the audit, provide the audit file and check citations, spelling, papers and DOIs; do not push.
- [x] AI-assisted second pass over all 658 audit rows (screening/audit-20261023/ai-audit-pass-20261102.csv; summary JSON; README addendum). Same-AI consistency check, not the human audit.
- [x] Applied resolution packet: O2008/O2036/O5049 excluded at full text, O1602 included (charted in chart-002.txt), O5204 to full text (OA download failed; NR01), O3810 code TA05. Included studies now 155.
- [x] Abstract tier now also covers attempted core reports from later dated plans (O5204); counts, figures, bibliography and tables regenerated; manuscript audit text updated with generated macros.
- [x] Reference check against DOI/arXiv registration records (manuscript/citation-check-20261102/); manuscript spelling check.
- [ ] Daniel or another named human: fill the human columns of the audit file; then record outcomes in a dated packet (Audit Status Complete requires a named human).
- [ ] Optional: place CC BY PDF of O5204 in fulltext/manual/ and ingest; assess at full text.
- [ ] Remaining citation-tracing screening (701 pending from O6076 onward; batches 301-317 were reconciled on 2 November) and the 66 routed reports.

### Local artifact synchronisation - 2 November 2026
Continuation of the active finalisation plan; no new research decisions.
- [x] Refresh current README/manuscript guidance/reporting counts after the AI consistency resolutions (155 included; 167 bibliography entries).
- [x] Preserve earlier workbook and build a post-audit CSV-backed snapshot; verify mapped tables and all thirteen CSV-backed tabs.
- [x] Refresh the local Overleaf package and add a separately dated post-audit artifact manifest, preserving the historical manifest.
- [ ] Remaining research gates above are unchanged: screening/retrieval, version linkage, named human audit and author declarations.

Workbook builder maintenance: replaced repeated populated-cell scans during string typing with direct row/column access. The post-audit export is verified against all thirteen CSV sources; screening dropdowns and Overview totals are checked separately.

## Human audit confirmation - 2 November 2026

Daniel explicitly confirmed in chat: "I completed the human audit of all 658 sampled records and agreed with every current decision." Recorded 658 agreements with current post-resolution decisions, including all 155 current full-text inclusions. The original sample is archived as audit-sample-before-human-confirmation-20261102.csv; human-confirmation-20261102.csv preserves original versus current decisions and the attestation basis. The date is the confirmation date; individual reading dates were not supplied. This is human verification of AI-assisted single-reviewer decisions, not independent dual human screening. Remaining screening (701), retrieval initiation (66), linkage and author declarations stay open; refresh audit coverage for later decisions. No commit, push or live Sheet write.

Human-confirmation verification: 658 current decision audits marked Complete with Daniel as named auditor, all 155 included studies covered; scope/manuscript checks and all 35 regression tests passed. Human-confirmed workbook matches all thirteen CSV-backed tables. Updated PDF remains 14 pages. Fixed sample confirmation does not close outstanding selection or final sampling.

## Remote update authorised - 3 November 2026
Daniel explicitly requested pushing the necessary updates. Prepared the current manuscript, DOI/arXiv checks, AI resolution history, human confirmation of 658 sampled decisions, CSV-backed workbooks and synchronisation reports for publication. Local TeX logs, source-paper downloads and compiler files are excluded. Research selection remains incomplete (701 TA pending, 66 retrieval initiations); no live Sheet update. Hosted CI is to be checked for the resulting commit.

## Selection completion - 3 November 2026
- [x] Title/abstract screening of the 701 pending records, each with a decision and recorded reason (screening/ta-ai-20261103/).
- [x] Retrieval initiated for the 66 routed reports plus 131 new F/U records (FULLTEXT-LOCATE-20261103-01); 36 retrieved, 161 not retrieved.
- [x] Full-text eligibility for the 36 retrieved reports; 18 new inclusions charted (173 included).
- [x] Refreshed audit sample prepared (screening/audit-20261103/).
- [x] Outputs regenerated: figures, abstract tier, bibliography (citation check 2026-11-03), tables, manuscript (15 pages), workbook Review_Tracker_20261103.xlsx (audited), Overleaf zip; validate_scope and 35 tests pass.
- [ ] Daniel: verify refreshed audit sample (A2 and B2 required; C2 and D2 recommended).
- [ ] Daniel: confirm O5989 SoftPatch as FT04 precursor of SoftPatch+ (O4487) or as a separate study.
- [ ] Author declarations; commit/push only when Daniel asks.

## Publication review - 3 November 2026
Reviewed the new selection work for the requested push. Validators report 0 pending TA and 0 retrieval initiations; 255 full texts assessed, 173 provisional inclusions. This does not verify substantive eligibility: 168 exclusions rely on title/metadata alone and require scrutiny under AGENTS.md rule 8; the refreshed human audit is pending. O5989 SoftPatch FT04 linkage to O4487 remains unresolved. Updated current status pages, corrected workbook snapshot dating and added the refreshed audit tab. Preserved all earlier workbooks and dated decisions. No source-paper PDFs or local compiler files are included.

## Author declarations confirmed - 4 November 2026
Daniel explicitly confirmed no funding and no conflict of interest, and requested the necessary acknowledgments. Updated the manuscript to state both declarations, acknowledge researchers and dataset/software maintainers, and retain the documented Claude/OpenAI assistance disclosure and author responsibility. No named personal contribution, institutional support or independent review was invented. Refreshed human audit remains separate and is not completed by this declaration. Other pre-existing local research edits are preserved.

## Publication verification - 4 November 2026
Daniel requested review and push. Verified the SoftPatch+ preliminary-version statement in local O4487 full text, preserving the recorded AI provenance and refreshed human-audit gate. Current map remains 173 studies, with 14 associated secondary reports. Fixed a replay risk in verify_version_linkage.py: preserve existing Study IDs and linkage dates, reject merges/splits of established IDs, and allocate new IDs after the existing maximum. Isolated replay preserved all 229 current memberships; 19 additional proposals remained temporary and were not applied. Added regression coverage. The unfinished ABSTRACT-CAPTURE-20261103-02 run has no manifest and remains local. Author declarations and manuscript compile checks pass; refreshed human audit and title-only exclusion evidence remain open.
