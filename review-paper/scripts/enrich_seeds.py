#!/usr/bin/env python3
"""Resolve seed bibliography from DOI metadata and arXiv Atom snapshots.
Every network attempt is logged. Names remain exactly as deposited.
"""
import concurrent.futures,csv,datetime,hashlib,json,pathlib,re,urllib.parse,urllib.request,xml.etree.ElementTree as ET
root=pathlib.Path(__file__).resolve().parents[2]
out=root/"review-paper/search-strategy/runs/SEED-METADATA-20261013"
out.mkdir(parents=True,exist_ok=True)
seeds=list(csv.DictReader((root/"review-paper/corpus/corpus.csv").open()))
extra=json.loads((root/"review-paper/corpus/additional-seeds.json").read_text())
req=[]
for s in seeds:
 u=s["Primary source URL"];doi=re.search(r'(10\.\d{4,9}/[^\s?#]+)',u)
 ar=re.search(r'arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})',u)
 req.append((s["ID"],doi.group(1) if doi else "",ar.group(1) if ar else ""))
req.extend((x[0],x[3],x[4]) for x in extra)
log=[]
def fetch(row):
 ident,doi,arxiv=row
 if not doi and not arxiv:return {"id":ident,"status":"not_attempted","reason":"No verified identifier"}
 url="https://api.crossref.org/works/"+urllib.parse.quote(doi,safe="") if doi else "https://export.arxiv.org/api/query?"+urllib.parse.urlencode({"id_list":arxiv})
 attempt={"id":ident,"doi":doi,"arxiv":arxiv,"url":url,"time_utc":datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"IndustrialInspectionScoping/0.3"}),timeout=25) as r:b=r.read()
  ext=".json" if doi else ".xml";(out/(ident+ext)).write_bytes(b)
  attempt.update(status="completed",file=ident+ext,sha256=hashlib.sha256(b).hexdigest())
 except Exception as exc:attempt.update(status="failed",error=str(exc))
 print(ident,attempt["status"],flush=True);return attempt
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:log=list(pool.map(fetch,req))
(out/"metadata_manifest.json").write_text(json.dumps({"attempts":log},indent=2))
