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

## Dated operational amendment - 14 October 2026
Daniel confirmed primary human screening by Daniel with a documented secondary audit. The auditor and audit coverage remain pending. No independent dual screening is claimed. A pending calibration template and provenance validator are now available; see docs/screening-workflow.md. Retrieval, human assessment, audit and synthesis admission remain separate states. These maintenance changes do not finalise eligibility rules or retrospectively register the protocol; all actual decisions remain pending.

## Dated amendment - protocol version 0.4, 16 October 2026
Recorded after Daniel's instruction of 16 October 2026 to run the remaining review pipeline. Earlier sections remain as the v0.3 record; where they conflict, this amendment governs work dated 16 October 2026 onward. The protocol is still not registered and is not described as preregistered.

### Screening arrangement (supersedes the v0.3 reviewer arrangement for new records)
- Daniel assessed the 20 calibration records and judged all of them as passing title/abstract (human assessment, recorded 2026-10-16).
- Daniel delegated subsequent screening and eligibility judgment to an AI assistant (Claude, Anthropic) operating under this protocol. He asked that every decision carry a defensible, scientific rationale. Records lacking defensible rationale may be removed, and recall of useful existing work is prioritised.
- AI-assisted decisions are recorded with Review Basis "AI-assisted under human delegation". Where the assistant refined Daniel's calibration judgment, the basis is "Human assessment with AI-assisted resolution" and the change is logged in TA Decision R2 and Adjudicator.
- This arrangement is single-reviewer, AI-assisted screening with human delegation. It is not independent dual human review and must be reported that way. Before submission, Daniel (or a named second human) verifies a documented sample: all full-text inclusions and a random 10% sample of title/abstract exclusions, with agreement reported.
- Synthesis admission before that audit is labelled "Provisional - audit pending".

### Eligibility (refines the v0.3 criteria; applies at title/abstract and full text)
Core evidence set (TA "Retrieve full text"; FT "Include"). All four conditions are required:
1. Context: industrial, energy or infrastructure assets, or manufactured products. Adjacent transferable infrastructure (bridges, tunnels, rail, aero-engines) is labelled as adjacent.
2. Evidence modality: image-based sensing (RGB, thermal/infrared, multispectral/hyperspectral, X-ray/radiographic images, depth/point cloud, video, or a multimodal combination including imagery).
3. AI component: a learned or data-driven model performing an inspection task (detection, segmentation, classification, anomaly detection, measurement, description).
4. Reliability dimension: the study proposes, evaluates or benchmarks at least one of R1 uncertainty quantification, confidence or calibration; R2 selective prediction, abstention, rejection, risk-controlled or conformal decisions; R3 distribution shift, domain adaptation or generalisation, OOD, open-set, or robustness to acquisition or corruption variation; R4 label noise or annotation reliability; R5 human-in-the-loop, referral or human-AI decision processes; R6 multimodal or sensor failure, missing modality or sensor degradation; R7 grounded or evidence-linked outputs, including vision-language hallucination; R8 evaluation validity (dataset realism, saturation, leakage, benchmark design for realistic conditions).

Background/supporting set (TA/FT "Background/supporting"). These are charted separately and are not counted as core evidence:
- Reviews and surveys. They are used for framing, overlap and novelty assessment.
- Methodology and reporting guidance.
- Foundational benchmarks or methods for visual industrial inspection that lack a reliability dimension but form the substrate of reliability evaluations (e.g. a benchmark used by many included studies).
- Adjacent non-visual studies, admitted only with an explicit rationale that they contribute a transferable reliability method or comparative evidence for an industrial inspection or condition-monitoring task (e.g. conformal or open-set fault diagnosis on process signals). They are never counted as visual evidence. Non-visual records without such a contribution are excluded.

Exclusion reasons add TA05 / FT06, "No reliability dimension proposed or evaluated (accuracy-only visual inspection)". A study whose reliability claim is only a generic statement (e.g. "the method is robust") without a corresponding design or evaluation meets FT06 at full text. Uncertain records go to full text rather than being excluded.

### Information sources (adds to v0.3)
Scopus, Web of Science and IEEE Xplore exports are not accessible in this project. OpenAlex (which indexes Crossref, arXiv, PubMed, institutional repositories and publisher metadata) is used as the primary multidisciplinary subject index, through Boolean title/abstract searches recorded in search-strategy/openalex-queries.json.
Because OpenAlex lacks abstracts for some publisher records, a title-only family (OA-T) restricted to records without abstracts complements the title/abstract families. The v0.3 Crossref pilot and seed records remain identification sources.
Search development is reported: run OPENALEX-20261016-01 failed (cursor pagination HTTP 401); run -02 completed with v0.4-draft blocks, but known-item testing showed missed core records, so the blocks were revised (see revision_note); run -03 failed (rate limit). The definitive run is the first completed run after -03.
Backward and forward citation tracing (OpenAlex referenced_works / cites) of core included studies supplements the database searches. Its scope is reported.
The access limitation (no Scopus/WoS/IEEE Xplore) is reported as a limitation.

### Charting and synthesis
The codebook axes from taxonomy-codebook-draft.md, R1-R8 above and the evidence-matrix fields are charted per core study from the full text, or from the abstract where the full text is not retrievable. Charting depth is recorded. The AI assistant performs charting under the same delegation; evidence locators are mandatory and unverified fields remain "Not reported" / "Not extracted" as defined in v0.3.

## Dated amendment - protocol version 0.5, 22 October 2026
Recorded when title/abstract screening was completed and the full-text stage began. The v0.4 amendment remains in force except where refined here.

### Title/abstract screening outcome
All 5,585 deduplicated report records were screened under the v0.4 delegation (AI-assisted single-reviewer screening; 2026-10-16 to 2026-10-22): 785 retrieve full text, 2 unclear (sent to full text), 406 background/supporting and 4,392 excluded (TA05 1,574; TA01 1,355; TA03 684; TA02 614; TA04 165). Consistency rules adopted while screening are dated in screening/ta-ai-20261022/screening-notes.md. Recodings are appended as later packets; earlier packets are kept.

### Version linkage
The 209 same-title candidates were compared on author lists (order-insensitive name tokens), year, record type, venue and identifiers (scripts/verify_version_linkage.py; corpus/version-linkage-verification.csv). Verified links (same authors, or a seed record without identifiers and an identical full title) define Study IDs in corpus/study-linkage.csv. Distinct works sharing a title, spurious candidates (non-Latin or empty titles) and pairs with insufficient metadata are not linked. Report records and identification events are not merged or deleted. Where reports of one study received different title/abstract decisions, the conflict is resolved at full text.

### Full-text retrieval and eligibility
- Retrieval uses open-access copies only: OpenAlex open-access locations recorded in the search responses, an OpenAlex DOI lookup for records without OpenAlex data, and arXiv versions found by exact normalised-title search. No subscription or unofficial sources are used. Every attempt is logged with URL, HTTP status and SHA256 (fulltext/retrieval-log.csv). Downloaded texts stay local; their hashes are recorded.
- Eligibility is decided per study, on the most complete retrieved report. Other reports of the same study are coded FT04. The version used (published, preprint, thesis) is recorded and evidence is labelled with it.
- The full-text reader examines the abstract, stated contributions, method, experimental setup and results. A keyword index of context, modality and R1-R8 terms is used only to locate passages; decisions cite page locators and apply the v0.4 criteria with FT01-FT06.
- Reports not retrieved after documented attempts are coded NR01 and appear as "reports not retrieved" in the PRISMA-ScR flow. Where the abstract supports eligibility, the study is charted from the abstract in a separately reported abstract-level tier and is never pooled with full-text-verified evidence.

### Charting and synthesis (22-23 October 2026)
The charting form (charting/charting-form.md) was piloted on ten studies spanning R1-R8, contexts and maturity levels (P01, P03, O1681, O4622, O2744, O3405, O0289, O4586, O1531, O2299) and revised to v0.2. The pilot rows were recoded to v0.2. All 157 included studies were charted from full text (charting/charting.csv). Synthesis is descriptive (multi-label counts, maturity, decision variables) and narrative with attribution; no quality score is assigned. Figures, count macros, tables and the bibliography are produced by scripts from the records, so they can be regenerated after any change.
