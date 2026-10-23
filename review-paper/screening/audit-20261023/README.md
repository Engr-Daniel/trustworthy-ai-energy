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
