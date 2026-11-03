# Human verification audit, prepared 23 October 2026

Protocol v0.4 requires a named human to verify a documented sample of the AI-assisted decisions before submission: all full-text inclusions and a random 10% of title/abstract exclusions. This folder holds that sample in `audit-sample.csv`. Open it in Excel or Google Sheets.

## Groups

| Group | Rows | Required? | What to check |
|---|---|---|---|
| A | 157 | Yes (protocol) | Each included study really meets all four core criteria: context, image-based modality, learned inspection model, and a reliability dimension that the study proposes or evaluates. Use the page locator. |
| B | 439 | Yes (protocol) | Each excluded record really fails a criterion. Title and rationale are usually enough; open the DOI link when unsure. |
| C | 62 | Recommended | Full-text exclusions and background decisions, where the eligibility judgement is hardest. |

Group B was drawn from all 4,392 title/abstract exclusions with Python `random.Random(20261023).sample`, without replacement. The SHA-256 prefix of the comma-joined sorted IDs is `30bf183faf6af98c`.

## How to fill it in

For each row, fill in `Auditor decision`, writing Agree or Disagree. If you write Disagree, add your reason in `Auditor rationale` and state what the decision should be. Fill in `Auditor` with your name and `Audit date` with the date.

Do not edit the AI columns. Disagreements are resolved in a dated packet that keeps the original decision, records the resolution and its reason, and states who resolved it.

## What gets reported

Agreement is reported per group, as percent agreement with its denominator, and Cohen's kappa for the binary include/exclude calls in groups A+C and B. Disagreements and their resolutions are listed. Once the audit is complete, the manuscript's "Selection and Reviewer Arrangement" and "Limitations of the Review Process" sections are updated.

## Addendum, 2 November 2026: AI-assisted second pass (not the human audit)

Daniel asked for the audit to be completed. The same AI assistant that made the original decisions (Claude) re-examined all 658 rows: the full-text opening of every group A and C report, targeted full-text searches for borderline rows, and the captured abstract or title of every group B record. Because the screener and the auditor are the same AI, this pass measures consistency, not agreement between independent reviewers. It does **not** satisfy the protocol's human audit: `validate_screening.py` accepts `Audit Status = Complete` only for a named human different from the screener, and every ledger row stays `Pending`.

Files:

| File | Contents |
|---|---|
| `ai-audit-pass-20261102.csv` | All 658 rows with `AI audit decision`, `AI audit rationale`, `AI proposed resolution`, `AI auditor` and `AI audit date`. The human columns are still blank for Daniel. |
| `ai-audit-summary-20261102.json` | Agreement per group and Cohen's kappa. |
| `resolution-packet-20261102.csv` | Dated revisions applied with `apply_decisions.py`. The earlier decision is kept as `R1 Decision`. |
| `build_ai_audit_pass.py` | Writes the three files above from the recorded judgments. It never overwrites an applied packet. |

Results:

| Group | Rows | Agree | Disagree |
|---|---|---|---|
| A: full-text inclusions | 157 | 154 | 3 |
| B: sampled title/abstract exclusions | 439 | 438 | 1 |
| C: full-text exclusions and background | 62 | 61 | 1 |

- Groups A+C: kappa for include versus not include is 0.96.
- Group B: kappa is 0 by construction, because every sampled AI decision is Exclude, so percent agreement is the meaningful statistic.

Resolutions:
- O2008 changed from Include to Exclude FT02: no image-based model was instantiated or evaluated.
- O2036 changed from Include to Exclude FT01: MNIST-only experiments.
- O5049 changed from Include to Exclude FT01: MNIST, Thyroid and Arrhythmia only.
- O1602 changed from Exclude FT06 to Include R3: OOD GAN-XCT and real NIST test sets.
- O5204 changed from Exclude TA05 to Retrieve full text: possible R6.
  - Open-access download failed. It is recorded as not retrieved, never excluded.
  - It is CC BY 4.0, so a manual PDF in `fulltext/manual/O5204.pdf` can be ingested.
- O3810 keeps its exclusion, but its code changed from TA01 to TA05.

To complete the protocol audit, Daniel (or another named human) fills the blank human columns of `ai-audit-pass-20261102.csv`, or of `audit-sample.csv`. Disagreements then go into a new dated packet with `Audit Status`, `Auditor`, `Audit Date`, `Audit Outcome` and `Audit Rationale` filled in.

## Human audit confirmation - 2 November 2026

Daniel explicitly confirmed in chat: "I completed the human audit of all 658 sampled records and agreed with every current decision." Recorded 658 agreements with current post-resolution decisions, including all 155 current full-text inclusions. The original sample is archived as audit-sample-before-human-confirmation-20261102.csv; human-confirmation-20261102.csv preserves original versus current decisions and the attestation basis. The date is the confirmation date; individual reading dates were not supplied. This is human verification of AI-assisted single-reviewer decisions, not independent dual human screening. Remaining screening (701), retrieval initiation (66), linkage and author declarations stay open; refresh audit coverage for later decisions. No commit, push or live Sheet write.
