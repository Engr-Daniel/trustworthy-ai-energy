# Check of scientific claims against source passages, 3 November 2026

Scope: every sentence in the Results and Discussion sections (from the evidence map to the Conclusion) that cites specific studies. That is 38 sentences. Sentences that cite only a generated dimension list (for example `\citeThree`) are reported counts, which `make_tables.py` derives from `charting.csv`. They are not checked here.

The checker is Claude, an AI assistant. It also made the eligibility and charting decisions, so this is a consistency check against the sources, not an independent verification.

## Method

1. **Numbers:** each number in a cited sentence was searched for in the cited study's retrieved full text, in `fulltext/text/`.
   - Ten sentences contain numbers outside their citation keys.
   - In nine, every number was found directly.
   - In the tenth, 92.2% and 97.2% for `alqahtani2026robust` were split across a PDF line break. The source reads "rejecting the top 20% of uncertain samples increases accuracy from a baseline of 92.22% to 97.22%" (O0289 p.11). It is confirmed.
2. **Wording:** each sentence was compared with the author-reported key finding, context and reliability dimensions charted for every cited study. Those charted fields carry page locators in `charting/charting.csv`.
3. **Mismatches:** where a sentence and its charted finding did not obviously agree, the full text was searched for the specific claim.

## Corrections made

- **R3, mitigation list:** `bai2026bridging` was listed as a domain-generalisation method. FGOS-Net is a segmentation architecture that was included for its cross-domain evaluation (p.14), not as a domain-generalisation method. It was removed from that list and stays in the R3 citation set.
- **R3, corruption sentence:** `agyemang2024multi` was grouped with corruption benchmarks. It is a detector evaluated under graded corruptions (p.16), not a benchmark. The sentence now says "graded corruption tests of individual detectors".

## Checked and supported (examples needing a source look-up)

- **`rintrawong2026coverage`,** cited for physical verification by ultrasonic thickness: O0021 p.2 says "ultrasonic gauging remains necessary for structural assessment".
- **`posadamoreno2023scale` (SPACE),** cited with work on Clever Hans effects missed by standard validation: its charted finding is that SPACE exposes biased or leaking concepts that standard validation misses. This is a different paper from the excluded O5610.

## Points for the author

- **Chemical-plant piping as energy context.** Two studies coded Core-energy (`shimbo2023pipe`, `shimbo2023operation`) concern external pipe corrosion in chemical plants. The Discussion calls them operational energy-asset studies. This follows the codebook coding that was audited on 2 November. Narrow it if the target journal reads "energy asset" more strictly.
- **Introduction and survey table.** The survey-comparison table and the introduction were not re-checked in this pass.
