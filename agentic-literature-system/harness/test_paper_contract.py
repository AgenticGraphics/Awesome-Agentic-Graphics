import copy,json
from pathlib import Path
from paper_contract import contract_errors,build_paper_schema

def fixture():
    cb=json.loads((Path(__file__).parent.parent/'skill/references/taxonomy-codebook.json').read_text())
    paper={'canonical_title':'Synthetic contract fixture','canonical_urls':['https://example.org/paper'],'identifiers':{},'authors':[],
        'abstract':'Fixture, not a research finding.','events':[],'source_records':[],'screening_status':'unresolved','screening_reason':'Not read',
        'screening_evidence':[],'application_families':[cb['application_families'][0]],'operations':[cb['operations'][0]],
        'taxonomy_cells':{k:['Unclear'] for k in cb['fields']},'field_evidence':{},'contribution':'Not established',
        'limitations':'Full reading pending','taxonomy_delta':[],'confidence':'Low'}
    return cb,paper

def test_record_contract_accepts_uncertainty_without_inventing_labels():
    cb,p=fixture();assert not contract_errors(p,cb)

def test_record_contract_exposes_the_observed_limitations_type_error():
    cb,p=fixture();p['limitations']=['pending']
    errors=contract_errors(p,cb);assert any(e.startswith('limitations:') for e in errors)

def test_record_contract_rejects_unknown_facets_and_missing_taxonomy_fields():
    cb,p=fixture();p['application_families']=['invented family'];p['taxonomy_cells'].pop(next(iter(cb['fields'])))
    errors=contract_errors(p,cb)
    assert any(e.startswith('application_families') for e in errors)
    assert any(e.startswith('taxonomy_cells') for e in errors)

def test_contract_is_valid_json_schema():
    from jsonschema import Draft202012Validator
    cb,_=fixture();Draft202012Validator.check_schema(build_paper_schema(cb))
