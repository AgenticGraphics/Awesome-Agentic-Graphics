import json
from types import SimpleNamespace
import pytest
from provider_retry import complete_with_recovery, retryable, retry_after


class Clock:
    def __init__(self):
        self.now = 0.0
        self.sleeps = []
    def mono(self): return self.now
    def wall(self): return 1800000000 + self.now
    def sleep(self, seconds):
        assert 0 <= seconds <= 5
        self.sleeps.append(seconds)
        self.now += seconds


def invoke(tmp_path, model, clock, seconds=120, **kwargs):
    events = []
    def save(path, data): path.write_text(json.dumps(data))
    return complete_with_recovery(model, '', [], deadline=clock.now + seconds,
        state_path=tmp_path/'retry.json', event=events.append, save=save,
        monotonic=clock.mono, wall=clock.wall, sleep=clock.sleep,
        jitter=lambda: 0, **kwargs)


def test_recovers_outage_longer_than_old_six_second_window(tmp_path):
    clock = Clock()
    class Model:
        calls = 0
        def complete(self, *args):
            self.calls += 1
            if clock.now < 12:
                raise RuntimeError('auth_unavailable: upstream server_is_overloaded')
            return 'DONE', {'cost': .01}
    model = Model()
    assert invoke(tmp_path, model, clock)[0] == 'DONE'
    assert clock.now == 15 and model.calls == 3
    assert json.loads((tmp_path/'retry.json').read_text())['consecutive_failures'] == 0


def test_permanent_auth_error_is_not_retried(tmp_path):
    clock = Clock()
    class Model:
        def complete(self, *args):
            error = RuntimeError('invalid API key')
            error.status_code = 401
            raise error
    with pytest.raises(RuntimeError, match='invalid API key'):
        invoke(tmp_path, Model(), clock)
    assert not clock.sleeps
    assert not json.loads((tmp_path/'retry.json').read_text())['retryable']


def test_long_retry_after_is_persisted_and_not_bypassed_on_resume(tmp_path):
    clock = Clock()
    class Model:
        calls = 0
        def complete(self, *args):
            self.calls += 1
            error = RuntimeError('rate limit')
            error.status_code = 429
            error.response = SimpleNamespace(headers={'Retry-After': '300'})
            raise error
    model = Model()
    with pytest.raises(RuntimeError, match='rate limit'): invoke(tmp_path, model, clock)
    with pytest.raises(TimeoutError, match='cooldown'): invoke(tmp_path, model, clock)
    assert model.calls == 1 and not clock.sleeps


def test_repeated_failure_respects_remaining_original_budget(tmp_path):
    clock = Clock()
    class Model:
        calls = 0
        def complete(self, *args):
            self.calls += 1
            raise RuntimeError('Selected model is at capacity')
    model = Model()
    with pytest.raises(RuntimeError): invoke(tmp_path, model, clock, seconds=65)
    assert clock.now == 35 and model.calls == 4
    with pytest.raises(TimeoutError): invoke(tmp_path, model, clock, seconds=30)
    assert clock.now == 35 and model.calls == 4


def test_retry_request_timeout_cannot_extend_retry_window(tmp_path):
    clock = Clock()
    class Model:
        timeouts = []
        def complete(self, *args):
            self.timeouts.append(self.timeout)
            clock.now += 20 if len(self.timeouts) == 1 else self.timeout
            raise RuntimeError('timeout')
    model = Model()
    with pytest.raises(RuntimeError): invoke(tmp_path, model, clock, seconds=1200, max_recovery_seconds=70)
    assert clock.now == 70 and model.timeouts == [70,45]


def test_retry_after_http_date_and_status_classification():
    error = RuntimeError('busy')
    error.response = SimpleNamespace(status_code=503,headers={'retry-after':'Wed, 21 Oct 2015 07:28:00 GMT'})
    assert retryable(error)
    assert retry_after(error,1445412470) == 10
    error.response.headers = {'Retry-After': 'garbage'}
    assert retry_after(error,0) == 0
