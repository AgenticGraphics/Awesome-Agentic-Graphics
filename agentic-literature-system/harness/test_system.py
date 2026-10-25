from paths import SKILL
import json
import pytest
from research_tools import ResearchTools, ROOT
from compare import compare
def test_workspace_escape():
    with pytest.raises(ValueError):ResearchTools(ROOT/'runs/test').path('../../secret')
def frame():return {'papers':[],'target_date':'2026-10-15','timezone':'America/Chicago','as_of':'2026-10-15T07:00:00+00:00','taxonomy_version':'test','source_snapshot':{}}
def test_empty_is_not_parity():
    out=compare(frame(),frame());assert out['same_day_new_equal'];assert not out['full_semantic_parity'];assert out['taxonomy_cell_agreement'] is None
def test_model_secret_not_in_shell():
    import os
    os.environ['TEST_API_KEY']='synthetic-test-value'
    r=ResearchTools(ROOT/'runs/test').python_exec("import os; print('TEST_API_KEY' in os.environ)")
    assert r['stdout'].strip()=='False'
def test_taxonomy_disagreement_is_not_hidden():
    import copy
    a=frame();a['papers']=[{'canonical_title':'Synthetic fixture','identifiers':{'arxiv':'2610.00001'},'screening_status':'core','events':[], 'taxonomy_cells':{'planning':['PO-1']}}]
    b=copy.deepcopy(a);b['papers'][0]['taxonomy_cells']['planning']=['PO-2']
    r=compare(a,b);assert not r['full_semantic_parity'];assert r['taxonomy_cell_agreement']==0
    assert r['differences'][0]['field']=='taxonomy.planning'
def test_missing_pdf_receipt_fails():
    from types import SimpleNamespace
    import importlib.util
    spec=importlib.util.spec_from_file_location('daily_test',SKILL/'scripts/daily_report.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    out=ROOT/'runs/test-receipt';out.mkdir(parents=True,exist_ok=True)
    p=out/'run-input.json'
    if p.exists():p.unlink()
    m.prepare(SimpleNamespace(output_dir=out,timezone='America/Chicago',date='2026-10-15',as_of='2026-10-15T07:00:53+00:00'))
    d=json.loads(p.read_text());cb=json.loads((SKILL/'references/taxonomy-codebook.json').read_text())
    d['papers']=[{'canonical_title':'Synthetic receipt fixture','canonical_urls':['https://example.org/paper'], 'identifiers':{},'authors':[], 'abstract':'test','events':[],'source_records':[], 'screening_status':'core','screening_reason':'fixture','screening_evidence':['fixture'], 'application_families':['2D Graphics'],'operations':['Generation'], 'taxonomy_cells':{k:['Not Reported'] for k in cb['fields']}, 'field_evidence':{},'contribution':'fixture','limitations':'fixture','taxonomy_delta':[],'confidence':'Low'}]
    p.write_text(json.dumps(d));r=ResearchTools(out).validate_report(str(p))
    assert not r['passed'];assert any('PDF reading receipt' in x for x in r['errors'])
def test_patch_stays_in_run():
    t=ResearchTools(ROOT/'runs/test-patch');p=t.run_dir/'sample.txt';p.write_text('before\n')
    patch='--- a/runs/test-patch/sample.txt\n+++ b/runs/test-patch/sample.txt\n@@ -1 +1 @@\n-before\n+after\n'
    assert t.apply_patch(patch)['exit_code']==0;assert p.read_text()=='after\n'
    with pytest.raises(ValueError):t.apply_patch(patch.replace('runs/test-patch/sample.txt','skill/SKILL.md'))
def test_live_shell_session():
    import sys,shlex
    t=ResearchTools(ROOT/'runs/test-session')
    r=t.exec_command(shlex.quote(sys.executable)+' -c '+shlex.quote('import time; print("ready", flush=True); time.sleep(.1); print("done")'),yield_time_ms=0)
    output=r['stdout']
    while r['exit_code'] is None:
        r=t.write_stdin(r['session_id'],yield_time_ms=100);output+=r['stdout']
    assert 'ready' in output and 'done' in output

def test_pdf_identity_and_page_union():
    t=ResearchTools(ROOT/'runs/test-identity')
    paper={'screening_status':'core','identifiers':{'arxiv':'2610.00001'},'full_text_reading':{'sha256':'fixture','sections_reviewed':['method']}}
    events=[{'tool':'pdf_read_receipt','sha256':'fixture','pages':[1,2],'total_pages':3},
            {'tool':'download_pdf','result':{'sha256':'fixture','url':'https://arxiv.org/pdf/2610.00002'}}]
    errors=t._reading_errors(paper,events)
    assert any('identity' in e for e in errors)
    assert any('complete PDF' in e for e in errors)
    events[1]['result']['url']='https://arxiv.org/pdf/2610.00001v2'
    events.append({'tool':'pdf_read_receipt','sha256':'fixture','pages':[3],'total_pages':3})
    assert not t._reading_errors(paper,events)

def test_structural_audit_alone_is_not_completion():
    from compare import execution_evidence
    p=ROOT/'runs/test-incomplete';p.mkdir(parents=True,exist_ok=True)
    for name in ('audit.json','reading-audit.json'):(p/name).write_text('{"passed":true}')
    (p/'agent_meta.json').write_text('{"done":false}')
    assert not execution_evidence(p/'run.json',p/'run.json')['both_validated']

def test_unread_agreement_does_not_inflate_fully_read_score():
    import copy
    a=frame();a['papers']=[{'canonical_title':'read','identifiers':{'arxiv':'2610.00001'},'screening_status':'core','events':[], 'taxonomy_cells':{'planning':['PO-1']},'full_text_reading':{'sha256':'test'}},
                         {'canonical_title':'unread','identifiers':{'arxiv':'2610.00002'},'screening_status':'unresolved','events':[], 'taxonomy_cells':{'planning':['Unclear']}}]
    b=copy.deepcopy(a);b['papers'][0]['taxonomy_cells']['planning']=['PO-2']
    result=compare(a,b)
    assert result['taxonomy_cell_agreement']==.5
    assert result['fully_read_taxonomy_cell_agreement']==0

def test_source_cache_is_scoped_to_frozen_time():
    paths=[]
    for name,asof in [('cache-a','2026-10-15T07:00:00+00:00'),('cache-b','2026-10-15T07:00:00+00:00'),('cache-c','2026-10-16T07:00:00+00:00')]:
        run=ROOT/'runs'/name;run.mkdir(parents=True,exist_ok=True)
        (run/'run-input.json').write_text(json.dumps({'as_of':asof}))
        paths.append(ResearchTools(run).observations)
    assert paths[0]==paths[1]
    assert paths[0]!=paths[2]

def test_listing_preserves_titles_without_scope_filtering():
    text='Wed, 14 Oct 2026\narXiv:2610.00001\n[\npdf\n]\nTitle:\nUnrelated controls paper\nAuthor\narXiv:2610.00002\nTitle:\nGraphics agent paper\n'
    entries=ResearchTools._listing_entries(text)
    assert len(entries)==2
    assert entries[0]['title']=='Unrelated controls paper'
    assert entries[1]['arxiv']=='2610.00002'
    assert entries[1]['listing_heading']=='Wed, 14 Oct 2026'

def test_listing_rejects_unobserved_page_size():
    with pytest.raises(ValueError,match='show choices'):ResearchTools(ROOT/'runs/test-listing').arxiv_recent(show=200)

def test_search_preserves_citation_urls():
    data={'output':[{'type':'message','content':[{'type':'output_text','text':'result','annotations':[{'type':'url_citation','url':'https://arxiv.org/abs/2610.00001','title':'fixture'}]}]}]}
    assert ResearchTools._search_citations(data)==[{'url':'https://arxiv.org/abs/2610.00001','title':'fixture'}]
