"""Bounded provider recovery; preserves the original run deadline across retries.

Only model requests are retried here. No tool or mutation is replayed. A durable
cooldown stops a freshly resumed process from immediately hammering the provider.
"""
import json
import random
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

TRANSIENT = ('overloaded', 'at capacity', 'timeout', 'connection', 'rate_limit',
             'ratelimit', 'rate limit', 'serviceunavailable', 'service unavailable',
             'temporarily unavailable', 'auth_unavailable', '502', '503', '504')


def retryable(error):
    status = getattr(error, 'status_code', None)
    response = getattr(error, 'response', None)
    status = status or getattr(response, 'status_code', None)
    if status in (400, 401, 403, 404, 422):
        return False
    return status in (408, 429, 500, 502, 503, 504) or any(x in str(error).lower() for x in TRANSIENT)


def retry_after(error, wall_now):
    response = getattr(error, 'response', None)
    headers = getattr(response, 'headers', None) or getattr(error, 'headers', {}) or {}
    value = next((v for k, v in headers.items() if str(k).lower() == 'retry-after'), None)
    if value is None:
        return 0.0
    try:
        return max(0.0, float(value))
    except (ValueError, TypeError):
        try:
            parsed = parsedate_to_datetime(str(value))
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return max(0.0, parsed.timestamp() - wall_now)
        except (ValueError, TypeError, OverflowError):
            return 0.0


def complete_with_recovery(client, system, messages, *, deadline, state_path,
                           event, save, monotonic=None, wall=None, sleep=None,
                           jitter=None, max_attempts=6, max_recovery_seconds=180):
    mono = monotonic or time.monotonic
    wall = wall or time.time
    sleep = sleep or time.sleep
    jitter = jitter or (lambda: random.uniform(0, 1))
    state_path = Path(state_path)
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    recovery_deadline = min(deadline, mono() + max_recovery_seconds)
    request_reserve = 30

    def persist(delay, failures, error):
        state.update(not_before_epoch=wall() + delay, consecutive_failures=failures,
                     retryable=retryable(error),
                     error=type(error).__name__ + ': ' + str(error),
                     updated_at=datetime.fromtimestamp(wall(), timezone.utc).isoformat())
        save(state_path, state)

    def wait(delay, label):
        if delay + request_reserve > min(deadline, recovery_deadline) - mono():
            event({'tool': 'provider_retry_skipped', 'reason': 'original_budget_or_retry_window',
                   'requested_delay_seconds': delay, 'remaining_seconds': max(0, deadline - mono())})
            return False
        event({'tool': 'provider_backoff', 'reason': label, 'delay_seconds': delay})
        # Small chunks keep shutdown responsive and never oversleep the deadline.
        until = mono() + delay
        while mono() < until:
            sleep(min(5, until - mono()))
        return True

    cooldown = max(0, state.get('not_before_epoch', 0) - wall())
    if cooldown and not wait(cooldown, 'persisted_cooldown'):
        raise TimeoutError('Provider cooldown cannot fit in the original remaining budget')
    for attempt in range(1, max_attempts + 1):
        remaining = deadline - mono()
        if remaining <= 0:
            raise TimeoutError('Original model-request budget exhausted')
        client.timeout = max(.001, min(180, remaining, recovery_deadline - mono()))
        try:
            result = client.complete(system, messages)
        except Exception as error:
            transient = retryable(error)
            failures = state.get('consecutive_failures', 0) + 1
            delay = max(min(60, 5 * 2 ** min(failures - 1, 4)) + jitter(), retry_after(error, wall()))
            persist(delay if transient else 0, failures, error)
            event({'tool': 'provider_error', 'attempt': attempt, 'retryable': transient,
                   'error': state['error'], 'next_retry_after_seconds': delay if transient else None})
            if not transient or attempt == max_attempts or not wait(delay, 'transient_provider_error'):
                raise
        else:
            save(state_path, {'not_before_epoch': 0, 'consecutive_failures': 0,
                              'last_success_at': datetime.fromtimestamp(wall(), timezone.utc).isoformat()})
            return result
