"""Source-derived date queue and coverage audit; never supplies relevance labels."""
import hashlib,json,re
from collections import Counter
from datetime import datetime,timedelta
from pathlib import Path

EXPECTED_SOURCES=('cs.GR-new','cs.GR-recent','cs.CV-new','cs.CV-recent')
FOCUS_BUCKETS={'target_day','history_needed','invalid_date'}
PAGE_FIELDS=('arxiv','title','abstract','version','canonical_url','source_entry_url',
             'published','updated','categories','date_queue','version_history_required',
             'metadata_sha256')


def source_provenance(rows):
    sources={}
    for row in rows:
        if row.get('metadata_source_url'):
            key=(row.get('metadata_sha256'),row['metadata_source_url'],row.get('metadata_retrieved_at'))
            sources[key]={'sha256':key[0],'url':key[1],'retrieved_at':key[2]}
    return list(sources.values())


def base_id(value):
    match=re.search(r'(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?(?!\d)',str(value))
    return match.group(1) if match else None


def timestamp(value):
    result=datetime.fromisoformat(value.replace('Z','+00:00'))
    if result.tzinfo is None:raise ValueError('Missing timestamp timezone')
    return result


def date_queue(record,frame):
    """Metadata dates are routing facts, not a complete intermediate-version history."""
    try:
        first,latest=timestamp(record['published']),timestamp(record['updated'])
        start,end,cutoff=(timestamp(frame[k]) for k in ('window_start','window_end','as_of'))
    except (KeyError,ValueError,TypeError,AttributeError):
        return 'invalid_date',True
    if latest<first:return 'invalid_date',True
    if first>cutoff:return 'after_cutoff',False
    # No revision can precede a paper's first publication. A paper first
    # published after the target window cannot conceal a target-day revision.
    if first>=end:return 'outside_window',False
    if any(start<=event<end and event<=cutoff for event in (first,latest)):
        return 'target_day',latest>cutoff
    # A later revision can hide an intermediate revision on the target day.
    if latest>=end or latest>cutoff:return 'history_needed',True
    if any(start-timedelta(days=7)<=event<start and event<=cutoff for event in (first,latest)):
        return 'lookback',False
    return 'outside_window',False


def build_catalog(run,frame,events):
    run=Path(run);sources={};identities={};source_errors=[]
    for path in sorted((run/'discovery').glob('*-titles.json')):
        raw=path.read_bytes();data=json.loads(raw)
        sources[path.stem.removesuffix('-titles')]={
            'path':str(path),'sha256':hashlib.sha256(raw).hexdigest(),
            'complete_observed_pagination':data.get('complete_observed_pagination',False)}
        for entry in data.get('entries',[]):
            key=base_id(entry.get('arxiv'))
            if not key:source_errors.append({'source':str(path),'error':'Invalid source identity'});continue
            identities.setdefault(key,{'title':entry.get('title',''),'source_pools':[]})['source_pools'].append(str(path))
    records={};failures=Counter()
    for event in events:
        if event.get('tool')!='arxiv_metadata':continue
        requested={base_id(x) for x in event.get('arguments',{}).get('ids',[])}-{None}
        result=event.get('result') or {};found=set()
        for record in result.get('records',[]):
            key=base_id(record.get('arxiv'))
            if key not in requested or key not in identities:continue
            # Keep the returned primary provenance, not model-written dates.
            records[key]=dict(record,metadata_source_url=result.get('url'),
                              metadata_retrieved_at=result.get('retrieved_at'),
                              metadata_sha256=result.get('sha256'))
            found.add(key)
        failures.update((requested-found)&identities.keys())
    pending=sorted(set(identities)-records.keys(),key=lambda key:(failures[key],key))
    retryable=[key for key in pending if failures[key]<2]
    rows=[]
    for key,record in sorted(records.items()):
        bucket,history=date_queue(record,frame)
        rows.append(dict(record,date_queue=bucket,version_history_required=history,
                         source_pools=identities[key]['source_pools']))
    summary={'source_pool_count':len(sources),'source_identity_count':len(identities),
             'missing_source_scans':sorted(set(EXPECTED_SOURCES)-sources.keys()),
             'incomplete_source_scans':[k for k,v in sources.items() if not v['complete_observed_pagination']],
             'source_errors':source_errors,'sources':sources,'resolved_metadata_count':len(rows),
             'date_queue_counts':dict(Counter(row['date_queue'] for row in rows)),
             'pending_metadata_ids':retryable,
             'unresolved_metadata_ids':[key for key in pending if failures[key]>=2],
             'metadata_complete_for_collected_ids':not pending,
             'warning':'This catalog covers collected arXiv source IDs, not all platforms or all relevant papers. Date routing is not scope classification. Current abstracts may describe a later version; inspect history where flagged.'}
    return rows,summary


def select_page(rows,bucket,start_index,page_size):
    if start_index<0 or not 1<=page_size<=20:raise ValueError('Invalid catalog page bounds')
    if bucket not in {'target_and_uncertain','target_day','history_needed','lookback','outside_window','after_cutoff','invalid_date','all'}:
        raise ValueError('Invalid catalog bucket')
    filtered=[r for r in rows if r['date_queue'] in FOCUS_BUCKETS] if bucket=='target_and_uncertain' else [r for r in rows if bucket=='all' or r['date_queue']==bucket]
    selected=filtered[start_index:start_index+page_size];end=start_index+len(selected)
    # Full primary abstracts stay verbatim. Author lists, duplicate link lists
    # and per-row source-pool paths remain in the durable full catalog.
    page=[{k:r[k] for k in PAGE_FIELDS if k in r} for r in selected]
    signature=hashlib.sha256(json.dumps(filtered,sort_keys=True).encode()).hexdigest()
    return {'operation':'read','bucket':bucket,'catalog_sha256':signature,'total':len(filtered),
            'start_index':start_index,'records':page,'next_index':end if end<len(filtered) else None,
            'metadata_sources':source_provenance(selected),
            'warning':'Full abstracts are returned without keyword filtering. Authors, extra links and source-pool memberships remain in catalog_path. A delivered page is not proof of comprehension or a relevance decision.'}


def audit_coverage(run,frame,events):
    rows,summary=build_catalog(run,frame,events);reviewed=set()
    for event in events:
        if event.get('tool')=='candidate_catalog' and event.get('result',{}).get('operation')=='read':
            reviewed.update(row['arxiv'] for row in event['result'].get('records',[]))
    triage_path=Path(run)/'triage.json'
    triage=json.loads(triage_path.read_text()) if triage_path.exists() else []
    if isinstance(triage,dict):triage=triage.get('candidates',triage.get('papers',[]))
    decisions={}
    for item in triage:
        if not isinstance(item,dict):continue
        key=base_id(item.get('id') or item.get('arxiv') or item.get('observed_source_url'))
        if key and item.get('triage_status') in ('retain','needs_full_read','reject_obvious') and item.get('reason'):
            decisions[key]=item
    focus={row['arxiv']:row for row in rows if row['date_queue'] in FOCUS_BUCKETS}
    untriaged=sorted(focus.keys()-decisions.keys())
    unreviewed=sorted(focus.keys()-reviewed)
    out=dict(summary,focus_candidate_count=len(focus),catalog_page_delivered_count=len(focus.keys()&reviewed),
             explicitly_triaged_count=len(focus.keys()&decisions.keys()),
             focus_ids_without_catalog_page=unreviewed,focus_ids_without_triage=untriaged,
             focus_candidates=[{'arxiv':key,'title':r['title'],'date_queue':r['date_queue'],
                                'catalog_page_delivered':key in reviewed,
                                'triage_status':decisions.get(key,{}).get('triage_status','unreviewed')}
                               for key,r in sorted(focus.items())])
    out['collected_arxiv_focus_accounted_for']=not any((summary['missing_source_scans'],summary['incomplete_source_scans'],
        summary['source_errors'],summary['pending_metadata_ids'],summary['unresolved_metadata_ids'],untriaged,unreviewed))
    out['note']='Coverage gaps are preserved as gaps, never converted into excluded papers. This mechanical audit does not certify screening correctness, full-text understanding, or non-arXiv coverage.'
    return out


def render_coverage(audit):
    rows=['','## Source-derived candidate coverage','',
          'Mechanical audit of collected arXiv titles; relevance and semantic correctness require paper evidence.',
          '',f'- Metadata resolved: {audit["resolved_metadata_count"]} / {audit["source_identity_count"]} collected IDs.',
          f'- Target-day / history-uncertain candidates: {audit["focus_candidate_count"]}.',
          f'- Explicit triage decisions: {audit["explicitly_triaged_count"]}; catalog-page delivery: {audit["catalog_page_delivered_count"]}.',
          f'- Missing source scans: {len(audit["missing_source_scans"])}; incomplete scans: {len(audit["incomplete_source_scans"])}.',
          f'- Unresolved metadata: {len(audit["pending_metadata_ids"])+len(audit["unresolved_metadata_ids"])}; no triage decision: {len(audit["focus_ids_without_triage"])}.',
          '- Full candidate IDs and remaining gaps: `coverage-audit.json`. Unreviewed entries are not exclusions.',
          '- Other platforms remain governed by the source ledger; this audit is not exhaustive discovery.','']
    return '\n'.join(rows)
