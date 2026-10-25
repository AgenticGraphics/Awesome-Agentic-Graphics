#!/usr/bin/env python3
"""Offline daily-search preparation, evidence validation and report rendering. No network retrieval."""
import argparse, hashlib, json, re, sys, unicodedata
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[1]
SOURCES=['arxiv','hugging_face','openreview','official_venues','project_author_lab']
STATUSES=['complete','partial','failed','blocked','not_applicable','not_reached_within_budget']
EVENTS=['first_submission','revision','formal_publication','artifact_release']
def read(p):return json.loads(Path(p).read_text())
def write(p,obj):Path(p).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def norm(s):return re.sub(r'[^\w]+','',unicodedata.normalize('NFKC',s).casefold())
def arxiv(s):
 m=re.search(r'\b(\d{4}\.\d{4,5})(?:v\d+)?\b',s or '')
 return m.group(1) if m else (s or '').strip()
def doi(s):return re.sub(r'^https?://(?:dx\.)?doi\.org/','',(s or '').strip().lower())
def keys(p):
 ids=p.get('identifiers',{}); out={'title:'+norm(p.get('canonical_title',''))}
 if ids.get('arxiv'):out.add('arxiv:'+arxiv(ids['arxiv']))
 if ids.get('doi'):out.add('doi:'+doi(ids['doi']))
 if ids.get('openreview'):out.add('openreview:'+ids['openreview'])
 for u in p.get('canonical_urls',[]):
  u=u.strip().rstrip('/')
  if 'arxiv.org/' in u:out.add('arxiv:'+arxiv(u))
  elif 'doi.org/' in u:out.add('doi:'+doi(u))
  else:out.add('url:'+u)
 return out-{'title:'}
def aware(s):
 dt=datetime.fromisoformat(s.replace('Z','+00:00'))
 if dt.tzinfo is None:raise ValueError('timestamp must include an offset')
 return dt
def event_day(e,tz,asof):
 """Only an authoritative, precisely zoned event qualifies for the exact local day."""
 if e.get('type') not in EVENTS:raise ValueError('invalid event type')
 if not e.get('primary_url') or not e.get('evidence') or e.get('authority')!='primary':return None
 if e.get('precision')=='timestamp':
  dt=aware(e['value'])
  return dt.astimezone(tz).date().isoformat() if dt<=asof else None
 if e.get('precision')=='date':
  day=date.fromisoformat(e['value'])
  # Date-only evidence in an unknown/different zone cannot establish an exact local day.
  if e.get('timezone')!=tz.key:return None
  return day.isoformat() if day<=asof.astimezone(tz).date() else None
 return None
def corpus_status(p,corpus):
 pk=keys(p)
 for r in corpus['records']:
  rk={'title:'+norm(r['title'])}|{'arxiv:'+arxiv(x) for x in r['arxiv_ids']}
  rk|={'doi:'+doi(x) for x in r['urls'] if 'doi.org/' in x}
  rk|={'url:'+u.strip().rstrip('/') for u in r['urls']}
  if pk&rk:return 'known_discussed_paper'
 return 'new_relative_to_snapshot'
def event_key(p,e):
 value=e.get('value')
 if e.get('precision')=='timestamp':value=aware(value).astimezone(timezone.utc).isoformat()
 version=e.get('version','') if e.get('precision')!='timestamp' else ''
 return {(k,e.get('type'),value,version) for k in keys(p)}
def prior_events(history_dir,output_dir):
 seen=set();files=[]
 if history_dir:
  for path in sorted(history_dir.rglob('run.json')):
   if path.parent.resolve()==output_dir.resolve():continue
   old=read(path);files.append(str(path.resolve()))
   for p in old.get('papers',[]):
    for e in p.get('events',[]):seen.update(event_key(p,e))
 return seen,files
def prepare(args):
 out=args.output_dir;out.mkdir(parents=True,exist_ok=True)
 tz=ZoneInfo(args.timezone); target=date.fromisoformat(args.date)
 asof=aware(args.as_of) if args.as_of else datetime.now(timezone.utc)
 if target>asof.astimezone(tz).date():raise ValueError('target date is after as-of time')
 end=min(datetime.combine(target+timedelta(days=1),time(),tz),asof)
 cb=read(ROOT/'references/taxonomy-codebook.json')
 queries=read(ROOT/'references/search-query-families.json')['families']
 manifest={'target_date':args.date,'timezone':args.timezone,'as_of':asof.isoformat(),'window_start':datetime.combine(target,time(),tz).isoformat(),'window_end':end.isoformat(),'taxonomy_version':cb['version'],'source_snapshot':cb['source'],'snapshot_status':'bundled_snapshot_not_live_refreshed','budget':{'minutes':6,'search_batches':10,'primary_opens':24},'counts':{'search_batches':0,'search_queries':0,'primary_opens':0},'source_ledger':[{'family':s,'status':'not_reached_within_budget','checks':[],'limitations':'Not yet attempted'}for s in SOURCES],'query_coverage':[{'family':q['id'],'status':'not_reached_within_budget','checks':[]}for q in queries],'coverage_limits':['Search indexes and public release pages may lag; field-wide completeness is not established.'],'papers':[]}
 p=out/'run-input.json'
 if p.exists():raise ValueError('run-input.json exists; use a new output directory')
 write(p,manifest)
 lines=['# Query plan',f'Target: {args.date} ({args.timezone}); verify dates on primary sources.','Search broad recent/new listings too: exact-date strings alone miss new indexing.']
 for q in queries:lines+=['\n## '+q['id']]+['- '+s for s in q['queries']]
 lines+=['\n## Sources','- arXiv new/recent: cs.GR, cs.CV, cs.AI, cs.HC, cs.RO, cs.MM, eess.IV; record which were actually reached.','- Hugging Face daily page for target day; curation date is only a lead.','- OpenReview, official venue/proceedings pages, and official project/author/lab pages.']
 (out/'query-plan.md').write_text('\n'.join(lines)+'\n')
 print(p)
def check_time_errors(c):
 try:
  if c.get('checked_at') is None:
   if c.get('time_basis')!='recorded_only':return ['missing time_basis for unknown retrieval time']
   aware(c['recorded_at'])
  else:aware(c['checked_at'])
  if c.get('checked_through'):
   if aware(c['checked_through'])<aware(c['checked_at']):return ['reversed retrieval time bracket']
  return []
 except (ValueError,TypeError,KeyError,AttributeError):return ['invalid or missing offset-aware check/recording time']
def validate(run,cb):
 errors=[]
 def need(ok,msg):
  if not ok:errors.append(msg)
 try:
  tz=ZoneInfo(run['timezone']);target=date.fromisoformat(run['target_date']);asof=aware(run['as_of'])
  need(target<=asof.astimezone(tz).date(),'target date is in future')
 except (KeyError,ValueError) as exc:return ['execution frame: '+str(exc)]
 need(run.get('taxonomy_version')==cb['version'],'taxonomy version mismatch')
 need(run.get('source_snapshot')==cb['source'],'source snapshot mismatch; refresh bundle before classifying')
 ledger=run.get('source_ledger',[])
 need(sorted(x.get('family','') for x in ledger)==sorted(SOURCES),'all five source families must occur once')
 for s in ledger:
  need(s.get('status') in STATUSES,'invalid source status')
  if s.get('status') in ['complete','partial']:
   need(bool(s.get('checks')),s['family']+': missing inspected queries/pages')
  for c in s.get('checks',[]):
   need(all(c.get(k) for k in ['query_or_url','outcome']),s['family']+': incomplete source check')
   errors.extend(s['family']+': '+x for x in check_time_errors(c))
  if s.get('status')!='complete':need(bool(s.get('limitations')),s['family']+': missing limitation')
 expected={x['id']for x in read(ROOT/'references/search-query-families.json')['families']}
 coverage=run.get('query_coverage',[])
 need({x.get('family') for x in coverage}==expected,'query-family coverage missing')
 for q in coverage:
  need(q.get('status') in STATUSES,'invalid query coverage status')
  if q.get('status') in ['complete','partial']:need(bool(q.get('checks')),'query family marked attempted without evidence')
  for c in q.get('checks',[]):
   need(isinstance(c,dict),'query check must be an object')
   if isinstance(c,dict):
    need(bool(c.get('query_or_url')) and bool(c.get('outcome')),'incomplete query check')
    errors.extend(q['family']+': '+x for x in check_time_errors(c))
 need(bool(run.get('coverage_limits')),'coverage limits required')
 seen={}
 for i,p in enumerate(run.get('papers',[])):
  prefix=f'paper {i}: '
  for k in ['canonical_title','canonical_urls','identifiers','authors','abstract','events','source_records','screening_status','screening_reason','screening_evidence','application_families','operations','taxonomy_cells','field_evidence','contribution','limitations','taxonomy_delta','confidence']:
   need(k in p,prefix+'missing '+k)
  need(bool(p.get('canonical_title')) and bool(p.get('canonical_urls')),prefix+'missing identity')
  for k in keys(p):
   need(k not in seen,prefix+'duplicate identity; merge provenance/events with record '+str(seen.get(k)))
   seen[k]=i
  need(p.get('screening_status') in ['core','enabling_or_adjacent','scope_dependent','excluded','unresolved'],prefix+'screening status')
  need(p.get('confidence') in ['High','Medium','Low'],prefix+'confidence')
  if p.get('screening_status')!='unresolved':need(bool(p.get('screening_evidence')) and bool(p.get('screening_reason')),prefix+'screening evidence required')
  for e in p.get('events',[]):
   try:event_day(e,tz,asof)
   except (ValueError,KeyError) as exc:errors.append(prefix+'event: '+str(exc))
  for k,opts in [('application_families',cb['application_families']),('operations',cb['operations'])]:
   need(bool(p.get(k)) and isinstance(p.get(k),list) and all(v in opts for v in p[k]),prefix+'invalid '+k)
  cells=p.get('taxonomy_cells',{});need(set(cells)==set(cb['fields']),prefix+'taxonomy fields mismatch')
  for k,vs in cells.items():
   valid=cb['fields'].get(k,[])+cb['sentinels']
   need(isinstance(vs,list) and bool(vs) and all(v in valid for v in vs),prefix+'invalid labels in '+k)
   if not isinstance(vs,list):continue
   need(not(set(vs)&set(cb['sentinels'])) or len(vs)==1,prefix+'sentinel mixed with concrete labels in '+k)
   if any(v not in cb['sentinels'] for v in vs):
    evidence=p.get('field_evidence',{}).get(k,{})
    need(all(evidence.get(x) for x in ['primary_url','evidence','locator','level']),prefix+'evidence missing for '+k)
    need(evidence.get('level') in ['reported','derived'],prefix+'evidence level for '+k)
    if evidence.get('level')=='derived':need(bool(evidence.get('reasoning')),prefix+'derived reasoning missing for '+k)
 return errors
def bucket(p,run):
 tz=ZoneInfo(run['timezone']);asof=aware(run['as_of']);target=run['target_date']
 events=[e for e in p['events'] if event_day(e,tz,asof)==target and e['type']!='artifact_release']
 if p['screening_status']=='excluded':return 'excluded'
 if p['screening_status']=='unresolved':return 'unresolved'
 if any(e['type']=='first_submission' for e in events):return 'same_day_new'
 if events:return 'same_day_updates'
 verified=[event_day(e,tz,asof) for e in p['events'] if e['type']!='artifact_release']
 if any(v and v<target for v in verified):return 'late_discovery'
 return 'date_unresolved'
def esc(x):return str(x).replace('|','\\|').replace('\n',' ')
def finalize(args):
 run=read(args.input);cb=read(ROOT/'references/taxonomy-codebook.json');errors=validate(run,cb)
 out=args.output_dir;out.mkdir(parents=True,exist_ok=True)
 audit={'passed':not errors,'errors':errors,'validation_scope':'Structural/date/label checks only; primary evidence truth and retrieval recall require agent review.'}
 write(out/'audit.json',audit)
 if errors:
  print(json.dumps(audit,indent=2));return 2
 corpus=read(ROOT/'references/paper-corpus.json');seen,history_files=prior_events(args.history_dir,out);run['history_comparison']={'files':history_files,'status':'compared' if history_files else 'unavailable_first_run_or_no_history_supplied'};groups={k:[]for k in ['already_reported','same_day_new','same_day_updates','late_discovery','date_unresolved','unresolved','excluded']}
 for p in run['papers']:
  p['known_corpus_status']=corpus_status(p,corpus)
  for e in p['events']:e['prior_event_status']='already_seen' if event_key(p,e)&seen else ('not_seen_in_supplied_history' if history_files else 'history_unavailable')
  p['report_bucket']=bucket(p,run)
  qualifying=[e for e in p['events'] if event_day(e,ZoneInfo(run['timezone']),aware(run['as_of']))==run['target_date'] and e['type']!='artifact_release']
  if p['report_bucket'] in ['same_day_new','same_day_updates'] and qualifying and all(e['prior_event_status']=='already_seen' for e in qualifying):p['report_bucket']='already_reported'
  groups[p['report_bucket']].append(p)
 # Hash the actual inputs used, not a presumed latest document.
 run['input_hashes']={name:hashlib.sha256((ROOT/'references'/name).read_bytes()).hexdigest()for name in ['taxonomy-codebook.json','paper-corpus.json','source-manifest.json']}
 write(out/'run.json',run)
 (out/'papers.jsonl').write_text(''.join(json.dumps(p,ensure_ascii=False)+'\n' for p in run['papers']))
 attempted=all(s['status'] in ['complete','partial'] for s in run['source_ledger'])
 label='browser-based same-day search; documented source coverage' if attempted else 'partial browser-based same-day search; source coverage incomplete'
 lines=['# Agentic Graphics daily report',f"Date: {run['target_date']} | Timezone: {run['timezone']} | As of: {run['as_of']}",label,f"Taxonomy: {run['taxonomy_version']} | Snapshot: {run.get('snapshot_status')}",'\n## Coverage limits']+['- '+x for x in run['coverage_limits']]
 if not groups['same_day_new'] and not groups['same_day_updates'] and not groups['already_reported']:lines+=['\nNo qualifying same-day Agentic Graphics paper was verified in the browsed source set.','Coverage is limited to the sources and queries below; unpublished or unindexed papers may be missing.']
 for name,ps in groups.items():
  lines+=['\n## '+name+f' ({len(ps)})']
  for p in ps:
   lines+=[f"\n### [{p['canonical_title']}]({p['canonical_urls'][0]})",f"{p['screening_status']} | {p['confidence']} | {p['known_corpus_status']}", 'Application: '+', '.join(p['application_families'])+'; operations: '+', '.join(p['operations']),p['contribution'],'Scope: '+p['screening_reason'],'Limits: '+p['limitations'],'\n| Taxonomy field | Values | Evidence |','|---|---|---|']
   for k,v in p['taxonomy_cells'].items():
    e=p['field_evidence'].get(k,{});lines.append('| '+k+' | '+esc(', '.join(v))+' | '+esc(e.get('evidence',''))+(f" ([source]({e['primary_url']}), {esc(e['locator'])})" if e.get('primary_url') else '')+' |')
   for extra in ['nearest_known_papers','artifact_links','evaluation','next_action']:
    if p.get(extra):lines+=['\n'+extra+': '+json.dumps(p[extra],ensure_ascii=False)]
   lines+=['\nEvents: '+json.dumps(p['events'],ensure_ascii=False),'Taxonomy deltas: '+json.dumps(p['taxonomy_delta'],ensure_ascii=False)]
 lines+=['\n## Application index','| Application | Papers |','|---|---|']
 for family in cb['application_families']:
  matches=[p for p in run['papers'] if family in p.get('application_families',[]) and p['screening_status']!='excluded']
  lines.append('| '+family+' | '+('; '.join('['+esc(p['canonical_title'])+']('+p['canonical_urls'][0]+') ['+p['report_bucket']+']' for p in matches) or 'None verified in this run')+' |')
 lines+=['\n## Source ledger','| Source | Status | Checked pages / queries | Limitations |','|---|---|---|---|']
 for s in run['source_ledger']:lines.append('| '+s['family']+' | '+s['status']+' | '+esc(json.dumps(s['checks'],ensure_ascii=False))+' | '+esc(s.get('limitations',''))+' |')
 lines+=['\n## Query coverage']+['- '+q['family']+': '+q['status']+'; '+esc(q['checks'])for q in run['query_coverage']]
 (out/'report.md').write_text('\n'.join(lines)+'\n')
 print(json.dumps({'passed':True,'counts':{k:len(v)for k,v in groups.items()},'report':str((out/'report.md').resolve())},indent=2));return 0
def main():
 p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
 a=sub.add_parser('prepare');a.add_argument('--date',required=True);a.add_argument('--timezone',default='America/Chicago');a.add_argument('--as-of');a.add_argument('--output-dir',type=Path,required=True)
 a=sub.add_parser('finalize');a.add_argument('--input',type=Path,required=True);a.add_argument('--output-dir',type=Path,required=True);a.add_argument('--history-dir',type=Path)
 args=p.parse_args()
 try:return prepare(args) if args.command=='prepare' else finalize(args)
 except (ValueError,KeyError,TypeError) as exc:print(str(exc),file=sys.stderr);return 2
if __name__=='__main__':sys.exit(main())
