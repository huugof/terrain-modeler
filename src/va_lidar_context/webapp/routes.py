"""All Flask route handlers, before_request hooks, and context processors."""

from __future__ import annotations

import io
import os
import re
import shutil
import threading
import time
import zipfile
from functools import wraps
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import urlparse as _urlparse

from flask import (
    Blueprint,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    send_file,
    send_from_directory,
    session,
    url_for,
)

from .. import auth_store
from ..config import (
    DEFAULT_EPT_ONLY,
    DEFAULT_FILL_MAX_DIST,
    DEFAULT_FILL_SMOOTHING,
    DEFAULT_FLOOR_TO_FLOOR,
    DEFAULT_FORMAT,
    DEFAULT_NAIP_FLIP_U,
    DEFAULT_NAIP_FLIP_V,
    DEFAULT_PERCENTILE,
    DEFAULT_PREFER_EPT,
    DEFAULT_UNITS,
    DEFAULT_XYZ_MODE,
    BuildConfig,
)
from ..pipeline.io import generate_job_id
from ..providers.usgs_index import query_for_point
from ..util import ensure_dir, get_logger
from . import jobs as _jobs_module
from . import rate_limiter as _rl
from . import settings as _settings
from .auth import (
    _exchange_clerk_token,
    _forbidden_response,
    _unauthorized_response,
    clerk_auth_ready,
    current_user,
    enforce_rate_limits,
    ensure_auth_store,
    ensure_logged_user_from_session,
    get_csrf_token,
    user_can_access_job,
    validate_csrf,
    verify_hmac_request,
)
from .forms import (
    ALLOWED_IMAGE_QUALITY,
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
from .jobs import (
    JOBS,
    JOBS_LOCK,
    Job,
    _collect_outputs,
    _job_logs_payload,
    _jobs_for_user,
    _list_job_artifacts,
    _notify_recent_jobs_change,
    _persist_job_snapshot,
    _recent_job_payload,
    _recent_jobs_change_cond,
    _resolve_job_output_dir,
    _run_build_job,
    sanitize_job_error,
)
from .settings import (
    CLEANUP_INTERVAL_SECONDS,
    COVERAGE_CACHE_TTL_SECONDS,
    DESKTOP_HOST,
    DESKTOP_MODE,
    DESKTOP_PORT,
    JOB_LOG_WAIT_MAX_SECONDS,
    RECENT_JOBS_LIMIT,
    RECENT_JOBS_WAIT_MAX_SECONDS,
)

bp = Blueprint("bp", __name__)

_coverage_cache: Dict[str, tuple[float, Optional[bool], str]] = {}
_coverage_cache_lock = threading.Lock()

# --- M7: per-user long-poll connection cap ---
_LONGPOLL_COUNTS: Dict[str, int] = {}
_LONGPOLL_LOCK = threading.Lock()
_LONGPOLL_MAX_PER_USER = int(os.getenv("LONGPOLL_MAX_PER_USER", "3"))


class _LongPollSlot:
    """Context manager that acquires/releases a long-poll slot for a user.

    Prevents a single user from exhausting all WSGI worker threads by opening
    many concurrent ``?wait=N`` requests.  Only use when ``wait_seconds > 0``.
    """

    def __init__(self, user_key: str) -> None:
        self.user_key = user_key
        self.acquired = False

    def __enter__(self) -> "_LongPollSlot":
        with _LONGPOLL_LOCK:
            count = _LONGPOLL_COUNTS.get(self.user_key, 0)
            if count >= _LONGPOLL_MAX_PER_USER:
                return self
            _LONGPOLL_COUNTS[self.user_key] = count + 1
            self.acquired = True
        return self

    def __exit__(self, *_: Any) -> None:
        if self.acquired:
            with _LONGPOLL_LOCK:
                _LONGPOLL_COUNTS[self.user_key] = max(0, _LONGPOLL_COUNTS.get(self.user_key, 1) - 1)


def _longpoll_user_key() -> str:
    """Return a stable key identifying the current requester for long-poll throttling."""
    user = current_user()
    if user is not None:
        return f"user:{user['id']}"
    return f"ip:{request.remote_addr or 'unknown'}"


def _rate_limit(endpoint: str, hourly: int, daily: int):
    """Decorator factory: apply IP-keyed sliding-window rate limiting to a route."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            allowed, msg = _rl.check(endpoint, hourly, daily)
            if not allowed:
                return jsonify({"error": msg}), 429
            return func(*args, **kwargs)

        return wrapper

    return decorator


def _safe_next_path(value: Any) -> str:
    """Return *value* only when it is a safe relative path; otherwise return '/'.

    Rejects protocol-relative URLs (//evil.com) and any value that has a
    scheme or netloc component after parsing.
    """
    path = str(value or "/").strip()
    if not path.startswith("/"):
        return "/"
    parsed = _urlparse(path)
    if parsed.netloc or parsed.scheme:
        return "/"
    return path


# ---------------------------------------------------------------------------
# Cleanup helpers (live in routes since they depend on app-level settings)
# ---------------------------------------------------------------------------


def _cleanup_out_dir(logger: Any) -> None:
    if _settings.RETENTION_DAYS <= 0:
        return
    cutoff = time.time() - (_settings.RETENTION_DAYS * 86400)
    if not _settings.OUT_DIR.exists():
        return
    for entry in _settings.OUT_DIR.iterdir():
        try:
            stat = entry.stat()
            if stat.st_mtime > cutoff:
                continue
            if entry.is_dir():
                shutil.rmtree(entry)
            else:
                entry.unlink()
            logger.info(f"Cleanup: removed {entry}")
        except Exception as exc:
            logger.warning(f"Cleanup failed for {entry}: {exc}")


def _cleanup_loop() -> None:
    logger = get_logger()
    while True:
        _cleanup_out_dir(logger)
        _rl.cleanup_expired()
        time.sleep(CLEANUP_INTERVAL_SECONDS)


_cleanup_thread_started = False
_cleanup_thread_lock = threading.Lock()


def _ensure_cleanup_thread() -> None:
    global _cleanup_thread_started
    with _cleanup_thread_lock:
        if _cleanup_thread_started:
            return
        thread = threading.Thread(target=_cleanup_loop, daemon=True)
        thread.start()
        _cleanup_thread_started = True


# ---------------------------------------------------------------------------
# Hooks
# ---------------------------------------------------------------------------


@bp.before_app_request
def _start_cleanup():
    _ensure_cleanup_thread()
    ensure_auth_store()
    ensure_logged_user_from_session()


@bp.app_context_processor
def inject_user_context():
    return {
        "current_user": current_user(),
        "auth_enabled": _settings.AUTH_ENABLED,
        "desktop_mode": DESKTOP_MODE,
        "csrf_token": get_csrf_token,
    }


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@bp.route("/healthz")
@_rate_limit("healthz", hourly=120, daily=2000)
def healthz():
    return jsonify({"status": "ok"})


@bp.route("/auth/login")
def auth_login():
    if not _settings.AUTH_ENABLED:
        return redirect(url_for("bp.index"))
    if not clerk_auth_ready():
        return ("Clerk auth is not configured.", 500)
    next_path = _safe_next_path(request.args.get("next"))
    force_sign_out = request.args.get("logged_out", "").lower() in ("1", "true", "yes")
    from .settings import (
        CLERK_FRONTEND_API_URL,
        CLERK_PUBLISHABLE_KEY,
        CLERK_SIGN_IN_URL,
    )

    return render_template(
        "auth_login.html",
        next_path=next_path,
        force_sign_out=force_sign_out,
        clerk_publishable_key=CLERK_PUBLISHABLE_KEY,
        clerk_sign_in_url=CLERK_SIGN_IN_URL,
        clerk_frontend_api_url=CLERK_FRONTEND_API_URL,
    )


@bp.route("/auth/clerk/exchange", methods=["POST"])
@_rate_limit("clerk_exchange", hourly=20, daily=100)
def auth_clerk_exchange():
    if not _settings.AUTH_ENABLED:
        return redirect(url_for("bp.index"))
    payload = request.get_json(silent=True) or {}
    raw_token = str(payload.get("token") or "").strip()
    next_path = _safe_next_path(payload.get("next"))
    if not raw_token:
        return jsonify({"error": "Missing Clerk session token."}), 400
    try:
        user = _exchange_clerk_token(raw_token)
    except Exception as exc:
        return jsonify({"error": f"Clerk auth failed: {exc}"}), 403

    sid = auth_store.create_session(
        _settings.DB_PATH, int(user["id"]), _settings.SESSION_TTL_SECONDS
    )
    session["sid"] = sid
    get_csrf_token()
    return jsonify({"ok": True, "next": next_path})


@bp.route("/auth/callback")
def auth_callback():
    return redirect(url_for("bp.auth_login"))


@bp.route("/auth/logout", methods=["POST"])
def auth_logout():
    if _settings.AUTH_ENABLED and not validate_csrf():
        return ("Invalid CSRF token.", 400)
    sid = session.get("sid")
    if sid:
        ensure_auth_store()
        auth_store.revoke_session(_settings.DB_PATH, str(sid))
    session.clear()
    if _settings.AUTH_ENABLED:
        return redirect(url_for("bp.auth_login", next="/", logged_out=1))
    return redirect(url_for("bp.index"))


@bp.route("/")
def index():
    defaults = snapshot_defaults()
    prefill_job_id = (request.args.get("from_job") or "").strip()
    if prefill_job_id and user_can_access_job(prefill_job_id):
        with JOBS_LOCK:
            prefill_job = JOBS.get(prefill_job_id)
        if prefill_job is not None:
            defaults = merge_prefill_defaults(defaults, prefill_job.summary.get("form_defaults"))
    parcel_sources = parcel_sources_payload()
    data_sources = data_sources_payload(parcel_sources)
    user = current_user()
    can_build = (not _settings.AUTH_ENABLED) or (user is not None)
    jobs = _jobs_for_user(user)
    sequence_by_job_id = {job.job_id: idx + 1 for idx, job in enumerate(jobs)}
    recent_jobs = jobs[-RECENT_JOBS_LIMIT:][::-1]
    recent_jobs_data = [
        _recent_job_payload(job, sequence_by_job_id.get(job.job_id, 0)) for job in recent_jobs
    ]
    return render_template(
        "index.html",
        defaults=defaults,
        data_sources=data_sources,
        parcel_sources=parcel_sources,
        recent_jobs=recent_jobs_data,
        can_build=can_build,
        retention_days=_settings.RETENTION_DAYS,
    )


@bp.route("/recent-jobs")
def recent_jobs():
    if _settings.AUTH_ENABLED and current_user() is None:
        return _unauthorized_response()
    since = parse_int(request.args.get("since")) or 0
    wait_seconds = parse_float(request.args.get("wait")) or 0.0
    since = max(0, since)
    wait_seconds = max(0.0, min(wait_seconds, RECENT_JOBS_WAIT_MAX_SECONDS))
    if wait_seconds > 0.0:
        with _LongPollSlot(_longpoll_user_key()) as slot:
            if not slot.acquired:
                return jsonify({"error": "Too many concurrent poll connections."}), 429
            deadline = time.monotonic() + wait_seconds
            while True:
                with _recent_jobs_change_cond:
                    current_version = _jobs_module._recent_jobs_change_version
                    if current_version != since:
                        break
                    remaining = deadline - time.monotonic()
                    if remaining <= 0.0:
                        break
                    _recent_jobs_change_cond.wait(timeout=remaining)
                    if _jobs_module._recent_jobs_change_version == current_version:
                        break
    with _recent_jobs_change_cond:
        current_version = _jobs_module._recent_jobs_change_version

    user = current_user()
    jobs = _jobs_for_user(user)
    sequence_by_job_id = {job.job_id: idx + 1 for idx, job in enumerate(jobs)}
    recent = jobs[-RECENT_JOBS_LIMIT:][::-1]
    payload = [_recent_job_payload(job, sequence_by_job_id.get(job.job_id, 0)) for job in recent]
    return jsonify({"jobs": payload, "version": current_version})


@bp.route("/admin/users")
def admin_users():
    if _settings.AUTH_ENABLED and (current_user() is None or not current_user().get("is_admin")):
        return _forbidden_response("Admin access required.")
    users = auth_store.list_users(_settings.DB_PATH)
    return render_template("admin_users.html", users=users)


@bp.route("/admin/users", methods=["POST"])
def admin_users_upsert():
    if _settings.AUTH_ENABLED and (current_user() is None or not current_user().get("is_admin")):
        return _forbidden_response("Admin access required.")
    if not validate_csrf():
        return ("Invalid CSRF token.", 400)
    email = (request.form.get("email") or "").strip().lower()
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return ("Invalid email.", 400)
    is_admin = request.form.get("is_admin") is not None
    is_active = request.form.get("is_active") is not None
    auth_store.upsert_user(_settings.DB_PATH, email, is_admin=is_admin, is_active=is_active)
    return redirect(url_for("bp.admin_users"))


@bp.route("/coverage")
@_rate_limit("coverage", hourly=60, daily=500)
def coverage():
    lon = parse_float(request.args.get("lon"))
    lat = parse_float(request.args.get("lat"))
    if lon is None or lat is None:
        return jsonify({"supported": None, "error": "Invalid coordinates"}), 400

    provider = resolve_provider(lat, lon)
    cache_key = coverage_cache_key(lon, lat)
    now = time.time()
    with _coverage_cache_lock:
        cached = _coverage_cache.get(cache_key)
        if cached is not None:
            ts, supported_cached, provider_cached = cached
            if now - ts <= COVERAGE_CACHE_TTL_SECONDS and provider_cached == provider:
                return jsonify(
                    {
                        "supported": supported_cached,
                        "provider": provider,
                        "cached": True,
                    }
                )
            _coverage_cache.pop(cache_key, None)

    supported: Optional[bool] = None
    error = None
    if provider == "va":
        supported = is_in_virginia(lon, lat)
    else:
        try:
            supported = bool(query_for_point(lon, lat))
        except Exception as exc:
            error = str(exc)
            supported = None

    result_payload = {"supported": supported, "provider": provider}
    if error:
        result_payload["error"] = error
    if supported is not None:
        with _coverage_cache_lock:
            _coverage_cache[cache_key] = (now, supported, provider)
    return jsonify(result_payload)


@bp.route("/run", methods=["POST"])
def run_job():
    if _settings.AUTH_ENABLED and current_user() is None:
        return _unauthorized_response()
    if not validate_csrf():
        return jsonify({"error": "Invalid CSRF token."}), 400

    user = current_user()
    user_id = int(user["id"]) if user else None
    if _settings.AUTH_ENABLED and user_id is not None:
        limit_error = enforce_rate_limits(user_id)
        if limit_error:
            return jsonify({"error": limit_error}), 429

    form = request.form
    custom_name = (form.get("job_name") or "").strip()
    if len(custom_name) > 120:
        return jsonify({"error": "Name must be 120 characters or fewer."}), 400
    out_dir = _settings.OUT_DIR
    ensure_dir(out_dir)
    _raw_units = (form.get("units") or DEFAULT_UNITS).strip().lower()
    units = _raw_units if _raw_units in ("feet", "meters") else DEFAULT_UNITS
    coords = form.get("coords") or ""
    parts = [p for p in re.split(r"[ ,]+", coords.strip()) if p]
    lat = parse_float(parts[0]) if len(parts) > 0 else None
    lon = parse_float(parts[1]) if len(parts) > 1 else None
    provider = resolve_provider(lat, lon)
    clip_size = parse_float(form.get("size"))
    if lat is None or lon is None:
        return jsonify({"error": "Provide coordinates as lat, lon."}), 400
    if clip_size is None:
        return jsonify({"error": "Provide a clip size."}), 400
    if clip_size <= 0:
        return jsonify({"error": "Clip size must be greater than 0."}), 400
    if clip_size > _settings.MAX_CLIP_SIZE:
        return jsonify({"error": f"Clip size exceeds max ({_settings.MAX_CLIP_SIZE:g})."}), 400

    center = (lat, lon) if lat is not None and lon is not None else None

    from ..config import DEFAULT_RESOLUTION

    resolution = DEFAULT_RESOLUTION
    terrain_complexity = parse_int(form.get("terrain_complexity"))
    if terrain_complexity is None:
        terrain_complexity = 2
    terrain_complexity = max(0, min(10, terrain_complexity))
    terrain_sample = max(1, 11 - terrain_complexity)
    fill_dtm = True
    fill_hard = True
    fill_max_dist = DEFAULT_FILL_MAX_DIST
    fill_smoothing = DEFAULT_FILL_SMOOTHING

    percentile = DEFAULT_PERCENTILE
    min_height = parse_float(form.get("min_height"))
    if min_height is None:
        from ..config import DEFAULT_MIN_HEIGHT

        min_height = DEFAULT_MIN_HEIGHT
    max_height = parse_float(form.get("max_height"))
    if max_height is None:
        from ..config import DEFAULT_MAX_HEIGHT

        max_height = DEFAULT_MAX_HEIGHT
    floor_to_floor = DEFAULT_FLOOR_TO_FLOOR

    random_min = parse_float(form.get("random_min_height"))
    if random_min is None:
        from .settings import DEFAULT_RANDOM_MIN_HEIGHT

        random_min = DEFAULT_RANDOM_MIN_HEIGHT
    random_max = parse_float(form.get("random_max_height"))
    if random_max is None:
        from .settings import DEFAULT_RANDOM_MAX_HEIGHT

        random_max = DEFAULT_RANDOM_MAX_HEIGHT
    random_seed = None

    naip_pixel_size, naip_max_size, naip_tiled = resolve_image_quality(form.get("image_quality"))
    naip_flip_u = DEFAULT_NAIP_FLIP_U
    naip_flip_v = DEFAULT_NAIP_FLIP_V

    outputs = []
    if parse_bool(form.get("output_terrain")):
        outputs.append("terrain")
    if parse_bool(form.get("output_buildings")):
        outputs.append("buildings")
    if parse_bool(form.get("output_contours")):
        outputs.append("contours")
    if parse_bool(form.get("output_naip")):
        outputs.append("naip")
    if parse_bool(form.get("output_xyz")):
        outputs.append("xyz")
    if not outputs:
        return jsonify({"error": "Select at least one output."}), 400
    output_terrain = "terrain" in outputs
    output_buildings = "buildings" in outputs
    output_contours = "contours" in outputs
    output_naip = "naip" in outputs
    output_xyz = "xyz" in outputs

    combine_output = False  # not exposed in web form; available via CLI --combine-output

    contours_enabled = "contours" in outputs
    xyz_enabled = "xyz" in outputs
    xyz_mode = (form.get("xyz_mode") or DEFAULT_XYZ_MODE).strip().lower()
    if xyz_mode not in ("contours", "grid"):
        xyz_mode = DEFAULT_XYZ_MODE
    contour_interval = (
        (parse_float(form.get("contour_interval")) or 2.0)
        if (contours_enabled or (xyz_enabled and xyz_mode == "contours"))
        else None
    )
    xyz_contour_spacing = parse_float(form.get("xyz_contour_spacing"))
    if xyz_mode != "contours":
        xyz_contour_spacing = None
    if xyz_contour_spacing is not None and xyz_contour_spacing <= 0:
        xyz_contour_spacing = None
    dxf_contour_spacing = parse_float(form.get("dxf_contour_spacing")) if contours_enabled else None
    if dxf_contour_spacing is not None and dxf_contour_spacing <= 0:
        dxf_contour_spacing = None
    dxf_include_parcels = parse_bool(form.get("dxf_include_parcels")) if contours_enabled else False
    dxf_include_buildings = (
        parse_bool(form.get("dxf_include_buildings")) if contours_enabled else False
    )
    keep_rasters = False

    flip_x = False
    flip_y = False
    terrain_flip_y = False
    rotate_z = parse_float(form.get("rotate_z"))
    if rotate_z is None:
        rotate_z = 0.0
    allow_multi_tile = True
    force = False

    job_id = generate_job_id(center, clip_size, units)
    cfg = BuildConfig(
        job_id=job_id,
        center=center,
        out_dir=out_dir,
        force=force,
        fmt=DEFAULT_FORMAT,
        units=units,
        resolution=resolution,
        percentile=percentile,
        min_height=min_height,
        max_height=max_height,
        floor_to_floor=floor_to_floor,
        keep_rasters=keep_rasters,
        terrain_sample=terrain_sample,
        fill_dtm=fill_dtm,
        fill_hard=fill_hard,
        fill_max_dist=fill_max_dist,
        fill_smoothing=fill_smoothing,
        random_heights_min=random_min,
        random_heights_max=random_max,
        random_seed=random_seed,
        naip_pixel_size=naip_pixel_size,
        naip_max_size=naip_max_size,
        naip_tiled=naip_tiled,
        naip_flip_u=naip_flip_u,
        naip_flip_v=naip_flip_v,
        combine_output=combine_output,
        contour_interval=contour_interval,
        size=clip_size,
        allow_multi_tile=allow_multi_tile,
        prefer_ept=DEFAULT_PREFER_EPT,
        flip_y=flip_y,
        flip_x=flip_x,
        terrain_flip_y=terrain_flip_y,
        rotate_z=rotate_z,
        xyz_mode=xyz_mode,
        xyz_contour_spacing=xyz_contour_spacing,
        dxf_contour_spacing=dxf_contour_spacing,
        dxf_include_parcels=dxf_include_parcels,
        dxf_include_buildings=dxf_include_buildings,
        provider=provider,
        ept_only=DEFAULT_EPT_ONLY,
        cleanup_intermediates=True,
        outputs=tuple(outputs),
    )

    target_summary = None
    if lat is not None and lon is not None:
        target_summary = f"latlon:{lat},{lon} size={clip_size}"

    summary = {
        "out": str(out_dir),
        "target": target_summary or "(tile lookup)",
        "provider": provider,
        "provider_label": provider_label(provider),
        "name": custom_name or job_id,
        "custom_name": custom_name,
        "form_defaults": extract_form_defaults(
            coords=f"{lat},{lon}",
            clip_size=clip_size,
            units=units,
            terrain_complexity=terrain_complexity,
            rotate_z=rotate_z,
            contour_interval=contour_interval,
            dxf_contour_spacing=dxf_contour_spacing,
            dxf_include_parcels=dxf_include_parcels,
            dxf_include_buildings=dxf_include_buildings,
            xyz_mode=xyz_mode,
            image_quality=_raw_iq
            if (_raw_iq := (form.get("image_quality") or "standard").strip().lower())
            in ALLOWED_IMAGE_QUALITY
            else "standard",
            random_min_height=random_min,
            random_max_height=random_max,
            output_terrain=output_terrain,
            output_buildings=output_buildings,
            output_contours=output_contours,
            output_naip=output_naip,
            output_xyz=output_xyz,
            custom_name=custom_name,
        ),
    }

    job = Job(
        job_id=job_id,
        status="queued",
        created_at=time.time(),
        user_id=user_id,
        summary=summary,
    )

    with JOBS_LOCK:
        JOBS[job_id] = job
    _persist_job_snapshot(job)
    _notify_recent_jobs_change()
    if _settings.AUTH_ENABLED:
        auth_store.record_job_owner(_settings.DB_PATH, job_id, user_id)
    if user_id is not None:
        auth_store.add_build_request(_settings.DB_PATH, user_id)
        auth_store.set_active_job(_settings.DB_PATH, job_id, user_id, status="queued")

    thread = threading.Thread(target=_run_build_job, args=(job, cfg), daemon=True)
    thread.start()

    if request.headers.get("X-Requested-With") == "fetch":
        return jsonify({"job_id": job_id})
    return redirect(url_for("bp.job_status", job_id=job_id))


@bp.route("/jobs/<job_id>")
def job_status(job_id: str):
    if _settings.AUTH_ENABLED and current_user() is None:
        return _unauthorized_response()
    if not user_can_access_job(job_id):
        return _forbidden_response("Not allowed to access this job.")
    with JOBS_LOCK:
        job = JOBS.get(job_id)
    if job is None:
        return "Job not found", 404
    embed_mode = request.args.get("embed", "").strip().lower() in ("1", "true", "yes")
    return render_template(
        "job_status.html",
        job=job,
        status_label=status_label,
        status_class=status_class,
        embed_mode=embed_mode,
    )


@bp.route("/logs/<job_id>")
def job_logs(job_id: str):
    if _settings.AUTH_ENABLED and current_user() is None:
        return _unauthorized_response()
    if not user_can_access_job(job_id):
        return _forbidden_response("Not allowed to access this job.")
    offset = parse_int(request.args.get("offset")) or 0
    wait_seconds = parse_float(request.args.get("wait")) or 0.0
    offset = max(0, offset)
    wait_seconds = max(0.0, min(wait_seconds, JOB_LOG_WAIT_MAX_SECONDS))

    with JOBS_LOCK:
        job = JOBS.get(job_id)
    if job is None:
        return jsonify({"error": "Job not found"}), 404

    if wait_seconds <= 0.0:
        with job.change_cond:
            return jsonify(_job_logs_payload(job, offset))

    with _LongPollSlot(_longpoll_user_key()) as slot:
        if not slot.acquired:
            return jsonify({"error": "Too many concurrent poll connections."}), 429
        deadline = time.monotonic() + wait_seconds
        while True:
            with job.change_cond:
                payload = _job_logs_payload(job, offset)
                status = str(payload.get("status") or "")
                has_logs = bool(payload.get("logs"))
                is_active = status in ("queued", "running")
                if has_logs or not is_active:
                    return jsonify(payload)
                remaining = deadline - time.monotonic()
                if remaining <= 0.0:
                    return jsonify(payload)
                observed_version = job.change_version
                job.change_cond.wait(timeout=remaining)
                if job.change_version == observed_version:
                    return jsonify(_job_logs_payload(job, offset))


@bp.route("/jobs/<job_id>/artifacts")
def job_artifacts(job_id: str):
    if _settings.AUTH_ENABLED and current_user() is None:
        return _unauthorized_response()
    if not user_can_access_job(job_id):
        return _forbidden_response("Not allowed to access this job.")
    with JOBS_LOCK:
        job = JOBS.get(job_id)
    if job is None:
        return jsonify({"error": "Job not found"}), 404

    artifacts = _list_job_artifacts(job)
    payload = [
        {
            "name": item["name"],
            "size": item["size"],
            "mtime": item["mtime"],
            "download_url": url_for("bp.job_download", job_id=job_id, name=item["name"]),
        }
        for item in artifacts
    ]
    return jsonify({"job_id": job_id, "files": payload})


@bp.route("/jobs/<job_id>/download/<name>")
def job_download(job_id: str, name: str):
    if "/" in name or "\\" in name:
        return jsonify({"error": "Invalid file name."}), 400
    if _settings.AUTH_ENABLED and current_user() is None:
        return _unauthorized_response()
    if not user_can_access_job(job_id):
        return _forbidden_response("Not allowed to access this job.")
    with JOBS_LOCK:
        job = JOBS.get(job_id)
    if job is None:
        return ("Job not found", 404)

    output_dir = _resolve_job_output_dir(job)
    if output_dir is None:
        return ("No artifacts available for this job.", 404)
    file_path = output_dir / name
    if not file_path.is_file():
        return ("File not found", 404)
    inline = request.args.get("inline", "").lower() in ("1", "true", "yes")
    output_dir_abs = output_dir.resolve()
    return send_from_directory(
        str(output_dir_abs),
        name,
        as_attachment=not inline,
        download_name=name,
    )


@bp.route("/jobs/<job_id>/download-all")
def job_download_all(job_id: str):
    if _settings.AUTH_ENABLED and current_user() is None:
        return _unauthorized_response()
    if not user_can_access_job(job_id):
        return _forbidden_response("Not allowed to access this job.")
    with JOBS_LOCK:
        job = JOBS.get(job_id)
    if job is None:
        return ("Job not found", 404)
    output_dir = _resolve_job_output_dir(job)
    if output_dir is None:
        return ("No artifacts available for this job.", 404)
    artifacts = _list_job_artifacts(job)
    if not artifacts:
        return ("No artifacts available for this job.", 404)

    data = io.BytesIO()
    with zipfile.ZipFile(data, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        for artifact in artifacts:
            name = artifact["name"]
            path = output_dir / name
            if path.is_file():
                archive.write(path, arcname=name)
    data.seek(0)
    return send_file(
        data,
        mimetype="application/zip",
        as_attachment=True,
        download_name=f"{job_id}_artifacts.zip",
    )


@bp.route("/internal/worker/jobs/<job_id>/complete", methods=["POST"])
def worker_job_complete(job_id: str):
    if not verify_hmac_request():
        return jsonify({"error": "Unauthorized callback."}), 401
    payload = request.get_json(silent=True) or {}
    with JOBS_LOCK:
        job = JOBS.get(job_id)
    if job is None:
        return jsonify({"error": "Job not found."}), 404

    with job.change_cond:
        job.status = payload.get("status", job.status)
        job.exit_code = payload.get("exit_code", job.exit_code)
        if "error" in payload:
            job.error = sanitize_job_error(payload.get("error"))
        summary = payload.get("summary")
        if isinstance(summary, dict):
            job.summary.update(summary)
        from .jobs import _notify_job_change_locked

        _notify_job_change_locked(job)
    _notify_recent_jobs_change()
    if _settings.AUTH_ENABLED and job.status in ("done", "error"):
        auth_store.set_job_status(_settings.DB_PATH, job_id, job.status)
        auth_store.finish_active_job(_settings.DB_PATH, job_id, job.status)
    _persist_job_snapshot(job)
    return jsonify({"ok": True})
