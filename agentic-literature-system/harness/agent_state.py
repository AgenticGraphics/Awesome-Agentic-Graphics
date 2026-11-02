"""Own-run journal recovery and evidence compaction; never reads another run."""
import json
from pathlib import Path


def archive_context_observation(run_dir, text):
    """Keep exact prior tool text in a content-addressed, atomically saved file."""
    import hashlib
    import os
    import tempfile
    raw=text.encode('utf-8');sha=hashlib.sha256(raw).hexdigest()
    directory=Path(run_dir)/'context-observations';directory.mkdir(parents=True,exist_ok=True)
    path=directory/(sha+'.json')
    if not path.exists() or path.read_bytes()!=raw:
        fd,name=tempfile.mkstemp(prefix='.observation-',dir=directory)
        try:
            with os.fdopen(fd,'wb') as stream:
                stream.write(raw);stream.flush();os.fsync(stream.fileno())
            os.replace(name,path)
        finally:
            if os.path.exists(name):os.unlink(name)
    return {'observation_path':str(path),'observation_sha256':sha}


def compact_archived_status(observation, run_dir, original):
    """Summarize bookkeeping only; actionable gaps and failures remain inline."""
    tool=observation['tool'];old=observation['result'];out=dict(old)
    bulky=('observed_arxiv_ids','metadata_resolved_arxiv_ids',
           'metadata_resolved_without_saved_decision','title_hint_leads_without_saved_decision') if tool=='research_status' else ('title_review_hints',)
    for key in bulky:
        if isinstance(out.get(key),list):
            values=out.pop(key);out[key+'_count']=len(values)
    return {'tool':tool,'compacted_bookkeeping':True,'result':out,
            **archive_context_observation(run_dir,original),
            'note':'Historical bookkeeping observation, already delivered once. Full lists are in observation_path and the original tool log. Counts are not scope decisions; unread leads remain unresolved. Reopen the saved JSON or call the tool again for full details.'}


def read_events(path):
    """A killed writer may leave a partial final line; never ignore interior damage."""
    if not Path(path).exists():
        return []
    text = Path(path).read_bytes()
    lines = text.splitlines()
    events = []
    for index, line in enumerate(lines):
        try:
            events.append(json.loads(line))
        except (json.JSONDecodeError, UnicodeDecodeError):
            if index != len(lines) - 1 or text.endswith(b'\n'):
                raise
    return events


def append_event(path, event):
    """Serialize concurrent writers; preserve a crash tail before repairing it."""
    import fcntl
    import os
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+b') as stream:
        fcntl.flock(stream.fileno(), fcntl.LOCK_EX)
        stream.seek(0, 2)
        size = stream.tell()
        if size:
            stream.seek(size - 1)
            if stream.read(1) != b'\n':
                # This slow recovery path runs only after an interrupted writer.
                stream.seek(0)
                content = stream.read()
                boundary = content.rfind(b'\n') + 1
                tail = content[boundary:]
                try:
                    json.loads(tail)
                except (json.JSONDecodeError, UnicodeDecodeError):
                    with path.with_suffix('.interrupted-tail').open('ab') as backup:
                        backup.write(tail + b'\n')
                    stream.truncate(boundary)
                else:
                    stream.seek(0, 2)
                    stream.write(b'\n')
        stream.seek(0, 2)
        stream.write((json.dumps(event, ensure_ascii=False) + '\n').encode())
        stream.flush()
        os.fsync(stream.fileno())
        fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def completed_readings(run_dir):
    """Only durable, validated checkpoints count, including calls made from scripts."""
    run_dir = Path(run_dir)
    result = {}
    for path in (run_dir / 'checkpoints').glob('*.json'):
        record = json.loads(path.read_text())
        paper = record['paper']
        sha = paper.get('full_text_reading', {}).get('sha256')
        if sha:
            result[sha] = {'path': str(path), 'paper': paper}
    return result


def pending_reading(run_dir):
    completed = completed_readings(run_dir)
    pending = None
    for event in read_events(Path(run_dir) / 'tool-events.jsonl'):
        if event.get('tool') == 'pdf_read_receipt' and event.get('sha256') not in completed:
            pending = event['path']
    return pending


def compact_observations(messages, run_dir):
    completed = completed_readings(run_dir)
    from candidate_catalog import base_id,source_provenance
    triage_path=Path(run_dir)/'triage.json'
    try:
        triage=json.loads(triage_path.read_text()) if triage_path.exists() else []
        if isinstance(triage,dict):triage=triage.get('candidates',triage.get('papers',[]))
        decisions={base_id(p.get('id') or p.get('arxiv') or p.get('observed_source_url')):p
                   for p in triage if isinstance(p,dict) and p.get('triage_status') in
                   ('retain','needs_full_read','reject_obvious') and isinstance(p.get('reason'),str) and p['reason'].strip()}
    except (ValueError,TypeError,OSError):
        decisions={}  # Never discard abstracts when the saved decision is unreadable.
    # Newly returned observations must reach the model once, including explicit
    # reopens of already-triaged abstracts or checkpointed PDFs.
    eligible=messages[:-1] if messages and messages[-1].get('role')=='user' else messages
    for message in eligible:
        if message.get('role')!='user':continue  # Preserve assistant reasoning-replay identity.
        for part in message['parts']:
            if part.get('kind') != 'text':
                continue
            try:
                observation = json.loads(part['text'])
            except (ValueError, TypeError):
                continue
            if not isinstance(observation, dict):
                continue
            old = observation.get('result', {})
            if not isinstance(old, dict):
                continue
            sha = old.get('sha256')
            if observation.get('compacted_bookkeeping'):
                continue
            if observation.get('tool') in ('research_status','arxiv_scan') and len(part['text'])>12000:
                part['text']=json.dumps(compact_archived_status(observation,run_dir,part['text']))
            elif observation.get('tool')=='candidate_catalog' and old.get('operation')=='read':
                records=[];changed=False
                for row in old.get('records',[]):
                    decision=decisions.get(base_id(row.get('arxiv')))
                    if decision:
                        compact={k:v for k,v in row.items() if k in ('arxiv','title','date_queue','version_history_required')}
                        compact.update(triage_compacted=True,triage_status=decision['triage_status'],
                                       triage_reason=decision['reason'])
                        changed=changed or compact!=row;records.append(compact)
                    else:records.append(row)
                if changed:
                    provenance=old.get('metadata_sources') or source_provenance(old.get('records',[]))
                    needed={row.get('metadata_sha256') for row in records if not row.get('triage_compacted')}
                    compact=dict(old,records=records,saved_triage_path=str(triage_path),
                        metadata_sources=[source for source in provenance if source.get('sha256') in needed],
                        raw_observation_log=str(Path(run_dir)/'tool-events.jsonl'),
                        compaction_note='Only abstracts with an explicit saved own-run triage decision were compacted. Full abstracts remain in catalog_path and the raw log; candidate_catalog can reopen them. Untriaged records remain intact.')
                    compact.update({key:old[key] for key in ('observation_path','observation_sha256') if key in old})
                    if 'observation_path' not in compact:
                        compact.update(archive_context_observation(run_dir,part['text']))
                    part['text']=json.dumps({'tool':'candidate_catalog','compacted_after_triage':True,'result':compact})
            elif observation.get('tool') == 'read_pdf' and sha in completed:
                checkpoint = completed[sha]
                paper = checkpoint['paper']
                part['text'] = json.dumps({'tool': 'read_pdf', 'compacted_after_checkpoint': True,
                    'sha256': sha, 'validated_checkpoint': checkpoint['path'],
                    'canonical_title': paper['canonical_title'], 'screening_status': paper['screening_status'],
                    'contribution': paper['contribution'], 'limitations': paper['limitations'],
                    'note': 'Full evidence and taxonomy are in the checkpoint; original PDF delivery is in tool-events.jsonl.'})
            elif completed and observation.get('tool') == 'arxiv_metadata' and not observation.get('compacted_after_checkpoint'):
                compact = {k: v for k, v in old.items() if k != 'records'}
                compact['records'] = [{k: v for k, v in r.items() if k not in ('abstract', 'authors', 'links')}
                                      for r in old.get('records', [])]
                compact['raw_observation_log'] = str(Path(run_dir) / 'tool-events.jsonl')
                part['text'] = json.dumps({'tool': 'arxiv_metadata', 'compacted_after_checkpoint': True, 'result': compact})
            elif completed and observation.get('tool') in ('open_page', 'arxiv_recent', 'hf_daily', 'web_search') and len(part['text']) > 7000 and not observation.get('compacted_after_checkpoint'):
                compact = {k: v for k, v in old.items() if k not in ('text', 'links', 'actions')}
                compact['text_excerpt'] = old.get('text', '')[:3000]
                compact['raw_observation_log'] = str(Path(run_dir) / 'tool-events.jsonl')
                part['text'] = json.dumps({'tool': observation['tool'], 'compacted_after_checkpoint': True, 'result': compact})


def recover_interrupted_batch(run_dir):
    """Do not replay possibly executed mutations after an ambiguous interruption."""
    path = Path(run_dir) / 'turn-journal.json'
    journal = json.loads(path.read_text()) if path.exists() else {'calls': []}
    results = []
    for index, call in enumerate(journal['calls']):
        result_path = Path(run_dir) / 'tool-results' / f"{journal['turn']}-{index}.json"
        if call.get('state') == 'completed' and result_path.exists():
            result = json.loads(result_path.read_text())
        else:
            result = {'error': 'Interrupted tool batch: execution outcome is unknown or call was not started. No automatic replay was performed. Inspect research_status and your own saved files before deciding the next action.', 'journal_state': call.get('state', 'planned')}
        results.append({'tool': call['name'], 'result': result})
    return results or [{'tool': 'harness_recovery', 'result': {'error': 'No completed tool journal. Inspect your own saved state; no call was replayed.'}}]
