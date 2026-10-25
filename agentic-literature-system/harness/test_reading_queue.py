import json
from pathlib import Path
import pytest
from reading_queue import attention_pool, attention_page, already_read_version, build_plan, history_rows


def row(key, **values):
    return dict(arxiv=key, title='Unmatched spectral observation', abstract='Complete primary abstract.',
                version='v1', published='2026-10-13T12:00:00Z', updated='2026-10-13T12:00:00Z',
                categories=['cs.CV'], date_queue='lookback', **values)


def decision(key, priority):
    return {'arxiv':key, 'triage_status':'needs_full_read', 'reason':'Primary abstract needs verification.',
            'reading_priority':priority, 'priority_reason':'Observed mechanism evidence, not a final label.'}


def test_unmatched_graphics_and_pending_abstracts_survive_without_title_hint():
    a=row('2610.00001');a['categories']=['cs.GR']
    b=row('2610.00002');c=row('2610.00003')
    selected,_=attention_pool([a,b,c],{b['arxiv']:{'needs_followup':True}})
    assert {x['arxiv'] for x in selected}=={a['arxiv'],b['arxiv']}
    assert selected[0]['abstract']==a['abstract']
    assert 'reading_priority' not in selected[0] and 'screening_status' not in selected[0]
    assert len([a,b,c])==3  # The full source catalog is not filtered in place.


def test_unchanged_version_deferred_but_new_version_and_conflict_revisited():
    a=row('2610.00001');a['categories']=['cs.GR']
    old={'observations':[{'full_text_reading':{'sha256':'old'},'events':[{'version':'v1','value':a['updated']}]}]}
    assert already_read_version(a,old)
    assert attention_pool([a],{a['arxiv']:old})[1]==[a['arxiv']]
    newer=dict(a,version='v2',updated='2026-10-14T12:00:00Z')
    assert not already_read_version(newer,old)
    assert attention_pool([newer],{a['arxiv']:old})[0]
    assert not already_read_version(a,dict(old,scope_disagreement=True))


def test_after_cutoff_and_outside_window_pending_do_not_enter_catchup_pool():
    rows=[row('2610.00001'),row('2610.00002')]
    rows[0]['date_queue']='after_cutoff';rows[1]['date_queue']='outside_window'
    assert attention_pool(rows,{r['arxiv']:{'needs_followup':True} for r in rows})[0]==[]


def test_attention_pages_expose_every_full_abstract_and_continuation():
    rows=[row(f'2610.{i:05d}') for i in range(23)]
    history={r['arxiv']:{'needs_followup':True} for r in rows}
    first=attention_page(rows,history,0,20);last=attention_page(rows,history,20,20)
    assert first['next_index']==20 and len(last['records'])==3 and last['next_index'] is None
    assert all(r['abstract']=='Complete primary abstract.' for r in first['records']+last['records'])


def test_model_evidence_priority_precedes_id_and_weak_backlog_never_promoted():
    rows=[row('2610.00001'),row('2610.00002'),row('2610.00003')]
    history={r['arxiv']:{'needs_followup':True} for r in rows}
    plan=build_plan(rows,history,[decision(rows[0]['arxiv'],'borderline'),decision(rows[1]['arxiv'],'direct_graphics_action')],[],2)
    assert [r['arxiv'] for r in plan['selected_next']]==['2610.00002','2610.00001']
    assert plan['priority_or_triage_gaps']==['2610.00003']
    assert len(plan['full_abstracts_not_delivered'])==3
    assert all('screening_status' not in r for r in plan['ranked_unread'])


def test_target_day_lane_precedes_backlog_and_non_arxiv_pdf_consumes_capacity():
    a=row('2610.00001');a['date_queue']='target_day'
    b=row('2610.00002')
    hist={b['arxiv']:{'needs_followup':True}}
    events=[{'tool':'download_pdf','result':{'url':'https://example.org/paper.pdf','sha256':'opaque'}},
            {'tool':'candidate_catalog','result':{'operation':'read','records':[a,b]}}]
    plan=build_plan([a,b],hist,[decision(a['arxiv'],'borderline'),decision(b['arxiv'],'direct_graphics_action')],events,2)
    assert [r['arxiv'] for r in plan['selected_next']]==[a['arxiv']]
    assert plan['remaining_pdf_capacity']==1 and not plan['full_abstracts_not_delivered']


def test_started_paper_is_not_scheduled_again_and_rejection_remains_saved():
    rows=[row('2610.00001'),row('2610.00002')]
    for r in rows:r['categories']=['cs.GR']
    events=[{'tool':'download_pdf','result':{'url':'https://arxiv.org/pdf/2610.00001v1','sha256':'first'}}]
    tri=[decision(rows[0]['arxiv'],'direct_graphics_action'),{'arxiv':rows[1]['arxiv'],'triage_status':'reject_obvious','reason':'No agent-related contribution in primary abstract.'}]
    plan=build_plan(rows,{},tri,events,3)
    assert not plan['selected_next'] and not plan['priority_or_triage_gaps']
    assert len(tri)==2 and plan['pool_count']==2


@pytest.mark.parametrize('policy',['abstract-first-v1','abstract-first-v2'])
def test_selected_history_is_only_searchable_history_and_snapshotted_input(tmp_path,monkeypatch,policy):
    import research_tools as module
    original=module.ROOT
    monkeypatch.setattr(module,'ROOT',tmp_path)
    run=tmp_path/'runs/new';run.mkdir(parents=True)
    frame={'reading_policy':policy,'history_context':{'directory':'knowledge/daily-history/old'}}
    (run/'frozen-frame.json').write_text(json.dumps(frame))
    for name in ['old','future']:
        p=tmp_path/'knowledge/daily-history'/name/'record.json';p.parent.mkdir(parents=True);p.write_text('{"paper":"needle"}')
    tools=module.ResearchTools(run)
    with pytest.raises(ValueError,match='frozen selected'):tools.read_file('knowledge/daily-history/future/record.json')
    hits=tools.knowledge_search('needle')['local']
    assert len(hits)==1 and '/old/' in hits[0]['path']
    assert all('/future/' not in p for p in tools.list_files())
    for name in ['research_tools.py','paper_contract.py','agent_state.py','process_control.py','title_triage.py','listing_scan.py','pdf_search.py','arxiv_metadata.py','source_dates.py','candidate_catalog.py','daily_history.py','reading_queue.py']:
        (tmp_path/name).write_bytes((original/name).read_bytes())
    module.snapshot_inputs(run)
    files=json.loads((run/'experiment-inputs.json').read_text())['files']
    assert any('/old/' in p for p in files) and not any('/future/' in p for p in files)


def test_history_details_cannot_escape_bundle(tmp_path):
    (tmp_path/'index.json').write_text(json.dumps([{'id':'arxiv:2610.00001','detail_path':'../outside.json'}]))
    with pytest.raises(ValueError,match='outside frozen'):history_rows(tmp_path)


def test_shared_tool_dispatch_builds_attention_pages_and_own_plan(tmp_path,monkeypatch):
    import research_tools as module
    monkeypatch.setattr(module,'ROOT',tmp_path)
    run=tmp_path/'runs/new';run.mkdir(parents=True)
    (run/'frozen-frame.json').write_text(json.dumps({'budget':{'read_candidates':2}}))
    a=row('2610.00001');a['categories']=['cs.GR']
    monkeypatch.setattr(module,'build_catalog',lambda *args:([a],{}))
    tools=module.ResearchTools(run)
    page=tools.call('candidate_catalog',{'operation':'read','bucket':'catchup_review'})
    assert page['records'][0]['abstract']==a['abstract']
    (run/'triage.json').write_text(json.dumps([decision(a['arxiv'],'direct_graphics_action')]))
    plan=tools.call('candidate_catalog',{'operation':'plan'})
    assert plan['selected_next'][0]['arxiv']==a['arxiv'] and not plan['full_abstracts_not_delivered']
    assert (run/'reading-plan.json').exists()


def test_evidence_rank_precedes_id_but_not_date_or_relation_priority():
    rows=[row('2610.00001'),row('2610.00002'),row('2610.00003')]
    for r in rows:r['categories']=['cs.GR']
    tri=[dict(decision(r['arxiv'],'direct_graphics_action'),reading_rank=rank)
         for r,rank in zip(rows,[3,2,1])]
    plan=build_plan(rows,{},tri,[],3)
    assert [r['arxiv'] for r in plan['selected_next']]==['2610.00003','2610.00002','2610.00001']
    tri[2]['reading_priority']='borderline'
    plan=build_plan(rows,{},tri,[],3)
    assert plan['selected_next'][-1]['arxiv']=='2610.00003'
    rows[2]['date_queue']='target_day'
    assert build_plan(rows,{},tri,[],3)['selected_next'][0]['arxiv']=='2610.00003'


def test_rank_defects_remain_explicit_and_do_not_delete_candidates():
    rows=[row(f'2610.{i:05d}') for i in range(4)]
    history={r['arxiv']:{'needs_followup':True} for r in rows}
    tri=[dict(decision(r['arxiv'],'direct_graphics_action'),reading_rank=rank)
         for r,rank in zip(rows,[1,1,True,0])]
    plan=build_plan(rows,history,tri,[],4)
    assert plan['duplicate_reading_ranks']=={'1':['2610.00000','2610.00001']}
    assert plan['reading_rank_gaps']==['2610.00002','2610.00003']
    assert len(plan['ranked_unread'])==4


def test_additional_official_lead_joins_queue_without_keyword_or_listing_membership():
    frame={'window_start':'2026-10-15T05:00:00Z','window_end':'2026-10-16T05:00:00Z',
           'as_of':'2026-10-16T00:16:00Z'}
    extra=row('2610.00009')
    tri=[dict(decision(extra['arxiv'],'direct_graphics_action'),reading_rank=1)]
    ev=[{'tool':'arxiv_metadata','arguments':{'ids':[extra['arxiv']]},'result':{'records':[extra]}}]
    plan=build_plan([],{},tri,ev,2,frame)
    assert plan['selected_next'][0]['arxiv']==extra['arxiv']
    assert plan['additional_source_ids']==[extra['arxiv']]
    assert not plan['full_abstracts_not_delivered']
    assert 'additional_source_with_primary_metadata' in plan['selected_next'][0]['attention_reasons']
    assert not build_plan([],{},[],ev,2,frame)['selected_next']
    assert not build_plan([],{},tri,[],2,frame)['selected_next']


def test_additional_lead_cannot_bypass_cutoff_or_reported_request_identity():
    frame={'window_start':'2026-10-15T05:00:00Z','window_end':'2026-10-16T05:00:00Z',
           'as_of':'2026-10-16T00:16:00Z'}
    extra=row('2610.00009');extra.update(published='2026-10-16T05:00:00Z',updated='2026-10-16T05:00:00Z')
    tri=[dict(decision(extra['arxiv'],'direct_graphics_action'),reading_rank=1)]
    ev=[{'tool':'arxiv_metadata','arguments':{'ids':[extra['arxiv']]},'result':{'records':[extra]}}]
    assert not build_plan([],{},tri,ev,2,frame)['selected_next']
    ev[0]['arguments']['ids']=['2610.00010']
    assert not build_plan([],{},tri,ev,2,frame)['additional_source_ids']
