"""Simple in-process sliding-window rate limiter for unauthenticated endpoints.

Keyed by (endpoint, client_ip).  No external dependencies — suitable for a
single-server deployment.  For multi-process/multi-host deployments, replace
with a Redis-backed solution (e.g. flask-limiter + redis).
"""
from __future__ import annotations

import threading
import time
from collections import deque
from typing import Deque

_buckets: dict[str, Deque[float]] = {}
_lock = threading.Lock()


def _client_ip() -> str:
    from flask import request

    forwarded = request.headers.get("X-Forwarded-For", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.remote_addr or "unknown"


def check(endpoint: str, hourly: int, daily: int) -> tuple[bool, str]:
    """Record the current request and return ``(allowed, error_message)``.

    If the caller is within both the hourly and daily caps the timestamp is
    appended and ``(True, "")`` is returned.  Otherwise the request is NOT
    recorded and ``(False, message)`` is returned.
    """
    ip = _client_ip()
    key = f"{endpoint}:{ip}"
    now = time.monotonic()
    hour_ago = now - 3600
    day_ago = now - 86400

    with _lock:
        bucket = _buckets.get(key)
        if bucket is None:
            bucket = deque()
            _buckets[key] = bucket

        # Evict entries older than 24 h to bound memory use
        while bucket and bucket[0] < day_ago:
            bucket.popleft()

        hour_count = sum(1 for t in bucket if t >= hour_ago)
        day_count = len(bucket)

        if hour_count >= hourly:
            return False, f"Rate limit exceeded: {hourly} requests/hour."
        if day_count >= daily:
            return False, f"Rate limit exceeded: {daily} requests/day."

        bucket.append(now)
        return True, ""


def cleanup_expired() -> None:
    """Remove buckets whose last entry is older than 24 h.

    Intended to be called from the existing cleanup thread in routes.py so no
    additional thread is needed.
    """
    now = time.monotonic()
    cutoff = now - 86400
    with _lock:
        stale = [k for k, dq in _buckets.items() if not dq or dq[-1] < cutoff]
        for k in stale:
            del _buckets[k]
