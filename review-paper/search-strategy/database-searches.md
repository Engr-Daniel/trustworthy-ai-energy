# Search specification and execution status
Version 0.3. Syntax below is planned, not executed.

## Keyword blocks
A Context: industrial OR manufactur* OR energy OR refinery OR petrochemical OR pipeline* OR corrosion OR bridge* OR infrastructure OR "asset inspection"
B Visual: image* OR visual OR vision OR RGB OR camera* OR infrared OR thermal OR multispectral OR hyperspectral OR "point cloud" OR RGB-D
C Inspection: defect* OR anomal* OR inspection OR "condition assessment" OR damage OR "surface assessment"
D AI: "machine learning" OR "deep learning" OR "artificial intelligence" OR neural OR transformer OR "computer vision"
E Reliability: uncertainty OR calibrat* OR robust* OR "domain shift" OR "distribution shift" OR "domain adaptation" OR "selective prediction" OR abstention OR "risk control" OR "human review" OR "missing modality" OR "sensor degradation" OR grounding OR hallucination OR "evidence grounded"

Broad discovery: A AND B AND C AND D
Reliability supplement: A AND B AND C AND E
Review overlap: A AND B AND C AND (review OR survey OR taxonomy)

## Database translations
Scopus: TITLE-ABS-KEY(A AND B AND C AND D), with each block expanded literally. Record exact expanded string and export all retrieved records.
Web of Science: TS=(A AND B AND C AND D), with expanded blocks. Record index collections and timespan.
IEEE Xplore: translate blocks to document title, abstract and author keywords within its current interface limits; split a long family into documented subqueries.
ACM Digital Library: translate and record the advanced-search fields and exact Boolean string.
arXiv/CVF/OpenReview: use precise industrial-vision query families and documented proceedings/citation searches; report coverage and any retrieval caps.

Placeholders A–E are notation for this draft, not runnable queries. Validate each platform's syntax before running and save the expanded query exactly as executed.
Do not use a publisher's search box as a substitute for a multi-database search without reporting that choice.

## Pilot implemented here
queries.json contains 16 actual scalar bibliographic queries.
Run PILOT-20261013-01: 13 queries succeeded, 3 hit HTTP 429.
Run PILOT-20261013-02: the 3 failed queries succeeded on a logged retry.
400 Crossref records were captured. Seed metadata lookups enrich existing records and do not add discovery occurrences.
Raw responses, timestamps, URLs, offsets, limits and SHA256 checksums are under runs/.

## Replay and expansion
From repository root:
```bash
python review-paper/scripts/build_corpus.py
python review-paper/scripts/validate_scope.py
```
Replay uses saved data and requires no network. It reproduces the pilot records and counts.

For a new live pilot:
```bash
python review-paper/scripts/collect_crossref.py --run-id NEW-UNIQUE-RUN-ID
```
Live results may change as indexes update. Never overwrite an old run.
To retry selected query IDs, pass --search-ids S02,S06,S11 and a new run ID.
A new live pilot may expand the record ledger but does not complete the planned subject searches.

## Importing formal exports
Preserve original RIS/BibTeX/CSV exports under runs/ with a search-manifest entry.
Implement a format-specific adapter after examining actual export headers.
Do not fabricate database counts, subtract uncaptured hits, or mark a search complete from a ranked preview.
