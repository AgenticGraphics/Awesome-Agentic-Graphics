"""Opt-in transport ablation; runs the original BVB research loop unchanged."""
import argparse,hashlib,json,shutil,sys,os
from pathlib import Path


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--project-root',default=str(Path(__file__).resolve().parent))
    p.add_argument('--run-dir',required=True);p.add_argument('--prompt',required=True)
    p.add_argument('--model',default=os.environ.get('AGENT_MODEL'));p.add_argument('--reasoning',default='medium')
    p.add_argument('--max-turns',type=int,default=80);p.add_argument('--max-seconds',type=float,default=1200)
    p.add_argument('--cost-limit',type=float,default=15);p.add_argument('--resume',action='store_true')
    args=p.parse_args()
    from runtime_config import model_name, api_key, api_base
    try:
        args.model=model_name(args.model);api_key();endpoint=api_base()
    except ValueError as error:p.error(str(error))
    if args.max_turns<=0 or args.max_seconds<=0 or args.cost_limit<=0:p.error('Budgets must be positive')
    root=Path(args.project_root).resolve()
    if root!=Path(__file__).resolve().parent:p.error('--project-root must name this harness directory')
    os.environ['AGENT_MODEL']=args.model
    os.environ['OPENAI_BASE_URL']=endpoint
    run=(root/args.run_dir).resolve()
    if not run.is_relative_to(root/'runs'):raise ValueError('Run must be inside this project runs directory')
    args.run_dir=str(run);args.prompt=str((root/args.prompt).resolve());args.transport='responses-items-v4'
    sys.path.insert(0,str(root/'third_party'));sys.path.insert(0,str(root))
    import agent
    from responses_model import ResponsesModel, _manual_cost
    _manual_cost(args.model,1,1)  # Fail before the first paid call if pricing is unknown.
    from research_tools import save
    adapter=Path(__file__).with_name('responses_model.py')
    fingerprint=hashlib.sha256(adapter.read_bytes()).hexdigest()
    if args.resume:
        prior=json.loads((run/'config.json').read_text())
        if prior.get('transport')!='responses-items-v4':raise ValueError('Cannot switch transport during a resumed run')
        if json.loads((run/'transport-config.json').read_text())['adapter_sha256']!=fingerprint:raise ValueError('Responses adapter changed since run start')
    else:
        if any((run/name).exists() for name in ('agent_meta.json','config.json','progress.json','conversation.json')):raise ValueError('Existing run retained; use a fresh name or explicit resume')
        snapshot=run/'harness-snapshot';snapshot.mkdir(parents=True,exist_ok=True)
        for source in (Path(__file__),adapter):shutil.copy2(source,snapshot/source.name)
        save(run/'transport-config.json',{'transport':'responses-items-v4','adapter_sha256':fingerprint,'protocol':'original BVB fenced tools','note':'Provider transport and returned item replay change; the BVB fenced-tool loop remains. This does not clone Codex instructions or compaction.'})
    os.environ['BVB_RESPONSES_STATE']=str(run/'responses-state.json')
    agent.Model=ResponsesModel
    return agent.run(args)


if __name__=='__main__':raise SystemExit(main())
