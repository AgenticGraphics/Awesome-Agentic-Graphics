"""Collect dates from returned primary observations, without inferring missing versions."""
from datetime import datetime, timezone
import re


def arxiv_id(url):
    match = re.search(r'arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})', url)
    return match.group(1) if match else None


def submission_history(text):
    text = re.sub(r'(?m)^\d+:\s*', '', text)
    if 'Submission history' not in text:
        return {}
    text = text.split('Submission history', 1)[1].split('Full-text', 1)[0]
    result = {}
    for version, date in re.findall(r'\[(v\d+)\]\s*((?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),\s+\d+\s+\w+\s+\d{4}\s+\d\d:\d\d:\d\d\s+UTC)', text):
        result[version] = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    return result


def collect_dates(events):
    dates, conflicts = {}, []

    def add(key, version, stamp):
        stamp = datetime.fromisoformat(stamp.replace('Z', '+00:00')) if isinstance(stamp, str) else stamp
        if stamp.tzinfo is None:
            raise ValueError('Primary timestamp lacks timezone')
        previous = dates.setdefault(key, {}).get(version)
        if previous is not None and previous != stamp:
            conflicts.append({'paper': key, 'version': version, 'first': previous.isoformat(), 'other': stamp.isoformat()})
        else:
            dates[key][version] = stamp

    for event in events:
        result = event.get('result', {})
        if not isinstance(result, dict) or result.get('error'):
            continue
        if event.get('tool') in ('open_page', 'click_link', 'find_in_page'):
            key = arxiv_id(result.get('url', ''))
            text = result.get('text', '') or '\n'.join(m.get('text', '') for m in result.get('matches', []))
            if key:
                for version, stamp in submission_history(text).items():
                    add(key, version, stamp)
        elif event.get('tool') == 'arxiv_metadata':
            for record in result.get('records', []):
                add(record['arxiv'], 'v1', record['published'])
                if record.get('version'):
                    add(record['arxiv'], record['version'], record['updated'])
    return dates, conflicts
