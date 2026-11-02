"""Compare independent artifacts, not wording. Empty sets never prove full parity."""
from paths import SKILL
import argparse, hashlib, json, sys
from pathlib import Path
from research_tools import ROOT, save
sys.path.insert(0,str(SKILL/'scripts'))
from daily_report import bucket, arxiv, norm
def ident(p):
    ids=p.get('identifiers',{})
    return ('arxiv:'+arxiv(ids['arxiv'])) if ids.get('arxiv') else ('doi:'+ids['doi']) if ids.get('doi') else 'title:'+norm(p['canonical_title'])
def compare(a,b):
    left={ident(p):p for p in a['papers']};right={ident(p):p for p in b['papers']};common=set(left)&set(right)
    diffs=[];same=0;total=0;read_same=0;read_total=0
    for k in sorted(common):
        x,y=left[k],right[k]
        for f in ('screening_status','application_families','operations'):
            xv,yv=x.get(f),y.get(f)
            if isinstance(xv,list):xv=sorted(xv)
            if isinstance(yv,list):yv=sorted(yv)
            if xv!=yv:diffs.append({'paper':k,'field':f,'codex':xv,'bvb':yv})
        if bucket(x,a)!=bucket(y,b):diffs.append({'paper':k,'field':'date_bucket','codex':bucket(x,a),'bvb':bucket(y,b)})
        for f in sorted(set(x.get('taxonomy_cells',{}))|set(y.get('taxonomy_cells',{}))):
            total+=1;xv=sorted(x.get('taxonomy_cells',{}).get(f,[]));yv=sorted(y.get('taxonomy_cells',{}).get(f,[]))
            if xv==yv:same+=1
            else:diffs.append({'paper':k,'field':'taxonomy.'+f,'codex':xv,'bvb':yv})
            if x.get('full_text_reading') and y.get('full_text_reading'):
                read_total+=1;read_same+=int(xv==yv)
    relevant=lambda run:{ident(p) for p in run['papers'] if p['screening_status'] in ('core','enabling_or_adjacent','scope_dependent')}
    lrel,rrel=relevant(a),relevant(b)
    today=lambda run:{ident(p) for p in run['papers'] if bucket(p,run)=='same_day_new'}
    updates=lambda run:{ident(p) for p in run['papers'] if bucket(p,run)=='same_day_updates'}
    target_a,target_b=today(a)|updates(a),today(b)|updates(b)
    target_common=target_a&target_b
    target_cells=[x for x in diffs if x['paper'] in target_common and x['field'].startswith('taxonomy.')]
    target_denominator=sum(len(set(left[k].get('taxonomy_cells',{}))|set(right[k].get('taxonomy_cells',{}))) for k in target_common)
    same_day=today(a)==today(b)
    frame=all(a.get(f)==b.get(f) for f in ('target_date','timezone','as_of','window_start','window_end','taxonomy_version','source_snapshot','snapshot_status','budget','evidence_policy','coverage_policy','scope_policy','history_context','reading_policy'))
    return {'same_execution_frame':frame,'codex_records':len(left),'bvb_records':len(right),'common_records':len(common),'only_codex':sorted(set(left)-set(right)),'only_bvb':sorted(set(right)-set(left)),'relevant_set_equal':lrel==rrel,'relevant_only_codex':sorted(lrel-rrel),'relevant_only_bvb':sorted(rrel-lrel),'relevant_set_jaccard':len(lrel&rrel)/len(lrel|rrel) if lrel|rrel else None,'same_day_new_equal':same_day,'same_day_new_count_codex':len(today(a)),'same_day_new_count_bvb':len(today(b)),'same_day_new_codex':sorted(today(a)),'same_day_new_bvb':sorted(today(b)),'same_day_updates_equal':updates(a)==updates(b),'same_day_updates_codex':sorted(updates(a)),'same_day_updates_bvb':sorted(updates(b)),'target_day_set_equal':target_a==target_b,'target_day_nonempty':bool(target_a and target_b),'target_day_taxonomy_cell_agreement':1-len(target_cells)/target_denominator if target_denominator else None,'taxonomy_cell_agreement':same/total if total else None,'taxonomy_cells_compared':total,'fully_read_taxonomy_cell_agreement':read_same/read_total if read_total else None,'fully_read_taxonomy_cells_compared':read_total,'differences':diffs,'non_vacuous':bool(lrel and rrel and total),'full_semantic_parity':frame and left.keys()==right.keys() and not diffs and bool(lrel and total),'note':'Same-day empty-set equality is explicitly insufficient for full semantic parity. Fully-read agreement excludes unresolved-only cells. Codex is a comparison reference, not ground truth; citations require evidence review.'}

def execution_evidence(left_path,right_path):
    summaries=[]
    for path in (left_path,right_path):
        run=Path(path).parent
        read=lambda name:json.loads((run/name).read_text()) if (run/name).exists() else None
        config=read('config.json') or {}
        specs=read('tool-specs.json')
        prompt=(run/'prompt.txt').read_text().replace(str(run.resolve()),'<RUN_DIR>') if (run/'prompt.txt').exists() else None
        summaries.append({'model':config.get('model'),'reasoning':config.get('reasoning'),'inputs':read('experiment-inputs.json'),'tool_specs_sha256':hashlib.sha256(json.dumps(specs,sort_keys=True).encode()).hexdigest() if specs else None,'normalized_prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest() if prompt else None,'schema_audit':read('audit.json'),'reading_audit':read('reading-audit.json'),'report_exists':(run/'report.md').exists(),'completion':read('agent_meta.json')})
    a,b=summaries
    valid=lambda s:bool((s['schema_audit'] or {}).get('passed') and (s['reading_audit'] or {}).get('passed') and s['report_exists'] and ((s['completion'] or {}).get('done') is True or (s['completion'] or {}).get('exit_code')==0))
    return {'codex':a,'bvb':b,'same_model_and_reasoning':bool(a['model'] and all(a[k]==b[k] for k in ('model','reasoning'))),'same_shared_tool_specs':bool(a['tool_specs_sha256'] and a['tool_specs_sha256']==b['tool_specs_sha256']),'same_normalized_task_prompt':bool(a['normalized_prompt_sha256'] and a['normalized_prompt_sha256']==b['normalized_prompt_sha256']),'same_knowledge_content':bool(a['inputs'] and b['inputs'] and a['inputs']['sha256']==b['inputs']['sha256']),'same_shared_tool_implementation':bool(a['inputs'] and b['inputs'] and a['inputs']['shared_tools_implementation_sha256']==b['inputs']['shared_tools_implementation_sha256']),'both_validated':all(valid(s) for s in summaries)}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('codex');p.add_argument('bvb');p.add_argument('--output',required=True);a=p.parse_args()
    result=compare(json.loads(Path(a.codex).read_text()),json.loads(Path(a.bvb).read_text()));result['execution_evidence']=execution_evidence(a.codex,a.bvb);save(Path(a.output),result);print(json.dumps(result,indent=2))
