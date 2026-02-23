"""Flask application for va_lidar_context."""

from __future__ import annotations

import argparse
import logging as _logging
import os
import secrets
import sys

from flask import Flask


# Default to desktop mode when launched from local dev CLIs and the user did
# not explicitly set DESKTOP_MODE. Keep server mode as the default elsewhere
# (e.g., gunicorn/docker).
def _should_default_desktop_mode() -> bool:
    if os.getenv("DESKTOP_MODE") is not None:
        return False
    _argv0 = os.path.basename(sys.argv[0]).strip().lower() if sys.argv else ""
    _run_from_flask_cli = os.getenv("FLASK_RUN_FROM_CLI", "").strip().lower() in {
        "1",
        "true",
        "yes",
    }
    return _run_from_flask_cli or _argv0 in {
        "flask",
        "va-lidar-context-web",
        "va-lidar-context-web.exe",
    }


def _bootstrap_local_dev_env() -> None:
    if not _should_default_desktop_mode():
        return
    os.environ.setdefault("DESKTOP_MODE", "1")
    # Keep local dev/backward compatibility with existing jobs under ./out.
    os.environ.setdefault("OUT_DIR", "./out")


_bootstrap_local_dev_env()

# These imports must come after _bootstrap_local_dev_env() sets env defaults.
# fmt: off
from . import settings  # noqa: E402, I001
from .auth import ensure_auth_store as ensure_auth_store  # noqa: E402
from .forms import parse_float as parse_float, parse_int as parse_int  # noqa: E402
from .jobs import (  # noqa: E402
    JOBS as JOBS,
    JOBS_LOCK as JOBS_LOCK,
    Job as Job,
    JobLogHandler as JobLogHandler,
    _notify_job_change_locked as _notify_job_change_locked,
    _notify_recent_jobs_change as _notify_recent_jobs_change,
    _run_build_job as _run_build_job,
)
from .routes import bp as bp  # noqa: E402
from .settings import AppConfig as AppConfig, load_config as load_config  # noqa: E402
# fmt: on

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
            "style-src 'self' 'unsafe-inline' https://unpkg.com https://cdn.jsdelivr.net",
            "img-src 'self' data: blob:",
            "connect-src 'self'",
            "worker-src 'self' blob:",
            "frame-ancestors 'self'",
        ]
        clerk_origin = (_cfg.clerk_frontend_api_url or "").rstrip("/")
        if clerk_origin:
            csp_parts[1] += f" {clerk_origin}"
            csp_parts[2] += f" {clerk_origin}"
            csp_parts[3] += f" {clerk_origin}"
            csp_parts[4] += f" {clerk_origin}"
            csp_parts[1] += " https://accounts.google.com https://apis.google.com"
            csp_parts[2] += " https://accounts.google.com"
            csp_parts[3] += " https://accounts.google.com https://img.clerk.com"
            csp_parts[4] += " https://accounts.google.com"
            csp_parts.append(
                f"font-src 'self' data: https://cdn.jsdelivr.net https://fonts.gstatic.com {clerk_origin}"
            )
            csp_parts.append(f"frame-src 'self' https://accounts.google.com {clerk_origin}")
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
    if not settings.DESKTOP_MODE:
        raise RuntimeError(
            "va-lidar-context-web runs Flask's development server and is intended "
            "for desktop mode only. In server mode use gunicorn, e.g. "
            '"gunicorn -c gunicorn.conf.py va_lidar_context.webapp:app".'
        )
    parser = argparse.ArgumentParser(prog="va-lidar-context-web")
    parser.add_argument("--host", default=os.getenv("WEB_HOST", settings.DESKTOP_HOST))
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("WEB_PORT", str(settings.DESKTOP_PORT))),
    )
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    app.run(host=args.host, port=args.port, debug=args.debug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
