"""Read-only source-identity/date audit. Does not equate valid citations with true claims."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from agent_state import read_events
from research_tools import save


from source_dates import arxiv_id, submission_history, collect_dates


def cited_page_numbers(locator):
    groups=re.findall(r'\b(?:page|pages|p|pp)\.?\s*(\d+(?:\s*[-–—]\s*\d+)?(?:\s*,\s*\d+(?:\s*[-–—]\s*\d+)?)*)',locator,re.I)
    return [int(value) for group in groups for value in re.findall(r'\d+',group)]


def audit(run):
    run=Path(run);data=json.loads((run/'run.json').read_text());receipts={};events=read_events(run/'tool-events.jsonl');histories,conflicts=collect_dates(events)
    for event in events:
        result=event.get('result',{})
        if event.get('tool')=='pdf_read_receipt':receipts[event['sha256']]=event['total_pages']
    errors=[{'kind':'conflicting_primary_dates',**c} for c in conflicts];unverified=[];verified_dates=0
    for paper in data['papers']:
        key=re.sub(r'v\d+$','',paper.get('identifiers',{}).get('arxiv',''));title=paper['canonical_title']
        for event in paper.get('events',[]):
            source_id=arxiv_id(event.get('primary_url',''))
            if key and source_id and key!=source_id:
                errors.append({'paper':key,'kind':'event_source_identity','source_id':source_id});continue
            if not key or event.get('type') not in ('first_submission','revision','updated','update'):continue
            version=event.get('version') or ('v1' if event['type']=='first_submission' else None)
            expected=histories.get(key,{}).get(version)
            if not expected:
                unverified.append({'paper':key,'kind':'date_not_in_returned_primary_metadata','version':version});continue
            if event.get('precision')!='timestamp':
                unverified.append({'paper':key,'kind':'non_timestamp_date','version':version});continue
            try:actual=datetime.fromisoformat(event['value'].replace('Z','+00:00'))
            except (ValueError,KeyError):
                errors.append({'paper':key,'kind':'invalid_timestamp','event':event});continue
            if actual!=expected:errors.append({'paper':key,'kind':'timestamp_mismatch','version':version,'reported':event['value'],'observed':expected.isoformat()})
            else:verified_dates+=1
        total=receipts.get(paper.get('full_text_reading',{}).get('sha256'))
        evidence_items=dict(paper.get('field_evidence',{}))
        if isinstance(paper.get('agent_graphics_relation'),dict):evidence_items['agent_graphics_relation']=paper['agent_graphics_relation']
        for field,evidence in evidence_items.items():
            source_id=arxiv_id(evidence.get('primary_url',''))
            if key and source_id and key!=source_id:errors.append({'paper':key,'kind':'field_source_identity','field':field,'source_id':source_id})
            pages=cited_page_numbers(evidence.get('locator',''))
            if total and any(p>total or p<1 for p in pages):errors.append({'paper':key or title,'kind':'page_locator_out_of_range','field':field,'locator':evidence['locator'],'total_pages':total})
    return {'passed':not errors,'errors':errors,'unverified':unverified,'verified_timestamp_count':verified_dates,
            'limitations':'Checks only directly comparable arXiv timestamps, source identities and explicit page ranges against this run\'s returned observations. Paraphrases and taxonomy judgments still need substantive review. Unverified is not automatically false.'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('run',type=Path);a=p.parse_args()
    result=audit(a.run);save(a.run/'evidence-audit.json',result);print(json.dumps(result,indent=2))
