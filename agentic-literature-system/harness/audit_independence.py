"""Trace-based independence check; not an OS-level isolation certificate."""
import json,re
from pathlib import Path
from agent_state import read_events
from research_tools import ROOT,now,save


def native_commands(value):
    if isinstance(value,dict):
        if value.get('type')=='command_execution' and isinstance(value.get('command'),str):
            yield value['command']
        for child in value.values():yield from native_commands(child)
    elif isinstance(value,list):
        for child in value:yield from native_commands(child)


def audit():
    summary=json.loads((ROOT/'runs/evaluation/summary.json').read_text())
    runs={Path(path) for row in summary['rows'] for path in row['runs'].values()}
    runs.update(path for path in (ROOT/'runs').iterdir() if path.is_dir()
                and re.match(r'^(codex|bvb)-\d{8}-',path.name) and (path/'tool-events.jsonl').exists())
    runs=sorted(runs)
    findings=[]
    for run in runs:
        inspected=[]
        for event in read_events(run/'tool-events.jsonl'):
            if 'arguments' in event:inspected.append({'source':'shared_tool','tool':event.get('tool'),'arguments':event['arguments']})
        native_traces=[run/'codex-events.jsonl',*sorted((run/'attempts').glob('codex-resume-*/codex-events.jsonl'))]
        for trace in native_traces:
            for event in read_events(trace):
                inspected.extend({'source':'native_command','trace':str(trace.relative_to(run)),
                                  'command':command} for command in native_commands(event))
        forbidden=[other.name for other in runs if other!=run]
        matches=[]
        for index,entry in enumerate(inspected):
            text=json.dumps(entry)
            hits=[name for name in forbidden if name in text]
            if hits:matches.append({'event_index':index,'other_run_names':hits,'source':entry['source']})
        findings.append({'run':run.name,'inspected_argument_or_command_records':len(inspected),
                         'native_traces_inspected':[str(p.relative_to(run)) for p in native_traces if p.exists()],
                         'explicit_other_run_references':matches})
    result={'audited_at':now(),'run_count':len(runs),'no_explicit_other_run_references_observed':all(not r['explicit_other_run_references'] for r in findings),'runs':findings,
            'limitations':'This checks explicit names in recorded tool arguments and native commands. It cannot prove absence of dynamically constructed paths, unrecorded native network access, or cross-process access. The runner is not an OS sandbox. Shared public observations and frozen knowledge are intentional; another run\'s paper decisions are prohibited.'}
    save(ROOT/'runs/evaluation/independence-audit.json',result)
    return result


if __name__=='__main__':
    result=audit();print(json.dumps({k:v for k,v in result.items() if k!='runs'}))
