import copy,hashlib,json
from pathlib import Path

from agent_state import compact_observations,archive_context_observation


def msg(value,role='user'):
    return {'role':role,'parts':[{'kind':'text','text':json.dumps(value)}]}


def older(value):
    return [msg(value),msg({'read':True},'assistant'),msg({'new':True})]


def status():
    ids=[f'2610.{i:05d}' for i in range(1300)]
    return {'tool':'research_status','result':{
        'observed_arxiv_ids':ids,'metadata_resolved_arxiv_ids':ids,
        'metadata_resolved_without_saved_decision':ids,
        'title_hint_leads_without_saved_decision':[{'arxiv':x,'title':'Potential lead'} for x in ids[:30]],
        'opened_without_saved_decision':['2610.00015'],
        'read_pdf_without_saved_reading':[{'sha256':'unfinished-pdf'}],
        'tool_error_count':1,'recent_errors':[{'tool':'open_page','error':'blocked'}],
        'warning':'Observed source IDs are not scope decisions.'}}


def test_bookkeeping_archive_is_exact_and_actionable_gaps_remain(tmp_path):
    original=status();messages=older(original)
    raw=tmp_path/'tool-events.jsonl';raw.write_text(json.dumps(original)+'\n');before=raw.read_bytes()
    compact_observations(messages,tmp_path)
    out=json.loads(messages[0]['parts'][0]['text']);saved=Path(out['observation_path'])
    assert json.loads(saved.read_text())==original
    assert hashlib.sha256(saved.read_bytes()).hexdigest()==out['observation_sha256']
    assert out['result']['observed_arxiv_ids_count']==1300
    for key in ['opened_without_saved_decision','read_pdf_without_saved_reading','recent_errors','warning']:
        assert out['result'][key]==original['result'][key]
    assert len(messages[0]['parts'][0]['text'])<len(json.dumps(original))/5
    assert raw.read_bytes()==before
    unchanged=copy.deepcopy(messages);compact_observations(messages,tmp_path)
    assert messages==unchanged


def test_new_or_assistant_status_is_not_archived(tmp_path):
    messages=[msg(status(),role='assistant'),msg(status())];before=copy.deepcopy(messages)
    compact_observations(messages,tmp_path)
    assert messages==before and not (tmp_path/'context-observations').exists()


def test_scan_compaction_does_not_hide_incomplete_sources(tmp_path):
    original={'tool':'arxiv_scan','result':{
        'title_review_hints':[{'arxiv':f'2610.{i:05d}','title':'Long candidate title'} for i in range(500)],
        'title_pool_path':'own/discovery/cs.CV-new-titles.json','complete_observed_pagination':False,
        'unvisited_observed_urls':['https://arxiv.org/list/cs.CV/new?skip=100'],
        'errors':['timeout'],'warnings':['inconsistent listing snapshot']}}
    messages=older(original);compact_observations(messages,tmp_path)
    out=json.loads(messages[0]['parts'][0]['text'])
    assert out['result']['complete_observed_pagination'] is False
    assert out['result']['errors']==['timeout']
    assert out['result']['unvisited_observed_urls']==original['result']['unvisited_observed_urls']
    assert json.loads(Path(out['observation_path']).read_text())==original


def test_mixed_catalog_retains_untriaged_primary_provenance(tmp_path):
    records=[{'arxiv':'2610.12345','title':'Triaged','abstract':'First full abstract','metadata_sha256':'s1'},
             {'arxiv':'2610.12346','title':'Unread','abstract':'Second full abstract','metadata_sha256':'s2'}]
    sources=[{'sha256':'s1','url':'https://primary.example/one'},
             {'sha256':'s2','url':'https://primary.example/two'}]
    original={'tool':'candidate_catalog','result':{'operation':'read','catalog_path':'own/catalog.json',
        'records':records,'metadata_sources':sources}}
    (tmp_path/'triage.json').write_text(json.dumps([{'id':'2610.12345','triage_status':'needs_full_read','reason':'Need the method.'}]))
    messages=older(original);compact_observations(messages,tmp_path)
    out=json.loads(messages[0]['parts'][0]['text'])['result']
    assert out['records'][1]==records[1] and out['metadata_sources']==sources[1:]
    assert json.loads(Path(out['observation_path']).read_text())==original


def test_interrupted_archive_is_repaired_from_exact_observation(tmp_path):
    original=json.dumps(status());result=archive_context_observation(tmp_path,original)
    path=Path(result['observation_path']);path.write_text('{interrupted')
    second=archive_context_observation(tmp_path,original)
    assert result==second and path.read_text()==original
    assert list(path.parent.iterdir())==[path]
