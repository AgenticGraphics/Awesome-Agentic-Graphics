import pytest,litellm
import importlib.util
from pathlib import Path
_spec=importlib.util.spec_from_file_location('responses_cost_v4_adapter',Path(__file__).with_name('responses_model.py'))
_adapter=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(_adapter)
usage_cost=_adapter.usage_cost


def test_cached_tokens_use_same_estimator_as_upstream_bvb():
    usage={'input_tokens':237933,'output_tokens':1637,'input_tokens_details':{'cached_tokens':233344}}
    cost,basis,upper=usage_cost('gpt-6-astra',usage)
    reference=litellm.completion_cost(completion_response={'model':'gpt-6-astra',
        'usage':{'prompt_tokens':237933,'completion_tokens':1637,'total_tokens':239570,
                 'prompt_tokens_details':{'cached_tokens':233344}},
        'choices':[{'index':0,'message':{'role':'assistant','content':''},'finish_reason':'stop'}]})
    assert cost==pytest.approx(reference) and cost<upper
    assert basis=='litellm_cache_aware_usage'


def test_missing_price_fallback_is_explicit(monkeypatch):
    monkeypatch.setattr(litellm,'completion_cost',lambda **kwargs:(_ for _ in ()).throw(ValueError('synthetic missing metadata')))
    cost,basis,upper=usage_cost('gpt-6-astra',{'input_tokens':100,'output_tokens':10})
    assert cost==upper and cost>0 and basis=='manual_uncached_fallback'
