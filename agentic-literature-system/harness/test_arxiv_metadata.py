import pytest
from arxiv_metadata import parse_atom,normalize_id


ATOM='''<feed xmlns="http://www.w3.org/2005/Atom"><entry>
<id>http://arxiv.org/abs/2610.00001v3</id><title>Synthetic title</title>
<summary>Example abstract.</summary><author><name>Example Author</name></author>
<published>2026-10-12T23:30:00Z</published><updated>2026-10-14T04:00:00Z</updated>
<category term="cs.GR"/><link title="pdf" href="http://arxiv.org/pdf/2610.00001v3"/>
</entry></feed>'''


def test_metadata_preserves_timestamps_version_and_missing_ids():
    result=parse_atom(ATOM,['2610.00001','2610.00002'])
    paper=result['records'][0]
    assert paper['published']=='2026-10-12T23:30:00Z' and paper['updated']=='2026-10-14T04:00:00Z'
    assert paper['version']=='v3' and result['missing_ids']==['2610.00002']
    assert 'events' not in paper  # No invented v2 revision/date or local-day decision.


def test_error_feed_is_not_an_empty_success():
    with pytest.raises(ValueError,match='error entry'):
        parse_atom(ATOM.replace('http://arxiv.org/abs/2610.00001v3','http://arxiv.org/api/errors'),['2610.00001'])


def test_invalid_ids_and_unzoned_source_dates_are_rejected():
    with pytest.raises(ValueError):normalize_id('2610.00001 OR all:agent')
    with pytest.raises(ValueError,match='timezone'):
        parse_atom(ATOM.replace('2026-10-12T23:30:00Z','2026-10-12T23:30:00'),['2610.00001'])


def test_requested_version_mismatch_is_visible():
    result=parse_atom(ATOM,['2610.00001v1'])
    assert result['version_mismatches']==[{'requested':'2610.00001v1','returned_versions':['v3']}]
    assert not result['requested_identities_complete']


def test_unrequested_identity_is_not_accepted_as_the_answer():
    result=parse_atom(ATOM,['2610.00002'])
    assert result['unexpected_ids']==['2610.00001']
    assert not result['requested_identities_complete']


def test_metadata_cache_cannot_silently_change_source_dates(monkeypatch,tmp_path):
    import json,httpx,research_tools
    monkeypatch.setattr(research_tools,'ROOT',tmp_path)
    monkeypatch.setattr(research_tools.time,'sleep',lambda seconds:None)
    tool=research_tools.ResearchTools(tmp_path/'runs'/'synthetic');calls=[]
    def fetch(url):
        calls.append(url)
        return httpx.Response(200,content=ATOM.encode(),request=httpx.Request('GET',url))
    monkeypatch.setattr(tool,'_fetch',fetch)
    first=tool.arxiv_metadata(['2610.00001'])
    path=__import__('pathlib').Path(first['metadata_path']);corrupt=json.loads(path.read_text())
    corrupt['records'][0]['published']='2026-10-13T23:30:00Z';path.write_text(json.dumps(corrupt))
    repaired=tool.arxiv_metadata(['2610.00001'])
    assert len(calls)==2 and repaired['records'][0]['published']=='2026-10-12T23:30:00Z'
