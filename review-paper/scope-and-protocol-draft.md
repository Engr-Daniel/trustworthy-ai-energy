> Historical session 2 record. The current scope is protocol.md v0.3; this file preserves the earlier reasoning.

# Review scope and protocol draft
Status: SCOPING. Protocol not frozen. Manuscript writing has not begun.

## Working title
Reliability Evaluation of AI-Based Visual Industrial Inspection: Distribution Shift, Uncertainty and Selective Prediction.

## Main question
What evaluation evidence supports automatic acceptance or human referral of visual inspection results under changing acquisition conditions?

## Research questions
- Which risk and reliability quantities are measured, at which decision unit?
- How are source, target, tuning, calibration and final evaluation data separated?
- What distinguishes synthetic corruption, real acquisition variation and cross-site evaluation?
- How is human-review workload linked to accepted-case errors and missed defects?
- Which claims are supported by benchmark, real-asset or prospective deployment evidence?

## Planned scope
Image-based industrial inspection: defect detection, localisation and surface-condition assessment.
RGB, thermal and multimodal studies enter where they test relevant reliability properties.
Process-only time series, cybersecurity and text-only reporting remain outside the core corpus. Statistical foundations may be retained as supporting references.

The current corpus is a seed list for scoping. All rows remain formally unscreened.
Candidate window: 2019 to the frozen search date, with older foundational references found by citation tracing.
The final scope, publication window, languages and database choices must be documented before systematic screening.

## Search families to pilot
(A) (industrial OR manufacturing OR corrosion OR asset inspection) AND
(visual OR image OR computer vision) AND
(uncertainty OR calibration OR selective prediction OR abstention OR rejection OR risk control)

(B) same industrial and image terms AND
(domain shift OR distribution shift OR domain adaptation OR acquisition conditions)

(C) same terms AND (review OR survey OR systematic review)

Translate each family to database-specific syntax. Save query, date, filters, database/platform, returned count and export filename. No formal database export has been completed.

## Screening plan
Deduplicate by DOI/arXiv identity and title. Link preprint and journal versions; retain version history.
Screen titles/abstracts, then full texts. Record explicit exclusion reasons.
Pilot eligibility on a small batch, adjust once if necessary and date the amendment before proceeding.
Reviewer arrangement is not yet fixed. Do not claim two independent reviewers if only one performs screening.

## Extraction plan
Stable ID, bibliographic version, asset, modalities, labels, data access, sampling unit, split design, shift type, target access, uncertainty method, calibration meaning, risk numerator/denominator, threshold choice, referral workload, class/group failures, statistical interval, human outcomes, compute and reproducibility.
Use reported, not reported, unclear and not applicable. Code “not reported” only after full-text inspection.
Keep evidence quotation/page locator distinct from interpretation; quotes stay short.

## Synthesis plan
An evidence map linking claims to evaluation designs, not an unqualified pooled accuracy leaderboard.
Compare methods only when task, risk denominator, data access and operating budget align.
Do not infer human-review effectiveness from referral rates alone.
Do not interpret missing publication detail as proof the method is invalid.
Any publication contribution depends on the closest-review comparison.
