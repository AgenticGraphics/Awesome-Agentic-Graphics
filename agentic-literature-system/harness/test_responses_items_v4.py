import copy,json,stat
import httpx,pytest
import importlib.util
from pathlib import Path
_spec=importlib.util.spec_from_file_location('responses_items_v4_adapter',Path(__file__).with_name('responses_model.py'))
_adapter=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(_adapter)
ResponsesModel=_adapter.ResponsesModel


def answer(text='NEXT',encrypted=True,status='completed',phase='commentary'):
    reasoning={'type':'reasoning','id':'r1','summary':[]}
    if encrypted:reasoning['encrypted_content']='synthetic-opaque-state'
    return {'id':'response1','status':status,'output':[reasoning,
        {'type':'message','id':'msg1','role':'assistant','phase':phase,'status':'completed',
         'content':[{'type':'output_text','text':text,'annotations':[]}]}],
        'usage':{'input_tokens':10,'output_tokens':2}}


def setup(monkeypatch,replies):
    bodies=[];client=httpx.Client
    def handle(request):
        bodies.append(json.loads(request.content));value=replies[len(bodies)-1]
        if isinstance(value,httpx.Response):return value
        return httpx.Response(200,json=value)
    monkeypatch.setattr(httpx,'Client',lambda **kwargs:client(transport=httpx.MockTransport(handle),**kwargs))
    monkeypatch.setenv('OPENAI_BASE_URL','http://synthetic.invalid/v1')
    monkeypatch.setenv('OPENAI_API_KEY','synthetic-no-network-test')
    return bodies


def message(role,text):return {'role':role,'parts':[{'kind':'text','text':text}]}


def test_replays_encrypted_items_and_phases_across_restart(monkeypatch,tmp_path):
    bodies=setup(monkeypatch,[answer(),answer('DONE',phase='final_answer')]);path=tmp_path/'state.json'
    first=ResponsesModel('gpt-6-astra',reasoning='medium',state_path=path)
    history=[message('user','start')]
    text,info=first.complete('system',history)
    assert info['encrypted_reasoning_items']==1
    assert stat.S_IMODE(path.stat().st_mode)==0o600
    second=ResponsesModel('gpt-6-astra',reasoning='medium',state_path=path)
    # An exact unconsumed request can reuse its saved response without another API request.
    assert second.complete('system',history)[1]['reused_unconsumed_response']
    history.extend([message('assistant',text),message('user','tool result')])
    assert second.complete('system',history)[0]=='DONE'
    inputs=bodies[1]['input']
    assert [i.get('type',i.get('role')) for i in inputs]==['system','user','reasoning','message','user']
    assert inputs[2]['encrypted_content']=='synthetic-opaque-state'
    assert inputs[3]['phase']=='commentary'
    assert not bodies[1]['store'] and bodies[1]['reasoning']=={'effort':'medium'}
    assert 'tools' not in bodies[1] and 'tool_choice' not in bodies[1]


def test_compacted_observations_keep_matching_assistant_items(monkeypatch,tmp_path):
    bodies=setup(monkeypatch,[answer(),answer('DONE')])
    model=ResponsesModel('gpt-6-astra',reasoning='medium',state_path=tmp_path/'state.json')
    model.complete('system',[message('user','very long original observation')])
    model.complete('system',[message('user','compacted observation'),message('assistant','NEXT'),message('user','continue')])
    assert bodies[1]['input'][1]['content']=='compacted observation'
    assert any(x.get('type')=='reasoning' for x in bodies[1]['input'])


def test_mismatched_history_system_and_model_are_rejected(monkeypatch,tmp_path):
    setup(monkeypatch,[answer()]);path=tmp_path/'state.json'
    model=ResponsesModel('gpt-6-astra',reasoning='medium',state_path=path)
    model.complete('system',[message('user','start')])
    with pytest.raises(ValueError,match='Assistant history changed'):
        model.complete('system',[message('user','start'),message('assistant','changed'),message('user','continue')])
    with pytest.raises(ValueError,match='changed system'):
        model.complete('other',[message('user','start')])
    with pytest.raises(ValueError,match='different model'):
        ResponsesModel('gpt-6-astra',reasoning='high',state_path=path)


def test_absent_encrypted_state_is_disclosed_and_not_replayed_by_id(monkeypatch,tmp_path):
    bodies=setup(monkeypatch,[answer(encrypted=False),answer('DONE')])
    model=ResponsesModel('gpt-6-astra',reasoning='medium',state_path=tmp_path/'state.json')
    text,info=model.complete('system',[message('user','start')])
    assert info['encrypted_reasoning_items']==0 and info['reasoning_items_without_replayable_content']==1
    model.complete('system',[message('user','start'),message('assistant',text),message('user','continue')])
    assert not any(x.get('type')=='reasoning' for x in bodies[1]['input'])


def test_failed_request_preserves_state_and_http_retry_headers(monkeypatch,tmp_path):
    setup(monkeypatch,[answer(),httpx.Response(429,headers={'Retry-After':'30'},json={'error':{'message':'busy'}})])
    path=tmp_path/'state.json';model=ResponsesModel('gpt-6-astra',reasoning='medium',state_path=path)
    model.complete('system',[message('user','start')]);before=path.read_bytes()
    with pytest.raises(httpx.HTTPStatusError) as error:
        model.complete('system',[message('user','start'),message('assistant','NEXT'),message('user','continue')])
    assert error.value.response.headers['Retry-After']=='30' and path.read_bytes()==before


def test_incomplete_response_is_never_cached_as_success(monkeypatch,tmp_path):
    setup(monkeypatch,[answer(status='incomplete')]);path=tmp_path/'state.json'
    model=ResponsesModel('gpt-6-astra',reasoning='medium',state_path=path)
    with pytest.raises(RuntimeError,match='not completed'):model.complete('system',[message('user','start')])
    assert not path.exists()
    assert len(list((tmp_path/'provider-responses').glob('*.json')))==1


def test_empty_failed_image_marker_is_archived_disclosed_and_never_replayed(monkeypatch,tmp_path):
    first=answer('```tool\n{"name":"clock_now","arguments":{}}\n```')
    marker={'id':'ig_synthetic','type':'image_generation_call','status':'failed'}
    first['output'].insert(1,marker)
    bodies=setup(monkeypatch,[first,answer('DONE')])
    model=ResponsesModel('gpt-6-astra',reasoning='medium',state_path=tmp_path/'state.json')
    history=[message('user','start')];reply,info=model.complete('system',history)
    assert info['omitted_empty_failed_image_markers']==[marker]
    assert not info['native_calls_dispatched_by_adapter']
    raw=Path(info['provider_response_path'])
    assert json.loads(raw.read_text())==first and stat.S_IMODE(raw.stat().st_mode)==0o600
    assert reply==first['output'][2]['content'][0]['text']
    history.extend([message('assistant',reply),message('user','clock result')])
    model.complete('system',history)
    assert not any(i.get('type')=='image_generation_call' for i in bodies[1]['input'])


@pytest.mark.parametrize('native',[
    {'id':'ig_synthetic','type':'image_generation_call','status':'completed'},
    {'id':'ig_synthetic','type':'image_generation_call','status':'in_progress'},
    {'id':'ig_synthetic','type':'image_generation_call','status':'failed','result':'payload'},
    {'type':'image_generation_call','status':'failed'},
    {'id':'fc_synthetic','type':'function_call','name':'clock_now','arguments':'{}','call_id':'c1'},
])
def test_real_or_unrecognized_native_outputs_are_rejected_and_preserved(monkeypatch,tmp_path,native):
    data=answer();data['output'].insert(1,native);setup(monkeypatch,[data])
    model=ResponsesModel('gpt-6-astra',reasoning='medium',state_path=tmp_path/'state.json')
    with pytest.raises(ValueError,match='Unexpected native tool output'):
        model.complete('system',[message('user','start')])
    assert not (tmp_path/'state.json').exists()
    raw=list((tmp_path/'provider-responses').glob('*.json'))
    assert len(raw)==1 and json.loads(raw[0].read_text())==data


def test_failed_image_marker_without_assistant_message_is_not_success(monkeypatch,tmp_path):
    data=answer();data['output']=[{'id':'ig_synthetic','type':'image_generation_call','status':'failed'}]
    setup(monkeypatch,[data])
    model=ResponsesModel('gpt-6-astra',reasoning='medium',state_path=tmp_path/'state.json')
    with pytest.raises(RuntimeError,match='no assistant text'):
        model.complete('system',[message('user','start')])
    assert not (tmp_path/'state.json').exists()
