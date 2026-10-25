import json
from tool_protocol import parse_calls


def fenced(call):
    return '```tool\n' + json.dumps(call) + '\n```\n'


def test_markdown_fences_inside_json_strings_are_preserved():
    call = {'name': 'write_file', 'arguments': {'path': 'report.md', 'content': 'Example\n```python\nprint(1)\n```\n'}}
    assert parse_calls(fenced(call)) == [call]


def test_mixed_tool_and_bash_calls_preserve_declared_order():
    first = {'name': 'clock_now', 'arguments': {}}
    third = {'name': 'read_file', 'arguments': {'path': 'new.txt'}}
    reply = fenced(first) + '```bash\nprintf created > new.txt\n```\n' + fenced(third)
    assert parse_calls(reply) == [first, {'name': 'exec_command', 'arguments': {'cmd': 'printf created > new.txt'}}, third]


def test_invalid_tool_is_not_executed_and_later_valid_call_survives():
    valid = {'name': 'clock_now', 'arguments': {}}
    calls = parse_calls('```tool\n[]\n```\n' + fenced(valid))
    assert calls[0]['name'] == '__invalid__' and calls[1] == valid


def test_unclosed_bash_is_not_executed():
    assert parse_calls('```bash\nunfinished')[0]['name'] == '__invalid__'
