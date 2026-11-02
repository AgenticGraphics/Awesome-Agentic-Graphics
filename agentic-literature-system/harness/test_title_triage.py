import copy
from title_triage import title_hints


def test_title_hints_are_metadata_only_and_never_remove_source_entries():
    entries=[{'arxiv':'synthetic-a','title':'A coding assistant for visual authoring'},
             {'arxiv':'synthetic-b','title':'Program synthesis for CAD design'},
             {'arxiv':'synthetic-c','title':'A new graphics representation'},
             {'arxiv':'synthetic-d','title':'Agents for database management'}]
    original=copy.deepcopy(entries)
    hints=title_hints(entries)
    assert {x['arxiv'] for x in hints}=={'synthetic-a','synthetic-b'}
    assert entries==original
    assert all('screening_status' not in x for x in hints)
