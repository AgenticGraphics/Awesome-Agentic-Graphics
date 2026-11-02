import copy,json
import pytest
from agent_state import compact_observations
from agent import finalization_due


def observation():
    return {'tool':'candidate_catalog','result':{'operation':'read','bucket':'target_and_uncertain',
        'catalog_path':'own/discovery/candidate-catalog.json','catalog_sha256':'original-catalog-hash',
        'records':[{'arxiv':'2610.12345','title':'Selected','abstract':'Complete first abstract.'*1000,
                    'published':'2026-10-14T06:00:00Z','metadata_sha256':'source1'},
                   {'arxiv':'2610.12346','title':'Not yet considered','abstract':'Preserve every word here.','metadata_sha256':'source2'}]}}


def message(value,role='user'):
    return {'role':role,'parts':[{'kind':'text','text':json.dumps(value)}]}


def history(value):
    return [message(value),message({'received':True},'assistant'),message({'next':'observation'})]


def decisions(path,status='needs_full_read',reason='Primary abstract needs a full-text check.'):
    (path/'triage.json').write_text(json.dumps([{'id':'2610.12345','triage_status':status,'reason':reason}]))


def test_only_persistently_triaged_abstracts_compact_before_any_pdf_checkpoint(tmp_path):
    original=observation();messages=history(original);decisions(tmp_path)
    raw=tmp_path/'tool-events.jsonl';raw.write_text(json.dumps(original)+'\n');before=raw.read_bytes()
    compact_observations(messages,tmp_path)
    result=json.loads(messages[0]['parts'][0]['text'])['result']
    first,second=result['records']
    assert 'abstract' not in first and first['triage_status']=='needs_full_read'
    from pathlib import Path
    archived=json.loads(Path(result['observation_path']).read_text())
    assert archived==original
    assert archived['result']['records'][0]['published']=='2026-10-14T06:00:00Z'
    assert second==original['result']['records'][1]
    assert result['catalog_path']==original['result']['catalog_path']
    assert result['catalog_sha256']=='original-catalog-hash'
    assert raw.read_bytes()==before and not (tmp_path/'checkpoints').exists()
    saved=copy.deepcopy(messages);compact_observations(messages,tmp_path)
    assert messages==saved  # Repeated compaction does not keep invalidating the prefix.


@pytest.mark.parametrize('kind',['absent','malformed','no_reason','invalid_status'])
def test_unsaved_or_invalid_triage_does_not_remove_abstracts(tmp_path,kind):
    if kind=='malformed':(tmp_path/'triage.json').write_text('{partial')
    elif kind=='no_reason':decisions(tmp_path,reason='')
    elif kind=='invalid_status':decisions(tmp_path,status='guessed')
    messages=history(observation());before=copy.deepcopy(messages)
    compact_observations(messages,tmp_path)
    assert messages==before


def test_assistant_history_is_never_compacted_even_if_it_resembles_a_tool_result(tmp_path):
    decisions(tmp_path);messages=[message(observation(),role='assistant')];before=copy.deepcopy(messages)
    compact_observations(messages,tmp_path)
    assert messages==before


def test_later_saved_decisions_can_compact_previously_untriaged_rows(tmp_path):
    decisions(tmp_path);messages=history(observation());compact_observations(messages,tmp_path)
    data=json.loads((tmp_path/'triage.json').read_text())
    data.append({'arxiv':'2610.12346','triage_status':'reject_obvious','reason':'Explicit own-run abstract triage, still provisional.'})
    (tmp_path/'triage.json').write_text(json.dumps(data));compact_observations(messages,tmp_path)
    rows=json.loads(messages[0]['parts'][0]['text'])['result']['records']
    assert all('abstract' not in r for r in rows)
    assert rows[1]['triage_status']=='reject_obvious' and 'screening_status' not in rows[1]


def test_newly_reopened_abstract_reaches_model_before_compaction(tmp_path):
    decisions(tmp_path);messages=[message(observation())];before=copy.deepcopy(messages)
    compact_observations(messages,tmp_path)
    assert messages==before
    messages.extend([message({'received':True},'assistant'),message({'next':'observation'})])
    compact_observations(messages,tmp_path)
    assert 'abstract' not in json.loads(messages[0]['parts'][0]['text'])['result']['records'][0]


@pytest.mark.parametrize('seconds,cost,expected',[(500,17.99,False),(500,18,True),(179,0,True),(180,0,False)])
def test_finalization_reserves_time_and_estimated_cost(seconds,cost,expected):
    assert finalization_due(seconds,cost,30) is expected
