"""Attach public date provenance from an audited corpus and optional arXiv API caches.

python3 scripts/enrich-publication-dates.py --papers papers.json \
  --metadata arxiv_metadata.json candidate_metadata.json --output data/daily-results.json
No network calls; no local paths or private metadata are exported.
"""
import argparse
import datetime
import json
import re
from pathlib import Path


def enrich(data, sources, metadata):
    by_id = {p['id'].removeprefix('arxiv:'): p for p in sources if p.get('included')}
    count = 0
    for day in data['dates']:
        if day.get('collectionType') != 'survey':
            continue
        for p in day['papers']:
            source = by_id[p['id']]
            date = source['date']
            precision = 'month' if re.fullmatch(r'\d{4}-\d{2}', date) else 'day'
            datetime.date.fromisoformat(date + '-01' if precision == 'month' else date)
            arxiv = bool(re.fullmatch(r'\d{4}\.\d{4,5}', p['id']))
            url = 'https://arxiv.org/abs/' + p['id'] if arxiv else p['url']
            if not url.startswith('https://'):
                raise ValueError('Expected a public HTTPS source')
            publication = {'date': date, 'precision': precision,
                'basis': 'arxiv_first_submission' if arxiv else 'publication',
                'source': url,
                'evidence': ('Retained arXiv first-submission metadata.' if arxiv else
                             'Publication date retained from the audited survey corpus.')}
            cached = metadata.get(p['id'], {}) if arxiv else {}
            if cached.get('published'):
                stamp = cached['published']
                datetime.datetime.fromisoformat(stamp.replace('Z', '+00:00'))
                if stamp[:10] != date:
                    raise ValueError('Conflicting submission dates: ' + p['id'])
                publication['timestamp'] = stamp
                publication['evidence'] = 'arXiv API published timestamp (v1, UTC).'
            elif arxiv and source.get('date_evidence', {}).get('kind') == 'citation_date':
                publication['evidence'] = 'arXiv abstract-page citation_date (first submission).'
            p['publication'] = publication
            count += 1
    return count


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--papers', required=True)
    ap.add_argument('--metadata', nargs='*', default=[])
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    read = lambda p: json.loads(Path(p).read_text())
    metadata = {}
    for file in args.metadata:
        metadata.update(read(file))
    data = read(args.output)
    count = enrich(data, read(args.papers), metadata)
    Path(args.output).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(f'Added publication-date provenance to {count} survey papers.')


if __name__ == '__main__':
    main()
