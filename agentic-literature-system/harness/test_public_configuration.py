import importlib.util
from pathlib import Path
import pytest
from runtime_config import api_base, api_key, model_name, search_model
from check_release import inspect_text
from research_tools import ResearchTools, ROOT, SKILL


def test_configuration_is_caller_supplied(monkeypatch):
    for key in ('AGENT_MODEL', 'SEARCH_MODEL', 'OPENAI_API_KEY', 'OPENAI_BASE_URL'):
        monkeypatch.delenv(key, raising=False)
    assert api_base() == 'https://api.openai.com/v1'
    with pytest.raises(ValueError):api_key()
    with pytest.raises(ValueError):model_name()
    monkeypatch.setenv('AGENT_MODEL', 'synthetic-model')
    assert search_model() == 'synthetic-model'
    monkeypatch.setenv('SEARCH_MODEL', 'synthetic-search')
    assert search_model() == 'synthetic-search'
    monkeypatch.setenv('OPENAI_BASE_URL', 'https://example.invalid/v1/')
    assert api_base() == 'https://example.invalid/v1'
    monkeypatch.setenv('OPENAI_BASE_URL', 'https://example.invalid/v1?token=synthetic')
    with pytest.raises(ValueError):api_base()


def test_sibling_skill_can_be_read_but_not_modified():
    tools=ResearchTools(ROOT/'runs/test-public-paths')
    assert tools.path('skill/SKILL.md') == (SKILL/'SKILL.md').resolve()
    assert tools.read_file('skill/SKILL.md')['total_lines']>0
    with pytest.raises(ValueError):tools.write_file('skill/SKILL.md','changed')
    with pytest.raises(ValueError):tools.path('skill/../../outside.txt')
    tools.close()


def test_release_scan_reports_categories_without_values():
    samples=['/'+'Users/'+ 'synthetic-user/project', 'https://docs.google.com/'+'document/d/'+'synthetic-id', 'sk-'+('x'*30), '.'.join(['192','168','42','8'])]
    for sample in samples:
        result=inspect_text(sample)
        assert result and sample not in str(result)
    assert not inspect_text('OPENAI_API_KEY=\nhttps://arxiv.org/abs/2610.00001')


def test_unknown_pricing_fails_closed_and_configured_rates_work(monkeypatch):
    from responses_model import _manual_cost, usage_cost
    for key in ('INPUT_COST_PER_MILLION','OUTPUT_COST_PER_MILLION'):
        monkeypatch.delenv(key,raising=False)
    with pytest.raises(ValueError,match='Unknown model pricing'):_manual_cost('synthetic-unpriced-model',1,1)
    monkeypatch.setenv('INPUT_COST_PER_MILLION','2')
    monkeypatch.setenv('OUTPUT_COST_PER_MILLION','8')
    assert _manual_cost('synthetic-model',1000,1000)==pytest.approx(.01)
    assert usage_cost('synthetic-model',{'input_tokens':1000,'output_tokens':1000})[1]=='configured_uncached_rates'
    monkeypatch.setenv('OUTPUT_COST_PER_MILLION','nan')
    with pytest.raises(ValueError):_manual_cost('synthetic-model',1,1)
