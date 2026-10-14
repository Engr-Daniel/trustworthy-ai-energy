# Repository review - 14 October 2026

## Assessment

The local workspace is a sound research foundation, with a draft scoping protocol, stable identities, raw search captures, explicit screening limits, an eligibility calibration packet, evidence templates and a novelty gate. It is not yet a completed review or validated experimental project. Local HEAD at review start: `ba4059a`.

The saved pilot contains 433 retrieval occurrences, 360 reports and a 230-record reading queue. All formal screening is pending. The live Google Sheet was not inspected or modified, so these figures describe the repository snapshot only.

GitHub metadata and the remote branch could not be verified: connected-tool requests failed and direct HTTPS access was unavailable. This assessment covers the local checkout; no remote update or CI result is claimed.

## Findings addressed

| Finding | Change | Evidence |
| --- | --- | --- |
| Validator omitted seed/baseline metadata captures | Validate all completed metadata checksums | 29 metadata captures verified alongside pilot searches |
| Ten XML captures had checkout line-ending changes | Restore only bytes matching recorded SHA256; preserve raw files with Git attributes | All ten match their existing manifests after restoration |
| Replay wrote pending decisions over the source corpus | Require a separate, empty output directory | Reproduction and overwrite-rejection regression test |
| Replay depended on platform encoding and path separators | Explicit UTF-8 and repository paths with forward slashes | Complete generated replay matches saved artifacts on Windows |
| Counts alone could miss corrupted links | Check event uniqueness, duplicate targets, identity registry, deduplication export and workbook JSON/CSV agreement | Damaged duplicate link is rejected |
| Python optimisation disabled assertion checks | Use explicit validation errors | Corrupted count rejected with `python -O` |
| Contributor and progression guidance scattered | Add contributor guide and staged acceptance criteria | Linked from README and task ledger |

## Remaining limits

- Formal screening requires a documented human reviewer arrangement and a validator migration before decisions are entered.
- The current draft search strings need source-specific validation and known-item checks. Subject-database coverage remains outstanding.
- Report-to-study linkage, full extraction, taxonomy and novelty conclusions remain pending.
- Repository JSON/CSV agreement does not establish agreement with the archived XLSX or live Sheet. An explicit workbook build/synchronisation procedure is still needed.
- The root delivery manifest is historical and does not describe later edits.
- Reuse licensing, reviewer identity, database access and protocol registration remain owner/research decisions.

## Validation

The strengthened pilot validator and five regression tests passed locally on Windows with Python 3.10. Tests cover the saved snapshot, corrupted raw metadata, corrupted counts under optimisation, corrupted duplicate targets, exact replay and rejection of occupied/source destinations. CI now runs these checks on Windows and Ubuntu with Python 3.10 and 3.12; hosted execution remains unverified.

## Publication and verified CI amendment - 14 October 2026

The improvements were published to master in commit [090f5db](https://github.com/Engr-Daniel/trustworthy-ai-energy/commit/090f5dbcb6ab365fd6f4325258d7e60e365ad0d4). GitHub [run 38629633313](https://github.com/Engr-Daniel/trustworthy-ai-energy/actions/runs/38629633313) completed successfully. All four jobs passed both the validator and regression tests: Ubuntu/Windows with Python 3.10/3.12. This supersedes the earlier remote-access limitation for publication and CI; it does not change research status or establish search completeness, evidence quality or novelty.

The workbook version/synchronisation procedure and archived-XLSX audit are now recorded separately. Pilot abstract evidence preparation has started; it does not constitute screening.

The workbook/abstract handoff was published in commit [8e0a54d](https://github.com/Engr-Daniel/trustworthy-ai-energy/commit/8e0a54d7da5d076e41a34c53a486bc9a84135142). Hosted [CI run 38630741777](https://github.com/Engr-Daniel/trustworthy-ai-energy/actions/runs/38630741777) passed all four jobs, including the pilot validator and all eight regression tests. This verifies software/data checks, not research completeness or eligibility.
