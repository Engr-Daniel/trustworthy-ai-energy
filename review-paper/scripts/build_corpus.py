#!/usr/bin/env python3
"""Replay saved pilot snapshots into stable records, a reading queue and audit CSVs.
No network required. Title prioritisation does not decide eligibility.
Identity: exact DOI, then arXiv ID. A title match attaches a seed only when unique;
different persistent identifiers are never collapsed on title alone.
"""
import argparse,csv,datetime,hashlib,html,json,pathlib,re,unicodedata,xml.etree.ElementTree as ET
from collections import defaultdict
from html.parser import HTMLParser
ROOT=pathlib.Path(__file__).resolve().parents[2]
C=ROOT/"review-paper/corpus";RUNS=ROOT/"review-paper/search-strategy/runs"
def norm(s):return re.sub(r"[^a-z0-9]","",unicodedata.normalize("NFKD",s).encode("ascii","ignore").decode().lower())
def readcsv(p):return list(csv.DictReader(p.open(encoding="utf-8")))
def writecsv(p,rows,headers=None):
 if headers is None:headers=list(rows[0]) if rows else []
 with p.open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=headers);w.writeheader();w.writerows(rows)
def crossref(m,source):
 dates=[m.get(k,{}).get("date-parts",[[]])[0] for k in ["published","published-online","published-print"]]
 dates=[d for d in dates if d]
 d=min(dates) if dates else []
 authors=m.get("author",[])
 names=[" ".join(filter(None,[a.get("given",""),a.get("family",a.get("name",""))])) for a in authors]
 title=html.unescape(re.sub("<[^>]+>","",(m.get("title") or [""])[0]))
 return {"title":title,"doi":m.get("DOI","").lower(),"arxiv":"","authors":"; ".join(names),
         "first_author":names[0] if names else "","year":d[0] if d else None,
         "venue":(m.get("container-title") or [""])[0],"publisher":m.get("publisher",""),
         "publisher_url":m.get("resource",{}).get("primary",{}).get("URL",m.get("URL","")),
         "access_url":m.get("URL",""),"record_type":m.get("type",""),"metadata_source":source,
         "metadata_status":"Verified against deposited metadata; publisher citation check pending"}
def arxiv(p,source):
 ns={"a":"http://www.w3.org/2005/Atom","x":"http://arxiv.org/schemas/atom"}
 tree=ET.parse(p);e=tree.find("a:entry",ns)
 if e is None:raise ValueError("arXiv entry missing")
 title=" ".join(e.findtext("a:title","",ns).split());names=[x.findtext("a:name","",ns) for x in e.findall("a:author",ns)]
 aid=re.search(r"(\d{4}\.\d{4,5})",e.findtext("a:id","",ns))
 return {"title":title,"doi":e.findtext("x:doi","",ns).lower(),"arxiv":aid.group(1) if aid else "",
         "authors":"; ".join(names),"first_author":names[0] if names else "",
         "year":int(e.findtext("a:published","",ns)[:4]),"venue":e.findtext("x:journal_ref","arXiv preprint",ns),
         "publisher":"arXiv","publisher_url":e.findtext("a:id","",ns),"access_url":e.findtext("a:id","",ns),
         "record_type":"arxiv-preprint","metadata_source":source,
         "metadata_status":"Verified against arXiv metadata; publication linkage pending"}
class Meta(HTMLParser):
 def __init__(self):super().__init__();self.fields=defaultdict(list)
 def handle_starttag(self,t,a):
  if t=="meta":
   x=dict(a)
   if x.get("name","").startswith("citation_"):self.fields[x["name"]].append(x.get("content",""))
def title_queue(t):
 asset=re.search(r"industrial|manufactur|defect|corrosion|inspection|quality control|pipeline|bridge|steel|thermal|infrared",t,re.I)
 visual=re.search(r"visual|vision|imag|segment|pixel|RGB|multimodal|anomal|defect|thermal|infrared|corrosion",t,re.I)
 outside=re.search(r"medic|healthcare|autonomous driving|brain|tumor|breast|road damage",t,re.I)
 return "Title-scope candidate" if asset and visual and not outside else "Lower-priority; inspect scope"

def main():
 parser=argparse.ArgumentParser(description="Replay the saved pilot into a new, empty directory; never overwrite research records.")
 parser.add_argument("--output-dir",required=True,type=pathlib.Path,help="New or empty directory for generated artifacts")
 args=parser.parse_args()
 output=args.output_dir.resolve()
 if output==C.resolve() or C.resolve() in output.parents:
  parser.error("Choose an output directory outside the source corpus")
 if output.exists() and (not output.is_dir() or any(output.iterdir())):
  parser.error("Output directory must be new or empty")
 output.mkdir(parents=True,exist_ok=True)
 legacy=readcsv(C/"legacy-session2/corpus.csv")
 extras=json.loads((C/"additional-seeds.json").read_text(encoding="utf-8"))+json.loads((C/"baseline-seeds.json").read_text(encoding="utf-8"))
 seeded=[]
 for s in legacy:
  u=s["Primary source URL"];doi=re.search(r"(10\.\d{4,9}/[^\s?#]+)",u);ar=re.search(r"arxiv.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})",u)
  seeded.append({"id":s["ID"],"title":s["Title"],"doi":doi.group(1).lower() if doi else "",
                 "arxiv":ar.group(1) if ar else "","paper_type":s["Type"],"url":u,
                 "year":int(s["Year"]) if s["Year"] else None,"reading":s["Reading stage"],
                 "evidence":s["Evidence extracted"],"implication":s["Novelty implication"],"next":s["Next action"]})
 for ident,typ,t,doi,ar,u in extras:
  seeded.append({"id":ident,"title":t,"doi":doi.lower(),"arxiv":ar,"paper_type":typ,"url":u,"year":None,
                 "reading":"Metadata only","evidence":"","implication":"","next":"Title/abstract screening"})
 search_rows=[];events=[];unique={};title_index=defaultdict(list)
 for run in sorted(RUNS.glob("PILOT-*")):
  manifest=json.loads((run/"search_manifest.json").read_text(encoding="utf-8"))
  for s in manifest["searches"]:
   search_rows.append({"Run ID":manifest["run_id"],"Search ID":s["search_id"],"Source/platform":s["platform"],
    "Search purpose":s["theme"],"Exact query":s["exact_query"],"Field":s["field"],"Filters":s["filters"],
    "Run status":s["status"],"Returned records":s["records_returned"],"API fuzzy hit count":s.get("api_total_results"),
    "Capture limit":s["rows_requested"],"Pagination":s["pagination"],"Search time UTC":s["started_utc"],
    "Raw file":(run/s.get("raw_file","")).relative_to(ROOT).as_posix() if s.get("raw_file") else "",
    "SHA256":s.get("sha256",""),"Notes":s.get("error",s.get("note",""))})
   if s["status"]!="completed":continue
   raw=run/s["raw_file"];blob=raw.read_bytes()
   if hashlib.sha256(blob).hexdigest()!=s["sha256"]:raise ValueError("Raw hash mismatch")
   for rank,m in enumerate(json.loads(blob)["message"]["items"],1):
    meta=crossref(m,raw.relative_to(ROOT).as_posix());key="doi:"+meta["doi"] if meta["doi"] else "title:"+norm(meta["title"])
    event={"Event ID":f"{manifest['run_id']}-{s['search_id']}-{rank:03d}","Source":"Crossref pilot","Run ID":manifest["run_id"],
           "Search ID":s["search_id"],"Rank":rank,"Identity":key,"Title":meta["title"],"DOI":meta["doi"],"Duplicate of":""}
    if key in unique:event["Duplicate of"]=unique[key]["event"]
    else:unique[key]={"meta":meta,"event":event["Event ID"],"searches":[],"seed":None};title_index[norm(meta["title"])].append(key)
    unique[key]["searches"].append(s["search_id"]);events.append(event)
 # Resolve seeds from saved identifier metadata, keeping previous IDs.
 for seed in seeded:
  meta=None
  for prefix in ["SEED-METADATA-20261013","BASELINE-METADATA-20261013"]:
   run=RUNS/prefix;mp=run/"metadata_manifest.json"
   if not mp.exists():continue
   log=json.loads(mp.read_text(encoding="utf-8"))
   a=next((a for a in log["attempts"] if a["id"]==seed["id"] and a["status"]=="completed"),None)
   if a:
    p=run/a["file"]
    if hashlib.sha256(p.read_bytes()).hexdigest()!=a["sha256"]:raise ValueError("Metadata hash mismatch")
    if p.suffix==".json":meta=crossref(json.loads(p.read_text(encoding="utf-8"))["message"],p.relative_to(ROOT).as_posix())
    elif p.suffix==".xml":meta=arxiv(p,p.relative_to(ROOT).as_posix())
    elif p.suffix==".html":
     x=Meta();x.feed(p.read_text(encoding="utf-8"));v=x.fields;names=v.get("citation_author",[])
     meta={"title":v.get("citation_title",[seed["title"]])[0],"doi":v.get("citation_doi",[""])[0].lower(),"arxiv":"",
       "authors":"; ".join(names),"first_author":names[0] if names else "","year":int(v.get("citation_publication_date",["2024"])[0][:4]),
       "venue":v.get("citation_conference_title",["CVPR 2024"])[0],"publisher":"CVF","publisher_url":seed["url"],"access_url":seed["url"],
       "record_type":"conference-paper","metadata_source":p.relative_to(ROOT).as_posix(),"metadata_status":"CVF metadata inspected"}
    break
  if meta is None:
   matches=title_index.get(norm(seed["title"]),[])
   meta=unique[matches[0]]["meta"].copy() if len(matches)==1 else {"title":seed["title"],"doi":seed["doi"],"arxiv":seed["arxiv"],
    "authors":"","first_author":"","year":seed["year"],"venue":"","publisher":"","publisher_url":seed["url"],"access_url":seed["url"],
    "record_type":"unresolved","metadata_source":"Legacy/web seed","metadata_status":"Needs bibliographic verification"}
  if not meta["arxiv"]:meta["arxiv"]=seed["arxiv"]
  # Preserve a verified DOI over an arXiv-only entry.
  if not meta["doi"]:meta["doi"]=seed["doi"]
  key="doi:"+meta["doi"] if meta["doi"] else "arxiv:"+meta["arxiv"] if meta["arxiv"] else "seed:"+seed["id"]
  # Attach identifier-free seed by one unique exact normalised title only.
  if key not in unique and not meta["doi"]:
   match=title_index.get(norm(meta["title"]),[])
   if len(match)==1:key=match[0]
  event={"Event ID":"SEED-"+seed["id"],"Source":"Seed register","Run ID":"SEED-20261013","Search ID":"SEED","Rank":None,
         "Identity":key,"Title":seed["title"],"DOI":meta["doi"],"Duplicate of":unique[key]["event"] if key in unique else ""}
  if key not in unique:unique[key]={"meta":meta,"event":event["Event ID"],"searches":[],"seed":seed}
  else:unique[key]["seed"]=seed;unique[key]["meta"]=meta
  unique[key]["searches"].append("SEED");events.append(event)
 registry_path=C/"identity-registry.json"
 registry=json.loads(registry_path.read_text(encoding="utf-8")) if registry_path.exists() else {}
 records=[];counter=max([int(v[1:]) for v in registry.values() if re.fullmatch(r"C\d+",v)]+[0])
 for key,u in unique.items():
  if u["seed"]:ident=u["seed"]["id"]
  elif key in registry:ident=registry[key]
  else:counter+=1;ident=f"C{counter:04d}"
  u["paper_id"]=ident
  registry[key]=ident
 (output/"identity-registry.json").write_text(json.dumps(registry,indent=2),encoding="utf-8")
 for e in events:e["Paper ID"]=unique[e["Identity"]]["paper_id"]
 headers=["Paper ID","Cluster ID","Cluster","Secondary Cluster","Pillar","Full Authors","First Author","Year","Full Title",
  "Venue / Journal","DOI","arXiv ID","Publisher URL","URL (Paper Access)","Modality","Task","Shift Type","Dataset / Benchmark",
  "Method Family","Paper Type","Evidence Type Rationale (keywords)","Method Family Assignment Rationale (if ambiguous)",
  "Evaluation Type","Inclusion Rationale","BibTeX Key","BibTeX Status","Cited in Main Text?","Citation Verified?","Accessible?",
  "Status","Study ID","Search IDs","Source Platform","Publication Status","Reading Stage","Metadata Status",
  "Record Type","Automated Queue","Evidence Locator","Last Checked"]
 ledger=[]
 for key,u in unique.items():
  m=u["meta"];seed=u["seed"];ident=u["paper_id"];queue="Supporting methodology" if seed and seed["paper_type"]=="Methodology" else "Seed priority" if seed else title_queue(m["title"])
  pt=seed["paper_type"] if seed else "Unassigned"
  record={h:"" for h in headers}
  first=m["first_author"];surname=norm(first.split()[-1]) if first else "unknown"
  bib=f"{surname}{m['year'] or 'nd'}_{ident}"
  stage=seed["reading"] if seed else "Metadata only"
  pub="Preprint / repository record" if m["record_type"] in ["posted-content","arxiv-preprint"] else "Publication status unverified"
  if m["record_type"] in ["journal-article","proceedings-article","conference-paper"]:pub="Journal / conference record; peer review not audited"
  record.update({"Paper ID":ident,"Cluster ID":"Unassigned","Cluster":"Unassigned","Secondary Cluster":"Unassigned","Pillar":"Unassigned",
   "Full Authors":m["authors"],"First Author":first,"Year":m["year"],"Full Title":m["title"],"Venue / Journal":m["venue"],
   "DOI":m["doi"],"arXiv ID":m["arxiv"],"Publisher URL":m["publisher_url"],"URL (Paper Access)":m["access_url"],
   "Modality":"Not extracted","Task":"Not extracted","Shift Type":"Not extracted","Dataset / Benchmark":"Not extracted","Method Family":"Unassigned",
   "Paper Type":pt,"Evaluation Type":"Not extracted","Inclusion Rationale":"Pending eligibility screening",
   "BibTeX Key":bib,"BibTeX Status":"Generated; needs verification" if m["authors"] and m["year"] else "Incomplete metadata",
   "Cited in Main Text?":"No manuscript yet","Citation Verified?":"No","Accessible?":"Not checked",
   "Status":"Unscreened","Study ID":"Not linked","Search IDs":"; ".join(sorted(set(u["searches"]))),
   "Source Platform":"Seed metadata / primary source" if seed else "Crossref REST API",
   "Publication Status":pub,"Reading Stage":stage,"Metadata Status":m["metadata_status"],"Record Type":m["record_type"],
   "Automated Queue":queue,"Evidence Locator":m["metadata_source"],"Last Checked":"2026-10-13"})
  if stage in ["Full text retrieved","Section extraction"]:record["Accessible?"]="Full text retrieved; current link not rechecked"
  records.append(record)
  ledger.append({"Paper ID":ident,"Full Title":m["title"],"DOI":m["doi"],"arXiv ID":m["arxiv"],"Record Type":m["record_type"],
   "Source / Search IDs":record["Search IDs"],"Queue":queue,"Reviewer 1":"Not assigned","TA Decision R1":"Not started",
   "Reviewer 2":"Not assigned","TA Decision R2":"Not started","TA Final":"Pending","TA Reason Code":"",
   "Full text sought?":"Not started","Retrieval Result":"Not started","FT Decision R1":"Not started","FT Decision R2":"Not started",
   "FT Final":"Pending","FT Exclusion Code":"","Decision Rationale":"","Decision Date":"","Adjudicator":"",
   "Study ID":"Not linked","Included in synthesis?":"Pending","Decision Integrity":""})
 # Keep all IDs in ledger. Corpus is a reading queue, not an inclusion set.
 corpus=[r for r in records if r["Automated Queue"]!="Lower-priority; inspect scope"]
 corpus.sort(key=lambda r:(0 if not r["Paper ID"].startswith("C") else 1,r["Paper ID"]))
 writecsv(output/"corpus.csv",corpus,headers);writecsv(output/"records-ledger.csv",ledger);writecsv(output/"identification-events.csv",events)
 writecsv(output/"search-runs.csv",search_rows)
 writecsv(output/"deduplication.csv",[{"Event ID":e["Event ID"],"Paper ID":e["Paper ID"],"Duplicate of":e["Duplicate of"],"Identity":e["Identity"]} for e in events if e["Duplicate of"]])
 # BibTeX from exact deposited names. It is a draft bibliography, not citation verification.
 entries=[]
 for r in corpus:
  meta=next(u["meta"] for u in unique.values() if u["paper_id"]==r["Paper ID"])
  esc=lambda s:str(s).replace("{","\\{").replace("}","\\}").replace("&","\\&").replace("%","\\%")
  fields={"title":r["Full Title"],"author":r["Full Authors"].replace("; "," and "),"year":r["Year"] or "",
          "journal":r["Venue / Journal"],"doi":r["DOI"],"eprint":r["arXiv ID"],"url":r["URL (Paper Access)"]}
  entries.append("@misc{"+r["BibTeX Key"]+",\n"+",\n".join("  "+k+" = {"+esc(v)+"}" for k,v in fields.items() if v)+"\n}")
 (output/"references-draft.bib").write_text("\n\n".join(entries),encoding="utf-8")
 stats={"retrieval_occurrences":len(events),"crossref_occurrences":sum(e["Source"]=="Crossref pilot" for e in events),
        "seed_occurrences":sum(e["Source"]=="Seed register" for e in events),"duplicate_occurrences":sum(bool(e["Duplicate of"]) for e in events),
        "unique_reports":len(unique),"reading_queue":len(corpus),"automatic_title_candidates":sum(r["Automated Queue"]=="Title-scope candidate" for r in records),
        "formal_screened":0,"formal_included":0,"status":"Pilot identification; screening not started"}
 (output/"scope-counts.json").write_text(json.dumps(stats,indent=2),encoding="utf-8")
 (output/"workbook-data.json").write_text(json.dumps({"corpus":corpus,"ledger":ledger,"events":events,"searches":search_rows,"counts":stats},ensure_ascii=False),encoding="utf-8")
 print(json.dumps(stats))
if __name__=="__main__":main()
