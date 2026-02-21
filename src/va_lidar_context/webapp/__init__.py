"""Flask application for va_lidar_context.

This package replaced the monolithic webapp.py module. All previously public
names are re-exported here so that existing imports and tests continue to work
unchanged.
"""

from __future__ import annotations

import argparse
import logging as _logging
import os
import secrets

from flask import Flask

# --- settings module (exposed so tests can monkeypatch via webapp.settings.X) ---
from . import settings

# --- auth ---
from .auth import (
    _auth_lock,
    _auth_started,
    clerk_auth_ready,
    current_user,
    enforce_rate_limits,
    ensure_auth_store,
    ensure_logged_user_from_session,
    get_csrf_token,
    require_admin,
    require_login,
    user_can_access_job,
    validate_csrf,
    verify_hmac_request,
)

# --- forms ---
from .forms import (
    coverage_cache_key,
    data_sources_payload,
    extract_form_defaults,
    is_in_virginia,
    merge_prefill_defaults,
    parcel_sources_payload,
    parse_bool,
    parse_float,
    parse_int,
    provider_label,
    resolve_image_quality,
    resolve_provider,
    snapshot_defaults,
    status_class,
    status_label,
)

# --- jobs ---
from .jobs import (
    JOBS,
    JOBS_LOCK,
    Job,
    JobLogHandler,
    _collect_outputs,
    _job_logs_payload,
    _jobs_for_user,
    _list_job_artifacts,
    _notify_job_change_locked,
    _notify_recent_jobs_change,
    _persist_job_snapshot,
    _recent_job_display_name,
    _recent_job_payload,
    _recent_jobs_change_cond,
    _recent_jobs_change_version,
    _rehydrate_jobs_from_store,
    _resolve_job_output_dir,
    _run_build_job,
)

# --- blueprint ---
from .routes import bp

# --- AppConfig and load_config exposed for test fixtures ---
# --- settings re-exports (kept for backwards compatibility) ---
from .settings import (
    AUTH_ENABLED,
    CLEANUP_INTERVAL_SECONDS,
    COVERAGE_CACHE_TTL_SECONDS,
    DB_PATH,
    DESKTOP_HOST,
    DESKTOP_MODE,
    DESKTOP_PORT,
    HMAC_KEYS,
    HMAC_MAX_SKEW_SECONDS,
    HMAC_NONCE_TTL_SECONDS,
    JOB_HISTORY_ENABLED,
    JOB_LOG_WAIT_MAX_SECONDS,
    JOB_REHYDRATE_LIMIT,
    MAX_ACTIVE_JOBS_PER_USER,
    MAX_CLIP_SIZE,
    OUT_DIR,
    RATE_LIMIT_DAILY,
    RATE_LIMIT_HOURLY,
    RECENT_JOBS_LIMIT,
    RECENT_JOBS_WAIT_MAX_SECONDS,
    RETENTION_DAYS,
    SESSION_COOKIE_SECURE,
    SESSION_TTL_SECONDS,
    WORKER_SHARED_TOKEN,
    AppConfig,
    load_config,
)

# ---------------------------------------------------------------------------
# App factory
# ---------------------------------------------------------------------------


def create_app(config: AppConfig | None = None) -> Flask:
    """Create and configure a Flask application instance.

    If *config* is provided it replaces the module-level ``_config`` singleton
    in ``settings``, so all settings lookups across the webapp package
    (auth, jobs, routes, forms) see the injected values.  This is the intended
    path for test fixtures.

    The global ``app`` instance is created by calling ``create_app()`` with no
    arguments, preserving the existing production behaviour.
    """
    import va_lidar_context.webapp.settings as _settings_mod

    if config is not None:
        _settings_mod._config = config

    _cfg = _settings_mod._config

    # --- H3: warn loudly when server mode runs without authentication ---
    if not _cfg.desktop_mode and not _cfg.auth_enabled:
        _logging.getLogger(__name__).warning(
            "SECURITY WARNING: Authentication is DISABLED. "
            "Set AUTH_PROVIDER=clerk to enable auth in server mode."
        )

    # --- M6: shared worker token is deprecated and ignored ---
    if _cfg.worker_shared_token:
        _logging.getLogger(__name__).warning(
            "SECURITY WARNING: WORKER_SHARED_TOKEN is set. "
            "This legacy auth path is deprecated and no longer accepted. "
            "Use HMAC_KEYS_JSON for worker authentication."
        )

    # --- M5: warn when DB path is relative in server mode ---
    if not _cfg.desktop_mode and not os.path.isabs(str(_cfg.db_path)):
        _logging.getLogger(__name__).warning(
            "SECURITY WARNING: DB_PATH is a relative path (%s). "
            "Set DB_PATH to an absolute path in production.",
            _cfg.db_path,
        )

    # --- H6: require Clerk JWKS URL and issuer when auth is enabled ---
    if _cfg.auth_enabled:
        if not _cfg.clerk_jwks_url:
            raise RuntimeError(
                "CLERK_JWKS_URL must be set when authentication is enabled. "
                "Find this in your Clerk Dashboard under API Keys."
            )
        if not _cfg.clerk_issuer:
            raise RuntimeError(
                "CLERK_ISSUER must be set when authentication is enabled. "
                "This is your Clerk Frontend API URL "
                "(e.g. https://clerk.<your-domain>.com)."
            )

    # --- C1: require a stable secret key in server mode ---
    _session_secret = os.getenv("SESSION_SECRET", "").strip()
    if not _session_secret:
        if _cfg.desktop_mode:
            _session_secret = secrets.token_hex(32)  # ephemeral key OK for desktop
        else:
            raise RuntimeError(
                "SESSION_SECRET must be set in server mode. "
                "Generate one with: "
                'python -c "import secrets; print(secrets.token_hex(32))"'
            )

    _app = Flask(__name__, template_folder="../templates", static_folder="../static")
    _app.secret_key = _session_secret
    _app.config["SESSION_COOKIE_HTTPONLY"] = True
    _app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    _app.config["SESSION_COOKIE_SECURE"] = (
        _cfg.session_cookie_secure if _cfg.auth_enabled else False
    )

    # --- H1: security response headers ---
    @_app.after_request
    def _add_security_headers(response):
        csp_parts = [
            "default-src 'self'",
            "script-src 'self' 'unsafe-inline' https://unpkg.com https://cdn.jsdelivr.net",
            "style-src 'self' 'unsafe-inline'",
            "img-src 'self' data: blob:",
            "connect-src 'self'",
            "worker-src 'self' blob:",
            "frame-ancestors 'self'",
        ]
        clerk_origin = (_cfg.clerk_frontend_api_url or "").rstrip("/")
        if clerk_origin:
            csp_parts[1] += f" {clerk_origin}"
        response.headers["Content-Security-Policy"] = "; ".join(csp_parts)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response

    _app.register_blueprint(bp)
    return _app


# Module-level instance — used by gunicorn (WSGI entry point) and existing imports.
app = create_app()


def main() -> int:
    if not DESKTOP_MODE:
        raise RuntimeError(
            "va-lidar-context-web runs Flask's development server and is intended "
            "for desktop mode only. In server mode use gunicorn, e.g. "
            '"gunicorn -c gunicorn.conf.py va_lidar_context.webapp:app".'
        )
    default_host = DESKTOP_HOST if DESKTOP_MODE else "127.0.0.1"
    default_port = DESKTOP_PORT if DESKTOP_MODE else 5000
    parser = argparse.ArgumentParser(prog="va-lidar-context-web")
    parser.add_argument("--host", default=os.getenv("WEB_HOST", default_host))
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("WEB_PORT", str(default_port))),
    )
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    app.run(host=args.host, port=args.port, debug=args.debug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
