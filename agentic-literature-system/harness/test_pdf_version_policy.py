import uuid
from research_tools import ROOT,ResearchTools,save


def fixture():
    run=ROOT/'runs'/('test-version-policy-'+uuid.uuid4().hex)
    save(run/'run-input.json',{'as_of':'2026-10-15T07:00:53+00:00','evidence_policy':'version-pinned-pdf-v1'})
    tool=ResearchTools(run)
    paper={'screening_status':'core','identifiers':{'arxiv':'2610.00001'},
           'full_text_reading':{'sha256':'synthetic','sections_reviewed':['method']},
           'events':[{'type':'first_submission','version':'v1','precision':'timestamp','value':'2026-10-13T12:00:00Z'}]}
    events=[{'tool':'pdf_read_receipt','sha256':'synthetic','pages':[1],'total_pages':1},
            {'tool':'download_pdf','result':{'sha256':'synthetic','url':'https://arxiv.org/pdf/2610.00001v1'}}]
    events.append({'tool':'arxiv_metadata','arguments':{'ids':['2610.00001v1']},'result':{'records':[
        {'arxiv':'2610.00001','version':'v1','published':'2026-10-13T12:00:00Z','updated':'2026-10-13T12:00:00Z'}]}})
    return tool,paper,events


def test_versioned_pdf_with_pre_cutoff_timestamp_is_accepted():
    tool,paper,events=fixture();assert not tool._reading_errors(paper,events)


def test_versionless_and_future_versions_are_rejected():
    tool,paper,events=fixture();events[1]['result']['url']='https://arxiv.org/pdf/2610.00001'
    assert any('explicitly versioned' in x for x in tool._reading_errors(paper,events))
    events[1]['result']['url']='https://arxiv.org/pdf/2610.00001v2'
    paper['events'].append({'type':'revision','version':'v2','precision':'timestamp','value':'2026-10-15T09:00:00Z'})
    assert any('frozen cutoff' in x for x in tool._reading_errors(paper,events))


def test_known_newer_eligible_version_cannot_be_ignored():
    tool,paper,events=fixture()
    events.append({'tool':'arxiv_metadata','arguments':{'ids':['2610.00001']},'result':{'records':[
        {'arxiv':'2610.00001','version':'v2','published':'2026-10-13T12:00:00Z','updated':'2026-10-14T12:00:00Z'}]}})
    assert any('newer eligible' in x for x in tool._reading_errors(paper,events))


def test_invented_version_timestamp_is_rejected():
    tool,paper,events=fixture();paper['events'][0]['value']='2026-10-13T12:01:00Z'
    assert any('not supported' in x for x in tool._reading_errors(paper,events))


def test_report_rewrite_cannot_silently_drop_or_change_frozen_frame():
    import json
    tool,paper,events=fixture()
    frame={'as_of':'2026-10-15T07:00:53+00:00','evidence_policy':'version-pinned-pdf-v1'}
    save(tool.run_dir/'frozen-frame.json',frame)
    save(tool.run_dir/'run-input.json',{'as_of':'2026-10-16T00:00:00Z','papers':[]})
    resumed=ResearchTools(tool.run_dir)
    errors=resumed._frame_errors(json.loads((tool.run_dir/'run-input.json').read_text()))
    assert any('as_of' in e for e in errors) and any('evidence_policy' in e for e in errors)
    assert resumed.execution_frame==frame


def test_retained_papers_require_analysis_target_and_explained_sentinels():
    from research_tools import CODEBOOK
    tool,paper,events=fixture()
    errors=tool._annotation_errors(paper)
    assert any('analysis_target' in x for x in errors)
    assert sum('reviewed-source' in x for x in errors)==18
    paper['analysis_target']='Synthetic task-time agent.'
    paper['field_evidence']={k:{'primary_url':'https://arxiv.org/pdf/2610.00001v1','locator':'Full method and appendix','evidence':'Synthetic reviewed-scope explanation.'} for k in CODEBOOK['fields']}
    assert not tool._annotation_errors(paper)
    paper['screening_status']='unresolved';paper.pop('analysis_target');paper['field_evidence']={}
    assert not tool._annotation_errors(paper)


def test_non_arxiv_publication_and_artifact_dates_are_not_pdf_versions():
    tool,paper,events=fixture()
    paper['events'] += [{'type':kind,'precision':'timestamp','value':'2026-10-14T13:00:00Z'} for kind in ('formal_publication','artifact_release')]
    assert not tool._reading_errors(paper,events)
