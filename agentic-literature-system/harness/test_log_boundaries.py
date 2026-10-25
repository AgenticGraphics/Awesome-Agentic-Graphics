import json
from agent_state import append_event, read_events


def test_interruption_inside_utf8_character_is_recoverable(tmp_path):
    path=tmp_path/'events.jsonl'
    path.write_bytes(b'{"ok":1}\n'+ '{"text":"论'.encode()[:-1])
    assert read_events(path)==[{'ok':1}]
    append_event(path,{'ok':2})
    assert read_events(path)==[{'ok':1},{'ok':2}]
    assert path.with_suffix('.interrupted-tail').exists()


def test_complete_json_without_newline_is_not_lost(tmp_path):
    path=tmp_path/'events.jsonl';path.write_text('{"ok":1}')
    append_event(path,{'ok':2})
    assert read_events(path)==[{'ok':1},{'ok':2}]
    assert not path.with_suffix('.interrupted-tail').exists()
