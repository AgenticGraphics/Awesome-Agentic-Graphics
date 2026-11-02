"""Migrate already retrieved public observations into an explicit experiment cache.
Copies raw retrievals only; never reads model reports or paper classifications.
New as-of frames normally start an empty cache automatically.
"""
import argparse,json,shutil
from research_tools import ROOT,digest,save,now
p=argparse.ArgumentParser();p.add_argument('--as-of',required=True);a=p.parse_args()
out=ROOT/'cache/observations'/digest(a.as_of)[:16];out.mkdir(parents=True,exist_ok=True)
files={}
for pattern in ('*.page.json','*.search.json','*.pdf.json'):
    for path in (ROOT/'cache').glob(pattern):
        target=out/path.name
        if not target.exists():shutil.copy2(path,target)
        files[path.name]=digest(path.read_bytes())
save(out/'migration.json',{'created_at':now(),'as_of':a.as_of,'source':'legacy public-retrieval cache only','files':files,'note':'The as-of time constrains paper release eligibility. Individual retrieved_at timestamps record actual fetch times, which can be later.'})
print('Frozen public observations:',len(files))
