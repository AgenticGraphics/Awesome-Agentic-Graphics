import pytest
from pdf_search import search_pdf


def fixture(tmp_path):
    import pymupdf
    path=tmp_path/'synthetic.pdf'
    doc=pymupdf.open()
    doc.new_page().insert_text((50,50),'Related work uses ModelX.\nMemory is discussed elsewhere.')
    doc.new_page().insert_text((50,50),'Implementation: our task agent uses ModelY.\nShort term memory spans calls.')
    doc.save(path);doc.close()
    return path


def test_pdf_search_preserves_context_page_and_hash(tmp_path):
    path=fixture(tmp_path);result=search_pdf(path,['ModelY','short term memory'])
    assert result['results']['ModelY']['matches'][0]['page']==2
    assert 'task agent' in result['results']['ModelY']['matches'][0]['excerpt']
    assert result['results']['short term memory']['total_matches']==1
    assert len(result['sha256'])==64 and result['total_pages']==2
    assert not (tmp_path/'tool-events.jsonl').exists()


def test_pdf_search_is_literal_and_reports_absence_without_inference(tmp_path):
    result=search_pdf(fixture(tmp_path),['Model.*','unmentioned phrase'])
    assert all(x['total_matches']==0 for x in result['results'].values())
    assert 'screening_status' not in result


def test_pdf_search_bounds_results(tmp_path):
    result=search_pdf(fixture(tmp_path),['model'],max_matches=1)
    assert result['results']['model']['total_matches']==2
    assert len(result['results']['model']['matches'])==1
    with pytest.raises(ValueError):search_pdf('unused.pdf',[''])
