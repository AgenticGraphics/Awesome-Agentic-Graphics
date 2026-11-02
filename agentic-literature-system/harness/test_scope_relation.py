import json
import pytest
import research_tools as module


def context(tmp_path,monkeypatch):
    monkeypatch.setattr(module,'ROOT',tmp_path)
    run=tmp_path/'run';run.mkdir()
    (run/'frozen-frame.json').write_text(json.dumps({'evidence_policy':'version-pinned-pdf-v1','scope_policy':'graphics-action-borderline-v1'}))
    paper={'screening_status':'core','analysis_target':'Synthetic task-time controller.',
           'field_evidence':{key:{'primary_url':'https://example.org/paper.pdf','locator':'p.2','evidence':'Synthetic evidence fixture.'} for key in module.CODEBOOK['fields']}}
    return module.ResearchTools(run),paper


def relation(status):
    return {'controller':'Synthetic controller','action_or_decision':'Select a render operation',
            'graphics_target':'Synthetic scene','primary_url':'https://example.org/paper.pdf',
            'locator':'p.2','evidence':'Synthetic tool selection description.','evidence_status':status}


def test_core_requires_explicit_action_relation(tmp_path,monkeypatch):
    tools,paper=context(tmp_path,monkeypatch)
    assert any('agent_graphics_relation' in error for error in tools._annotation_errors(paper))


def test_uncertain_relation_cannot_silently_become_core(tmp_path,monkeypatch):
    tools,paper=context(tmp_path,monkeypatch);paper['agent_graphics_relation']=relation('uncertain')
    assert any('demonstrated' in error for error in tools._annotation_errors(paper))
    paper['screening_status']='scope_dependent'
    assert tools._annotation_errors(paper)==[]


def test_explicitly_enabling_relation_keeps_separate_scope(tmp_path,monkeypatch):
    tools,paper=context(tmp_path,monkeypatch)
    paper.update(screening_status='enabling_or_adjacent',agent_graphics_relation=relation('explicit_enabling'))
    assert tools._annotation_errors(paper)==[]
    paper['agent_graphics_relation']['locator']=''
    assert any('located primary evidence' in error for error in tools._annotation_errors(paper))


def test_legacy_frame_does_not_rewrite_old_scope_requirements(tmp_path,monkeypatch):
    tools,paper=context(tmp_path,monkeypatch);tools.execution_frame.pop('scope_policy')
    assert tools._annotation_errors(paper)==[]


def test_action_relation_cannot_cite_a_different_paper(tmp_path,monkeypatch):
    tools,paper=context(tmp_path,monkeypatch)
    paper.update(identifiers={'arxiv':'2610.12345'},agent_graphics_relation=relation('demonstrated'))
    paper['agent_graphics_relation']['primary_url']='https://arxiv.org/pdf/2610.99999v1'
    assert any('different paper identity' in error for error in tools._annotation_errors(paper))


def test_page_audit_checks_both_range_endpoints_and_comma_lists():
    from audit_evidence import cited_page_numbers
    assert cited_page_numbers('Section 3, pp. 2–4, 8, 10-12; Fig. 99')==[2,4,8,10,12]
    assert cited_page_numbers('Appendix B p. 17')==[17]
