import json
import uuid
import httpx
import pytest
from research_tools import ROOT,ResearchTools
from agent_state import read_events


def test_pdf_cache_corruption_is_refetched_and_repaired(monkeypatch):
    import pymupdf
    tool=ResearchTools(ROOT/'runs'/('test-corrupt-'+uuid.uuid4().hex))
    url='https://example.org/synthetic-'+uuid.uuid4().hex+'.pdf'
    document=pymupdf.open();document.new_page().insert_text((50,50),'Synthetic '+uuid.uuid4().hex)
    content=document.tobytes();document.close();calls=[]
    def fetch(url):calls.append(url);return httpx.Response(200,content=content,request=httpx.Request('GET',url))
    monkeypatch.setattr(tool,'_fetch',fetch)
    first=tool.download_pdf(url);path=tool.path(first['path']);path.write_bytes(b'corrupted test cache')
    second=tool.download_pdf(url)
    assert len(calls)==2 and first['sha256']==second['sha256']
    assert path.read_bytes()==content
    assert any(e.get('tool')=='cache_invalidated' for e in read_events(tool.trace))


def test_missing_page_text_cache_is_rebuilt_without_network(monkeypatch):
    tool=ResearchTools(ROOT/'runs'/('test-page-cache-'+uuid.uuid4().hex));calls=[]
    url='https://example.org/'+uuid.uuid4().hex
    def fetch(url):calls.append(url);return httpx.Response(200,text='<html><body>Original observation</body></html>',request=httpx.Request('GET',url))
    monkeypatch.setattr(tool,'_fetch',fetch)
    first=tool._page(url);tool.path(first['text_path']).unlink();second=tool._page(url)
    assert len(calls)==1 and tool.path(second['text_path']).read_text()=='Original observation'


def test_http_retry_respects_api_spacing_and_stops_on_forbidden(monkeypatch):
    import research_tools
    waits=[];responses=[503,200];calls=[]
    class Client:
        def __init__(self,**kwargs):pass
        def __enter__(self):return self
        def __exit__(self,*args):pass
        def get(self,url,**kwargs):
            calls.append(url);return httpx.Response(responses.pop(0),content=b'ok',request=httpx.Request('GET',url))
    monkeypatch.setattr(research_tools.httpx,'Client',Client)
    monkeypatch.setattr(research_tools.time,'sleep',waits.append)
    tool=ResearchTools(ROOT/'runs'/('test-http-retry-'+uuid.uuid4().hex))
    assert tool._fetch('https://export.arxiv.org/api/query?x=synthetic').status_code==200
    assert waits==[3] and len(calls)==2
    responses[:]=[403];calls.clear();waits.clear()
    with pytest.raises(httpx.HTTPStatusError):tool._fetch('https://example.org/forbidden')
    assert len(calls)==1 and not waits


def test_invalid_pdf_bytes_are_not_reported_as_a_download(monkeypatch):
    tool=ResearchTools(ROOT/'runs'/('test-invalid-pdf-'+uuid.uuid4().hex))
    monkeypatch.setattr(tool,'_fetch',lambda url:httpx.Response(200,content=b'%PDF synthetic invalid bytes',request=httpx.Request('GET',url)))
    result=tool.call('download_pdf',{'url':'https://example.org/'+uuid.uuid4().hex+'.pdf'})
    assert result.get('error') and 'sha256' not in result


def test_long_retry_after_prevents_immediate_later_tool_refetch(monkeypatch):
    import research_tools
    calls=[];host='cooldown-'+uuid.uuid4().hex+'.example.org'
    class Client:
        def __init__(self,**kwargs):pass
        def __enter__(self):return self
        def __exit__(self,*args):pass
        def get(self,url,**kwargs):
            calls.append(url)
            return httpx.Response(429,headers={'Retry-After':'120'},request=httpx.Request('GET',url))
    monkeypatch.setattr(research_tools.httpx,'Client',Client)
    tool=ResearchTools(ROOT/'runs'/('test-cooldown-'+uuid.uuid4().hex))
    with pytest.raises(httpx.HTTPStatusError):tool._fetch('https://'+host+'/one')
    with pytest.raises(ValueError,match='cooldown'):tool._fetch('https://'+host+'/two')
    assert len(calls)==1
