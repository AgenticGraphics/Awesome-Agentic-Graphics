import json
from copy import deepcopy
from pathlib import Path
import pytest
from daily_history import build, context, delta, identity, read, verify_context, write


def source(tmp_path, name='bvb-old', status='unresolved', date='2026-10-14'):
    path=tmp_path/'runs'/name
    paper={'canonical_title':'A graphics controller', 'identifiers':{'arxiv':'2610.12345v1'},
           'screening_status':status, 'screening_reason':'Prior observation, not a label instruction',
           'events':[{'type':'first_submission','value':'2026-10-14T06:00:00Z','precision':'timestamp','version':'v1'}]}
    if status in {'core','scope_dependent'}:paper['full_text_reading']={'sha256':'source-pdf'}
    write(path/'run.json',{'target_date':date,'as_of':'2026-10-15T07:00:53+00:00','papers':[paper]})
    for name,value in [('agent_meta.json',{'done':True}),('audit.json',{'passed':True}),('reading-audit.json',{'passed':True})]:
        write(path/name,value)
    (path/'report.md').write_text('Complete historical report')
    return path


def bundle(tmp_path):
    directory=tmp_path/'knowledge/history'
    build([source(tmp_path)],directory)
    return directory


def frame(tmp_path,directory):
    return {'target_date':'2026-10-15','as_of':'2026-10-16T00:20:00+00:00',
            'history_context':context(tmp_path,directory,'2026-10-15','2026-10-16T00:20:00+00:00')}


def test_history_preserves_conflicting_labels_without_promoting_them(tmp_path):
    out=tmp_path/'knowledge/history'
    manifest=build([source(tmp_path,'a','core'),source(tmp_path,'b','scope_dependent'),source(tmp_path,'c')],out)
    assert manifest['paper_count']==1 and manifest['retained_read_count']==1 and manifest['pending_count']==0
    row=read(out/'index.json')[0]
    assert row['prior_statuses']==['core','scope_dependent','unresolved'] and row['scope_disagreement']
    assert len(read(out/row['detail_path'])['observations'])==3
    assert len(list((out/'reports').glob('*/run.json')))==3


def test_history_does_not_overwrite_existing_bundle(tmp_path):
    out=bundle(tmp_path);before=(out/'manifest.json').read_bytes()
    with pytest.raises(ValueError,match='immutable'):build([source(tmp_path)],out)
    assert (out/'manifest.json').read_bytes()==before


@pytest.mark.parametrize('name,value',[('agent_meta.json',{'done':False,'exit_code':1}),('audit.json',{'passed':False}),('reading-audit.json',{'passed':False})])
def test_incomplete_or_failed_sources_cannot_enter_memory(tmp_path,name,value):
    run=source(tmp_path);write(run/name,value)
    with pytest.raises(ValueError):build([run],tmp_path/'knowledge/history')
    assert not (tmp_path/'knowledge/history').exists()


def test_same_day_or_future_source_rejected(tmp_path):
    out=bundle(tmp_path)
    with pytest.raises(ValueError,match='strictly earlier'):context(tmp_path,out,'2026-10-14','2026-10-16T00:20:00+00:00')
    with pytest.raises(ValueError,match='later than'):context(tmp_path,out,'2026-10-15','2026-10-15T06:00:00+00:00')


@pytest.mark.parametrize('change',['edit','extra','manifest'])
def test_modified_memory_is_rejected_after_freeze(tmp_path,change):
    out=bundle(tmp_path);f=frame(tmp_path,out)
    if change=='edit':(out/'INDEX.md').write_text('changed evidence')
    elif change=='extra':write(out/'reports/new/run.json',{'papers':[]})
    else:
        m=read(out/'manifest.json');m['note']='changed';write(out/'manifest.json',m)
    with pytest.raises(ValueError,match='History|Frozen history'):verify_context(tmp_path,f)


def test_memory_must_belong_to_project_knowledge(tmp_path):
    out=tmp_path/'elsewhere';build([source(tmp_path)],out)
    with pytest.raises(ValueError,match='knowledge'):context(tmp_path,out,'2026-10-15','2026-10-16T00:20:00+00:00')


def test_delta_closes_only_actually_read_pending_records_without_importing_history(tmp_path):
    out=bundle(tmp_path);f=frame(tmp_path,out)
    assert delta(tmp_path,f,[])['remaining_prior_pending_ids']==['arxiv:2610.12345']
    paper=read(next((out/'reports').glob('*/run.json')))['papers'][0]
    assert delta(tmp_path,f,[paper])['remaining_prior_pending_ids']==['arxiv:2610.12345']
    paper['full_text_reading']={'sha256':'fresh-pdf'};paper['screening_status']='core'
    result=delta(tmp_path,f,[paper])
    assert result['remaining_prior_pending_ids']==[]
    assert result['current_records'][0]['history_state']=='prior_unread_now_read'
    assert read(out/'index.json')[0]['prior_statuses']==['unresolved']


def test_identity_does_not_merge_different_papers_with_same_alias():
    a={'canonical_title':'IterCAD','identifiers':{'arxiv':'2610.12345v2'}}
    b={'canonical_title':'IterCAD','identifiers':{'arxiv':'2610.54321'}}
    assert identity(a)=='arxiv:2610.12345' and identity(a)!=identity(b)


def test_frozen_history_is_part_of_comparison_execution_frame():
    from compare import compare
    a={'papers':[],'history_context':{'manifest_sha256':'first'}}
    b=deepcopy(a);b['history_context']['manifest_sha256']='second'
    assert not compare(a,b)['same_execution_frame']


def test_triage_and_reading_queue_survive_without_inventing_full_paper_labels(tmp_path):
    run=source(tmp_path)
    write(run/'triage.json',[{'arxiv':'2610.22222','title':'Unfinished controller',
        'triage_status':'needs_full_read','reading_priority':'direct_graphics_action','reason':'Read later'},
        {'arxiv':'2610.33333','title':'Preliminary rejection','triage_status':'reject_obvious','reason':'No graphics action'}])
    write(run/'reading-plan.json',{'ranked_unread':[{'arxiv':'2610.44444','title':'Queue-only lead','priority':'unclear'}]})
    out=tmp_path/'knowledge/new';manifest=build([run],out)
    rows={r['id']:r for r in read(out/'index.json')}
    assert manifest['paper_count']==4 and manifest['candidate_only_count']==3
    assert rows['arxiv:2610.22222']['needs_followup']
    assert rows['arxiv:2610.44444']['needs_followup']
    assert not rows['arxiv:2610.33333']['needs_followup']
    for key in ['arxiv:2610.22222','arxiv:2610.33333','arxiv:2610.44444']:
        detail=read(out/rows[key]['detail_path'])
        assert rows[key]['prior_statuses']==['unresolved']
        assert all(o['full_text_reading'] is None and not o['events'] for o in detail['observations'])
    assert (out/'reports'/run.name/'reading-plan.json').exists()
    f=frame(tmp_path,out);write(out/'reports'/run.name/'triage.json',[])
    with pytest.raises(ValueError,match='changed'):verify_context(tmp_path,f)


def test_actual_paper_record_takes_precedence_over_same_run_candidate(tmp_path):
    run=source(tmp_path,status='core')
    write(run/'triage.json',[{'arxiv':'2610.12345','title':'A graphics controller','triage_status':'needs_full_read'}])
    out=tmp_path/'knowledge/new';m=build([run],out);r=read(out/'index.json')[0]
    assert m['paper_count']==1 and m['candidate_only_count']==0
    assert r['prior_statuses']==['core'] and not r['needs_followup']
    assert len(read(out/r['detail_path'])['observations'])==1


def test_completed_empty_reading_queue_is_not_an_unindexed_format_gap(tmp_path):
    run = source(tmp_path, status='core')
    write(run/'reading-plan.json', {'policy': 'abstract-first-v2', 'pool_count': 0,
          'ranked_unread': [], 'remaining_pdf_capacity': 0})
    out = tmp_path/'knowledge/completed'
    manifest = build([run], out)
    assert manifest['unindexed_candidate_gap_count'] == 0
    assert manifest['retained_read_count'] == 1 and manifest['pending_count'] == 0
    assert read(out/'reports'/run.name/'reading-plan.json')['ranked_unread'] == []


def test_later_full_read_closes_candidate_memory_without_erasing_observation(tmp_path):
    a=source(tmp_path,'first');write(a/'triage.json',[{'arxiv':'2610.54321','title':'Later paper','triage_status':'needs_full_read'}])
    b=source(tmp_path,'second',status='core');data=read(b/'run.json')
    data['papers'][0]['identifiers']['arxiv']='2610.54321';write(b/'run.json',data)
    out=tmp_path/'knowledge/new';build([a,b],out)
    r=next(x for x in read(out/'index.json') if x['id']=='arxiv:2610.54321')
    assert r['prior_statuses']==['core','unresolved'] and not r['needs_followup']
    assert not r['candidate_only'] and len(read(out/r['detail_path'])['observations'])==2


def test_additional_queues_keep_unknown_title_ids_and_explicit_format_gaps(tmp_path):
    run=source(tmp_path)
    write(run/'additional-source-deferred.json',{'ranked_unread':[{'arxiv':'2610.22222','status':'unresolved_metadata'}],
        'external_source_decisions':[{'title':'Project-only evidence','url':'https://example.org/project','status':'date_unverified'},
                                     {'id':'ProjectAlias','url':'https://example.org/unreleased','status':'report_not_released'}]})
    write(run/'additional-deferred.json',{'unexpected_format':True})
    out=tmp_path/'knowledge/new';m=build([run],out)
    rows={r['id']:r for r in read(out/'index.json')}
    assert 'arxiv:2610.22222' in rows and 'not yet verified' in rows['arxiv:2610.22222']['title']
    assert m['candidate_only_count']==3 and m['unindexed_candidate_gap_count']==1
    assert rows['url:https://example.org/unreleased']['needs_followup']
    assert not rows['url:https://example.org/unreleased']['previously_retained_with_full_read']
    assert (out/'reports'/run.name/'additional-deferred.json').exists()
