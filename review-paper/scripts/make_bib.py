#!/usr/bin/env python3
"""Build manuscript/refrence.bib for included studies and cited methodology records, with a verification log.

No network required. Metadata come from corpus.csv (OpenAlex/Crossref/seed records). For each included
study the primary report's title is checked against page 1 of its retrieved full text (>= 80% of title
words present); methodology/seed records not retrieved are marked as checked against deposited DOI metadata
only when corpus Metadata Status says so. Entries failing a check are still written but flagged in
manuscript/citation-verification.csv, which the author must clear before submission.
"""
import csv, pathlib, re, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
RP = ROOT / "review-paper"
EXTRA = ["F01", "F02", "F03", "B01", "R01", "R02", "R03", "R04", "R10", "R11", "C0006", "O0744"]  # methodology, MVTec AD, retrieved prior reviews

def read(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def latex(s):
    s = unicodedata.normalize("NFC", s or "")
    for a, b in [("\\", " "), ("&", r"\&"), ("%", r"\%"), ("_", r"\_"), ("#", r"\#"), ("$", r"\$"), ("~", " ")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()

def ascii_word(s):
    return re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower())

def words(s):
    return [w for w in re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()) if len(w) > 2]

def main():
    corpus = {r["Paper ID"]: r for r in read(RP / "corpus/corpus.csv")}
    # Records outside the reading-queue corpus: ledger fields plus documented overrides from the primary source.
    ledger = {r["Paper ID"]: r for r in read(RP / "corpus/records-ledger.csv")}
    for o in read(RP / "manuscript/metadata-overrides.csv"):
        base = corpus.get(o["Paper ID"]) or {"Paper ID": o["Paper ID"], "Full Title": ledger[o["Paper ID"]]["Full Title"],
                                              "DOI": ledger[o["Paper ID"]]["DOI"], "arXiv ID": ledger[o["Paper ID"]]["arXiv ID"],
                                              "Record Type": ledger[o["Paper ID"]]["Record Type"], "Metadata Status": "Override: " + o["Source"]}
        base.update({k: o[k] for k in ("Full Authors", "Year", "Venue / Journal") if o[k]})
        corpus[o["Paper ID"]] = base
    charted = [r["Paper ID used"] for r in read(RP / "charting/charting.csv")]
    ids = charted + [e for e in EXTRA if e in corpus]
    entries, log, keys = [], [], {}
    for pid in ids:
        m = corpus[pid]
        authors = [a.strip() for a in m["Full Authors"].split(";") if a.strip()]
        first = ascii_word(authors[0].split()[-1]) if authors else "anon"
        key = f"{first or 'anon'}{m['Year'] or 'nd'}{ascii_word(words(m['Full Title'])[0] if words(m['Full Title']) else 'x')}"
        keys[key] = keys.get(key, 0) + 1
        if keys[key] > 1:
            key += chr(ord("a") + keys[key] - 1)
        rtype = m["Record Type"]
        kind = {"conference-paper": "inproceedings", "proceedings-article": "inproceedings", "book-chapter": "incollection",
                "dissertation": "phdthesis"}.get(rtype, "article" if rtype in ("article", "journal-article", "review") else "misc")
        fields = {"author": " and ".join(latex(a) for a in authors) or "{Anonymous}", "title": "{" + latex(m["Full Title"]) + "}",
                  "year": m["Year"] or "n.d."}
        venue = latex(m["Venue / Journal"])
        text = RP / "fulltext/text" / f"{pid}.txt"
        if kind == "phdthesis" and text.exists() and re.search(r"Master of Science|Masters? of Research|MSc", text.read_text(encoding="utf-8", errors="replace")[:4000]):
            kind = "mastersthesis"
        if kind == "article":
            fields["journal"] = venue or "Unknown venue"
        elif kind in ("inproceedings", "incollection"):
            fields["booktitle"] = venue or "Unknown proceedings"
        elif kind in ("phdthesis", "mastersthesis"):
            fields["school"] = venue or "Unknown institution"
        else:
            fields["howpublished"] = venue or ("arXiv preprint arXiv:" + m["arXiv ID"] if m["arXiv ID"] else "Preprint")
        if m["DOI"]:
            fields["doi"] = m["DOI"]
        elif m["arXiv ID"]:
            fields["note"] = "arXiv:" + m["arXiv ID"]
        entries.append(f"@{kind}{{{key},\n" + ",\n".join(f"  {k} = {{{v}}}" if k != "title" else f"  {k} = {v}" for k, v in fields.items()) + "\n}\n")
        if text.exists():
            page1 = " ".join(words(text.read_text(encoding="utf-8", errors="replace")[:6000]))
            tw = words(m["Full Title"])
            hit = sum(w in page1 for w in tw) / max(1, len(tw))
            status = "Verified: title matches retrieved full text page 1" if hit >= 0.8 else f"CHECK: only {hit:.0%} of title words on page 1"
        else:
            status = "Verified against deposited metadata (corpus)" if m["Metadata Status"].startswith("Verified") else "CHECK: not verified"
        log.append({"Paper ID": pid, "BibTeX key": key, "Entry type": kind, "DOI": m["DOI"], "arXiv ID": m["arXiv ID"],
                    "Verification": status, "Missing fields": "; ".join(k for k in ("author", "year", "venue")
                                                                       if (k == "author" and not authors) or (k == "year" and not m["Year"]) or (k == "venue" and not venue))})
    out = RP / "manuscript"
    (out / "refrence.bib").write_text("% Generated by scripts/make_bib.py from corpus.csv; see citation-verification.csv.\n\n" + "\n".join(entries), encoding="utf-8")
    with (out / "citation-verification.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(log[0])); w.writeheader(); w.writerows(log)
    flagged = [l for l in log if l["Verification"].startswith("CHECK") or l["Missing fields"]]
    print(len(entries), "entries;", len(flagged), "flagged:", [(l["Paper ID"], l["Verification"][:30], l["Missing fields"]) for l in flagged])

if __name__ == "__main__":
    main()
