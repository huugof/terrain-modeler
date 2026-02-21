"""Runtime configuration read from environment variables."""
from __future__ import annotations

import os
import threading
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List

from ..config import (
    DEFAULT_DESKTOP_HOST,
    DEFAULT_DESKTOP_MODE,
    DEFAULT_DESKTOP_OUT_DIR,
    DEFAULT_DESKTOP_PORT,
    DEFAULT_DESKTOP_RETENTION_DAYS,
    DEFAULT_OUT_DIR,
)
from ..hmac_auth import parse_key_map


@dataclass
class AppConfig:
    """All runtime configuration for the webapp package."""

    desktop_mode: bool
    out_dir: Path
    retention_days: int
    cleanup_interval_seconds: int
    default_random_min_height: float
    default_random_max_height: float
    coverage_cache_ttl_seconds: int
    db_path: Path
    desktop_host: str
    desktop_port: int
    auth_provider: str
    auth_enabled: bool
    clerk_publishable_key: str
    clerk_secret_key: str
    clerk_sign_in_url: str
    clerk_jwks_url: str
    clerk_issuer: str
    clerk_api_url: str
    clerk_frontend_api_url: str
    clerk_allowed_domain: str
    require_local_allowlist: bool
    clerk_authorized_parties: List[str]
    admin_email: str
    session_ttl_seconds: int
    session_cookie_secure: bool
    rate_limit_hourly: int
    rate_limit_daily: int
    max_active_jobs_per_user: int
    max_clip_size: float
    job_history_enabled: bool
    job_rehydrate_limit: int
    job_log_wait_max_seconds: float
    recent_jobs_wait_max_seconds: float
    recent_jobs_limit: int
    hmac_keys_json: str
    hmac_max_skew_seconds: int
    hmac_nonce_ttl_seconds: int
    hmac_keys: Dict[str, str] = field(default_factory=dict)
    worker_shared_token: str = ""


def load_config(overrides: dict | None = None) -> AppConfig:
    """Build an AppConfig from environment variables.

    overrides: optional dict mapping lowercase AppConfig field names to values.
               Applied after all env-var defaults are computed.
    """
    ov = overrides or {}

    desktop_mode: bool = os.getenv(
        "DESKTOP_MODE", "1" if DEFAULT_DESKTOP_MODE else "0"
    ).lower() in ("1", "true", "yes")
    desktop_mode = ov.get("desktop_mode", desktop_mode)

    out_dir: Path = Path(
        os.getenv(
            "OUT_DIR",
            str(DEFAULT_DESKTOP_OUT_DIR if desktop_mode else DEFAULT_OUT_DIR),
        )
    )
    out_dir = ov.get("out_dir", out_dir)

    retention_days: int = int(
        os.getenv(
            "RETENTION_DAYS",
            str(DEFAULT_DESKTOP_RETENTION_DAYS if desktop_mode else 7),
        )
    )

    cleanup_interval_seconds: int = int(os.getenv("CLEANUP_INTERVAL", "3600"))
    default_random_min_height: float = 15.0
    default_random_max_height: float = 40.0
    coverage_cache_ttl_seconds: int = int(os.getenv("COVERAGE_CACHE_TTL", "600"))
    db_path: Path = Path(os.getenv("DB_PATH", "./data/app.db"))
    auth_provider: str = os.getenv("AUTH_PROVIDER", "").strip().lower()
    auth_enabled: bool = (not desktop_mode) and auth_provider == "clerk"
    clerk_publishable_key: str = os.getenv("CLERK_PUBLISHABLE_KEY", "").strip()
    clerk_secret_key: str = os.getenv("CLERK_SECRET_KEY", "").strip()
    clerk_sign_in_url: str = os.getenv("CLERK_SIGN_IN_URL", "").strip()
    clerk_jwks_url: str = os.getenv("CLERK_JWKS_URL", "").strip()
    clerk_issuer: str = os.getenv("CLERK_ISSUER", "").strip()
    clerk_api_url: str = os.getenv(
        "CLERK_API_URL", "https://api.clerk.com/v1"
    ).strip()
    clerk_frontend_api_url: str = os.getenv("CLERK_FRONTEND_API_URL", "").strip()
    clerk_allowed_domain: str = os.getenv(
        "CLERK_ALLOWED_DOMAIN", ""
    ).strip().lower()
    require_local_allowlist: bool = os.getenv(
        "REQUIRE_LOCAL_ALLOWLIST", "0"
    ).lower() in ("1", "true", "yes")
    clerk_authorized_parties: List[str] = [
        p.strip()
        for p in os.getenv("CLERK_AUTHORIZED_PARTIES", "").split(",")
        if p.strip()
    ]
    session_ttl_seconds: int = int(
        os.getenv("SESSION_TTL_SECONDS", str(7 * 86400))
    )
    session_cookie_secure: bool = os.getenv(
        "SESSION_COOKIE_SECURE", "1"
    ).lower() not in ("0", "false", "no")
    admin_email: str = os.getenv("ADMIN_EMAIL", "").strip().lower()
    rate_limit_hourly: int = int(os.getenv("RATE_LIMIT_HOURLY", "3"))
    rate_limit_daily: int = int(os.getenv("RATE_LIMIT_DAILY", "10"))
    max_active_jobs_per_user: int = int(os.getenv("MAX_ACTIVE_JOBS_PER_USER", "1"))
    max_clip_size: float = float(os.getenv("MAX_CLIP_SIZE", "5000"))
    job_history_enabled: bool = os.getenv(
        "JOB_HISTORY_ENABLED", "1"
    ).lower() in ("1", "true", "yes")
    job_rehydrate_limit: int = int(os.getenv("JOB_REHYDRATE_LIMIT", "500"))
    job_log_wait_max_seconds: float = float(
        os.getenv("JOB_LOG_WAIT_MAX_SECONDS", "25")
    )
    recent_jobs_wait_max_seconds: float = float(
        os.getenv("RECENT_JOBS_WAIT_MAX_SECONDS", "25")
    )
    recent_jobs_limit: int = int(os.getenv("RECENT_JOBS_LIMIT", "5"))
    hmac_keys_json: str = os.getenv("HMAC_KEYS_JSON", "").strip()
    hmac_max_skew_seconds: int = int(os.getenv("HMAC_MAX_SKEW_SECONDS", "300"))
    hmac_nonce_ttl_seconds: int = int(os.getenv("HMAC_NONCE_TTL_SECONDS", "600"))
    worker_shared_token: str = os.getenv("WORKER_SHARED_TOKEN", "").strip()
    desktop_host: str = DEFAULT_DESKTOP_HOST
    desktop_port: int = DEFAULT_DESKTOP_PORT

    hmac_keys: Dict[str, str] = {}
    if hmac_keys_json:
        try:
            hmac_keys = parse_key_map(hmac_keys_json)
        except Exception:
            hmac_keys = {}

    cfg = AppConfig(
        desktop_mode=desktop_mode,
        out_dir=out_dir,
        retention_days=retention_days,
        cleanup_interval_seconds=cleanup_interval_seconds,
        default_random_min_height=default_random_min_height,
        default_random_max_height=default_random_max_height,
        coverage_cache_ttl_seconds=coverage_cache_ttl_seconds,
        db_path=db_path,
        desktop_host=desktop_host,
        desktop_port=desktop_port,
        auth_provider=auth_provider,
        auth_enabled=auth_enabled,
        clerk_publishable_key=clerk_publishable_key,
        clerk_secret_key=clerk_secret_key,
        clerk_sign_in_url=clerk_sign_in_url,
        clerk_jwks_url=clerk_jwks_url,
        clerk_issuer=clerk_issuer,
        clerk_api_url=clerk_api_url,
        clerk_frontend_api_url=clerk_frontend_api_url,
        clerk_allowed_domain=clerk_allowed_domain,
        require_local_allowlist=require_local_allowlist,
        clerk_authorized_parties=clerk_authorized_parties,
        admin_email=admin_email,
        session_ttl_seconds=session_ttl_seconds,
        session_cookie_secure=session_cookie_secure,
        rate_limit_hourly=rate_limit_hourly,
        rate_limit_daily=rate_limit_daily,
        max_active_jobs_per_user=max_active_jobs_per_user,
        max_clip_size=max_clip_size,
        job_history_enabled=job_history_enabled,
        job_rehydrate_limit=job_rehydrate_limit,
        job_log_wait_max_seconds=job_log_wait_max_seconds,
        recent_jobs_wait_max_seconds=recent_jobs_wait_max_seconds,
        recent_jobs_limit=recent_jobs_limit,
        hmac_keys_json=hmac_keys_json,
        hmac_max_skew_seconds=hmac_max_skew_seconds,
        hmac_nonce_ttl_seconds=hmac_nonce_ttl_seconds,
        hmac_keys=hmac_keys,
        worker_shared_token=worker_shared_token,
    )

    # Apply any explicit overrides after construction
    for key, value in (ov or {}).items():
        if key not in ("desktop_mode", "out_dir"):  # already applied above
            setattr(cfg, key, value)

    return cfg


# ---------------------------------------------------------------------------
# Module-level singleton — replaced by tests via monkeypatch or create_app()
# ---------------------------------------------------------------------------

_config: AppConfig = load_config()


def __getattr__(name: str) -> object:
    """Proxy SCREAMING_CASE attribute lookups to _config for backward compat.

    Allows existing code that does ``_settings.AUTH_ENABLED`` or
    ``from va_lidar_context.webapp import AUTH_ENABLED`` to continue working
    after the module-level constants were removed.
    """
    lower = name.lower()
    try:
        return getattr(_config, lower)
    except AttributeError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


# ---------------------------------------------------------------------------
# Background-thread state (not config values — stay as module globals)
# ---------------------------------------------------------------------------

_cleanup_started: bool = False
_cleanup_lock: threading.Lock = threading.Lock()
