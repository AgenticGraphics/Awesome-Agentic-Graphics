"""Read-only attribution of differences to observed stages, never reference injection."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
from agent_state import read_events
from compare import compare, ident
from diagnose import diagnose
from research_tools import save

PATTERN=re.compile(r'(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?(?!\d)')
RETRIEVAL={'arxiv_metadata','arxiv_recent','arxiv_scan','hf_daily','web_search','openreview_search','open_page','find_in_page','click_link'}


def stages(run):
    run=Path(run)
    records=json.loads((run/'run.json').read_text())
    evidence={};downloads={};receipts={};errors=[];counts=Counter()
    def state(key):
        return evidence.setdefault(key,{'observed_in':set(),'collected_in_source_pools':set(),'primary_opened':False,'metadata_resolved':False,'pdf_hashes':set(),'fully_delivered_hashes':set(),'saved_status':None})
    for event in read_events(run/'tool-events.jsonl'):
        tool=event.get('tool');result=event.get('result',{});counts[tool]+=1
        if isinstance(result,dict) and (result.get('error') or result.get('saved') is False):
            errors.append({'tool':tool,'error':result.get('error') or result.get('errors')})
        if tool=='arxiv_scan' and isinstance(result,dict) and result.get('title_pool_path'):
            pool=Path(result['title_pool_path']).resolve()
            if pool.is_relative_to(run.resolve()/'discovery') and pool.exists():
                for entry in json.loads(pool.read_text()).get('entries',[]):
                    key=re.sub(r'v\d+$','',entry.get('arxiv',''))
                    if key:state('arxiv:'+key)['collected_in_source_pools'].add(str(pool))
        if tool in RETRIEVAL and isinstance(result,dict) and not result.get('error'):
            for key in PATTERN.findall(json.dumps(result)):
                state('arxiv:'+key)['observed_in'].add(tool)
            if tool=='arxiv_metadata':
                for record in result.get('records',[]):state('arxiv:'+record['arxiv'])['metadata_resolved']=True
            url=result.get('url','')
            if re.search(r'arxiv\.org/(abs|html)/',url):
                for key in PATTERN.findall(url):state('arxiv:'+key)['primary_opened']=True
        if tool=='download_pdf' and isinstance(result,dict) and result.get('sha256'):
            downloads[result['sha256']]=PATTERN.findall(result.get('url',''))
        if tool=='pdf_read_receipt':
            receipt=receipts.setdefault(event['sha256'],{'pages':set(),'total_pages':event['total_pages']})
            receipt['pages'].update(event['pages'])
    for sha,keys in downloads.items():
        for key in keys:
            item=state('arxiv:'+key);item['pdf_hashes'].add(sha)
            receipt=receipts.get(sha)
            if receipt and receipt['pages']==set(range(1,receipt['total_pages']+1)):
                item['fully_delivered_hashes'].add(sha)
    for paper in records['papers']:
        item=state(ident(paper));item['saved_status']=paper['screening_status'];item['title']=paper['canonical_title']
    for item in evidence.values():
        for key,value in item.items():
            if isinstance(value,set):item[key]=sorted(value)
    return {'records':records,'evidence':evidence,'tool_counts':dict(counts),'tool_errors':errors}


def explain(item):
    if item.get('fully_delivered_hashes') and not item.get('saved_status'):return 'full_PDF_delivered_but_not_saved'
    if item.get('saved_status'):return 'saved_as_'+item['saved_status']
    if item.get('pdf_hashes'):return 'downloaded_without_complete_delivery'
    if item.get('primary_opened'):return 'primary_opened_without_saved_disposition'
    if item.get('metadata_resolved'):return 'primary_metadata_without_saved_disposition'
    if item.get('observed_in'):return 'source_mention_without_primary_resolution'
    if item.get('collected_in_source_pools'):return 'collected_in_source_pool_without_individual_primary_resolution'
    return 'not_observed_in_shared_retrieval_trace'


def diagnose_runs(left,right):
    a,b=stages(left),stages(right)
    comparison=compare(a['records'],b['records'])
    reading=diagnose(a['records'],b['records'])
    rows=[]
    for key in sorted(set(comparison['relevant_only_codex']+comparison['relevant_only_bvb'])):
        x=a['evidence'].get(key,{});y=b['evidence'].get(key,{})
        rows.append({'paper':key,'codex_stage':explain(x),'bvb_stage':explain(y),'codex':x,'bvb':y})
    field_counts=Counter(d['field'] for d in reading['same_pdf_taxonomy_differences'])
    return {'runs':{'codex':str(left),'bvb':str(right)},'comparison':comparison,'reading':reading,
            'relevant_set_difference_stages':rows,'same_pdf_disagreement_by_field':dict(field_counts),
            'tool_counts':{'codex':a['tool_counts'],'bvb':b['tool_counts']},
            'tool_errors':{'codex':a['tool_errors'],'bvb':b['tool_errors']},
            'limitation':'Returned observations and separately marked collected title-pool artifacts establish different levels of source availability. A stored pool is not proof the model inspected every title. A source mention may be a reference or unrelated hit. No relevance is inferred from presence; no semantic claim is judged true solely because Codex made it.'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('codex',type=Path);p.add_argument('bvb',type=Path);p.add_argument('--output',required=True,type=Path);args=p.parse_args()
    result=diagnose_runs(args.codex,args.bvb);save(args.output,result)
    print(json.dumps({'relevant_set_difference_stages':result['relevant_set_difference_stages'],'same_pdf_disagreement_by_field':result['same_pdf_disagreement_by_field'],'tool_errors':result['tool_errors']},indent=2))
