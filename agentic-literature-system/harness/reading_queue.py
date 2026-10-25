"""Source/history attention pool and auditable model-authored reading priorities.

No paper identities, expected classifications or reference answers are encoded.
The pool is a bounded attention aid, not an exhaustive relevance filter.
"""
import json
from pathlib import Path
from candidate_catalog import base_id, FOCUS_BUCKETS, select_page, date_queue
from title_triage import title_hints

PRIORITIES = ('direct_graphics_action', 'explicit_enabling', 'borderline', 'unclear')


def history_rows(directory):
    if directory is None:
        return {}
    directory = Path(directory)
    result = {}
    for row in json.loads((directory / 'index.json').read_text()):
        if not row['id'].startswith('arxiv:'):
            continue
        detail = (directory / row['detail_path']).resolve()
        if not detail.is_relative_to(directory.resolve()):
            raise ValueError('History detail outside frozen bundle')
        observations = json.loads(detail.read_text())['observations']
        result[row['id'][6:]] = dict(row, observations=observations)
    return result


def already_read_version(row, history):
    if history.get('scope_disagreement'):
        return False
    for obs in history.get('observations', []):
        if not obs.get('full_text_reading'):
            continue
        for event in obs.get('events', []):
            if (event.get('version') == row.get('version') and event.get('value')
                    and event['value'].replace('+00:00', 'Z') == row.get('updated', '').replace('+00:00', 'Z')):
                return True
    return False


def attention_pool(rows, history):
    hints = {r['arxiv'] for r in title_hints(rows)}
    selected, deferred = [], []
    for row in rows:
        old = history.get(row['arxiv'], {})
        reasons = []
        if row['date_queue'] in FOCUS_BUCKETS:
            reasons.append('target_or_uncertain_date')
        elif row['date_queue'] == 'lookback':
            if already_read_version(row, old):
                deferred.append(row['arxiv'])
                continue
            if old.get('needs_followup'):
                reasons.append('prior_pending')
            if 'cs.GR' in row.get('categories', []):
                reasons.append('graphics_category_without_keyword_requirement')
            if row['arxiv'] in hints:
                reasons.append('transparent_title_hint')
            if row.get('additional_source_lead'):
                reasons.append('additional_source_with_primary_metadata')
        if reasons:
            selected.append(dict(row, attention_reasons=reasons))
    # Date order is for reviewing abstracts, not a fixed PDF reading order.
    selected.sort(key=lambda r: (r['date_queue'] not in FOCUS_BUCKETS, r['arxiv']))
    return selected, deferred


def attention_page(rows, history, start_index, page_size):
    pool, deferred = attention_pool(rows, history)
    result = select_page(pool, 'all', start_index, page_size)
    reasons = {r['arxiv']: r['attention_reasons'] for r in pool}
    for r in result['records']:
        r['attention_reasons'] = reasons[r['arxiv']]
    result.update(bucket='catchup_review', unchanged_completed_deferred_count=len(deferred),
        warning='Full primary abstracts for date-focus, prior pending, graphics-category and title-hint leads. No relevance labels supplied. The rest of the source catalog remains available; this is not exhaustive discovery. Unchanged completed versions are deferred, never excluded.')
    return result


def build_plan(rows, history, triage, events, read_cap, frame=None):
    if isinstance(triage, dict):
        triage = triage.get('candidates', triage.get('papers', []))
    decisions = {base_id(t.get('arxiv') or t.get('id') or t.get('observed_source_url')): t
                 for t in triage if isinstance(t, dict)}
    # The listing catalog keeps its original denominator. Additional model-triaged
    # leads join the reading queue only with returned official primary metadata.
    source_ids = {r['arxiv'] for r in rows}
    extras = {}
    if frame:
        for event in events:
            if event.get('tool') != 'arxiv_metadata' or event.get('result', {}).get('error'):
                continue
            requested = {base_id(x) for x in event.get('arguments', {}).get('ids', [])}
            for r in event.get('result', {}).get('records', []):
                key = r.get('arxiv')
                if key in source_ids or key not in requested or key not in decisions or not r.get('abstract'):
                    continue
                bucket, uncertain = date_queue(r, frame)
                extras[key] = dict(r, date_queue=bucket, version_history_required=uncertain,
                                  additional_source_lead=True)
    rows = list(rows) + list(extras.values())
    pool, deferred = attention_pool(rows, history)
    delivered = {r['arxiv'] for e in events if e.get('tool') == 'candidate_catalog'
                 and e.get('result', {}).get('operation') == 'read'
                 for r in e['result'].get('records', []) if r.get('abstract')}
    delivered.update(extras)
    pending, gaps, rank_gaps = [], [], []
    for r in pool:
        t = decisions.get(r['arxiv'], {})
        if t.get('triage_status') == 'reject_obvious' and t.get('reason'):
            continue
        priority = t.get('reading_priority')
        reason = t.get('priority_reason')
        if priority not in PRIORITIES or not reason or not t.get('reason'):
            gaps.append(r['arxiv'])
            priority = 'unclear'
        rank = t.get('reading_rank')
        if type(rank) is not int or rank < 1:
            rank_gaps.append(r['arxiv'])
            rank = None
        pending.append({'arxiv':r['arxiv'], 'title':r['title'], 'date_queue':r['date_queue'],
            'priority':priority, 'reason':reason or 'No complete model-authored priority yet; preserve unresolved.',
            'reading_rank':rank,
            'attention_reasons':r['attention_reasons'], 'primary_abstract_delivered':r['arxiv'] in delivered,
            'version':r.get('version'), 'published':r.get('published'), 'updated':r.get('updated')})
    def order(r):
        return (r['date_queue'] not in FOCUS_BUCKETS, PRIORITIES.index(r['priority']),
                r['reading_rank'] if r['reading_rank'] is not None else float('inf'), r['arxiv'])
    pending.sort(key=order)
    downloads = [e['result'] for e in events if e.get('tool') == 'download_pdf' and e.get('result', {}).get('sha256')]
    read_ids = {base_id(d.get('url')) for d in downloads} - {None}
    started_files = len({d['sha256'] for d in downloads})
    available = [r for r in pending if r['arxiv'] not in read_ids]
    selected = available[:max(0, read_cap - started_files)]
    opens = [e for e in events if e.get('tool') in ('open_page', 'click_link')]
    ranks = {}
    for r in pending:
        if r['reading_rank'] is not None:
            ranks.setdefault(r['reading_rank'], []).append(r['arxiv'])
    return {'policy':'abstract-first-v2', 'pool_count':len(pool),
        'additional_source_ids':sorted(extras),
        'reading_rank_gaps':rank_gaps,
        'duplicate_reading_ranks':{str(k):v for k,v in ranks.items() if len(v)>1},
        'full_abstracts_not_delivered':sorted(r['arxiv'] for r in pool if r['arxiv'] not in delivered),
        'priority_or_triage_gaps':gaps, 'unchanged_completed_deferred_ids':deferred,
        'ranked_unread':available, 'selected_next':selected,
        'pdfs_started':started_files, 'remaining_pdf_capacity':max(0, read_cap-started_files),
        'page_open_invocations':len(opens),
        'note':'Model-authored relation priority and explicit within-pool reading_rank schedule verification; neither is a final inclusion decision. Missing/duplicate ranks are reported, never silently inferred from keywords. Date lane and relation priority precede rank; canonical ID only breaks rank ties. Explicitly explain any override in backlog-plan.json. Additional leads need own triage plus official metadata. The source catalog and triage preserve deferred leads.'}
