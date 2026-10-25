"""Locate evidence in a PDF without pretending a snippet is a full-paper read."""
import hashlib
from pathlib import Path
import re


def search_pdf(path,queries,max_matches=8):
    import pymupdf
    if not isinstance(queries,list) or not 1<=len(queries)<=10 or any(not isinstance(q,str) or not q.strip() or len(q)>120 for q in queries):
        raise ValueError('Provide 1..10 nonempty literal queries, each at most 120 characters')
    if not isinstance(max_matches,int) or not 1<=max_matches<=30:raise ValueError('max_matches must be 1..30 per query')
    path=Path(path);patterns={q:re.compile(r'\s+'.join(re.escape(word) for word in q.split()),re.I) for q in queries}
    results={q:{'total_matches':0,'matches':[]} for q in queries}
    with pymupdf.open(path) as doc:
        total_pages=len(doc)
        for page_no,page in enumerate(doc,1):
            text=page.get_text()
            for query,pattern in patterns.items():
                for match in pattern.finditer(text):
                    item=results[query];item['total_matches']+=1
                    if len(item['matches'])<max_matches:
                        item['matches'].append({'page':page_no,'excerpt':text[max(0,match.start()-180):match.end()+300]})
    return {'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'total_pages':total_pages,
            'results':results,'note':'Literal search snippets only. This call does not produce a full-PDF delivery receipt. Read the surrounding context before treating a match as evidence about the studied system.'}
