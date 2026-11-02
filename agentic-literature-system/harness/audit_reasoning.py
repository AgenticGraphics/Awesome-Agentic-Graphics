"""Read-only review flags; never infer correct labels or alter completion status."""
import argparse,collections,json,re
from pathlib import Path


def audit(run):
    path=Path(run)/'run.json'
    if not path.exists():path=Path(run)/'run-input.json'
    records=json.loads(path.read_text()).get('papers',[])
    flags=[];derived=0
    for paper in records:
        if paper.get('screening_status') not in ('core','enabling_or_adjacent','scope_dependent'):continue
        groups=collections.defaultdict(list)
        for field,evidence in paper.get('field_evidence',{}).items():
            if not isinstance(evidence,dict) or evidence.get('level')!='derived':continue
            if not set(paper.get('taxonomy_cells',{}).get(field,[]))-{'Not Reported','Not Applicable','Unclear'}:continue
            derived+=1
            reasoning=re.sub(r'\s+',' ',evidence.get('reasoning','')).strip().lower()
            if reasoning:groups[reasoning].append(field)
        for text,fields in groups.items():
            if len(fields)>=4:
                flags.append({'paper':paper.get('identifiers') or paper['canonical_title'],
                              'fields':fields,'reused_reasoning':text,
                              'review_reason':'Identical derivation explanation across at least four distinct axes; inspect whether each label has its own evidence-to-label bridge.'})
    return {'run':str(run),'derived_fields':derived,'reused_explanation_flags':flags,
            'scope':'Concrete derived labels of retained papers only; unresolved and sentinel-only fields are excluded.',
            'warning':'A review flag is not proof of an incorrect label. This audit does not certify semantic quality or change a run result.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('run');parser.add_argument('--output');args=parser.parse_args()
    result=audit(args.run)
    if args.output:Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'derived_fields':result['derived_fields'],'review_flags':len(result['reused_explanation_flags'])}))
