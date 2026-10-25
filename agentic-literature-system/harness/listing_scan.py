"""Bounded traversal of observed arXiv pagination links; preserves raw title pool."""
import re
import time
from urllib.parse import parse_qs, urlparse


def scan_listing(category,mode,max_pages,fetch,parse_entries,max_seconds=150):
    path=f'/list/{category}/{mode}'
    pending={0:f'https://arxiv.org{path}?skip=0&show=100'}
    visited=set();pages=[];entries={};total=None;started=time.monotonic();errors=[];page_totals=[];attempts=0;warnings=[]
    while pending and attempts<max_pages and time.monotonic()-started<max_seconds:
        skip=min(pending);url=pending.pop(skip)
        if skip in visited:continue
        visited.add(skip)
        attempts+=1
        try:page=fetch(url)
        except Exception as exc:
            errors.append({'url':url,'error':type(exc).__name__+': '+str(exc)});continue
        parsed=parse_entries(page['text'])
        for entry in parsed:
            key=re.sub(r'v\d+$','',entry['arxiv'])
            entries.setdefault(key,entry)
        pages.append({'url':url,'entry_count':len(parsed),'retrieved_at':page.get('retrieved_at'),'sha256':page.get('sha256')})
        match=re.search(r'total\s+of\s+([\d,]+)\s+entries',page['text'],re.I)
        if match:
            page_totals.append(int(match.group(1).replace(',','')))
            total=max(total or 0,page_totals[-1])
        # A single observed "all" page avoids combining shifting pagination snapshots.
        # It consumes one page of the same budget and is used only if it is complete.
        if skip==0 and max_pages>1:
            for link in page.get('links',[]):
                parsed_url=urlparse(link['url']);query=parse_qs(parsed_url.query)
                if link.get('text','').lower()!='all' or parsed_url.hostname!='arxiv.org' or parsed_url.path!=path or query.get('skip')!=['0']:continue
                try:capacity=int(query['show'][0])
                except (KeyError,ValueError,IndexError):continue
                if not 100<capacity<=2000 or (total and total>capacity):continue
                attempts+=1
                try:
                    full=fetch(link['url']);full_entries=parse_entries(full['text'])
                    count=re.search(r'total\s+of\s+([\d,]+)\s+entries',full['text'],re.I)
                    expected=int(count.group(1).replace(',','')) if count else None
                    unique={re.sub(r'v\d+$','',e['arxiv']):e for e in full_entries}
                    contains_first_page=set(entries)<=set(unique)
                    if expected is not None and len(full_entries)==expected and contains_first_page:
                        return {'entries':list(unique.values()),'pages':pages+[{'url':link['url'],'entry_count':len(full_entries),'retrieved_at':full.get('retrieved_at'),'sha256':full.get('sha256')}],
                                'data_source_url':link['url'],'navigation_source_url':url,'reported_total_entries':expected,
                                'unvisited_observed_urls':[],'complete_observed_pagination':True,'consistent_listing_snapshot':True,
                                'errors':[],'warnings':warnings,'requests_attempted':attempts,'elapsed_seconds':time.monotonic()-started,
                                'warning':'All title entries come from one observed full-list response. This is source-list completeness, not relevance recall or a historical availability guarantee.'}
                    warnings.append({'url':link['url'],'warning':'Full-list response rejected: it is incomplete or omits IDs already seen on the first page','reported_total':expected,'contains_first_page':contains_first_page})
                except Exception as exc:
                    errors.append({'url':link['url'],'error':type(exc).__name__+': '+str(exc)})
                break
        for link in page.get('links',[]):
            if not re.fullmatch(r'\d+\s*[-–]\s*\d+',link.get('text','')):continue
            parsed_url=urlparse(link['url']);query=parse_qs(parsed_url.query)
            if parsed_url.hostname!='arxiv.org' or parsed_url.path!=path or query.get('show')!=['100']:continue
            try:other=int(query['skip'][0])
            except (KeyError,ValueError,IndexError):continue
            if other>=0 and other not in visited:pending[other]=link['url']
    consistent=len(set(page_totals))<=1
    if not consistent:errors.append({'error':'Listing totals changed between pages; this is not a consistent snapshot','observed_totals':sorted(set(page_totals))})
    delivered=sum(p['entry_count'] for p in pages)
    if not pending and total is not None and delivered!=total:errors.append({'error':'Parsed entry count does not match source total','parsed_entries':delivered,'reported_total':total})
    return {'entries':list(entries.values()),'pages':pages,'reported_total_entries':total,'consistent_listing_snapshot':consistent,
            'unvisited_observed_urls':[url for _,url in sorted(pending.items())],
            'complete_observed_pagination':not pending and not errors,
            'errors':errors,'warnings':warnings,'requests_attempted':attempts,'elapsed_seconds':time.monotonic()-started,
            'warning':'Completeness refers only to observed pagination of this source listing, not all research papers or relevance recall. Cross-lists may share identities.'}
