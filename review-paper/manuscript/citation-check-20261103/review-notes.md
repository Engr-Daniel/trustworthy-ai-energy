# Reference check, 3 November 2026

`scripts/check_citations.py --date 2026-11-03` compared all 185 `refrence.bib` entries with their registration records. The raw responses and SHA256 hashes are in `raw/` and `manifest.json`. Re-comparisons after corrections used `--reuse`.

The 18 entries added for the studies included on 3 November were checked on the first pass:
- **Agreed:** 14 matched the registry for title, first author and year.
- **Corrected:** 4 were fixed in `manuscript/metadata-overrides.csv`, with a source stated for each correction:

| Entry | Correction | Evidence |
|---|---|---|
| O5246 (`flotzinger2026synth`) | Author "Heiko Neumann B" corrected to Heiko Neumann (a stray letter from OpenAlex) | Full text p.1 and the registry record |
| O5735 (`liu2022deep`) | "Yang Chun-hua" corrected to Chunhua Yang | Full text p.1 and the registry record |
| O5819 (CrackGAN) | Year changed from 2020 to 2021; the key is now `zhang2021crackgan` | Registry record: issued February 2021, IEEE T-ITS |
| O6133 (`rillgarcia2022syncrack`) | OpenAlex had duplicated the second author; authors set to Rodrigo Rill-García, Eva Dokladalova and Petr Dokládal | HAL full text p.1 and the registry record |

Final result:
- **OK:** 165
- **Check:** 16, the same entries explained in `../citation-check-20261102/review-notes.md`
- **No identifier:** 4
