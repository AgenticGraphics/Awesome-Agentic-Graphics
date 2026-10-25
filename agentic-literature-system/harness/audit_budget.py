"""Read-only observed budget audit; tool invocations are not provider billing."""
import argparse,json
from pathlib import Path
from agent_state import read_events


def audit(run):
    run=Path(run)
    frame=run/'frozen-frame.json'
    frame=json.loads(frame.read_text()) if frame.exists() else json.loads((run/'run-input.json').read_text())
    budget=frame.get('budget',{})
    events=read_events(run/'tool-events.jsonl')
    hashes={e['sha256'] for e in events if e.get('tool')=='pdf_read_receipt'}
    searches=sum(e.get('tool') in ('web_search','openreview_search') for e in events)
    meta=run/'agent_meta.json';meta=json.loads(meta.read_text()) if meta.exists() else {}
    observed={'distinct_pdf_files_with_delivered_pages':len(hashes),'search_tool_invocations':searches,
              'active_duration_seconds':meta.get('duration_seconds'),
              'page_open_tool_invocations':sum(e.get('tool') in ('open_page','click_link') for e in events)}
    violations=[]
    if budget.get('read_candidates') is not None and len(hashes)>budget['read_candidates']:
        violations.append('Delivered pages from more distinct PDF files than the declared reading cap')
    if budget.get('search_batches') is not None and searches>budget['search_batches']:
        violations.append('More search tool invocations than the declared search-batch cap')
    if observed['active_duration_seconds'] is not None and budget.get('minutes') is not None and observed['active_duration_seconds']>budget['minutes']*60+5:
        violations.append('Recorded active duration exceeds declared time budget by more than five seconds')
    return {'run':str(run),'declared_budget':budget,'observed':observed,'measured_caps_passed':not violations,
            'violations':violations,'limitations':[
                'Incomplete runs cannot establish successful budgeted completion.',
                'PDF count includes partial delivery; receipts do not prove comprehension.',
                'Page-open count is informational: candidate primary pages are not automatically distinguished from other pages.',
                'Metadata/listing scans have separate per-call bounds; native shell retrieval is outside this shared-tool audit.',
                'Search invocations are not individual search queries or billing units; model usage is separately logged.']}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('run');p.add_argument('--output');a=p.parse_args();result=audit(a.run)
    if a.output:Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
