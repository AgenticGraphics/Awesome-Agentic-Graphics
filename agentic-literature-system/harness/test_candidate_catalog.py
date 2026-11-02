import json
from pathlib import Path

import pytest
from candidate_catalog import build_catalog,date_queue,select_page,audit_coverage,render_coverage


FRAME={'window_start':'2026-10-14T00:00:00-05:00','window_end':'2026-10-15T00:00:00-05:00',
       'as_of':'2026-10-15T07:00:53+00:00','target_date':'2026-10-14'}


def record(key='2610.12345',**changes):
    return dict({'arxiv':key,'title':'A title with no matching keywords',
                 'abstract':'The full primary abstract remains available.','version':'v1',
                 'published':'2026-10-14T06:00:00Z','updated':'2026-10-14T06:00:00Z'},**changes)


def sources(run,ids):
    folder=run/'discovery';folder.mkdir(parents=True,exist_ok=True)
    for name in ('cs.GR-new','cs.GR-recent','cs.CV-new','cs.CV-recent'):
        (folder/(name+'-titles.json')).write_text(json.dumps({'complete_observed_pagination':True,
            'entries':[{'arxiv':key,'title':'Unmatched title'} for key in ids]}))


def event(ids,records):
    return {'tool':'arxiv_metadata','arguments':{'ids':ids},
            'result':{'records':records,'url':'https://export.arxiv.org/api/query',
                      'sha256':'synthetic-source-hash','retrieved_at':'2026-10-15T09:00:00Z'}}


@pytest.mark.parametrize('first,latest,queue,history',[
    ('2026-10-14T04:59:59Z','2026-10-14T04:59:59Z','lookback',False),
    ('2026-10-14T05:00:00Z','2026-10-14T05:00:00Z','target_day',False),
    ('2026-10-14T06:00:00Z','2026-10-16T00:00:00Z','target_day',True),
    ('2026-10-01T00:00:00Z','2026-10-15T05:00:00Z','history_needed',True),
    ('2026-10-15T08:00:00Z','2026-10-15T08:00:00Z','after_cutoff',False),
    ('2026-10-15T05:00:00Z','2026-10-15T05:00:00Z','outside_window',False),
    ('2026-10-15T06:00:00Z','2026-10-16T06:00:00Z','outside_window',False),
    ('2026-10-01T00:00:00Z','2026-10-01T00:00:00Z','outside_window',False),
    ('2026-10-14T06:00:00','2026-10-14T06:00:00Z','invalid_date',True),
    ('2026-10-14T06:00:00Z','2026-10-13T06:00:00Z','invalid_date',True),
])
def test_primary_time_routing_preserves_cutoff_and_intermediate_history(first,latest,queue,history):
    assert date_queue(record(published=first,updated=latest),FRAME)==(queue,history)


def test_next_day_first_publication_never_enters_previous_day_focus(tmp_path):
    previous=FRAME|{'window_start':'2026-10-13T00:00:00-05:00','window_end':'2026-10-14T00:00:00-05:00','target_date':'2026-10-13'}
    sources(tmp_path,['2610.12345'])
    rows,summary=build_catalog(tmp_path,previous,[event(['2610.12345'],[record()])])
    assert summary['source_identity_count']==1 and summary['resolved_metadata_count']==1
    assert select_page(rows,'target_and_uncertain',0,20)['records']==[]
    assert len(select_page(rows,'all',0,20)['records'])==1


def test_all_source_titles_survive_without_keyword_filtering(tmp_path):
    sources(tmp_path,['2610.12345','2610.12346'])
    rows,summary=build_catalog(tmp_path,FRAME,[event(['2610.12345'],[record()])])
    assert summary['source_identity_count']==2 and len(rows)==1
    assert rows[0]['title']=='A title with no matching keywords'
    assert summary['pending_metadata_ids']==['2610.12346']
    assert not summary['metadata_complete_for_collected_ids']
    assert 'screening_status' not in rows[0]


def test_missing_ids_do_not_starve_new_work_and_exhaustion_is_explicit(tmp_path):
    sources(tmp_path,['2610.12345','2610.12346'])
    missing=event(['2610.12345'],[])
    _,summary=build_catalog(tmp_path,FRAME,[missing])
    assert summary['pending_metadata_ids']==['2610.12346','2610.12345']
    _,summary=build_catalog(tmp_path,FRAME,[missing,missing])
    assert summary['pending_metadata_ids']==['2610.12346']
    assert summary['unresolved_metadata_ids']==['2610.12345']


def test_catalog_pages_preserve_full_abstracts_and_report_continuation():
    rows=[dict(record(str(i)),date_queue='target_day') for i in range(23)]
    page=select_page(rows,'target_and_uncertain',0,20)
    assert len(page['records'])==20 and page['next_index']==20
    assert page['records'][0]['abstract']==record()['abstract']
    last=select_page(rows,'target_and_uncertain',20,20)
    assert len(last['records'])==3 and last['next_index'] is None


def test_catalog_pages_project_wrapping_metadata_without_losing_primary_abstract():
    row=record();row.update(date_queue='target_day',authors=['Many authors']*100,
        links=[{'href':'https://arxiv.org/pdf/2610.12345v1'}],source_pools=['repeated pool path'],
        metadata_sha256='primary-hash',categories=['cs.GR'])
    row.update(metadata_source_url='https://export.arxiv.org/api/query?id_list='+','.join(str(i) for i in range(100)),
               metadata_retrieved_at='2026-10-15T07:01:00Z')
    page=select_page([row],'target_and_uncertain',0,20)
    shown=page['records'][0]
    assert shown['abstract']==row['abstract'] and shown['metadata_sha256']=='primary-hash'
    assert shown['categories']==['cs.GR'] and shown['published']==row['published']
    assert 'authors' not in shown and 'links' not in shown and 'source_pools' not in shown
    assert 'metadata_source_url' not in shown
    assert page['metadata_sources']==[{'sha256':'primary-hash','url':row['metadata_source_url'],
                                      'retrieved_at':row['metadata_retrieved_at']}]
    assert len(row['authors'])==100 and row['links']  # Stored record remains intact.


def test_metadata_delivery_without_explicit_triage_stays_a_coverage_gap(tmp_path):
    sources(tmp_path,['2610.12345']);events=[event(['2610.12345'],[record()])]
    audit=audit_coverage(tmp_path,FRAME,events)
    assert audit['focus_ids_without_triage']==['2610.12345']
    assert audit['focus_candidates'][0]['triage_status']=='unreviewed'
    assert not audit['collected_arxiv_focus_accounted_for']
    text=render_coverage(audit)
    assert 'Unreviewed entries are not exclusions' in text


def test_audited_complete_focus_still_does_not_claim_global_discovery(tmp_path):
    sources(tmp_path,['2610.12345']);events=[event(['2610.12345'],[record()])]
    events.append({'tool':'candidate_catalog','result':{'operation':'read','records':[record()]}})
    (tmp_path/'triage.json').write_text(json.dumps([{'id':'2610.12345','triage_status':'needs_full_read','reason':'Primary abstract needs full paper verification.'}]))
    audit=audit_coverage(tmp_path,FRAME,events)
    assert audit['collected_arxiv_focus_accounted_for']
    assert 'not all platforms' in audit['warning']
    assert 'not exhaustive discovery' in render_coverage(audit)


def test_actual_tool_dispatch_resumes_from_own_metadata_events(tmp_path,monkeypatch):
    import research_tools as module
    monkeypatch.setattr(module,'ROOT',tmp_path)
    run=tmp_path/'runs/synthetic';sources(run,['2610.12345','2610.12346'])
    (run/'frozen-frame.json').write_text(json.dumps(FRAME))
    tools=module.ResearchTools(run);calls=[]
    def resolve(ids):
        calls.append(ids)
        return event(ids,[record(key) for key in ids])['result']
    monkeypatch.setattr(tools,'arxiv_metadata',resolve)
    first=tools.call('candidate_catalog',{'operation':'resolve'})
    assert first['resolved_metadata_count']==2 and first['pending_metadata_count']==0
    second=tools.call('candidate_catalog',{'operation':'resolve'})
    assert second['metadata_batches_attempted']==0 and len(calls)==1
    page=tools.call('candidate_catalog',{'operation':'read','page_size':1})
    assert len(page['records'])==1 and page['next_index']==1
