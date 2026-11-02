"""Parse BVB fenced calls without treating JSON string contents as fence endings."""
import json
import re

START = re.compile(r'^```(tool|bash)[ \t]*\n', re.M)
END = re.compile(r'^```[ \t]*(?:\n|$)', re.M)


def parse_calls(reply):
    calls, cursor = [], 0
    while match := START.search(reply, cursor):
        start = match.end()
        if match.group(1) == 'bash':
            end = END.search(reply, start)
            if end is None:
                calls.append({'name': '__invalid__', 'arguments': {'error': 'Unclosed bash fence'}})
                break
            calls.append({'name': 'exec_command', 'arguments': {'cmd': reply[start:end.start()].strip()}})
            cursor = end.end()
            continue
        body = reply[start:]
        offset = len(body) - len(body.lstrip())
        try:
            value, length = json.JSONDecoder().raw_decode(body, offset)
            tail = body[length:]
            fence = re.match(r'\s*```[ \t]*(?:\n|$)', tail)
            if fence is None:
                raise ValueError('Tool JSON must be followed by a closing fence')
            if not isinstance(value, dict) or not isinstance(value.get('name'), str) or not isinstance(value.get('arguments', {}), dict):
                raise ValueError('Expected a tool object with name and object arguments')
            calls.append(value)
            cursor = start + length + fence.end()
        except ValueError as error:
            calls.append({'name': '__invalid__', 'arguments': {'error': str(error)}})
            end = END.search(reply, start)
            cursor = end.end() if end else len(reply)
    return calls
