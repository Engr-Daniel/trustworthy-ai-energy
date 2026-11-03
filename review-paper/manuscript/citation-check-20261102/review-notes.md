# Reference check, 2 November 2026

`scripts/check_citations.py` compared each of the 167 `refrence.bib` entries with its registration record. DOIs were checked through doi.org content negotiation (CSL JSON); arXiv-only entries were checked through the arXiv API. The raw responses and their SHA256 hashes are in `raw/` and `manifest.json`, and the per-entry results are in `report.csv`.

The first pass found errors that were corrected through `manuscript/metadata-overrides.csv`, with a source stated for each correction. Two earlier runs from the same day, made on the uncorrected or partially corrected bibliography, were overwritten. Only this final run is kept, re-compared with `--reuse` after the accent-handling fix.

## Corrections made after the first pass

- **Author names, from the registry record and the full-text byline:**
  - Sahoo (bib had "Prakash"), Liang Xu (bib had "Xu Liang"), You Li (bib had "Li You", 2 entries).
  - Rui Zhao and Ye Zheng (MIAD), Mingkai Lu and the full ICME 2026 challenge author list, Paul Berlin Ndjoko, Ítalo P. Caliari, İsmail Hakkı Kınalıoğlu, Sinan Ilyas and Cemil Oz, Jun Wu, Daniel Atewin Amoshie.
- **Compound surnames:** Dalle Pezze (4 entries), Sadat Taghavi, Ben Braiek, Naghavi Khanghah, Ghosh Mondal, Oliveira Santos, Le Callet.
- **Group author:** "PRISMA-S Group" is braced so BibTeX does not parse it as a person.
- **Years taken from the issued record:** poniatowski 2026, frittoli 2022, SoftPatch+ 2025, MVTec-C robustness benchmark 2024.
- **Venues:**
  - O0299 is MED 2021, not "2006 14th MED".
  - O1854 and O4372 are CASE 2024, not "2022 CASE".
  - O2564 is ASME IDETC/CIE 2025, not an arXiv preprint.
  - O2410 is in the AAAI proceedings.
  - O1852 is a Zenodo deposit.
  - OpenAlex host strings are normalised through `VENUE` in `make_bib.py`; examples are the CVPR string, "Lecture notes in…" and "Jornal of Kryvyi Rih…".
- **Identifiers:**
  - O1478's DOI 10.71465/jgs55 does not exist at doi.org, so the article URL is cited instead.
  - O1522's printed DOI 10.17051/ECC/04.03.01 does not exist either, so the entry carries no DOI.
  - O1608 gained arXiv:2603.26776, after confirming title and authors against the arXiv record.
- **Titles:** three all-capitals titles were set in title case, and a trailing period was removed.
- **Typesetting:**
  - Titles are double-braced, so IEEEtran keeps acronyms such as HDSI-YOLO.
  - Accented and Turkish letters are braced, so initials render correctly (for example J{\~{a}}o gives "J.").
  - Citation keys are now built from the surname. This fixed `dmytro2025synthetic`, which became `bondar2025synthetic`.

## Final status: 147 OK, 16 Check, 4 No identifier

Every remaining Check was read against the registry record and the full-text byline. None of them is a citation error.

| Pattern | Entries | Resolution |
|---|---|---|
| Registry puts the full name in the family field | khandagale (2), thakur, amoshie, shimbo, lo, zambuk | The bib follows the printed byline |
| Registry has blank author slots | estermann, yosifov, wang2024robustness | Named authors match the paper |
| Registry splits compound surnames wrongly ("Davide Dalle" / "Pezze", "Patrick Le" / "Callet") | poniatowski, bugarin, dallepezze, barusco, sun2026icme | The bib uses the correct surname |
| Apostrophe form (D'Antoni) | barusco | Same name |
| Group author and the particle "de Kock" | rethlefsen | Intentional |

The four entries without identifiers were verified against the retrieved full text only:

| Entry | Why there is no identifier |
|---|---|
| kulkarni2017classification | Virginia Tech MSc thesis |
| lapointe2022for | NRC Publications Archive |
| alvarez2026foundation | Its DOI is unregistered |
| reginald2026plant | Its printed DOI is unregistered |

Every title matches its registry record. Year disagreements were resolved in favour of the issued record.

## Flags for the author (appraisal, not citation correctness)

- **O1478 (alvarez2026foundation):** a manufacturing paper in a "Journal of Geospace Science" with an unregistered DOI.
- **O1522 (reginald2026plant):** its printed DOI is not registered.
- **O0449 (thakur2024deep):** the venue is a biomedical journal.

These records are eligible under the protocol. A Q1 venue may still question them, so consider noting them in the quality discussion.
