from paths import SKILL
import json
from concurrent.futures import ThreadPoolExecutor
from types import SimpleNamespace
import pytest
from agent_state import append_event, read_events, pending_reading, compact_observations, recover_interrupted_batch
from research_tools import ROOT, ResearchTools, save
from test_paper_contract import fixture


def test_partial_trace_write_is_preserved_then_repaired(tmp_path):
    path=tmp_path/'events.jsonl'
    path.write_text('{"ok":1}\n{"interrupted":')
    assert read_events(path)==[{'ok':1}]
    append_event(path,{'ok':2})
    assert read_events(path)==[{'ok':1},{'ok':2}]
    assert 'interrupted' in path.with_suffix('.interrupted-tail').read_text()


def test_complete_corrupt_event_is_not_silently_ignored(tmp_path):
    path=tmp_path/'events.jsonl';path.write_text('not json\n')
    with pytest.raises(json.JSONDecodeError):read_events(path)


def test_parallel_large_tool_events_do_not_interleave(tmp_path):
    path=tmp_path/'events.jsonl'
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(lambda i:append_event(path,{'i':i,'text':'x'*50000}),range(24)))
    assert sorted(x['i'] for x in read_events(path))==list(range(24))


def test_checkpoint_from_separate_tool_instance_clears_pending_pdf():
    import importlib.util,uuid
    run=ROOT/'runs'/('test-nested-'+uuid.uuid4().hex)
    spec=importlib.util.spec_from_file_location('daily_nested',SKILL/'scripts/daily_report.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.prepare(SimpleNamespace(output_dir=run,timezone='America/Chicago',date='2026-10-13',as_of='2026-10-15T07:00:53+00:00'))
    first=ResearchTools(run);h='a'*64;pdf=str(ROOT/'cache/synthetic-test.pdf')
    first.event({'tool':'pdf_read_receipt','path':pdf,'sha256':h,'pages':[1,2],'total_pages':2})
    first.event({'tool':'download_pdf','result':{'sha256':h,'url':'https://arxiv.org/pdf/2610.00001'}})
    assert pending_reading(run)==pdf
    _,paper=fixture();paper.update(screening_status='core',screening_evidence=['Synthetic test evidence'])
    paper['identifiers']={'arxiv':'2610.00001v1'}
    paper['full_text_reading']={'sha256':h,'sections_reviewed':['method']}
    second=ResearchTools(run)
    assert second.checkpoint_paper(paper)['saved']
    assert pending_reading(run) is None
    paper['identifiers']['arxiv']='2610.00001v2'
    assert second.checkpoint_paper(paper)['saved']
    assert len(json.loads((run/'run-input.json').read_text())['papers'])==1
    messages=[{'role':'user','parts':[{'kind':'text','text':json.dumps({'tool':'read_pdf','result':{'sha256':h,'content':[{'text':'long original PDF'}]}})}]}]
    # The full observation has already reached the model; a later checkpoint
    # result is now the newest user message and must itself remain unmodified.
    messages.extend([{'role':'assistant','parts':[{'kind':'text','text':'checkpoint the paper'}]},
                     {'role':'user','parts':[{'kind':'text','text':'checkpoint saved'}]}])
    compact_observations(messages,run)
    result=json.loads(messages[0]['parts'][0]['text'])
    assert result['validated_checkpoint']
    assert 'long original PDF' not in messages[0]['parts'][0]['text']
    assert read_events(first.trace)[0]['pages']==[1,2]


def test_interrupted_batch_recovers_observation_without_replaying_mutation(tmp_path):
    save(tmp_path/'turn-journal.json',{'turn':3,'calls':[
        {'name':'read_file','state':'completed'},
        {'name':'exec_command','state':'started'},
        {'name':'write_file','state':'planned'}]})
    save(tmp_path/'tool-results/3-0.json',{'text':'persisted observation'})
    results=recover_interrupted_batch(tmp_path)
    assert results[0]['result']['text']=='persisted observation'
    assert all('No automatic replay' in r['result']['error'] for r in results[1:])
    assert results[1]['result']['journal_state']=='started'


def test_tool_contract_catches_bad_type_before_tool_runs():
    tool=ResearchTools(ROOT/'runs/test-argument-types')
    result=tool.call('read_pdf',{'path':'unused.pdf','max_pages':'all'})
    assert result['error']=='Invalid tool arguments'
    with pytest.raises(ValueError,match='max_pages'):tool.read_pdf('unused.pdf',max_pages=0)


def test_stage_audit_separates_observation_reading_and_saved_decision():
    import uuid
    run=ROOT/'runs'/('test-stage-'+uuid.uuid4().hex)
    save(run/'run-input.json',{'papers':[]})
    tool=ResearchTools(run)
    tool.event({'tool':'web_search','result':{'text':'arXiv 2610.00001 and 2610.00002'}})
    tool.event({'tool':'open_page','result':{'url':'https://arxiv.org/abs/2610.00001v2'}})
    result=tool.research_status()
    assert result['observed_arxiv_ids']==['2610.00001','2610.00002']
    assert result['opened_without_saved_decision']==['2610.00001']
    assert result['saved_status_by_arxiv']=={}


def test_full_agent_resume_after_mutation_does_not_replay_it(monkeypatch):
    """Synthetic fake model only; exercise actual run/resume persistence and dispatch."""
    import uuid
    import agent
    run=ROOT/'runs'/('test-agent-crash-'+uuid.uuid4().hex);run.mkdir(parents=True)
    (run/'prompt.txt').write_text('Synthetic fault-injection test, not a research experiment.')
    save(run/'run-input.json',{'papers':[]})
    observed=[]
    class FakeModel:
        def __init__(self,*args,**kwargs):pass
        def complete(self,system,messages):
            observed.append(messages)
            reply='DONE' if len(observed)>1 else '```tool\n'+json.dumps({'name':'exec_command','arguments':{'cmd':"printf one >> mutation-count.txt"}})+'\n```'
            return reply,{'cost':.25,'input_tokens':10,'output_tokens':5}
    monkeypatch.setattr(agent,'Model',FakeModel)
    original=ResearchTools.call
    injected=[]
    def fail_after_mutation(self,name,args):
        if name=='validate_report':return {'passed':True}  # Stub completion for the synthetic protocol test only.
        result=original(self,name,args)
        if name=='exec_command' and not injected:
            injected.append(True)
            raise KeyboardInterrupt('Injected interruption after effect, before result journal')
        return result
    monkeypatch.setattr(ResearchTools,'call',fail_after_mutation)
    args=SimpleNamespace(run_dir=str(run),prompt=str(run/'prompt.txt'),model='synthetic',reasoning='medium',max_turns=5,max_seconds=60,cost_limit=2,resume=False)
    with pytest.raises(KeyboardInterrupt):agent.run(args)
    assert (run/'mutation-count.txt').read_text()=='one'
    args.resume=True
    snapshot_path=run/'experiment-inputs.json'
    snapshot=json.loads(snapshot_path.read_text())
    original_snapshot=snapshot_path.read_text()
    first=next(iter(snapshot['files']))
    snapshot['files'][first]='synthetic-mismatch'
    save(snapshot_path,snapshot)
    with pytest.raises(ValueError,match='Knowledge snapshot changed'):agent.run(args)
    snapshot_path.write_text(original_snapshot)
    assert agent.run(args)==0
    assert (run/'mutation-count.txt').read_text()=='one'
    assert 'No automatic replay' in json.dumps(observed[1])
    meta=json.loads((run/'agent_meta.json').read_text())
    assert meta['model_cost_estimate_usd']==.5 and meta['input_tokens']==20
    assert meta['turns']==2
    assert len(read_events(run/'model-turns.jsonl'))==2


@pytest.mark.parametrize('seconds,expected_exit,expected_calls',[(60,0,2),(30,3,1)])
def test_provider_capacity_error_gets_bounded_retry(monkeypatch,seconds,expected_exit,expected_calls):
    import uuid,agent
    run=ROOT/'runs'/('test-capacity-'+uuid.uuid4().hex);run.mkdir(parents=True)
    (run/'prompt.txt').write_text('Synthetic provider capacity recovery test.')
    save(run/'run-input.json',{'papers':[]});calls=[]
    class FakeModel:
        def __init__(self,*args,**kwargs):pass
        def complete(self,system,messages):
            calls.append(1)
            if len(calls)==1:raise RuntimeError('Selected model is at capacity. Please try again.')
            return 'DONE',{'cost':0.01,'input_tokens':1,'output_tokens':1}
    monkeypatch.setattr(agent,'Model',FakeModel)
    clock=[1000.0]
    monkeypatch.setattr(agent.time,'monotonic',lambda:clock[0])
    monkeypatch.setattr(agent.time,'sleep',lambda seconds:clock.__setitem__(0,clock[0]+seconds))
    monkeypatch.setattr(ResearchTools,'call',lambda self,name,args:{'passed':True})
    args=SimpleNamespace(run_dir=str(run),prompt=str(run/'prompt.txt'),model='synthetic',reasoning='medium',resume=False,max_turns=2,max_seconds=seconds,cost_limit=1)
    assert agent.run(args)==expected_exit and len(calls)==expected_calls
    assert any(e.get('tool')=='provider_error' for e in read_events(run/'tool-events.jsonl'))
