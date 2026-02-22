"""Authentication, session management, CSRF, Clerk integration, and HMAC verification."""

from __future__ import annotations

import secrets
import threading
import time
from functools import wraps
from typing import Any, Dict, Optional

import jwt
import requests
from flask import g, jsonify, redirect, request, session, url_for

from .. import auth_store
from ..constants import DEFAULT_PREVIEW_JOB_ID
from ..hmac_auth import (
    canonical_payload,
    choose_secret,
    validate_timestamp,
    verify_signature,
)
from . import settings as _settings

_auth_started: bool = False
_auth_lock = threading.Lock()


def ensure_auth_store() -> None:
    from .jobs import _rehydrate_jobs_from_store  # avoid circular at module level

    global _auth_started

    if not _settings.AUTH_ENABLED and not _settings.HMAC_KEYS and not _settings.JOB_HISTORY_ENABLED:
        return
    with _auth_lock:
        if _auth_started:
            return
        auth_store.init_db(_settings.DB_PATH, _settings._config.admin_email or None)
        _rehydrate_jobs_from_store()
        _auth_started = True


def current_user() -> Optional[Dict[str, Any]]:
    user = getattr(g, "current_user", None)
    return user if isinstance(user, dict) else None


def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not _settings.AUTH_ENABLED:
            return func(*args, **kwargs)
        if current_user() is None:
            return _unauthorized_response()
        return func(*args, **kwargs)

    return wrapper


def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not _settings.AUTH_ENABLED:
            return func(*args, **kwargs)
        user = current_user()
        if user is None:
            return _unauthorized_response()
        if not user.get("is_admin"):
            return _forbidden_response("Admin access required.")
        return func(*args, **kwargs)

    return wrapper


def get_csrf_token() -> str:
    token = session.get("csrf_token")
    if token:
        return str(token)
    token = secrets.token_urlsafe(24)
    session["csrf_token"] = token
    return token


def validate_csrf() -> bool:
    if not _settings.AUTH_ENABLED:
        return True
    sent = request.form.get("csrf_token") or request.headers.get("X-CSRF-Token")
    expected = session.get("csrf_token")
    if not sent or not expected:
        return False
    return secrets.compare_digest(str(sent), str(expected))


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _is_api_request() -> bool:
    if request.headers.get("X-Requested-With") == "fetch":
        return True
    accept = request.headers.get("Accept", "")
    return "application/json" in accept


def _unauthorized_response() -> Any:
    if _is_api_request():
        return jsonify({"error": "Authentication required."}), 401
    return redirect(url_for("bp.auth_login", next=request.path))


def _forbidden_response(message: str = "Forbidden") -> Any:
    if _is_api_request():
        return jsonify({"error": message}), 403
    return (message, 403)


def ensure_logged_user_from_session() -> None:
    g.current_user = None
    if not _settings.AUTH_ENABLED:
        return
    sid = session.get("sid")
    ensure_auth_store()
    if sid:
        user = auth_store.get_user_by_session(_settings.DB_PATH, str(sid))
        if user is not None and user.get("is_active"):
            g.current_user = user
            return
        session.pop("sid", None)

    raw = request.headers.get("Authorization", "")
    token = ""
    if raw.lower().startswith("bearer "):
        token = raw.split(" ", 1)[1].strip()
    if not token:
        return
    try:
        user = _exchange_clerk_token(token)
    except Exception:
        return
    sid = auth_store.create_session(
        _settings.DB_PATH, int(user["id"]), _settings._config.session_ttl_seconds
    )
    session["sid"] = sid
    g.current_user = user


def user_can_access_job(job_id: str) -> bool:
    if not _settings.AUTH_ENABLED:
        return True
    user = current_user()
    owner_id = auth_store.get_job_owner_id(_settings.DB_PATH, job_id)
    if user is None:
        if job_id != DEFAULT_PREVIEW_JOB_ID or owner_id is not None:
            return False
        from .jobs import JOBS, JOBS_LOCK  # avoid circular at module level

        with JOBS_LOCK:
            job = JOBS.get(job_id)
        return job is not None and job.user_id is None and job.status == "done"
    return owner_id is not None and owner_id == user["id"]


def enforce_rate_limits(user_id: int) -> Optional[str]:
    now = time.time()
    hour_count = auth_store.count_build_requests_since(_settings.DB_PATH, user_id, now - 3600)
    if hour_count >= _settings._config.rate_limit_hourly:
        return f"Hourly limit reached ({_settings._config.rate_limit_hourly}/hour)."
    day_count = auth_store.count_build_requests_since(_settings.DB_PATH, user_id, now - 86400)
    if day_count >= _settings._config.rate_limit_daily:
        return f"Daily limit reached ({_settings._config.rate_limit_daily}/day)."
    active_count = auth_store.count_active_jobs(_settings.DB_PATH, user_id)
    if active_count >= _settings._config.max_active_jobs_per_user:
        return "Active job limit reached. Wait for running jobs to finish."
    return None


def verify_hmac_request() -> bool:
    key_id = request.headers.get("X-Key-Id", "")
    signature = request.headers.get("X-Signature", "")
    nonce = request.headers.get("X-Nonce", "")
    timestamp_raw = request.headers.get("X-Timestamp", "")
    if not (_settings.HMAC_KEYS and key_id and signature and nonce and timestamp_raw):
        return False
    try:
        timestamp = int(timestamp_raw)
    except ValueError:
        return False
    if not validate_timestamp(timestamp, _settings._config.hmac_max_skew_seconds):
        return False
    secret = choose_secret(_settings.HMAC_KEYS, key_id)
    if not secret:
        return False
    body = request.get_data(cache=True) or b""
    path = request.path
    payload = canonical_payload(request.method, path, timestamp, nonce, body)
    if not verify_signature(secret, payload, signature):
        return False
    ensure_auth_store()
    return auth_store.consume_nonce(
        _settings.DB_PATH, nonce, _settings._config.hmac_nonce_ttl_seconds
    )


# ---------------------------------------------------------------------------
# Clerk integration
# ---------------------------------------------------------------------------


def clerk_auth_ready() -> bool:
    return bool(_settings._config.clerk_publishable_key and _settings._config.clerk_secret_key)


_JWKS_CLIENT_CACHE: dict[str, tuple[jwt.PyJWKClient, float]] = {}
_JWKS_CACHE_LOCK = threading.Lock()
_JWKS_CACHE_TTL = 3600  # seconds — refresh after 1 h to pick up key rotations


def _clerk_jwk_client(jwks_url: str) -> jwt.PyJWKClient:
    """Return a cached PyJWKClient for *jwks_url*, refreshed every hour."""
    with _JWKS_CACHE_LOCK:
        entry = _JWKS_CLIENT_CACHE.get(jwks_url)
        if entry is not None:
            client, expires_at = entry
            if time.monotonic() < expires_at:
                return client
        client = jwt.PyJWKClient(jwks_url, cache_keys=True)
        _JWKS_CLIENT_CACHE[jwks_url] = (client, time.monotonic() + _JWKS_CACHE_TTL)
        return client


def _verify_clerk_session_token(raw_token: str) -> Dict[str, Any]:
    jwks_url = str(_settings._config.clerk_jwks_url or "").strip()
    if not jwks_url:
        raise RuntimeError("CLERK_JWKS_URL is not configured.")
    jwk_client = _clerk_jwk_client(jwks_url)
    signing_key = jwk_client.get_signing_key_from_jwt(raw_token)
    configured_issuer = str(_settings._config.clerk_issuer or "").strip()
    claims = jwt.decode(
        raw_token,
        signing_key.key,
        algorithms=["RS256"],
        options={"require": ["sub", "exp", "iat", "iss"]},
    )
    # Accept issuer values that differ only by trailing slash.
    if configured_issuer:
        token_issuer = str(claims.get("iss") or "").strip()
        if token_issuer.rstrip("/") != configured_issuer.rstrip("/"):
            raise RuntimeError("Invalid issuer")
    azp = str(claims.get("azp") or "")
    if (
        _settings._config.clerk_authorized_parties
        and azp not in _settings._config.clerk_authorized_parties
    ):
        raise RuntimeError("Token authorized party is not allowed.")
    return claims


def _clerk_primary_email(user_payload: Dict[str, Any]) -> str:
    primary_id = str(user_payload.get("primary_email_address_id") or "")
    addresses = user_payload.get("email_addresses") or []
    if isinstance(addresses, list):
        for item in addresses:
            if not isinstance(item, dict):
                continue
            if primary_id and str(item.get("id") or "") != primary_id:
                continue
            email = str(item.get("email_address") or "").strip().lower()
            if email:
                return email
        for item in addresses:
            if not isinstance(item, dict):
                continue
            email = str(item.get("email_address") or "").strip().lower()
            if email:
                return email
    return ""


def _fetch_clerk_user_email(clerk_user_id: str) -> str:
    if not _settings._config.clerk_secret_key:
        raise RuntimeError("Missing CLERK_SECRET_KEY.")
    resp = requests.get(
        f"{_settings._config.clerk_api_url.rstrip('/')}/users/{clerk_user_id}",
        headers={"Authorization": f"Bearer {_settings._config.clerk_secret_key}"},
        timeout=20,
    )
    resp.raise_for_status()
    payload = resp.json()
    email = _clerk_primary_email(payload)
    if not email:
        raise RuntimeError("No email found on Clerk user profile.")
    return email


def _exchange_clerk_token(raw_token: str) -> Dict[str, Any]:
    claims = _verify_clerk_session_token(raw_token)
    clerk_user_id = str(claims.get("sub") or "").strip()
    if not clerk_user_id:
        raise RuntimeError("Missing Clerk user id (sub) claim.")

    email = str(claims.get("email") or "").strip().lower()
    if not email:
        email = _fetch_clerk_user_email(clerk_user_id)
    if not email:
        raise RuntimeError("Unable to resolve user email from Clerk.")

    if _settings._config.clerk_allowed_domain and not email.endswith(
        "@" + _settings._config.clerk_allowed_domain
    ):
        raise RuntimeError("Account domain is not allowed.")

    user = auth_store.find_user_by_email(_settings.DB_PATH, email)
    if _settings._config.require_local_allowlist:
        if user is None or not user.get("is_active"):
            raise RuntimeError("Access denied for this account.")
        return user

    is_admin = bool(_settings._config.admin_email and email == _settings._config.admin_email)
    merged_admin = is_admin or bool(user and user.get("is_admin"))
    auth_store.upsert_user(_settings.DB_PATH, email, is_admin=merged_admin, is_active=True)
    user = auth_store.find_user_by_email(_settings.DB_PATH, email)
    if user is None:
        raise RuntimeError("Failed to initialize local user session.")
    return user
