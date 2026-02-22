"""Security regression tests for Critical and High issues."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

import va_lidar_context.webapp.settings as _webapp_settings
from va_lidar_context.webapp.settings import load_config

# ---------------------------------------------------------------------------
# C2 — DDL allowlist
# ---------------------------------------------------------------------------


def test_ddl_allowlist_rejects_unknown_table():
    from va_lidar_context.auth_store import _ALLOWED_DDL_TABLES, _validate_ddl_name

    with pytest.raises(ValueError, match="Disallowed DDL identifier"):
        _validate_ddl_name("injected_table; DROP TABLE users;--", _ALLOWED_DDL_TABLES)


def test_ddl_allowlist_rejects_unknown_column():
    from va_lidar_context.auth_store import _ALLOWED_DDL_COLUMNS, _validate_ddl_name

    with pytest.raises(ValueError, match="Disallowed DDL identifier"):
        _validate_ddl_name("evil_col TEXT; DROP TABLE users;--", _ALLOWED_DDL_COLUMNS)


def test_ddl_allowlist_accepts_known_table():
    from va_lidar_context.auth_store import _ALLOWED_DDL_TABLES, _validate_ddl_name

    _validate_ddl_name("jobs", _ALLOWED_DDL_TABLES)  # must not raise


def test_ddl_allowlist_accepts_known_column():
    from va_lidar_context.auth_store import _ALLOWED_DDL_COLUMNS, _validate_ddl_name

    _validate_ddl_name("started_at", _ALLOWED_DDL_COLUMNS)  # must not raise


# ---------------------------------------------------------------------------
# H5 — SSRF URL validation
# ---------------------------------------------------------------------------


def test_require_https_url_rejects_file_scheme():
    from va_lidar_context.util import require_https_url

    with pytest.raises(ValueError, match="Unsafe URL scheme"):
        require_https_url("file:///etc/passwd")


def test_require_https_url_rejects_ftp_scheme():
    from va_lidar_context.util import require_https_url

    with pytest.raises(ValueError, match="Unsafe URL scheme"):
        require_https_url("ftp://example.com/data.laz")


def test_require_https_url_rejects_s3_scheme():
    from va_lidar_context.util import require_https_url

    with pytest.raises(ValueError, match="Unsafe URL scheme"):
        require_https_url("s3://my-bucket/data.laz")


def test_require_https_url_accepts_https():
    from va_lidar_context.util import require_https_url

    require_https_url("https://rockyweb.usgs.gov/vdelivery/tile.laz")  # must not raise


def test_require_https_url_accepts_http():
    from va_lidar_context.util import require_https_url

    require_https_url("http://example.com/tile.laz")  # must not raise


# ---------------------------------------------------------------------------
# H4 — Filesystem paths stripped from API response
# ---------------------------------------------------------------------------


def test_sanitize_summary_removes_dir_from_outputs():
    from va_lidar_context.webapp.jobs import _sanitize_summary_for_response

    summary = {
        "name": "My Job",
        "out": "/data/out/job-abc",
        "report_path": "/data/out/job-abc/report.json",
        "outputs": {"dir": "/data/out/job-abc", "files": ["terrain.obj"]},
    }
    result = _sanitize_summary_for_response(summary)
    assert "out" not in result
    assert "report_path" not in result
    assert "dir" not in result.get("outputs", {})
    assert result["outputs"]["files"] == ["terrain.obj"]


def test_sanitize_summary_preserves_other_fields():
    from va_lidar_context.webapp.jobs import _sanitize_summary_for_response

    summary = {"name": "My Job", "tile": "abc", "warnings": []}
    result = _sanitize_summary_for_response(summary)
    assert result["name"] == "My Job"
    assert result["tile"] == "abc"


def test_sanitize_summary_handles_missing_outputs():
    from va_lidar_context.webapp.jobs import _sanitize_summary_for_response

    result = _sanitize_summary_for_response({"name": "x"})
    assert result["name"] == "x"


# ---------------------------------------------------------------------------
# H3 — Startup warning when auth disabled in server mode
# ---------------------------------------------------------------------------


def test_create_app_warns_when_auth_disabled(monkeypatch):
    import logging

    from va_lidar_context.webapp import create_app

    records = []

    class _Capture(logging.Handler):
        def emit(self, record):
            records.append(record)

    handler = _Capture()
    logger = logging.getLogger("va_lidar_context.webapp")
    logger.addHandler(handler)
    try:
        cfg = load_config(overrides={"desktop_mode": False, "auth_provider": ""})
        monkeypatch.setattr(_webapp_settings, "_config", cfg)
        create_app(config=cfg)
    finally:
        logger.removeHandler(handler)

    assert any("Authentication is DISABLED" in r.getMessage() for r in records)


def test_create_app_no_warning_in_desktop_mode(monkeypatch, caplog):
    import logging

    from va_lidar_context.webapp import create_app

    cfg = load_config(overrides={"desktop_mode": True})
    monkeypatch.setattr(_webapp_settings, "_config", cfg)
    with caplog.at_level(logging.WARNING, logger="va_lidar_context.webapp"):
        create_app(config=cfg)
    assert not any("Authentication is DISABLED" in r.message for r in caplog.records)


# ---------------------------------------------------------------------------
# H6 — Clerk JWKS URL and issuer required when auth enabled
# ---------------------------------------------------------------------------


def test_create_app_raises_without_clerk_jwks_url(monkeypatch):
    from va_lidar_context.webapp import create_app

    cfg = load_config(
        overrides={
            "desktop_mode": False,
            "auth_enabled": True,
            "clerk_jwks_url": "",
            "clerk_issuer": "https://clerk.example.com",
        }
    )
    monkeypatch.setattr(_webapp_settings, "_config", cfg)
    with pytest.raises(RuntimeError, match="CLERK_JWKS_URL"):
        create_app(config=cfg)


def test_create_app_raises_without_clerk_issuer(monkeypatch):
    from va_lidar_context.webapp import create_app

    cfg = load_config(
        overrides={
            "desktop_mode": False,
            "auth_enabled": True,
            "clerk_jwks_url": "https://clerk.example.com/.well-known/jwks.json",
            "clerk_issuer": "",
        }
    )
    monkeypatch.setattr(_webapp_settings, "_config", cfg)
    with pytest.raises(RuntimeError, match="CLERK_ISSUER"):
        create_app(config=cfg)


def test_verify_clerk_session_token_requires_configured_jwks_url(monkeypatch):
    import va_lidar_context.webapp.auth as auth_mod

    cfg = load_config(
        overrides={
            "desktop_mode": True,
            "clerk_jwks_url": "",
            "clerk_issuer": "https://clerk.example.com",
        }
    )
    monkeypatch.setattr(_webapp_settings, "_config", cfg)
    with pytest.raises(RuntimeError, match="CLERK_JWKS_URL"):
        auth_mod._verify_clerk_session_token("not-a-token")


# ---------------------------------------------------------------------------
# C1 — SESSION_SECRET required in server mode
# ---------------------------------------------------------------------------


def test_create_app_raises_without_session_secret_in_server_mode(monkeypatch):
    from va_lidar_context.webapp import create_app

    monkeypatch.delenv("SESSION_SECRET", raising=False)
    cfg = load_config(overrides={"desktop_mode": False})
    monkeypatch.setattr(_webapp_settings, "_config", cfg)
    with pytest.raises(RuntimeError, match="SESSION_SECRET"):
        create_app(config=cfg)


def test_create_app_allows_random_key_in_desktop_mode(monkeypatch):
    from va_lidar_context.webapp import create_app

    monkeypatch.delenv("SESSION_SECRET", raising=False)
    cfg = load_config(overrides={"desktop_mode": True})
    monkeypatch.setattr(_webapp_settings, "_config", cfg)
    flask_app = create_app(config=cfg)
    assert flask_app.secret_key  # a random key was generated


# ---------------------------------------------------------------------------
# C1.1 — Default desktop mode for local dev CLIs when unset
# ---------------------------------------------------------------------------


def test_should_default_desktop_mode_for_flask_cli(monkeypatch):
    import sys

    import va_lidar_context.webapp as webapp

    monkeypatch.delenv("DESKTOP_MODE", raising=False)
    monkeypatch.setenv("FLASK_RUN_FROM_CLI", "true")
    monkeypatch.setattr(sys, "argv", ["python"])
    assert webapp._should_default_desktop_mode() is True


def test_bootstrap_local_dev_env_sets_out_dir_for_cli(monkeypatch):
    import sys

    import va_lidar_context.webapp as webapp

    monkeypatch.delenv("DESKTOP_MODE", raising=False)
    monkeypatch.delenv("OUT_DIR", raising=False)
    monkeypatch.setenv("FLASK_RUN_FROM_CLI", "true")
    monkeypatch.setattr(sys, "argv", ["python"])
    webapp._bootstrap_local_dev_env()
    assert os.getenv("DESKTOP_MODE") == "1"
    assert os.getenv("OUT_DIR") == "./out"


def test_should_not_default_desktop_mode_for_server_process(monkeypatch):
    import sys

    import va_lidar_context.webapp as webapp

    monkeypatch.delenv("DESKTOP_MODE", raising=False)
    monkeypatch.delenv("FLASK_RUN_FROM_CLI", raising=False)
    monkeypatch.setattr(sys, "argv", ["gunicorn"])
    assert webapp._should_default_desktop_mode() is False


def test_bootstrap_local_dev_env_keeps_explicit_out_dir(monkeypatch):
    import sys

    import va_lidar_context.webapp as webapp

    monkeypatch.delenv("DESKTOP_MODE", raising=False)
    monkeypatch.setenv("OUT_DIR", "/tmp/custom-out")
    monkeypatch.setenv("FLASK_RUN_FROM_CLI", "true")
    monkeypatch.setattr(sys, "argv", ["python"])
    webapp._bootstrap_local_dev_env()
    assert os.getenv("DESKTOP_MODE") == "1"
    assert os.getenv("OUT_DIR") == "/tmp/custom-out"


# ---------------------------------------------------------------------------
# H1 — Security headers present on responses
# ---------------------------------------------------------------------------


def test_security_headers_on_response():
    import va_lidar_context.webapp as webapp

    client = webapp.app.test_client()
    resp = client.get("/healthz")
    assert resp.headers.get("Content-Security-Policy") is not None
    assert resp.headers.get("X-Content-Type-Options") == "nosniff"
    assert resp.headers.get("X-Frame-Options") == "SAMEORIGIN"
    assert resp.headers.get("Referrer-Policy") == "strict-origin-when-cross-origin"
    csp = resp.headers["Content-Security-Policy"]
    assert "default-src 'self'" in csp
    assert "https://cdn.jsdelivr.net" in csp
    assert "https://unpkg.com" in csp


def test_security_headers_include_clerk_frontend_in_script_and_connect(monkeypatch):
    from va_lidar_context.webapp import create_app

    cfg = load_config(
        overrides={
            "desktop_mode": True,
            "clerk_frontend_api_url": "https://clerk.example.com",
        }
    )
    monkeypatch.setattr(_webapp_settings, "_config", cfg)
    flask_app = create_app(config=cfg)
    client = flask_app.test_client()
    resp = client.get("/healthz")
    csp = resp.headers["Content-Security-Policy"]
    assert (
        "script-src 'self' 'unsafe-inline' https://unpkg.com https://cdn.jsdelivr.net https://clerk.example.com"
        in csp
    )
    assert "connect-src 'self' https://clerk.example.com" in csp


def test_auth_login_template_has_no_unpkg_clerk_fallback_and_uses_sri():
    content = Path("src/va_lidar_context/templates/auth_login.html").read_text()
    assert "https://unpkg.com/@clerk/clerk-js@" not in content
    assert "https://cdn.jsdelivr.net/npm/@clerk/clerk-js@" in content
    assert content.count("integrity: CLERK_JS_SRI_HASH") >= 2


# ---------------------------------------------------------------------------
# M3 — _safe_next_path open-redirect prevention
# ---------------------------------------------------------------------------


def test_safe_next_path_rejects_protocol_relative():
    from va_lidar_context.webapp.routes import _safe_next_path

    assert _safe_next_path("//evil.com") == "/"


def test_safe_next_path_rejects_absolute_url():
    from va_lidar_context.webapp.routes import _safe_next_path

    assert _safe_next_path("https://evil.com/steal") == "/"


def test_safe_next_path_rejects_non_slash_start():
    from va_lidar_context.webapp.routes import _safe_next_path

    assert _safe_next_path("evil.com") == "/"


def test_safe_next_path_accepts_relative():
    from va_lidar_context.webapp.routes import _safe_next_path

    assert _safe_next_path("/dashboard") == "/dashboard"


def test_safe_next_path_accepts_none():
    from va_lidar_context.webapp.routes import _safe_next_path

    assert _safe_next_path(None) == "/"


# ---------------------------------------------------------------------------
# M4 — JWKS client cache expires after TTL
# ---------------------------------------------------------------------------


def test_jwks_client_cache_expires_after_ttl(monkeypatch):
    import jwt as pyjwt

    import va_lidar_context.webapp.auth as auth_mod

    # Clear the cache so we start fresh
    auth_mod._JWKS_CLIENT_CACHE.clear()

    calls = []
    original_client = pyjwt.PyJWKClient

    def mock_client(url, **kwargs):
        calls.append(url)
        return original_client.__new__(original_client)

    monkeypatch.setattr(pyjwt, "PyJWKClient", mock_client)

    fake_url = "https://example.com/.well-known/jwks.json"

    # Seed the cache with an already-expired entry (expires_at = 0)
    dummy = object()
    auth_mod._JWKS_CLIENT_CACHE[fake_url] = (dummy, 0.0)  # type: ignore[assignment]

    # Calling _clerk_jwk_client should detect expiry and create a new client
    auth_mod._clerk_jwk_client(fake_url)
    assert len(calls) == 1, "Expected a new PyJWKClient to be created after TTL expiry"


def test_jwks_client_cache_reuses_within_ttl(monkeypatch):
    import time as _time

    import jwt as pyjwt

    import va_lidar_context.webapp.auth as auth_mod

    auth_mod._JWKS_CLIENT_CACHE.clear()
    calls = []

    def mock_client(url, **kwargs):
        calls.append(url)
        return object()  # type: ignore[return-value]

    monkeypatch.setattr(pyjwt, "PyJWKClient", mock_client)

    fake_url = "https://example.com/fresh/.well-known/jwks.json"
    future = _time.monotonic() + 3600
    dummy = object()
    auth_mod._JWKS_CLIENT_CACHE[fake_url] = (dummy, future)  # type: ignore[assignment]

    result = auth_mod._clerk_jwk_client(fake_url)
    assert result is dummy, "Cache hit expected within TTL"
    assert len(calls) == 0, "No new PyJWKClient should be created within TTL"


# ---------------------------------------------------------------------------
# M6 — worker_shared_token deprecated; HMAC required
# ---------------------------------------------------------------------------


def test_worker_shared_token_is_not_accepted_even_with_fresh_timestamp(monkeypatch):
    import time

    import va_lidar_context.webapp.settings as _ws
    from va_lidar_context.webapp import create_app
    from va_lidar_context.webapp.settings import load_config

    cfg = load_config(overrides={"desktop_mode": True, "worker_shared_token": "test-token"})
    monkeypatch.setattr(_ws, "_config", cfg)
    flask_app = create_app(config=cfg)

    with flask_app.test_request_context(
        "/internal/worker/jobs/x/complete",
        method="POST",
        headers={
            "X-Worker-Token": "test-token",
            "X-Timestamp": str(int(time.time())),
        },
    ):
        from va_lidar_context.webapp.auth import verify_hmac_request

        assert verify_hmac_request() is False


def test_create_app_warns_when_worker_shared_token_set(monkeypatch):
    import logging

    from va_lidar_context.webapp import create_app

    records = []

    class _Capture(logging.Handler):
        def emit(self, record):
            records.append(record)

    handler = _Capture()
    logger = logging.getLogger("va_lidar_context.webapp")
    logger.addHandler(handler)
    cfg = load_config(overrides={"desktop_mode": True, "worker_shared_token": "legacy-token"})
    monkeypatch.setattr(_webapp_settings, "_config", cfg)
    try:
        create_app(config=cfg)
    finally:
        logger.removeHandler(handler)
    assert any(
        "legacy auth path is deprecated and no longer accepted" in r.getMessage() for r in records
    )


# ---------------------------------------------------------------------------
# M1 — In-process rate limiter
# ---------------------------------------------------------------------------


def test_rate_limiter_allows_within_limits():
    from va_lidar_context.webapp import rate_limiter

    rate_limiter._buckets.clear()

    import va_lidar_context.webapp as webapp

    client = webapp.app.test_client()
    # Just verify a single request gets through (bucket is fresh)
    resp = client.get("/healthz")
    assert resp.status_code == 200


def test_rate_limiter_blocks_on_hourly_limit(monkeypatch):
    import time

    from va_lidar_context.webapp import rate_limiter

    rate_limiter._buckets.clear()

    # Fake IP so we don't bleed into other tests
    monkeypatch.setattr(rate_limiter, "_client_ip", lambda: "10.0.0.1")

    now = time.monotonic()
    # Pre-fill the bucket with hourly=2 worth of entries (all recent)
    key = "test_ep:10.0.0.1"
    from collections import deque

    rate_limiter._buckets[key] = deque([now - 10, now - 5])

    allowed, msg = rate_limiter.check("test_ep", hourly=2, daily=1000)
    assert not allowed
    assert "requests/hour" in msg


def test_rate_limiter_blocks_on_daily_limit(monkeypatch):
    import time

    from va_lidar_context.webapp import rate_limiter

    rate_limiter._buckets.clear()
    monkeypatch.setattr(rate_limiter, "_client_ip", lambda: "10.0.0.2")

    now = time.monotonic()
    key = "test_ep2:10.0.0.2"
    # Put entries in the bucket that are >1 h old but <24 h old (hits daily cap)
    from collections import deque

    rate_limiter._buckets[key] = deque([now - 7200, now - 3700])

    allowed, msg = rate_limiter.check("test_ep2", hourly=100, daily=2)
    assert not allowed
    assert "requests/day" in msg


def test_rate_limiter_separate_buckets_per_ip(monkeypatch):
    import time

    from va_lidar_context.webapp import rate_limiter

    rate_limiter._buckets.clear()
    now = time.monotonic()
    from collections import deque

    # IP A is at limit
    monkeypatch.setattr(rate_limiter, "_client_ip", lambda: "10.0.1.1")
    rate_limiter._buckets["sep_ep:10.0.1.1"] = deque([now - 1, now - 2])
    allowed_a, _ = rate_limiter.check("sep_ep", hourly=2, daily=1000)
    assert not allowed_a

    # IP B should still be allowed
    monkeypatch.setattr(rate_limiter, "_client_ip", lambda: "10.0.1.2")
    allowed_b, _ = rate_limiter.check("sep_ep", hourly=2, daily=1000)
    assert allowed_b


def test_rate_limiter_cleanup_removes_expired():
    import time
    from collections import deque

    from va_lidar_context.webapp import rate_limiter

    rate_limiter._buckets.clear()
    now = time.monotonic()
    # Add a stale bucket (last entry > 24 h ago)
    rate_limiter._buckets["stale:1.2.3.4"] = deque([now - 90000])
    # Add a fresh bucket
    rate_limiter._buckets["fresh:1.2.3.4"] = deque([now - 10])

    rate_limiter.cleanup_expired()

    assert "stale:1.2.3.4" not in rate_limiter._buckets
    assert "fresh:1.2.3.4" in rate_limiter._buckets


# ---------------------------------------------------------------------------
# M7 — Long-poll slot cap
# ---------------------------------------------------------------------------


def test_longpoll_slot_acquires_and_releases():
    import va_lidar_context.webapp.routes as routes_mod
    from va_lidar_context.webapp.routes import (
        _LONGPOLL_COUNTS,
        _LONGPOLL_MAX_PER_USER,
        _LongPollSlot,
    )

    routes_mod._LONGPOLL_COUNTS.clear()
    key = "user:test_longpoll_slot"

    with _LongPollSlot(key) as slot:
        assert slot.acquired
        assert routes_mod._LONGPOLL_COUNTS.get(key) == 1

    # Should be released after context exit
    assert routes_mod._LONGPOLL_COUNTS.get(key) == 0


def test_longpoll_slot_rejects_when_limit_reached():
    import va_lidar_context.webapp.routes as routes_mod
    from va_lidar_context.webapp.routes import _LongPollSlot

    routes_mod._LONGPOLL_COUNTS.clear()
    key = "user:test_longpoll_reject"
    max_per_user = routes_mod._LONGPOLL_MAX_PER_USER

    # Fill up to the limit
    routes_mod._LONGPOLL_COUNTS[key] = max_per_user

    with _LongPollSlot(key) as slot:
        assert not slot.acquired

    # Count should be unchanged (no double-decrement)
    assert routes_mod._LONGPOLL_COUNTS.get(key) == max_per_user


def test_longpoll_slot_releases_on_exception():
    import va_lidar_context.webapp.routes as routes_mod
    from va_lidar_context.webapp.routes import _LongPollSlot

    routes_mod._LONGPOLL_COUNTS.clear()
    key = "user:test_longpoll_exc"

    try:
        with _LongPollSlot(key) as slot:
            assert slot.acquired
            raise RuntimeError("simulated error")
    except RuntimeError:
        pass

    assert routes_mod._LONGPOLL_COUNTS.get(key) == 0


# ---------------------------------------------------------------------------
# LOW-severity hardening checks
# ---------------------------------------------------------------------------


def test_admin_users_page_renders_without_build_error():
    import va_lidar_context.webapp as webapp

    client = webapp.app.test_client()
    resp = client.get("/admin/users")
    assert resp.status_code == 200


def test_sanitize_job_error_hides_internal_exception_text():
    from va_lidar_context.webapp.jobs import sanitize_job_error

    assert sanitize_job_error("OSError: /Users/hugo/.aws/credentials not found") == (
        "Build failed. Check server logs for details."
    )


def test_sanitize_job_error_preserves_restart_message():
    from va_lidar_context.webapp.jobs import sanitize_job_error

    assert sanitize_job_error("Job interrupted (server restarted).") == (
        "Job interrupted (server restarted)."
    )


def test_web_cli_main_rejects_server_mode(monkeypatch):
    import sys

    import va_lidar_context.webapp as webapp

    monkeypatch.setattr(webapp, "DESKTOP_MODE", False)
    monkeypatch.setattr(sys, "argv", ["va-lidar-context-web"])
    with pytest.raises(RuntimeError, match="desktop mode only"):
        webapp.main()


def test_auth_store_connect_enables_wal(tmp_path):
    from va_lidar_context import auth_store

    db_path = tmp_path / "app.db"
    auth_store.init_db(db_path)
    with auth_store._connect(db_path) as conn:
        mode = conn.execute("PRAGMA journal_mode").fetchone()[0]
    assert str(mode).lower() == "wal"


def test_run_build_job_sets_error_on_nonzero_exit_code(monkeypatch):
    """B3: job.error must be set when build returns exit_code != 0 without raising."""
    import va_lidar_context.webapp.jobs as jobs_mod
    from va_lidar_context.pipeline.types import BuildResult
    from va_lidar_context.webapp.jobs import Job

    cfg = load_config(overrides={"desktop_mode": True, "job_history_enabled": False})
    monkeypatch.setattr(_webapp_settings, "_config", cfg)
    monkeypatch.setattr(jobs_mod.auth_store, "set_job_status", lambda *a, **k: None)
    monkeypatch.setattr(jobs_mod.auth_store, "set_active_job", lambda *a, **k: None)
    monkeypatch.setattr(jobs_mod.auth_store, "finish_active_job", lambda *a, **k: None)
    monkeypatch.setattr(jobs_mod, "build_pipeline", lambda cfg: BuildResult(exit_code=1))
    monkeypatch.setattr(jobs_mod, "_persist_job_snapshot", lambda job: None)

    from va_lidar_context.config import BuildConfig

    job = Job(job_id="job-nonzero-exit", status="queued", created_at=0.0)
    cfg_build = BuildConfig(
        center=(36.0, -112.0),
        size=1000,
        outputs=("terrain",),
    )
    jobs_mod._run_build_job(job, cfg_build)

    assert job.status == "error"
    assert job.error is not None, "B3: job.error must be set when exit_code != 0"


def test_run_build_job_writes_error_log_for_exceptions(tmp_path, monkeypatch):
    import va_lidar_context.webapp.jobs as jobs_mod
    from va_lidar_context.webapp.jobs import Job

    cfg = load_config(
        overrides={
            "desktop_mode": True,
            "job_history_enabled": False,
            "out_dir": tmp_path / "out",
        }
    )
    monkeypatch.setattr(_webapp_settings, "_config", cfg)
    monkeypatch.setattr(jobs_mod.auth_store, "set_job_status", lambda *a, **k: None)
    monkeypatch.setattr(jobs_mod.auth_store, "set_active_job", lambda *a, **k: None)
    monkeypatch.setattr(jobs_mod.auth_store, "finish_active_job", lambda *a, **k: None)

    def _boom(_cfg):
        raise RuntimeError("boom")

    monkeypatch.setattr(jobs_mod, "build_pipeline", _boom)
    monkeypatch.setattr(jobs_mod, "_persist_job_snapshot", lambda job: None)

    from va_lidar_context.config import BuildConfig

    job = Job(job_id="job-error-log", status="queued", created_at=0.0)
    cfg_build = BuildConfig(
        center=(36.0, -112.0),
        size=1000,
        outputs=("terrain",),
        out_dir=cfg.out_dir,
    )
    jobs_mod._run_build_job(job, cfg_build)

    error_log = cfg.out_dir / "job-error-log" / "error.log"
    assert error_log.is_file()
    text = error_log.read_text()
    assert "RuntimeError: boom" in text
    assert job.summary.get("error_log") == "error.log"


def test_job_log_handler_extracts_stage_progress():
    import logging

    from va_lidar_context.webapp.jobs import Job, JobLogHandler

    job = Job(job_id="job-stage", status="running", created_at=0.0)
    handler = JobLogHandler(job)
    record = logging.LogRecord(
        name="va_lidar_context",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="Stage 4/6: generate rasters",
        args=(),
        exc_info=None,
    )
    handler.emit(record)

    assert job.stage_label == "generate rasters"
    assert job.stage_index == 4
    assert job.stage_total == 6
    assert job.stage_progress == 67


def test_persist_job_snapshot_logs_database_errors(monkeypatch):
    import logging

    import va_lidar_context.webapp.auth as auth_mod
    import va_lidar_context.webapp.jobs as jobs_mod
    from va_lidar_context.webapp.jobs import Job

    records = []

    class _Capture(logging.Handler):
        def emit(self, record):
            records.append(record)

    handler = _Capture()
    logger = logging.getLogger("va_lidar_context.webapp.jobs")
    logger.addHandler(handler)
    cfg = load_config(overrides={"desktop_mode": True, "job_history_enabled": True})
    monkeypatch.setattr(_webapp_settings, "_config", cfg)
    monkeypatch.setattr(auth_mod, "ensure_auth_store", lambda: None)

    def _boom(*_args, **_kwargs):
        raise RuntimeError("database is locked")

    monkeypatch.setattr(jobs_mod.auth_store, "upsert_job_snapshot", _boom)
    job = Job(job_id="job-db-lock", status="queued", created_at=0.0)
    try:
        jobs_mod._persist_job_snapshot(job)
    finally:
        logger.removeHandler(handler)
    assert any("Failed to persist job snapshot for job-db-lock" in r.getMessage() for r in records)
