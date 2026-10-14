# Trustworthy AI Energy Research Log
## Research story, evidence register and first novelty check

**Owner:** Daniel Oyewale  
**Started:** 13 October 2026, Africa/Lagos  
**Version:** 0.3
**Stage:** Initial scoping completed; full novelty assessment pending  
**Implementation status:** No technical project approved  
**Origin:** [Shared planning conversation](https://chatgpt.com/share/6acd745d-3590-83ea-a9a0-c6ed541b0e2a)

## 1. The story we are preserving

The programme began with a practical question: how can experience in reliable computer vision be applied to energy-industry problems and produce both publishable research and a credible employment portfolio?

The shared conversation first suggested a single reliability-aware inspection project. Daniel then changed the structure to an umbrella programme with two or three candidate branches. He explicitly required specific industrial relevance and a novelty stress test before implementation. He subsequently added a review paper as a connected research workstream.

In this conversation, we proposed narrowing the technical focus to image-based industrial inspection, with corrosion as the first branch to investigate. Daniel authorised proceeding and asked that the process be documented so the story is retained.

**Distinguish commitments from proposals:** The umbrella structure, literature-first approach, novelty gate and connected review are user requirements. The narrowed review title, corrosion-first ordering and candidate experimental questions are working proposals. No publication outcome, company adoption or novelty claim has been established.

### Programme commitments

- Preserve the umbrella: **Trustworthy AI for Energy and Industrial Systems**.
- Investigate specific inspection tasks with identifiable assets, users and decisions.
- Keep review synthesis and original experiments connected but separately assessed.
- Compare closest prior work before building a project.
- Use public data and modest compute as the working feasibility constraints from the shared brief.
- Record negative findings and abandoned ideas alongside promising ones.
- Target relevance to oil and gas, refining and industrial inspection; named companies are intended audiences, not verified partners or customers.

## 2. What this first pass did—and did not do

This was a targeted web scoping search on 13 October 2026. It sought:
1. Existing reviews overlapping the proposed review.
2. Original research threatening broad novelty claims.
3. Public-data candidates and barriers to meaningful domain-shift evaluation.

Search discovery used two web search engines. Interpretation relied on publisher pages, research-paper pages and author repositories. No Scopus, Web of Science or IEEE database export was completed. No exhaustive screening, citation-network search, dataset download or experiment was performed. Retrieval failures and abstract-only evidence are retained below.

**Consequently:** this pass can identify overlap and veto broad claims; it cannot certify that a narrower gap is unoccupied. A search result with no relevant hits was treated as inconclusive.

### Search record

Queries were issued in the order below. Quoted phrases were used for some follow-up searches.

| ID | Query | Purpose |
|---|---|---|
| Q01 | industrial visual anomaly detection survey uncertainty domain shift selective prediction review | Review overlap |
| Q02 | corrosion detection dataset cross domain generalization uncertainty pipeline inspection | Corrosion evidence and data |
| Q03 | industrial anomaly detection selective classification conformal prediction risk coverage | Decision-policy prior work |
| Q04 | "industrial" "anomaly detection" "survey" "uncertainty" "evaluation" | Second-engine check; results largely irrelevant |
| Q05 | "corrosion" "dataset" "Corrosion Condition State" | Real-image corrosion candidate |
| Q06 | "corrosion" "selective prediction" | Specific combination; no conclusion from poor retrieval |
| Q07 | Deep learning corrosion detection with confidence 2022 uncertainty 14 images | Verify named precedent; nature.com filter |
| Q08 | K-Pipelines Leo-Thomas synthetic dataset 2024 | Verify dataset; github.com/arxiv.org filters |
| Q09 | Risk-Based Thresholding for Reliable Anomaly Detection ECML 2025 | Identify decision-policy precedent |
| Q10 | industrial visual anomaly detection uncertainty quantification survey reliability review 2026 | Recent review leads; publisher/arXiv filters |
| Q11 | "ADShift" anomaly detection distribution shifts Cao 2023 | Shift-aware baseline precedent |
| Q12 | "Deep learning corrosion detection with confidence" dataset github authors | Code/data availability |
| Q13 | "Risk-Calibrated Multimodal Inspection" industrial anomaly detection | Multimodal reliability lead |

Dates and versions below use primary-page bibliographic information where available. Relative search-engine dates were not treated as publication dates.

## 3. Evidence register: closest reviews

“Page inspected” means the accessible page or stated sections were read, not that the entire PDF was critically reviewed.

| ID | Source and link | Evidence inspected | Overlap and implication |
|---|---|---|---|
| R01 | [Deep Industrial Image Anomaly Detection: A Survey](https://doi.org/10.1007/s11633-023-1459-z), Liu et al., 2024 | Publisher abstract and bibliographic page | Organises methods through architectures, supervision, losses, metrics and datasets. A generic methods-and-datasets review would overlap. Full PDF comparison pending. |
| R02 | [A survey of deep learning for industrial visual anomaly detection](https://doi.org/10.1007/s10462-025-11287-7), Li et al., 2025 | Accessible publisher text; abstract, introduction and selected method sections | Reviews 196 papers, learning strategies, methods and 2D/3D data. Discusses distribution-shift approaches and uncertainty-related methods. Reliability terminology alone will not distinguish our review. |
| R03 | [A Survey on Visual Anomaly Detection: Challenge, Approach, and Prospect](https://arxiv.org/abs/2401.16402), Cao et al., 2024 preprint | arXiv abstract and metadata | Uses training-data scarcity, modality diversity and anomaly hierarchy as organising challenges. A challenge-based taxonomy already exists; ours must add a different analytical result. |
| R04 | [Anomaly Detection for Industrial Applications, Its Challenges, Solutions, and Future Directions: A Review](https://arxiv.org/abs/2501.11310), Alzarooni et al., 2025 preprint | arXiv abstract and metadata | Covers acquisition, preprocessing, learning and evaluation. “Deployment-oriented pipeline review” is insufficient differentiation by itself. |
| R05 | [A survey on industrial image anomaly detection: methods, benchmarks and rethinks](https://www.sciencedirect.com/science/article/pii/S0263224125017361), DOI 10.1016/j.measurement.2025.118377 | Publisher search extract only; page retrieval failed | Additional recent overlap lead. Taxonomy and reliability coverage cannot yet be coded. |
| R06 | [A comprehensive survey for real-world industrial surface defect detection: Challenges, approaches, and prospects](https://www.sciencedirect.com/science/article/abs/pii/S0278612525002845) | Publisher search extract only; page retrieval failed | Real-world defect inspection overlap. Verify bibliography, scope and full text before deciding review novelty. |
| R07 | [Automated visual inspection of linear and areal surface defects: A metrological survey](https://www.sciencedirect.com/science/article/abs/pii/S0263224126022311), DOI 10.1016/j.measurement.2026.122522 | Publisher search extract only; page retrieval failed | Potential overlap on measurement uncertainty and evidence quality. Statistical predictive uncertainty must be separated from physical-measurement uncertainty. |

**Review verdict:** broad scope requires refinement. The proposed reliability-evaluation synthesis remains worth investigating, but its novelty is **not established**.

## 4. Evidence register: original research that changes the plan

| ID | Source and link | What the inspected evidence supports | Consequence |
|---|---|---|---|
| P01 | [Deep learning corrosion detection with confidence](https://doi.org/10.1038/s41529-022-00232-6), Nash, Zheng and Birbilis, 2022; [SpotRust author code](https://github.com/StuvX/SpotRust) | Publisher search extracts describe uncertainty and out-of-domain evaluation. Author README provides dropout, variational and ensemble inference; original dataset is unavailable due to industry restrictions. Full paper retrieval failed. | Reject “first uncertainty-aware corrosion inspection” framing. Compare evaluation protocol before proposing an extension. Public code does not imply public training data. |
| P02 | [Anomaly Detection under Distribution Shift](https://arxiv.org/abs/2303.13845), Tri Cao, Zhu and Pang, ICCV 2023; [author code](https://github.com/mala-lab/ADShift) | Paper abstract addresses shifted normal data and benchmarks across four datasets. | Reject “first industrial anomaly detection under shift” framing. A relevant comparator to assess in the full-text phase. |
| P03 | [Risk-Based Thresholding for Reliable Anomaly Detection in Concentrated Solar Power Plants](https://arxiv.org/html/2503.19146v2), Estievenart, Patra and Ben Taieb, 2025 | Abstract and method/deployment sections describe paired thresholds, abstention, Learn then Test risk control and evaluation on two plants. Real data is confidential; a simulated dataset is provided. | A particularly close energy-image precedent. Combining risk control, abstention and industrial imagery is already established. Our question must differ substantively. |
| P04 | [Risk-Calibrated Multimodal Inspection for Full-Coverage Industrial Anomaly Detection](https://ieeexplore.ieee.org/abstract/document/11669645/) | Publisher search extract describes multimodal inspection with difficult cases flagged for review. Date and full method not verified. | Keep as a high-priority multimodal novelty threat, not a fully assessed comparison. |
| P05 | [Class-conditional conformal prediction with discriminant-analysis backbones for reliable open-set fault diagnosis in safety-critical industrial systems](https://www.sciencedirect.com/science/article/pii/S0959152426000843) | Publisher search extract concerns industrial open-set fault diagnosis and uncertainty. Full page blocked. | Adjacent-method lead; do not assume it is image-based or a direct corrosion comparator. |

## 5. Data feasibility: candidate roles and unresolved checks

| ID | Candidate | Verified description | Proposed role and limitation |
|---|---|---|---|
| D01 | [MVTec AD 2](https://www.mvtec.com/research-teaching/datasets/mvtec-ad-2) | Official page: eight scenarios, more than 8,000 images; defect-free training/validation; varying test lighting; public and private test portions. CC BY-NC-SA 4.0. | Benchmark acquisition-condition robustness. Audit whether public labels expose the needed groups. It is not a corrosion-field dataset. Hidden labels may prevent our custom local analysis. |
| D02 | [K-Pipelines](https://github.com/leoxthomas/K-Pipelines) | Author README: 600 synthetic pipeline images, balanced corrosion classes; augmented version 1,080 images. Repository lists classification splits. | Optional synthetic classification experiment. Do not invent pixel masks or field-validation claims. Audit original/augmentation relationships before splitting. Verify dataset terms separately from repository software terms. |
| D03 | [Corrosion Condition State Semantic Segmentation Dataset](https://doi.org/10.7294/16624663.v2); [author repository](https://github.com/beric7/corrosion_cs_classification) | Author repository describes bridge inspection segmentation with good/background, fair, poor and severe classes. Institutional record was discovered but could not be read. | Real-image candidate for an asset-inspection study. Bridge imagery cannot establish refinery transfer. Licences, files, class meanings, parent-image grouping and site metadata still need inspection. |
| D04 | SpotRust original corrosion data | Author repository explicitly states industry restrictions prevent providing it. | Prior-work comparison, not an assumed public-data source. |
| D05 | Simulated CSP thermal data associated with P03 | Paper states a simulated dataset is released; field dataset is confidential. | Thermal fallback lead. Actual download availability, labels, licence and compute needs still need auditing. |

**Correction to the earlier plan:** MVTec AD and AD 2 should be treated as separate benchmark tasks with documented training/calibration/evaluation protocols. Merely evaluating both does not establish cross-facility transfer. Likewise, different corrosion datasets may have incompatible labels and tasks.

No candidate has yet passed a data audit for real cross-site corrosion evaluation.

## 6. Revised review proposal

**Working title:** Reliability Evaluation of AI-Based Visual Industrial Inspection: Distribution Shift, Uncertainty and Selective Prediction.

**Working question:** What evidence supports accepting or deferring model outputs when industrial inspection images differ from training conditions?

**Proposed analytical contribution to test:** an evidence map connecting each reliability claim to its evaluation conditions, calibration data, independent sampling unit, risk definition and human-review workload.

This is our proposed framework, not a finding that previous reviews lack these elements.

### Proposed scope

Core: image-based industrial defect detection, localisation and surface-condition assessment. Include RGB or thermal studies when they evaluate uncertainty, shift, calibration, rejection or decision thresholds. Multimodal studies enter when they address reliability of inspection decisions.

Exclude from the core synthesis: process-only time series, generic cybersecurity, text-only reporting, and physical integrity conclusions unsupported by image labels. Keep foundational statistical methods as methodological references.

A practical initial date window is 2019–13 October 2026, with earlier foundational papers included through citation tracing. Freeze the window only after scoping confirms it is manageable.

### Proposed extraction fields

Record paper/version, asset, modality, task, labels, data origin, public access, defect prevalence, training split, calibration split, independent sampling unit, shift definition, target-data access, uncertainty score, probability calibration, rejection rule, risk denominator, review workload, error by class/group, statistical intervals, compute, code and limitations.

Use **reported / not reported / unclear / not applicable**. A missing item in an abstract is not “not reported” in the full paper.

The synthesis should separately compare:
- Ranking quality, probability calibration and thresholded decision risk.
- Controlled corruptions, real acquisition shifts and cross-site shifts.
- Image decisions and localisation decisions.
- Benchmark evidence, real-asset retrospective evidence and prospective deployment.
- Conditional risk among accepted cases and population-level missed defects.
- Referral rates and demonstrated human-review outcomes.

## 7. Candidate first project—question under investigation

**Provisional question:** With a frozen inspection model and a fixed human-review budget, how much does a decision policy calibrated on one acquisition condition deteriorate on an unseen condition, and does a small, separately labelled target-calibration sample improve it?

This is a testable scoping question. We have not established that it is new.

Corrosion-specific implementation is conditional on suitable real-image data. If data only supports controlled changes, describe the contribution as acquisition-corruption evaluation. Do not rename it cross-operator validation.

### Candidate hypotheses, not an approved protocol

- H1: A source-calibrated policy exceeds its prespecified empirical accepted-error target on at least one held-out acquisition condition.
- H2: Target-labelled recalibration improves accepted-error performance at a matched review workload relative to source calibration.
- H3: A complex uncertainty policy does not necessarily outperform score-margin rejection at matched coverage and inference cost.

These hypotheses must survive closest-work comparison. Existing P03 methods are a serious challenge to H2-based novelty.

### Minimal design if the gate is passed

Start with one task, two justified models and simple decision baselines. Separate model fitting, policy tuning, risk calibration and final evaluation. Freeze risk definitions and thresholds before inspecting test outcomes. Give each method the same target-label budget.

Predefine both accepted-case error and the proportion of true defects automatically labelled normal. Referral is not proof a defect was detected by a human. Report class-specific referral rates and zero-acceptance cases. Plot risk against coverage and review workload.

For repeated images, crops or augmented derivatives, split and quantify uncertainty at the parent asset/image level as appropriate. Pixel counts cannot substitute for independent inspections. Repeat calibration sampling to measure policy stability; select repetitions and compute budget after the data audit.

A low-coverage policy can look accurate by accepting almost nothing. Match operating budgets rather than comparing arbitrary thresholds.

## 8. Decision ledger

| Decision | Date | Status | Reason | Evidence / reopening condition |
|---|---|---|---|---|
| DEC-001: Use an umbrella programme and separate gated projects | 13 Oct 2026; reconstructed from shared conversation | User requirement | Preserve related projects without premature implementation | Origin conversation |
| DEC-002: Maintain a review workstream | 13 Oct 2026; reconstructed | User requirement | Synthesis should inform project choice | Origin conversation |
| DEC-003: Narrow first investigation to visual inspection reliability | 13 Oct 2026 | Working scope | Broad energy-AI scope is unmanageable | R01–R07; refine after full-text comparison |
| DEC-004: Investigate corrosion first | 13 Oct 2026 | Provisional | Specific visible-asset use case | Reopen if public data lacks suitable labels/domains |
| DEC-005: Reject generic uncertainty-plus-corrosion novelty | 13 Oct 2026 | Rejected claim | Clear prior overlap | P01 |
| DEC-006: Reject generic shift-aware anomaly-detection novelty | 13 Oct 2026 | Rejected claim | Clear prior overlap | P02 |
| DEC-007: Reject risk-control-plus-abstention as a new industrial-image combination | 13 Oct 2026 | Rejected claim | Close energy-domain precedent | P03 |
| DEC-008: Treat K-Pipelines as synthetic evidence | 13 Oct 2026 | Evidence constraint | Data generation differs from field acquisition | D02 |
| DEC-009: Keep all branches outside implementation | 13 Oct 2026 | Active gate | Novelty and data feasibility remain unresolved | Requires gate evidence below |

## 9. Branch status

| Branch | Current status | Required next evidence |
|---|---|---|
| Corrosion under shift | Priority investigation; novelty/data unresolved | Full P01/P02/P03 comparison; real data with defensible groups and labels |
| Thermal–visual inspection | Retained alternative; not assessed enough to rank novelty | Paired-data audit and missing/degraded-sensor closest work, including P04 |
| Evidence-grounded reporting | Parked pending definition | Grounded annotation source, error rubric and closest inspection-reporting studies |
| Review paper | Scope refined; novelty unresolved | Full-text comparison of R01–R07 and additional reliability-specific reviews |

## 10. Gates and continuation plan

### Review gate

Complete a comparison matrix across the closest reviews: questions, search dates/databases, screening methods, taxonomy, reliability metrics, calibration, shift types, sampling assumptions, referral workload and field evidence. Continue only if our synthesis adds a useful analysis beyond existing reviews. Otherwise narrow further, merge scope or discontinue the proposed review.

### Technical-project gate

Require:
1. At least five genuinely close original studies compared in full text, with citation tracing.
2. A specific contribution differing in question, method or evaluation evidence—not just dataset or model substitution.
3. Public usable data, meaningful splits and compatible ground truth.
4. A small feasible baseline matrix and a prespecified evaluation design.
5. A written negative-result story explaining what the study would teach if the proposed method fails.

### Next bounded work package

1. Obtain and read full texts for P01, P02 and P03.
2. Compare R01–R04 in full and resolve access for R05–R07.
3. Trace backward/forward citations for decision calibration and selective inspection.
4. Audit corrosion data files, licences, parent groups and label compatibility.
5. Produce a closest-work matrix with **continue / redefine / stop** recommendations.
6. Freeze the review protocol only after the comparison supports a distinct synthesis.

GitHub foundation remains an intended deliverable from the originating conversation. No repository has been created or modified in this pass.

## 11. Continuity rules for subsequent sessions

Treat this document as the current record. Update the same file and retain dated entries. Correct factual mistakes explicitly; do not silently turn earlier proposals into commitments.

For each work session append: question investigated, exact searches, source/version and access level, evidence found, interpretation, decision, rejected alternative, remaining uncertainty and next task. Use stable source and decision IDs. Add experiment IDs only once implementation is authorised by the research gate.

**Session 1 restart capsule (historical):** We are scoping a reliability-focused industrial-visual-inspection programme. A connected review and corrosion-first investigation are proposed. Existing reviews overlap; SpotRust already covers uncertain corrosion inference; ADShift covers anomaly detection under shift; the 2025 CSP paper already combines risk thresholds and abstention. Public-data feasibility is unresolved. All branches remain unapproved. Resume with closest-work full-text comparison and a data audit, not model training.

## 12. Session 2: review clarification, corpus tracker and evidence audit

**Date:** 13 October 2026, Africa/Lagos. **Version:** 0.3.
Daniel authorised continuing and creating an Excel corpus tracker, and asked whether the review had begun and whether a GitHub repository should be created.

### Clarification
The review is already in its scoping and novelty-assessment stage. Formal systematic database searching/screening and manuscript writing have not begun. Repository setup should proceed now; the novelty gate applies to technical implementation.

### Work completed
Created a tracker with 18 papers, six dataset candidates, 25 web-scoping searches and 13 decisions. Seven records have selected-section extraction, two have full text retrieved without completed extraction, and the remainder have abstract/search evidence. All formal screening decisions remain unscreened.

P01 primary HTML and P02 PDF were successfully retrieved after earlier web-reader failures. P01 also evaluates pixel sparsity, so selective pixel removal cannot be treated as a new idea.
Added newer P06 SPARC and P07 NFAD, plus P08 AeBAD, P09 SafeRestore, P10 domain-adaptive corrosion work and R08 an electronics-defect systematic review.
P06 addresses few-shot correction of frozen detectors. P09 studies independently certified selective restoration. Our prior recalibration proposal requires further differentiation.

### Data progress
D03 v2 primary metadata, README, annotation guide and ZIP file index were inspected. The archive confirms original/resized versions of 396 training and 44 test images. The licence is CC0. The good class includes minimal corrosion; site/asset grouping and duplication remain unaudited.
D06 author documentation specifies CC BY 4.0; actual images/grouping are still pending.
D05 author README has a TODO dataset link. The separate paper link remains unverified.

### Decisions added
- DEC-010: review scoping is active; formal screening not started.
- DEC-011: maintain an Excel corpus tracker with stable IDs.
- DEC-012: distinguish feature correction, probability calibration and risk-threshold calibration before proposing novelty.
- DEC-013: prepare GitHub foundation; remote creation pending because the connected GitHub connector lacks that operation.

### Deliverables
Excel corpus tracker; repository-ready foundation with programme charter, review scope/protocol draft, closest-work comparison, CSV records, branch briefs and this research story.

### Current next step
Complete closest-review coverage coding and the formal search protocol; inspect actual dataset grouping. The candidate question is whether improved ranking after feature correction translates into fewer automatically missed defects at a fixed review budget across acquisition conditions. Novelty remains unconfirmed. No technical implementation is approved.

This session supersedes the earlier restart capsule. Resume from version 0.2 and the accompanying tracker; do not repeat initial scoping or begin model training.



## 13. Session 3: broad scoping, PRISMA workflow and shared Drive workspace

**Date:** 13 October 2026, Africa/Lagos. **Version:** 0.3.

### User steering
Daniel asked to add memory, agent and task files to the ZIP; broaden literature scoping before reviewing/grouping papers; use PRISMA-style reporting; adapt his 30-column medical-imaging corpus schema; and prepare screening, evidence and synthesis records. He then supplied the Trustworthy_AI_Energy Drive folder.

### Methodological decision
Interpreted “PRISMA_src” as PRISMA-ScR and checked the official guidance. Use PRISMA-ScR for scoping-review reporting, PRISMA-S for search reporting and JBI guidance for conduct. The design is a systematic scoping review and evidence map. Whether to undertake a narrower systematic review is a later decision. PRISMA reporting does not itself establish a complete or rigorous review.

Protocol v0.3 is a dated draft, not preregistered. It broadens discovery beyond the earlier selective-prediction working question. Cluster, pillar and method-family assignments remain unassigned until charting. Core context is AI visual industrial inspection; adjacent bridge and blade evidence must retain its context.

### Searches performed and captured
Executed 16 scalar, ranked Crossref bibliographic query families with 25 records per query and a publication cutoff of 13 October 2026. Three first-run requests returned HTTP 429; a separately logged retry captured the missing pages.
Captured raw JSON, exact query and field, request URL, filter, date/time, offset, requested limit, returned records and SHA256.
Additional primary-source and identifier lookups enriched seed metadata. Metadata enrichment is not counted as new discovery.

Pilot audit:
- Crossref retrieval occurrences: 400.
- Seed occurrences: 33.
- Total captured occurrences: 433.
- Duplicate occurrences by persistent identity: 73.
- Unique report records: 360.
- Prioritised reading queue: 230, including supporting methodology.
- Formal title/abstract decisions, full-text decisions and final inclusions: zero; these tasks are pending.

Crossref is fuzzy, ranked and capped. Its large API total-results values are not eligible-paper counts. No Scopus, Web of Science, IEEE or ACM full database export was conducted. This pilot is not an exhaustive or completed systematic search.

### Corpus and workflow changes
Preserved Daniel's 30 fields and added ten for study identity, discovery source, search IDs, publication status, reading stage, metadata verification, record type, reading priority, evidence location and check date.
Names remain as deposited; initials are not expanded. Some author/year/venue fields remain missing. Bibliographic drafts and metadata verification do not count as final citation verification.
Generated a draft BibTeX file with keys, but all citations still require verification.
All identified records remain in the screening ledger. A transparent title prioritisation rule selects the reading queue; it does not silently exclude records.
Separate report identity from Study ID and preserve possible preprint/journal linkage for later verification.

The workbook has nine sheets: Overview, Corpus, Screening, Identification, Searches, Evidence matrix, Synthesis, Data audit and Decisions.
The evidence matrix retains six pilot selected-section extracts with human audit pending. All remaining scientific fields await extraction.
Synthesis prompts are working questions and provisional observations, not field-wide gap findings.
Reviewer fields are unassigned. No dual-human screening or independent double extraction is claimed.

### Continuity and reproducibility
Added memory.md, AGENTS.md, agent.md and task.md.
Added protocol, amendments, search specification, reason codes, data dictionary, draft taxonomy codebook, raw search snapshots, identity registry and replay/validation scripts.
Preserved the previous corpus/search/decision records under legacy-session2.
The older narrow scope and closest-work memo are labelled historical rather than deleted.
Replayed the records and validated raw hashes, IDs, occurrence accounting and queue/ledger links.
Checked workbook formulas, missing-reviewer behaviour, tables, validation and visual layout.

### Shared workspace
Drive folder: https://drive.google.com/drive/folders/15KlOofeUQ7soHwr26TbkoSw-7ppkw9eD
Native tracker: https://docs.google.com/spreadsheets/d/14NW5z6UziqVTzN2ZsmPbhT8Nmjo-ZQzQo0YaLDvNHTw/edit

Native import, folder parent, table coverage, dropdown columns and overview counts were verified. The Google Sheet timezone is Africa/Lagos. The archived XLSX is a snapshot; future edits must read current shared-sheet changes before synchronisation.
No GitHub repository has been created.

### Next research work
Pilot eligibility on 20 varied records; appoint/reveal the reviewer arrangement; refine and freeze the protocol; execute full subject-database searches and citation tracing; link report versions; screen and chart; then develop taxonomy and synthesis.
Do not select or implement an original technical project merely because a pilot search found a promising title.

This session supersedes the session 2 working angle and restart capsule. Current restart files are memory.md, AGENTS.md, task.md and protocol.md v0.3.



# Research-story continuation 04
Date: 13 October 2026, Africa/Lagos.

User repeated the instruction to continue in Trustworthy_AI_Energy. Existing native tracker identity and requested parent folder were confirmed. The existing sheet was preserved because it has a later modification timestamp than the original import and may contain user work.

Produced a separate 20-record eligibility calibration packet, explicit title/metadata evidence limits, reviewer fields, candidate rule clarifications and two expanded draft arXiv searches. No manuscripts, abstracts or full texts were newly assessed; no human reviewers were assigned or simulated. No search hits were added.

Counts remain 433 captured occurrences, 360 unique reports and 230 prioritised records from the last verified intake snapshot. No confirmed screening or inclusion totals were inferred from the live sheet in this session. Pilot calibration is pending human review.

Next research action: retrieve abstracts for the 20 records, document human reviewer decisions and reconcile rule ambiguity; validate and execute the planned source searches with complete exports.

Core working title remains Reliability of AI-Based Visual Industrial Inspection: A Systematic Scoping Review and Evidence Map. No novelty claim or final taxonomy is established. GitHub publication remains pending.


## Session 05 — GitHub workspace, 14 October 2026
Daniel created https://github.com/Engr-Daniel/trustworthy-ai-energy and authorised uploading the prepared workspace. The empty public repository is being initialised on its existing default branch, master. The saved v0.3 corpus and workbook are a snapshot; the shared Google Sheet has not been overwritten. Session 04 eligibility suggestions remain title/metadata-only, not formal screening. No new papers were retrieved in this publication step.

## Session 06 - Repository review, 14 October 2026
Flattened the nested repository into the single Personal/trustworthy-ai-energy folder. Reviewed the local research workflow and saved records. Added validation for identity/duplicate links, metadata hashes and workbook JSON/CSV agreement, with non-assert checks that remain active under Python optimisation. Ten XML files had Windows checkout line-ending changes; restored only bytes that match the original manifest checksums and added raw-capture Git attributes. Replay now writes to a separate empty output directory with explicit UTF-8 and portable paths; tests verify reproduction and reject overwrite attempts. Added contributor guidance and milestone acceptance criteria. No research decisions, counts, scientific extractions or live Sheet data were changed. GitHub access failed, so no remote-state verification, publication or hosted CI result is claimed. See docs/repository-review-20261014.md for findings and local validation.

## Session 07 - Publication verification and research handoff, 14 October 2026

Published the reviewed improvements in commit 090f5dbcb6ab365fd6f4325258d7e60e365ad0d4. Verified GitHub Actions run 38629633313, conclusion success, including successful validator and regression steps in all four Windows/Ubuntu and Python 3.10/3.12 jobs. Earlier GitHub access limitations were resolved.

Established docs/workbook-synchronisation.md with version identities, field/key mappings, three-way reconciliation, conflict handling and release/readback checks. Archived-XLSX audit shows matching mapped key sets and no substantive differences; date/timestamp representations differ, the identity field is CSV-only and historical searches are a separate block. The live Sheet was inspected for metadata and bounded header/sample ranges only; full data equivalence was not established, and no cells were written.

Prepared separate abstract evidence for the existing 20-record pilot: 14 available, six unresolved after recorded retrieval attempts. Used saved primary/deposited captures where available and retained new request provenance, hashes and failures. P08 matching-title preprint is a linkage candidate, not a confirmed merged study. Human reviewer arrangement was requested and remains pending. No eligibility decisions, extraction conclusions, novelty findings or formal counts changed. Snapshot counts remain 433 occurrences, 360 reports and 230 queue records.

### Reviewer arrangement confirmed - 14 October 2026
Daniel confirmed primary human screening by Daniel with a documented secondary audit. Secondary auditor identity and audit details remain pending; no independent dual-review claim is made and no screening decisions or audit outcomes are implied. See review-paper/screening/abstracts-20261014/reviewer-arrangement.md.

The workbook/abstract handoff was published in commit [8e0a54d](https://github.com/Engr-Daniel/trustworthy-ai-energy/commit/8e0a54d7da5d076e41a34c53a486bc9a84135142). Hosted [CI run 38630741777](https://github.com/Engr-Daniel/trustworthy-ai-energy/actions/runs/38630741777) passed all four jobs, including the pilot validator and all eight regression tests. This verifies software/data checks, not research completeness or eligibility.

## Session 08 - Calibration readiness, 14 October 2026
Retried the six unresolved abstracts using primary source pages/metadata and logged requests, errors, exact discovery queries and raw hashes. Recovered a matching-title arXiv:2107.10880 abstract for C0028; OSF/preprint linkage remains unverified. Abstract availability is 15/20 with five unresolved captures. No paper was excluded for failed retrieval and no identities were merged.

Implemented screening provenance validation and a separate 20-record pending human decision template. Confirmed decisions now require reviewer/date/protocol/evidence/rationale, stage-appropriate exclusion codes, ledger/evidence agreement and derived counts. Full-text decisions require retrieved text; synthesis admission requires linked study and completed secondary audit. Pending templates passing checks do not establish completed human review. Added regression cases for valid primary decisions, missing provenance, count mismatch, NR01 misuse, progression and audit gates. No actual decisions or audit results were created. The saved corpus, workbook and live Sheet remain unchanged; 433/360/230 are still snapshot counts.

Published calibration readiness in commit [b98c16c](https://github.com/Engr-Daniel/trustworthy-ai-energy/commit/b98c16ce07f29ea929d41344fa5d8de0be2d3b39). Verified [GitHub Actions run 38637160912](https://github.com/Engr-Daniel/trustworthy-ai-energy/actions/runs/38637160912): all four Windows/Ubuntu and Python 3.10/3.12 jobs passed the record validator and all 15 tests. No human screening or research-completeness conclusion follows from these checks.
