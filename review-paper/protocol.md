# Scoping review protocol
Version 0.3, 13 October 2026. Draft under pilot refinement; not preregistered.

## Review design and reporting
Conduct a systematic scoping review and evidence map. Use JBI scoping-review methodology for conduct, PRISMA-ScR for reporting and PRISMA-S for search reporting.
PRISMA is a reporting framework, not a search engine or assurance that the review is rigorous.
Decide whether a narrower systematic review is warranted after mapping the field. Do not call the current pilot a completed systematic review.

Working title: **Reliability of AI-Based Visual Industrial Inspection: A Systematic Scoping Review and Evidence Map**.
The earlier title focused on shift, uncertainty and selective prediction; this broader working title follows Daniel's instruction to scope before fixing taxonomy or a narrow research angle.

## Population, concept and context
- Population / unit: AI inspection systems, image-based inspection tasks and associated evaluation studies.
- Concept: reliability evidence, including robustness, uncertainty, calibration, selective decisions, sensor quality, multimodal failures and evidence-grounded outputs.
- Context: energy and industrial assets, manufacturing, refining, pipelines and transferable infrastructure inspection.

Include adjacent bridge and aero-engine evidence with explicit context labels. Do not treat it as validated refinery transfer.
Medical imaging remains a methodological bridge only, not the core domain.

## Questions
1. Which assets, tasks, sensor modalities and method families are studied?
2. How are reliability properties defined and evaluated?
3. How do datasets, splits and shift settings support the claims?
4. How are predictions connected to operating decisions and human review?
5. What field structure and unresolved questions emerge after charting?

## Eligibility to pilot and freeze
Include original journal/conference studies, benchmarks and method papers relevant to AI visual industrial inspection.
Tag reviews separately for background, taxonomy and overlap assessment.
Tag preprints separately; include them in discovery and analyse publication status without implying peer review.
Keep methodology references in a supporting set rather than counting them as industrial evidence.
Do not require a reliability keyword for broad discovery; accuracy-only studies may reveal evaluation coverage.

Exclude at screening: no industrial/asset-inspection relevance; no image/visual evidence; no AI/analytical inspection component; unrelated clinical/security/navigation tasks; non-scholarly promotional items; peer-review reports mistaken for research papers; duplicate report versions after explicit linkage.
Process-only time series and physical corrosion-rate modelling are adjacent unless connected to an eligible visual-inspection task.
Record an explicit reason and reviewer for every exclusion. No automatic keyword exclusion has been applied.

Discovery has no lower date limit. Current cutoff is 13 October 2026. Confirm first-online dates when metadata conflicts with issue dates.
Full-text languages will initially be those the reviewers can assess (English); any language restriction must be declared at screening, not hidden in discovery.

## Information sources and search layers
Planned subject sources: IEEE Xplore, Scopus or Web of Science (depending on access), ACM Digital Library, CVF/OpenReview proceedings and arXiv. Publisher searches and citation tracing supplement these.
Executed pilot: 16 ranked Crossref bibliographic queries, 25 returned records each, plus documented seed records and primary-source metadata lookups.
Crossref query.bibliographic is fuzzy, ranked and capped. It is not a Boolean subject-database search; its total-results field is not the number of relevant papers.
No Scopus/Web of Science/IEEE database export has been performed.

Use both broad asset-modality-task-AI searches and focused reliability searches.
Pilot synonyms, inspect known-item retrieval and ask an information specialist to review the search when feasible. Report whether that review actually occurred.
Retain exact platform syntax, fields, filters, dates, pagination, returned records, raw exports and hashes.
Record failed attempts and retries. Metadata enrichment is not an additional discovery count.

## Record management
Keep one occurrence per source/search retrieval in identification-events.csv.
Keep one persistent-identifier report in records-ledger.csv. Exact DOI and arXiv IDs drive identity.
Do not silently merge different persistent IDs by similar title. Flag potential preprint/journal versions and link a Study ID after verification.
Corpus.csv is a prioritised reading queue, not an included-study set.
All records remain formally unscreened at this stage.

## Screening and charting
Pilot title/abstract criteria on 20 varied records before full screening.
Preferred arrangement: two independent human reviewers with adjudication of disagreements. Reviewers are not appointed yet; AI-assisted triage is not an independent reviewer.
If only one reviewer is available, declare that arrangement and arrange a documented secondary audit. Do not claim dual screening.
Keep title/abstract decisions, retrieval attempts, full-text decisions, exclusion reasons, adjudicator and decision date.
Separate not retrieved, excluded and awaiting assessment.
Use the decision-integrity check to expose decisions without an assigned reviewer or reason.

Chart with the user's bibliographic fields plus provenance and industrial-reliability fields in the evidence matrix.
Pilot the charting form and codebook on 10 diverse papers, then version changes.
Clusters/pillars remain unassigned until reading supports them. Search themes are not taxonomy assignments.
Missing bibliographic metadata remains blank; unextracted scientific fields say Not extracted.
Only use Not reported after inspecting the relevant full text.

## Appraisal and synthesis
A scoping review can describe the evidence without a pooled effect estimate.
For our reliability agenda, record evaluation limitations qualitatively: independence, leakage, target access, threshold selection, risk definitions, uncertainty intervals, reproducibility and deployment validation.
Do not invent a numerical quality score or apply clinical appraisal tools indiscriminately.
Compare image-level and pixel-level decisions separately. Distinguish feature correction, probability calibration and decision-risk calibration.
Map method/task/modalities and reliability-evaluation coverage after extraction. Analyse benchmark, controlled-shift, real-asset and prospective evidence separately.
Treat proposed research opportunities as hypotheses until closest-work checks establish a distinct question.

## Amendments and reporting
Protocol registration is pending. Preserve the pilot date; do not retrospectively describe this search as preregistered.
Log amendments in amendments.csv. The pilot flow counts are audit counts, not final manuscript PRISMA counts.
Before publication complete subject-database searches, screening, version linkage, full extraction, citation verification and a final search update.

## Methodology sources
- PRISMA-ScR: https://www.prisma-statement.org/scoping
- PRISMA-S: https://www.prisma-statement.org/prisma-search
- JBI guidance: https://doi.org/10.11124/JBIES-20-00167
