"""Import the audited survey collection without exporting private research metadata.

Usage: python3 scripts/import-survey.py --papers papers.json --taxonomy corpus.json
       --tasks dated_taxonomy_305.json --output data/daily-results.json
All inputs are local, previously curated snapshots. This does not run discovery.
"""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlsplit


def read(path):
    return json.loads(Path(path).read_text())


def clean(text):
    text = str(text or '').strip()
    if re.search(r'/Users/|/home/|file://|https?://(?:localhost|127\.|10\.|192\.168\.)|docs\.google\.com|slack\.com|(?:api[_-]?key|token)\s*[:=]', text, re.I):
        raise ValueError('Private metadata found in an export field')
    return text


def public_url(url):
    u = urlsplit(url)
    return u.scheme in ('https', 'http') and bool(u.hostname) and not u.username and not u.password


TASK_AREAS = {
    **dict.fromkeys(['svg','design','figures','datavis','documents'], '2D Graphics'),
    **dict.fromkeys(['geometry','materials','asset_edit'], 'Static / Object'),
    **dict.fromkeys(['cad_gen','cad_rec','cad_edit'], 'Static / CAD'),
    **dict.fromkeys(['scene_gen','scene_rec','scene_edit'], 'Static / Scene'),
    'animation':'Dynamic / Animation and temporal scene',
    'simulation':'Dynamic / Physical simulation and effects',
    'articulation':'Dynamic / Articulated assets',
}


def build(papers, taxonomy, tasks, labels, summaries=()):
    by_url = {url: p for p in taxonomy for url in p['canonical_urls']}
    by_id = {p['row_id']: p for p in tasks}
    by_summary = {p['row_id']: p for p in summaries}
    records = []
    for source in papers:
        if not source['included']:
            continue
        matches = {by_url[u]['row_id']: by_url[u] for u in source['source_urls'] if u in by_url}
        if len(matches) != 1:
            raise ValueError('Missing or ambiguous source identity: ' + source['id'])
        p = next(iter(matches.values()))
        if p['screening_status'] not in ('core','enabling_or_adjacent','scope_dependent'):
            raise ValueError('Unsupported scope: ' + source['id'])
        url = next(u for u in p['canonical_urls'] if public_url(u))
        known_tasks = by_id.get(p['row_id'], {}).get('tasks', [])
        areas = list(dict.fromkeys(TASK_AREAS[t] for t in known_tasks if t in TASK_AREAS))
        if not areas and p['paper_role'] == 'benchmark_setting':
            areas = ['Datasets and Benchmarks']
        # Unmapped legacy groups stay explicit instead of guessing from titles.
        areas = areas or ['Cross-category']
        cells, evidence, grades = {}, {}, {}
        for field in labels['fields']:
            vals = p['taxonomy_cells'][field]
            grade = p['field_grades'].get(field, 'U')
            ev = p['field_evidence'].get(field, {})
            supported = grade in ('A','B')
            sentinel = len(vals) == 1 and vals[0] in labels['sentinels']
            cells[field] = vals if supported or sentinel else ['Unclear']
            grades[field] = grade
            if supported and public_url(ev.get('source_url', '')) and ev.get('reason') and ev.get('section_or_page'):
                evidence[field] = {
                    'primary_url': clean(ev['source_url']),
                    'locator': clean(ev['section_or_page']),
                    'evidence': clean(ev['reason']),
                    'level': 'primary' if grade == 'A' else 'derived',
                    'reasoning': 'Retained primary-source reading.' if grade == 'A' else 'Retained evidence recoded into the survey taxonomy; not a fresh paper read.',
                }
        pack = by_summary.get(p['row_id'], {})
        candidates = [(pack.get('legacy_review') or {}).get('summary', ''), *pack.get('summaries', [])]
        candidates = [v for v in candidates if len(v) > 60 and not re.search(r'[\u4e00-\u9fff]', v)
                      and not v.startswith(('PDF describes', 'Current-taxonomy', 'Current taxonomy', 'No retained'))]
        description = next(iter(candidates), p['configuration_note'])
        # Keep complete sentences; do not silently turn a curation note into an abstract.
        sentences = re.split(r'(?<=[.!?])\s+', description)
        short = sentences[0]
        for sentence in sentences[1:]:
            if len(short) + len(sentence) > 520:
                break
            short += ' ' + sentence
        record = {
            'id': source['id'].removeprefix('arxiv:'), 'title': clean(p['canonical_title']), 'url': clean(url),
            'summary': clean(short), 'summaryKind': 'curation_note',
            'scope': p['screening_status'], 'scopeReason': 'Included in the audited survey collection.',
            'bucket': 'survey_collection', 'eventType': 'first_submission',
            'eventDate': source['date'], 'dateKind': 'publication_or_first_submission',
            'applications': areas, 'application': areas[0], 'operations': [],
            'taxonomy': cells, 'taxonomyEvidence': evidence, 'taxonomyGrades': grades,
            'taxonomyVersion': labels['version'],
            'provenance': {'collection': 'Survey corpus', 'row': p['row_id'], 'snapshot': '2026-10-19',
                           'applicationBasis': 'Retained task annotations' if known_tasks else 'Benchmark role' if p['paper_role']=='benchmark_setting' else 'Not assigned to a specific application'},
        }
        if not record['summary']:
            raise ValueError('Missing retained summary: ' + source['id'])
        records.append(record)
    return records


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ['papers','taxonomy','tasks','output']:
        ap.add_argument('--'+name, required=True)
    ap.add_argument('--summaries', help='Retained evidence packs with short method summaries')
    args=ap.parse_args()
    labels=read(Path(__file__).resolve().parents[1]/'data/taxonomy-labels.json')
    records=build(read(args.papers),read(args.taxonomy),read(args.tasks),labels,read(args.summaries) if args.summaries else ())
    data=read(args.output)
    # Preserve verified date provenance when refreshing the historical annotations.
    dates={p['id']:p['publication'] for d in data['dates'] if d.get('collectionType')=='survey' for p in d['papers'] if p.get('publication')}
    for record in records:
        if record['id'] in dates:
            record['publication']=dates[record['id']]
    data['title']='Agentic graphics paper library'
    data['intro']='Browse the survey collection and daily discoveries, or choose a search date.'
    data['collectionNote']='The historical survey snapshot is stored separately from daily search reports using collectionType=survey.'
    data['dates']=[d for d in data['dates'] if d.get('collectionType')!='survey']
    data['dates'].append({'date':'2026-10-19','collectionType':'survey','title':'Survey collection',
        'summary':'Historical papers from the audited survey corpus. This is a collection snapshot, not a daily discovery run.',
        'feedNote':'Historical papers from the survey. Original publication dates are shown on each card.',
        'artifacts':[{'label':'Collection notes','url':'data/survey-collection.md'}],
        'papers':records})
    # Keep daily reports first for existing exports; consumers sort by date.
    latest={p['id']:p for d in sorted(data['dates'],key=lambda d:d['date']) for p in d['papers']}
    data['uniquePapers']=sum(p['scope'] not in ('excluded','unresolved') for p in latest.values())
    Path(args.output).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(f'Imported {len(records)} historical papers; {data["uniquePapers"]} unique papers overall.')


if __name__=='__main__':
    main()
