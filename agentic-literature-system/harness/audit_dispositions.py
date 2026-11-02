"""Read-only reporting of primary-resolution and annotation-accountability gaps."""
import argparse,json,re
from pathlib import Path
from agent_state import read_events
from research_tools import save
from source_dates import arxiv_id


def audit(run):
    run=Path(run);data=json.loads((run/'run.json').read_text());primary=set()
    for event in read_events(run/'tool-events.jsonl'):
        result=event.get('result',{})
        if not isinstance(result,dict) or result.get('error'):continue
        if event.get('tool')=='arxiv_metadata':
            primary.update(r['arxiv'] for r in result.get('records',[]) if r.get('abstract','').strip())
        if event.get('tool') in ('open_page','click_link','find_in_page'):
            key=arxiv_id(result.get('url',''))
            if key and (result.get('text') or result.get('matches')):primary.add(key)
    excluded_without_primary=[];missing_targets=[];missing_explanations=[];retained=0
    for paper in data['papers']:
        key=re.sub(r'v\d+$','',paper.get('identifiers',{}).get('arxiv',''));status=paper['screening_status']
        if status=='excluded' and key and key not in primary:excluded_without_primary.append(key)
        if status not in ('core','enabling_or_adjacent','scope_dependent'):continue
        retained+=1
        if not paper.get('analysis_target'):missing_targets.append(key or paper['canonical_title'])
        for field in paper.get('taxonomy_cells',{}):
            explanation=paper.get('field_evidence',{}).get(field,{})
            if not all(explanation.get(k,'').strip() for k in ('primary_url','locator','evidence')):
                missing_explanations.append({'paper':key or paper['canonical_title'],'field':field})
    return {'retained_papers':retained,'excluded_without_returned_arxiv_primary_resolution':excluded_without_primary,
            'retained_without_analysis_target':missing_targets,'fields_without_source_scope_explanation':missing_explanations,
            'limitations':'Reports gaps in recorded shared-tool observations, not proof that an exclusion is false. Other primary sources and native access need separate review. Explained fields are not automatically correct; original outputs and parity metrics are unchanged.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('run',type=Path);args=parser.parse_args()
    result=audit(args.run);save(args.run/'disposition-audit.json',result)
    print(json.dumps({k:(len(v) if isinstance(v,list) else v) for k,v in result.items()},ensure_ascii=False))
