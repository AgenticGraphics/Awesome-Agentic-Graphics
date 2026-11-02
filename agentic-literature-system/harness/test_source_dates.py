from datetime import datetime, timezone
from source_dates import collect_dates


def metadata(version='v2', updated='2026-10-14T10:00:00Z'):
    return {'tool': 'arxiv_metadata', 'result': {'records': [
        {'arxiv': '2610.00001', 'version': version, 'published': '2026-10-13T12:00:00Z', 'updated': updated}]}}


def test_atom_does_not_invent_intermediate_revision_dates():
    dates, conflicts = collect_dates([metadata('v4')])
    assert set(dates['2610.00001']) == {'v1', 'v4'}
    assert not conflicts


def test_source_conflicts_are_not_silently_overwritten():
    page = {'tool': 'open_page', 'result': {'url': 'https://arxiv.org/abs/2610.00001',
            'text': '1: Submission history\n2: [v2] Wed, 14 Oct 2026 11:00:00 UTC'}}
    dates, conflicts = collect_dates([metadata(), page])
    assert dates['2610.00001']['v2'] == datetime(2026, 10, 14, 10, tzinfo=timezone.utc)
    assert len(conflicts) == 1 and conflicts[0]['version'] == 'v2'


def test_failed_metadata_does_not_establish_a_date():
    dates, conflicts = collect_dates([{'tool': 'arxiv_metadata', 'result': {'error': 'unavailable'}}])
    assert not dates and not conflicts
