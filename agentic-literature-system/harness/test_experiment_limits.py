import json
import uuid
import pytest
from prepare_experiment import prepare
from compare import compare


def test_extended_budget_is_explicit_frozen_and_reflected_in_prompt():
    run=prepare('test-extended-budget-'+uuid.uuid4().hex,'2026-10-13','2026-10-15T07:00:53+00:00',
                minutes=45,read_candidates=30,primary_opens=80)
    frame=json.loads((run/'frozen-frame.json').read_text())
    data=json.loads((run/'run-input.json').read_text())
    assert frame['budget']==data['budget']=={'minutes':45,'read_candidates':30,'primary_opens':80,'search_batches':10}
    prompt=(run/'prompt.txt').read_text()
    assert 'Budget: 45 minutes' in prompt and '30 full-paper reads' in prompt
    assert 'override the bounded-pass defaults' in prompt


def test_budget_changes_cannot_pass_equal_execution_frame():
    a={'papers':[],'budget':{'minutes':20,'read_candidates':10}}
    b={'papers':[],'budget':{'minutes':45,'read_candidates':30}}
    assert not compare(a,b)['same_execution_frame']
    assert not compare(a,b)['full_semantic_parity']


@pytest.mark.parametrize('kwargs',[{'minutes':0},{'read_candidates':-1},{'primary_opens':0}])
def test_invalid_experiment_budgets_rejected_before_preparation(kwargs):
    with pytest.raises(ValueError,match='positive'):prepare('unused','2026-10-13','2026-10-15T07:00:53+00:00',**kwargs)
