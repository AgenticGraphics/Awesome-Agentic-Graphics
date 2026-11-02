"""Export validated checkpoints after failure; never mark the run successful."""
import argparse,json
from pathlib import Path
from research_tools import save,now


def export(run):
    run=Path(run);meta=json.loads((run/'agent_meta.json').read_text())
    if meta.get('done') is True or meta.get('exit_code')==0:
        raise ValueError('Run completed successfully; use its original report, not a failure-recovery export')
    records=[]
    for path in sorted((run/'checkpoints').glob('*.json')):
        record=json.loads(path.read_text())
        records.append({'checkpoint_path':str(path),'validated_at':record.get('validated_at'),'paper':record['paper']})
    result={'status':'partial_artifact_not_successful_completion','exported_at':now(),'source_run':str(run),'agent_outcome':meta,'validated_checkpoints':records,
            'limitation':'These are this run\'s own saved paper decisions. Source coverage, remaining candidates and final workflow completion are not certified. This export is excluded from successful-run/parity counts.'}
    save(run/'recovery-partial.json',result)
    lines=['# Partial recovery artifact','', 'The research run did not complete successfully. This file preserves its own validated paper checkpoints; it is not a successful-run or equivalence result.','',f'Saved checkpoints: {len(records)}. Outcome: {meta.get("stop_reason",meta.get("exit_code"))}.','', '| Paper | Saved scope | Checkpoint |','|---|---|---|']
    for record in records:
        paper=record['paper'];url=paper.get('canonical_urls',[''])[0]
        lines.append('| ['+paper['canonical_title'].replace('|','/')+']('+url+') | '+paper['screening_status']+' | '+Path(record['checkpoint_path']).name+' |')
    lines+=['','Full records: recovery-partial.json. Unfinished discovery/triage remains in the original run directory. Original failure and recovery metadata are unchanged.']
    (run/'recovery-partial.md').write_text('\n'.join(lines)+'\n')
    return {'saved_checkpoints':len(records),'partial_artifact':str(run/'recovery-partial.md'),'run_success_status_unchanged':True}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('run',type=Path);args=p.parse_args();print(json.dumps(export(args.run)))
