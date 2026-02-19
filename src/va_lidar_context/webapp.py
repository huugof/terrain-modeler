from __future__ import annotations

import argparse
import functools
import io
import json
import logging
import os
import re
import secrets
import shutil
import threading
import time
import zipfile
from dataclasses import dataclass, field
from functools import wraps
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

import jwt
import requests
from flask import (
    Flask,
    g,
    jsonify,
    redirect,
    render_template,
    render_template_string,
    request,
    send_file,
    send_from_directory,
    session,
    url_for,
)

from . import auth_store
from .config import (
    DEFAULT_COMBINE_OUTPUT,
    DEFAULT_DESKTOP_HOST,
    DEFAULT_DESKTOP_MODE,
    DEFAULT_DESKTOP_OUT_DIR,
    DEFAULT_DESKTOP_PORT,
    DEFAULT_DESKTOP_RETENTION_DAYS,
    DEFAULT_DXF_CONTOUR_SPACING,
    DEFAULT_DXF_INCLUDE_BUILDINGS,
    DEFAULT_DXF_INCLUDE_PARCELS,
    DEFAULT_EPT_ONLY,
    DEFAULT_FILL_MAX_DIST,
    DEFAULT_FILL_SMOOTHING,
    DEFAULT_FLOOR_TO_FLOOR,
    DEFAULT_FORMAT,
    DEFAULT_MAX_HEIGHT,
    DEFAULT_MIN_HEIGHT,
    DEFAULT_NAIP_FLIP_U,
    DEFAULT_NAIP_FLIP_V,
    DEFAULT_OUT_DIR,
    DEFAULT_OUTPUTS,
    DEFAULT_PERCENTILE,
    DEFAULT_PREFER_EPT,
    DEFAULT_PROJECT_ZERO,
    DEFAULT_PROVIDER,
    DEFAULT_RESOLUTION,
    DEFAULT_UNITS,
    DEFAULT_XYZ_MODE,
    BuildConfig,
)
from .hmac_auth import (
    canonical_payload,
    choose_secret,
    parse_key_map,
    validate_timestamp,
    verify_signature,
)
from .parcels.registry import load_sources
from .pipeline.build import build as build_pipeline
from .pipeline.io import generate_job_id
from .providers.usgs_index import query_for_point
from .util import ensure_dir, get_logger

app = Flask(__name__)
app.secret_key = os.getenv("VA_SESSION_SECRET", secrets.token_hex(32))
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = os.getenv(
    "VA_SESSION_COOKIE_SECURE", "1"
).lower() not in ("0", "false", "no")


DESKTOP_MODE = os.getenv(
    "VA_DESKTOP_MODE", "1" if DEFAULT_DESKTOP_MODE else "0"
).lower() in (
    "1",
    "true",
    "yes",
)
OUT_DIR = Path(
    os.getenv(
        "VA_OUT_DIR",
        str(DEFAULT_DESKTOP_OUT_DIR if DESKTOP_MODE else DEFAULT_OUT_DIR),
    )
)
RETENTION_DAYS = int(
    os.getenv(
        "VA_RETENTION_DAYS",
        str(DEFAULT_DESKTOP_RETENTION_DAYS if DESKTOP_MODE else 7),
    )
)
CLEANUP_INTERVAL_SECONDS = int(os.getenv("VA_CLEANUP_INTERVAL", "3600"))
DEFAULT_RANDOM_MIN_HEIGHT = 15.0
DEFAULT_RANDOM_MAX_HEIGHT = 40.0
COVERAGE_CACHE_TTL_SECONDS = int(os.getenv("VA_COVERAGE_CACHE_TTL", "600"))
DB_PATH = Path(os.getenv("VA_DB_PATH", "./data/app.db"))
AUTH_PROVIDER = os.getenv("VA_AUTH_PROVIDER", "").strip().lower()
AUTH_ENABLED = (not DESKTOP_MODE) and AUTH_PROVIDER == "clerk"
CLERK_PUBLISHABLE_KEY = os.getenv("VA_CLERK_PUBLISHABLE_KEY", "").strip()
CLERK_SECRET_KEY = os.getenv("VA_CLERK_SECRET_KEY", "").strip()
CLERK_SIGN_IN_URL = os.getenv("VA_CLERK_SIGN_IN_URL", "").strip()
CLERK_JWKS_URL = os.getenv("VA_CLERK_JWKS_URL", "").strip()
CLERK_ISSUER = os.getenv("VA_CLERK_ISSUER", "").strip()
CLERK_API_URL = os.getenv("VA_CLERK_API_URL", "https://api.clerk.com/v1").strip()
CLERK_FRONTEND_API_URL = os.getenv("VA_CLERK_FRONTEND_API_URL", "").strip()
CLERK_ALLOWED_DOMAIN = os.getenv("VA_CLERK_ALLOWED_DOMAIN", "").strip().lower()
REQUIRE_LOCAL_ALLOWLIST = os.getenv("VA_REQUIRE_LOCAL_ALLOWLIST", "0").lower() in (
    "1",
    "true",
    "yes",
)
CLERK_AUTHORIZED_PARTIES = [
    p.strip()
    for p in os.getenv("VA_CLERK_AUTHORIZED_PARTIES", "").split(",")
    if p.strip()
]
SESSION_TTL_SECONDS = int(os.getenv("VA_SESSION_TTL_SECONDS", str(7 * 86400)))
SESSION_COOKIE_SECURE = os.getenv("VA_SESSION_COOKIE_SECURE", "1").lower() not in (
    "0",
    "false",
    "no",
)
ADMIN_EMAIL = os.getenv("VA_ADMIN_EMAIL", "").strip().lower()
RATE_LIMIT_HOURLY = int(os.getenv("VA_RATE_LIMIT_HOURLY", "3"))
RATE_LIMIT_DAILY = int(os.getenv("VA_RATE_LIMIT_DAILY", "10"))
MAX_ACTIVE_JOBS_PER_USER = int(os.getenv("VA_MAX_ACTIVE_JOBS_PER_USER", "1"))
MAX_CLIP_SIZE = float(os.getenv("VA_MAX_CLIP_SIZE", "5000"))
JOB_HISTORY_ENABLED = os.getenv("VA_JOB_HISTORY_ENABLED", "1").lower() in (
    "1",
    "true",
    "yes",
)
JOB_REHYDRATE_LIMIT = int(os.getenv("VA_JOB_REHYDRATE_LIMIT", "500"))
HMAC_KEYS_JSON = os.getenv("VA_HMAC_KEYS_JSON", "").strip()
HMAC_MAX_SKEW_SECONDS = int(os.getenv("VA_HMAC_MAX_SKEW_SECONDS", "300"))
HMAC_NONCE_TTL_SECONDS = int(os.getenv("VA_HMAC_NONCE_TTL_SECONDS", "600"))
WORKER_SHARED_TOKEN = os.getenv("VA_WORKER_SHARED_TOKEN", "").strip()
app.config["SESSION_COOKIE_SECURE"] = SESSION_COOKIE_SECURE if AUTH_ENABLED else False

_cleanup_started = False
_cleanup_lock = threading.Lock()
_coverage_cache: Dict[str, tuple[float, Optional[bool], str]] = {}
_coverage_cache_lock = threading.Lock()

HMAC_KEYS: Dict[str, str] = {}
if HMAC_KEYS_JSON:
    try:
        HMAC_KEYS = parse_key_map(HMAC_KEYS_JSON)
    except Exception:
        HMAC_KEYS = {}


@dataclass
class Job:
    job_id: str
    status: str
    created_at: float
    user_id: Optional[int] = None
    started_at: Optional[float] = None
    finished_at: Optional[float] = None
    exit_code: Optional[int] = None
    error: Optional[str] = None
    logs: List[str] = field(default_factory=list)
    summary: Dict[str, Any] = field(default_factory=dict)


JOBS: Dict[str, Job] = {}
JOBS_LOCK = threading.Lock()
_auth_started = False
_auth_lock = threading.Lock()


def _is_api_request() -> bool:
    if request.headers.get("X-Requested-With") == "fetch":
        return True
    accept = request.headers.get("Accept", "")
    return "application/json" in accept


def _unauthorized_response() -> Any:
    if _is_api_request():
        return jsonify({"error": "Authentication required."}), 401
    return redirect(url_for("auth_login", next=request.path))


def _forbidden_response(message: str = "Forbidden") -> Any:
    if _is_api_request():
        return jsonify({"error": message}), 403
    return (message, 403)


def ensure_auth_store() -> None:
    global _auth_started
    if not AUTH_ENABLED and not HMAC_KEYS and not JOB_HISTORY_ENABLED:
        return
    with _auth_lock:
        if _auth_started:
            return
        auth_store.init_db(DB_PATH, ADMIN_EMAIL or None)
        _rehydrate_jobs_from_store()
        _auth_started = True


def current_user() -> Optional[Dict[str, Any]]:
    user = getattr(g, "current_user", None)
    return user if isinstance(user, dict) else None


def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not AUTH_ENABLED:
            return func(*args, **kwargs)
        if current_user() is None:
            return _unauthorized_response()
        return func(*args, **kwargs)

    return wrapper


def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not AUTH_ENABLED:
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
    if not AUTH_ENABLED:
        return True
    sent = request.form.get("csrf_token") or request.headers.get("X-CSRF-Token")
    expected = session.get("csrf_token")
    if not sent or not expected:
        return False
    return secrets.compare_digest(str(sent), str(expected))


def _ensure_logged_user_from_session() -> None:
    g.current_user = None
    if not AUTH_ENABLED:
        return
    sid = session.get("sid")
    ensure_auth_store()
    if sid:
        user = auth_store.get_user_by_session(DB_PATH, str(sid))
        if user is not None and user.get("is_active"):
            g.current_user = user
            return
        session.pop("sid", None)

    # Optional fallback for API clients that pass Clerk tokens directly.
    # Do not consume Clerk browser cookies here, otherwise explicit app logout
    # can immediately recreate a local session.
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
    sid = auth_store.create_session(DB_PATH, int(user["id"]), SESSION_TTL_SECONDS)
    session["sid"] = sid
    g.current_user = user


def _user_can_access_job(job_id: str) -> bool:
    if not AUTH_ENABLED:
        return True
    user = current_user()
    if user is None:
        return False
    owner_id = auth_store.get_job_owner_id(DB_PATH, job_id)
    return owner_id is not None and owner_id == user["id"]


def _enforce_rate_limits(user_id: int) -> Optional[str]:
    now = time.time()
    hour_count = auth_store.count_build_requests_since(DB_PATH, user_id, now - 3600)
    if hour_count >= RATE_LIMIT_HOURLY:
        return f"Hourly limit reached ({RATE_LIMIT_HOURLY}/hour)."
    day_count = auth_store.count_build_requests_since(DB_PATH, user_id, now - 86400)
    if day_count >= RATE_LIMIT_DAILY:
        return f"Daily limit reached ({RATE_LIMIT_DAILY}/day)."
    active_count = auth_store.count_active_jobs(DB_PATH, user_id)
    if active_count >= MAX_ACTIVE_JOBS_PER_USER:
        return "Active job limit reached. Wait for running jobs to finish."
    return None


def _verify_hmac_request() -> bool:
    if WORKER_SHARED_TOKEN:
        provided = request.headers.get("X-Worker-Token", "")
        return secrets.compare_digest(provided, WORKER_SHARED_TOKEN)
    key_id = request.headers.get("X-Key-Id", "")
    signature = request.headers.get("X-Signature", "")
    nonce = request.headers.get("X-Nonce", "")
    timestamp_raw = request.headers.get("X-Timestamp", "")
    if not (HMAC_KEYS and key_id and signature and nonce and timestamp_raw):
        return False
    try:
        timestamp = int(timestamp_raw)
    except ValueError:
        return False
    if not validate_timestamp(timestamp, HMAC_MAX_SKEW_SECONDS):
        return False
    secret = choose_secret(HMAC_KEYS, key_id)
    if not secret:
        return False
    body = request.get_data(cache=True) or b""
    path = request.path
    payload = canonical_payload(request.method, path, timestamp, nonce, body)
    if not verify_signature(secret, payload, signature):
        return False
    ensure_auth_store()
    return auth_store.consume_nonce(DB_PATH, nonce, HMAC_NONCE_TTL_SECONDS)


def cleanup_out_dir(logger: logging.Logger) -> None:
    if RETENTION_DAYS <= 0:
        return
    cutoff = time.time() - (RETENTION_DAYS * 86400)
    if not OUT_DIR.exists():
        return
    for entry in OUT_DIR.iterdir():
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


def cleanup_loop() -> None:
    logger = get_logger()
    while True:
        cleanup_out_dir(logger)
        time.sleep(CLEANUP_INTERVAL_SECONDS)


def ensure_cleanup_thread() -> None:
    global _cleanup_started
    with _cleanup_lock:
        if _cleanup_started:
            return
        thread = threading.Thread(target=cleanup_loop, daemon=True)
        thread.start()
        _cleanup_started = True


class JobLogHandler(logging.Handler):
    def __init__(self, job: Job) -> None:
        super().__init__()
        self.job = job
        self.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        self.job.logs.append(msg)


STATUS_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Job {{ job.job_id }}</title>
    <style>
      html, body { height: 100%; }
      body { margin: 0; font-family: "Avenir Next", "Avenir", "Futura", sans-serif; background:#f7f4ef; color:#1f1f1f; }
      header { padding: 20px 24px; }
      main { padding: 0 24px 32px; }
      .card { background:#fff; border:1px solid #e4ded4; border-radius:12px; padding:16px; margin-bottom:16px; }
      .meta { color: #666; margin-top: 6px; }
      .actions { margin-top: 10px; }
      a { color: #B39CD0; text-decoration: none; }
      .status-chip {
        display: inline-block;
        border-radius: 999px;
        padding: 2px 10px;
        font-size: 12px;
        font-weight: 600;
      }
      .status-running { background: #3f2f1b; color: #ffd58e; }
      .status-done { background: #203328; color: #b8f2c9; }
      .status-error { background: #3b1f1f; color: #ffd4d4; }
      .status-unknown { background: #2f2f2f; color: #d4d4d4; }
      .tab-row {
        display: flex;
        gap: 8px;
        margin-bottom: 12px;
      }
      .tab-btn {
        border: 1px solid #d6d6d6;
        border-radius: 8px;
        background: #fff;
        color: #1f1f1f;
        padding: 8px 12px;
        cursor: pointer;
      }
      .tab-btn.active {
        border-color: #b39cd0;
        background: #f5f1fb;
      }
      .tab-panel.hidden {
        display: none;
      }
      pre { background:#0f1410; color:#bde7c0; padding:14px; border-radius:8px; height:420px; overflow:auto; margin: 0; }
      #preview-container {
        width: 100%;
        height: 500px;
        background: #1a1a1a;
        border-radius: 8px;
        position: relative;
        overflow: hidden;
      }
      #preview-message {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: #d9d9d9;
        font-size: 14px;
        pointer-events: none;
      }
      #preview-controls {
        display: flex;
        gap: 10px;
        align-items: center;
        margin-top: 12px;
        flex-wrap: wrap;
      }
      #preview-controls button,
      #preview-controls select {
        font: inherit;
        border-radius: 6px;
        border: 1px solid #d6d6d6;
        background: #ffffff;
        color: #1f1f1f;
        padding: 8px 10px;
      }
      #preview-controls button { cursor: pointer; }
      #preview-controls button:hover { border-color: #b39cd0; }
      #preview-file { min-width: 180px; }
      body.embed-mode {
        overflow: hidden;
        background: #2c2c2c;
        color: #e4e4e4;
      }
      body.embed-mode main {
        padding: 0;
        box-sizing: border-box;
        height: 100%;
      }
      body.embed-mode .card {
        height: 100%;
        box-sizing: border-box;
        margin-bottom: 0;
        border: 0;
        border-radius: 0;
        background: #1a1a1a;
        box-shadow: none;
        padding: 0;
        display: flex;
        flex-direction: column;
        overflow: hidden;
      }
      body.embed-mode h3 {
        margin: 0 0 10px;
        color: #e4e4e4;
      }
      body.embed-mode .tab-row {
        margin-bottom: 12px;
        gap: 8px;
      }
      body.embed-mode .tab-btn {
        border: 1px solid #444444;
        border-radius: 8px;
        background: #2f2f2f;
        color: #bcbcbc;
        padding: 8px 12px;
      }
      body.embed-mode .tab-btn.active {
        border-color: #b39cd0;
        background: #464646;
        color: #e4e4e4;
      }
      body.embed-mode #preview-container {
        flex: 1;
        min-height: 0;
        height: auto;
        border-radius: 0;
        border: 0;
      }
      body.embed-mode #preview-controls {
        position: absolute;
        left: 12px;
        bottom: 12px;
        top: auto;
        right: auto;
        margin-top: 0;
        gap: 10px;
        padding: 0;
        border-radius: 0;
        background: transparent;
        z-index: 6;
      }
      body.embed-mode #preview-controls button,
      body.embed-mode #preview-controls select {
        border: 1px solid #444444;
        border-radius: 8px;
        background: rgba(47, 47, 47, 0.72);
        color: #e4e4e4;
        padding: 10px 12px;
      }
      body.embed-mode #preview-controls button:hover {
        border-color: #b39cd0;
        background: #3a3a3a;
      }
      body.embed-mode #preview-controls button:disabled {
        border-color: #3a3a3a;
        background: rgba(47, 47, 47, 0.65);
        color: #9a9a9a;
        cursor: not-allowed;
      }
      body.embed-mode #preview-wireframe-btn.is-active {
        border-color: #b39cd0;
        background: #b39cd0;
        color: #ffffff;
      }
      body.embed-mode #preview-file {
        display: none;
      }
      body.embed-mode #preview-scene-select {
        min-width: 220px;
      }
      #preview-zoom-controls {
        display: none;
      }
      body.embed-mode #preview-zoom-controls {
        position: absolute;
        right: 12px;
        bottom: 12px;
        top: auto;
        transform: none;
        display: flex;
        flex-direction: row;
        gap: 8px;
        z-index: 7;
      }
      body.embed-mode #preview-zoom-controls button {
        width: 36px;
        height: 36px;
        border: 1px solid #444444;
        border-radius: 8px;
        background: rgba(47, 47, 47, 0.92);
        color: #e4e4e4;
        font-size: 17px;
        line-height: 1;
        cursor: pointer;
      }
      body.embed-mode #preview-zoom-controls button:hover {
        border-color: #b39cd0;
        background: #3a3a3a;
      }
      body.embed-mode pre {
        background: #0f1410;
        border: 1px solid #2f2f2f;
        color: #b7e3c0;
        border-radius: 8px;
        padding: 14px;
      }
      body.embed-mode #preview-message {
        color: #d9d9d9;
      }
      body.embed-mode .tab-panel {
        flex: 1;
        min-height: 0;
      }
      body.embed-mode #panel-preview {
        display: flex;
        flex-direction: column;
        position: relative;
        height: 100%;
      }
      body.embed-mode #panel-preview.hidden {
        display: none;
      }
      body.embed-mode #panel-log {
        height: 100%;
      }
      body.embed-mode pre {
        height: 100%;
        box-sizing: border-box;
        margin: 0;
        border: 0;
        border-radius: 0;
      }
      @media (max-width: 700px) {
        #preview-container { height: 340px; }
      }
    </style>
  </head>
  <body{% if embed_mode %} class="embed-mode"{% endif %}>
    {% if not embed_mode %}
    <header>
      <h2>{{ job.summary.get('name') or job.job_id }}</h2>
      <div class="meta">Job ID: {{ job.job_id }}</div>
      <div class="meta">Status: <span id="status" class="status-chip {{ status_class(job.status) }}">{{ status_label(job.status) }}</span></div>
      <div class="meta">Provider: {{ job.summary.get('provider_label') or job.summary.get('provider') }}</div>
      <div class="meta">Output folder: {{ job.summary.get('out') }}</div>
      <div class="meta">Target: {{ job.summary.get('target') }}</div>
      {% if job.summary.get('tile') %}
        <div class="meta">Tile: {{ job.summary.get('tile') }}</div>
      {% endif %}
      <div class="meta actions">
        <a href="{{ url_for('index', from_job=job.job_id) }}">Reuse settings in main form</a>
        ·
        <a href="{{ url_for('index') }}">Back to form</a>
      </div>
    </header>
    {% endif %}
    <main>
      {% if not embed_mode %}
      {% if job.error or job.summary.get('warnings') %}
      <div class="card">
        <h3>Job Notes</h3>
        {% if job.error %}
          <p><strong>This job did not complete.</strong> {{ job.error }}</p>
        {% endif %}
        {% if job.summary.get('warnings') %}
          <p><strong>Warnings:</strong></p>
          <ul>
          {% for warning in job.summary.get('warnings') %}
            <li>{{ warning }}</li>
          {% endfor %}
          </ul>
        {% endif %}
      </div>
      {% endif %}
      {% endif %}
      <div class="card">
        {% if not embed_mode %}
        <h3>3D Preview & Activity</h3>
        <div class="tab-row">
          <button type="button" class="tab-btn" data-tab="preview" id="tab-preview">Preview</button>
          <button type="button" class="tab-btn" data-tab="log" id="tab-log">Activity Log</button>
        </div>
        {% endif %}
        <div id="panel-preview" class="tab-panel">
          <div id="preview-container">
            <div id="preview-message">Waiting for model files...</div>
          </div>
          <div id="preview-controls">
            <button id="preview-wireframe-btn" type="button" onclick="toggleWireframe()">Wireframe</button>
            {% if embed_mode %}
            <select id="preview-scene-select" aria-label="Preview model"></select>
            {% endif %}
            <select id="preview-file"></select>
          </div>
          <div id="preview-zoom-controls" aria-label="Zoom controls">
            <button type="button" onclick="zoomOut()" aria-label="Zoom out">-</button>
            <button type="button" onclick="zoomIn()" aria-label="Zoom in">+</button>
          </div>
        </div>
        <div id="panel-log" class="tab-panel">
          <pre id="logs"></pre>
        </div>
      </div>
    </main>
    <script type="importmap">
      {
        "imports": {
          "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js"
        }
      }
    </script>
    <script type="module">
      import * as THREE_NS from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';
      import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/controls/OrbitControls.js';
      import { OBJLoader } from 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/loaders/OBJLoader.js';
      import { MTLLoader } from 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/loaders/MTLLoader.js';
      window.THREE = THREE_NS;
      window.OrbitControls = OrbitControls;
      window.OBJLoader = OBJLoader;
      window.MTLLoader = MTLLoader;
    </script>
    <script>
      const STATUS_LABELS = {
        queued: 'Queued',
        running: 'Running',
        done: 'Completed',
        error: 'Failed',
      };
      const STATUS_CLASSES = {
        queued: 'status-running',
        running: 'status-running',
        done: 'status-done',
        error: 'status-error',
      };
      const previewState = {
        jobId: '{{ job.job_id }}',
        initialized: false,
        activationStarted: false,
        wireframe: false,
        filesByName: new Map(),
        models: [],
        currentModelKey: null,
        scene: null,
        camera: null,
        renderer: null,
        controls: null,
        currentObject: null,
      };
      const EMBED_MODE = {{ embed_mode | tojson }};

      function setActiveTab(tabName) {
        const isPreview = tabName === 'preview';
        const previewPanel = document.getElementById('panel-preview');
        const logPanel = document.getElementById('panel-log');
        const previewBtn = document.getElementById('tab-preview');
        const logBtn = document.getElementById('tab-log');
        if (previewPanel) previewPanel.classList.toggle('hidden', !isPreview);
        if (logPanel) logPanel.classList.toggle('hidden', isPreview);
        if (previewBtn) previewBtn.classList.toggle('active', isPreview);
        if (logBtn) logBtn.classList.toggle('active', !isPreview);
      }

      function initTabs(initialStatus) {
        if (EMBED_MODE) {
          setActiveTab(initialStatus === 'done' ? 'preview' : 'log');
          return;
        }
        document.querySelectorAll('.tab-btn[data-tab]').forEach((button) => {
          button.addEventListener('click', () => {
            const tab = button.dataset.tab === 'preview' ? 'preview' : 'log';
            setActiveTab(tab);
          });
        });
        const params = new URLSearchParams(window.location.search);
        const requested = params.get('tab');
        setActiveTab(requested === 'preview' ? 'preview' : 'log');
      }

      function setStatusBadge(status) {
        const statusEl = document.getElementById('status');
        if (!statusEl) return;
        const label = STATUS_LABELS[status] || status;
        const className = STATUS_CLASSES[status] || 'status-unknown';
        statusEl.textContent = label;
        statusEl.className = `status-chip ${className}`;
      }

      function setPreviewMessage(message) {
        const msgEl = document.getElementById('preview-message');
        if (msgEl) {
          msgEl.textContent = message;
          msgEl.style.display = message ? 'block' : 'none';
        }
      }

      function addInlineMode(url) {
        if (!url) return '';
        return url.includes('?') ? `${url}&inline=1` : `${url}?inline=1`;
      }

      function buildDownloadUrl(name) {
        const fileMeta = previewState.filesByName.get(name);
        if (fileMeta && fileMeta.download_url) {
          return addInlineMode(fileMeta.download_url);
        }
        return `/jobs/${previewState.jobId}/download/${encodeURIComponent(name)}?inline=1`;
      }

      function pickAvailableModels(filesByName) {
        const models = [];
        const hasTerrain = filesByName.has('terrain.obj');
        const hasBuildings = filesByName.has('buildings.obj');
        const hasCombined = filesByName.has('combined.obj');
        const terrainMtl = filesByName.has('terrain.mtl') ? 'terrain.mtl' : null;
        const combinedMtl = filesByName.has('combined.mtl') ? 'combined.mtl' : null;

        if (hasTerrain && hasBuildings) {
          models.push({
            key: 'scene',
            label: 'Terrain + Buildings',
            parts: [
              { obj: 'terrain.obj', mtl: terrainMtl },
              { obj: 'buildings.obj', mtl: null },
            ],
          });
        }
        if (hasCombined) {
          models.push({
            key: 'combined',
            label: 'Combined',
            parts: [{ obj: 'combined.obj', mtl: combinedMtl }],
          });
        }
        if (hasTerrain) {
          models.push({
            key: 'terrain',
            label: 'Terrain',
            parts: [{ obj: 'terrain.obj', mtl: terrainMtl }],
          });
        }
        if (hasBuildings) {
          models.push({
            key: 'buildings',
            label: 'Buildings',
            parts: [{ obj: 'buildings.obj', mtl: null }],
          });
        }
        return models;
      }

      function ensureThreeContext() {
        if (previewState.initialized) return true;
        const OrbitControlsCtor = window.OrbitControls;
        if (!window.THREE || !window.OBJLoader || !OrbitControlsCtor || !window.MTLLoader) {
          setPreviewMessage('Loading 3D renderer...');
          return false;
        }
        const container = document.getElementById('preview-container');
        if (!container) return false;

        container.innerHTML = '<div id="preview-message"></div>';
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x1a1a1a);
        const camera = new THREE.PerspectiveCamera(55, 1, 0.1, 5000000);
        camera.up.set(0, 0, 1);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
        renderer.outputColorSpace = THREE.SRGBColorSpace;
        renderer.shadowMap.enabled = false;
        renderer.domElement.style.width = '100%';
        renderer.domElement.style.height = '100%';
        container.appendChild(renderer.domElement);

        const controls = new OrbitControlsCtor(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.07;
        controls.screenSpacePanning = true;

        scene.add(new THREE.AmbientLight(0xffffff, 0.6));
        const directional = new THREE.DirectionalLight(0xffffff, 1.0);
        directional.position.set(200, -150, 300);
        scene.add(directional);

        previewState.scene = scene;
        previewState.camera = camera;
        previewState.renderer = renderer;
        previewState.controls = controls;
        previewState.initialized = true;

        const resize = () => {
          if (!previewState.renderer || !previewState.camera) return;
          const width = Math.max(container.clientWidth, 1);
          const height = Math.max(container.clientHeight, 1);
          previewState.camera.aspect = width / height;
          previewState.camera.updateProjectionMatrix();
          previewState.renderer.setSize(width, height, false);
        };
        window.addEventListener('resize', resize);
        resize();

        const animate = () => {
          if (!previewState.renderer || !previewState.scene || !previewState.camera) return;
          requestAnimationFrame(animate);
          if (previewState.controls) previewState.controls.update();
          previewState.renderer.render(previewState.scene, previewState.camera);
        };
        animate();
        return true;
      }

      function applyWireframeMode(enabled) {
        if (!previewState.currentObject) return;
        previewState.currentObject.traverse((node) => {
          if (!node.isMesh || !node.material) return;
          const materials = Array.isArray(node.material) ? node.material : [node.material];
          for (const material of materials) {
            if (enabled) {
              if (material.map) {
                material.userData = material.userData || {};
                material.userData.savedMap = material.map;
                material.map = null;
              }
            } else if (
              material &&
              material.userData &&
              material.userData.savedMap &&
              !material.map
            ) {
              material.map = material.userData.savedMap;
            }
            material.wireframe = enabled;
            material.needsUpdate = true;
          }
        });
      }

      function clearCurrentObject() {
        if (!previewState.scene || !previewState.currentObject) return;
        previewState.scene.remove(previewState.currentObject);
        previewState.currentObject = null;
      }

      function centerAndPrepareObject(obj) {
        obj.traverse((node) => {
          if (!node.isMesh) return;
          if (node.geometry) node.geometry.computeVertexNormals();
          if (!node.material) return;
          const materials = Array.isArray(node.material) ? node.material : [node.material];
          for (const material of materials) material.side = THREE.DoubleSide;
        });
        const box = new THREE.Box3().setFromObject(obj);
        if (!box.isEmpty()) {
          const center = box.getCenter(new THREE.Vector3());
          obj.position.sub(center);
        }
      }

      function loadObjPart(part) {
        const manager = new THREE.LoadingManager();
        manager.setURLModifier((url) => {
          if (!url) return url;
          if (url.startsWith('data:') || /^https?:\\/\\//i.test(url)) return url;
          const clean = url.split('#')[0].split('?')[0];
          const name = clean.slice(clean.lastIndexOf('/') + 1);
          if (previewState.filesByName.has(name)) return buildDownloadUrl(name);
          return url;
        });

        return (async () => {
          const objLoader = new window.OBJLoader(manager);
          if (part.mtl) {
            try {
              const mtlResp = await fetch(buildDownloadUrl(part.mtl), { cache: 'no-store' });
              if (mtlResp.ok) {
                const mtlText = await mtlResp.text();
                const mtlLoader = new window.MTLLoader(manager);
                const mtlPath = `/jobs/${previewState.jobId}/download/`;
                const materials = mtlLoader.parse(mtlText, mtlPath);
                materials.preload();
                for (const key of Object.keys(materials.materials)) {
                  const material = materials.materials[key];
                  if (material && material.map) {
                    // Keep TextureLoader's default flipY behavior; our OBJ UVs
                    // are already exported in OBJ convention (v flipped once).
                    material.map.needsUpdate = true;
                  }
                }
                objLoader.setMaterials(materials);
              }
            } catch (error) {
              // Continue without MTL if it cannot be loaded.
            }
          }

          const objUrl = buildDownloadUrl(part.obj);
          const objResp = await fetch(objUrl, { cache: 'no-store' });
          if (!objResp.ok) throw new Error(`OBJ fetch failed (${objResp.status}) for ${part.obj}`);
          const objText = await objResp.text();
          return objLoader.parse(objText);
        })();
      }

      async function renderModel(modelKey, options = {}) {
        const model = previewState.models.find((m) => m.key === modelKey);
        if (!model || !previewState.scene) return;
        const shouldResetView = options.resetView !== false;
        setPreviewMessage('Loading model...');
        clearCurrentObject();
        try {
          const group = new THREE.Group();
          for (const part of model.parts) {
            try {
              const partObj = await loadObjPart(part);
              group.add(partObj);
            } catch (error) {
              console.warn('Preview part failed', part.obj, error);
            }
          }
          if (!group.children.length) throw new Error('No preview geometry could be loaded.');
          centerAndPrepareObject(group);
          previewState.scene.add(group);
          previewState.currentObject = group;
          previewState.currentModelKey = model.key;
          applyWireframeMode(previewState.wireframe);
          updateWireframeButton();
          updateSceneSelect();
          if (shouldResetView) resetCamera();
          setPreviewMessage('');
        } catch (error) {
          const msg = (error && error.message) ? error.message : 'Failed to load preview model.';
          setPreviewMessage(msg);
        }
      }

      async function activatePreview() {
        if (previewState.activationStarted) return;
        previewState.activationStarted = true;
        let artifactPayload;
        try {
          const resp = await fetch(`/jobs/${previewState.jobId}/artifacts`, { cache: 'no-store' });
          if (!resp.ok) {
            previewState.activationStarted = false;
            setPreviewMessage('Preview will be available when model files are generated.');
            return;
          }
          artifactPayload = await resp.json();
        } catch (error) {
          previewState.activationStarted = false;
          setPreviewMessage('Preview could not be loaded.');
          return;
        }

        const files = Array.isArray(artifactPayload.files) ? artifactPayload.files : [];
        previewState.filesByName = new Map(files.map((f) => [f.name, f]));
        previewState.models = pickAvailableModels(previewState.filesByName);
        if (!previewState.models.length) {
          previewState.activationStarted = false;
          setPreviewMessage('No 3D model artifacts found for this job.');
          return;
        }

        if (!ensureThreeContext()) {
          previewState.activationStarted = false;
          setTimeout(activatePreview, 600);
          return;
        }

        const select = document.getElementById('preview-file');
        if (!select) return;
        select.innerHTML = '';
        for (const model of previewState.models) {
          const option = document.createElement('option');
          option.value = model.key;
          option.textContent = model.label;
          select.appendChild(option);
        }
        if (select.dataset.bound !== 'true') {
          select.addEventListener('change', (event) => {
            const value = event.target.value;
            if (value) renderModel(value, { resetView: false });
          });
          select.dataset.bound = 'true';
        }
        updateSceneSelect();
        const defaultModel =
          previewState.models.find((model) => model.key === 'scene') ||
          previewState.models[0];
        if (defaultModel) renderModel(defaultModel.key);
      }

      async function pollLogs(jobId) {
        const logsEl = document.getElementById('logs');
        if (!logsEl) return;
        let offset = 0;

        async function poll() {
          const logResp = await fetch(`/logs/${jobId}?offset=${offset}`);
          if (!logResp.ok) return;
          const logData = await logResp.json();
          if (logData.logs && logData.logs.length) {
            logsEl.textContent += logData.logs.join('\\n') + '\\n';
            logsEl.scrollTop = logsEl.scrollHeight;
            offset = logData.offset;
          }
          setStatusBadge(logData.status);
          if (EMBED_MODE) {
            setActiveTab(logData.status === 'done' ? 'preview' : 'log');
          }
          if (logData.status === 'done') activatePreview();
          if (logData.status === 'running' || logData.status === 'queued') setTimeout(poll, 1500);
        }
        poll();
      }

      function toggleWireframe() {
        previewState.wireframe = !previewState.wireframe;
        applyWireframeMode(previewState.wireframe);
        updateWireframeButton();
      }

      function updateWireframeButton() {
        const wireframeBtn = document.getElementById('preview-wireframe-btn');
        if (!wireframeBtn) return;
        wireframeBtn.classList.toggle('is-active', previewState.wireframe);
      }

      function resetCamera() {
        if (!previewState.camera || !previewState.controls) return;
        let radius = 100.0;
        if (previewState.currentObject) {
          const box = new THREE.Box3().setFromObject(previewState.currentObject);
          if (!box.isEmpty()) {
            const sphere = box.getBoundingSphere(new THREE.Sphere());
            radius = Math.max(sphere.radius, 1.0);
          }
        }
        previewState.camera.near = Math.max(radius / 1000.0, 0.01);
        previewState.camera.far = Math.max(radius * 200.0, 1000.0);
        previewState.camera.position.set(radius * 1.35, radius * 1.35, radius * 0.95);
        previewState.controls.target.set(0, 0, 0);
        previewState.camera.updateProjectionMatrix();
        previewState.controls.update();
      }

      function updateSceneSelect() {
        const sceneSelect = document.getElementById('preview-scene-select');
        if (!sceneSelect) return;
        if (sceneSelect.dataset.bound !== 'true') {
          sceneSelect.addEventListener('change', (event) => {
            const modelKey = event.target.value;
            if (modelKey) renderModel(modelKey, { resetView: false });
          });
          sceneSelect.dataset.bound = 'true';
        }

        const preferredKeys = new Set(['scene', 'terrain', 'buildings']);
        let options = previewState.models.filter((model) => preferredKeys.has(model.key));
        if (!options.length) options = previewState.models.slice();

        sceneSelect.innerHTML = '';
        for (const model of options) {
          const option = document.createElement('option');
          option.value = model.key;
          option.textContent = model.label;
          sceneSelect.appendChild(option);
        }
        sceneSelect.disabled = options.length === 0;

        if (!options.length) return;
        const hasCurrent = options.some((model) => model.key === previewState.currentModelKey);
        sceneSelect.value = hasCurrent ? previewState.currentModelKey : options[0].key;
      }

      function zoomBy(scale) {
        if (!previewState.camera || !previewState.controls) return;
        const target = previewState.controls.target.clone();
        const offset = previewState.camera.position.clone().sub(target);
        const currentDistance = offset.length();
        if (!Number.isFinite(currentDistance) || currentDistance <= 0) return;

        let minDistance = 0.5;
        let maxDistance = 1000000.0;
        if (previewState.currentObject) {
          const box = new THREE.Box3().setFromObject(previewState.currentObject);
          if (!box.isEmpty()) {
            const sphere = box.getBoundingSphere(new THREE.Sphere());
            minDistance = Math.max(sphere.radius * 0.15, 0.5);
            maxDistance = Math.max(sphere.radius * 25.0, minDistance * 4.0);
          }
        }
        const nextDistance = Math.min(
          maxDistance,
          Math.max(minDistance, currentDistance * scale)
        );
        offset.setLength(nextDistance);
        previewState.camera.position.copy(target.add(offset));
        previewState.camera.updateProjectionMatrix();
        previewState.controls.update();
      }

      function zoomIn() {
        zoomBy(0.92);
      }

      function zoomOut() {
        zoomBy(1.08);
      }

      window.toggleWireframe = toggleWireframe;
      window.resetCamera = resetCamera;
      window.zoomIn = zoomIn;
      window.zoomOut = zoomOut;

      document.addEventListener('DOMContentLoaded', () => {
        const initialStatus = '{{ job.status }}';
        updateWireframeButton();
        initTabs(initialStatus);
        setStatusBadge(initialStatus);
        if (initialStatus === 'done') {
          activatePreview();
        } else if (initialStatus === 'error') {
          setPreviewMessage('Build failed. Preview unavailable.');
        } else {
          setPreviewMessage('Preview will be available when the build completes.');
        }
        pollLogs('{{ job.job_id }}');
      });
    </script>
  </body>
</html>
"""


def parse_float(value: str | None) -> Optional[float]:
    if value is None:
        return None
    value = value.strip()
    if value == "":
        return None
    return float(value)


def parse_int(value: str | None) -> Optional[int]:
    if value is None:
        return None
    value = value.strip()
    if value == "":
        return None
    return int(value)


def parse_bool(value: str | None) -> bool:
    return value is not None


VA_BOUNDS = {"lat_min": 36.5, "lat_max": 39.5, "lon_min": -83.0, "lon_max": -75.0}


def is_in_virginia(lon: float, lat: float) -> bool:
    return (
        VA_BOUNDS["lon_min"] <= lon <= VA_BOUNDS["lon_max"]
        and VA_BOUNDS["lat_min"] <= lat <= VA_BOUNDS["lat_max"]
    )


def resolve_provider(lat: float | None, lon: float | None) -> str:
    if lat is None or lon is None:
        return DEFAULT_PROVIDER
    return "va" if is_in_virginia(lon, lat) else "national"


def provider_label(provider: str) -> str:
    return "VGIN (Virginia)" if provider == "va" else "USGS 3DEP (National)"


def status_label(status: str) -> str:
    mapping = {
        "queued": "Queued",
        "running": "Running",
        "done": "Completed",
        "error": "Failed",
    }
    return mapping.get(status, status.title())


def status_class(status: str) -> str:
    if status in ("queued", "running"):
        return "status-running"
    if status == "done":
        return "status-done"
    if status == "error":
        return "status-error"
    return "status-unknown"


def _coverage_cache_key(lon: float, lat: float) -> str:
    return f"{round(lon, 4)},{round(lat, 4)}"


def resolve_image_quality(value: str | None) -> tuple[float, int, bool]:
    quality = (value or "").strip().lower()
    if quality == "high":
        return (0.5, 8000, False)
    if quality == "ultra":
        return (0.3, 12000, False)
    return (1.0, 4000, False)


def _find_latest_report(out_dir: Path, started_at: float) -> Optional[Path]:
    if not out_dir.exists():
        return None
    latest_path: Optional[Path] = None
    latest_mtime = 0.0
    cutoff = started_at - 5.0
    for path in out_dir.rglob("report.json"):
        if "_cache" in path.parts:
            continue
        try:
            mtime = path.stat().st_mtime
        except OSError:
            continue
        if mtime < cutoff:
            continue
        if latest_path is None or mtime > latest_mtime:
            latest_path = path
            latest_mtime = mtime
    return latest_path


OUTPUT_ARTIFACT_CANDIDATES = (
    "terrain.obj",
    "terrain.mtl",
    "buildings.obj",
    "combined.obj",
    "combined.mtl",
    "terrain.png",
    "contours.dxf",
    "terrain.xyz",
)


def _dir_has_known_outputs(path: Path) -> bool:
    return any((path / name).is_file() for name in OUTPUT_ARTIFACT_CANDIDATES)


def _discover_output_dir_for_job(job_id: str) -> Optional[Path]:
    job_root = OUT_DIR / job_id
    if not (job_root.exists() and job_root.is_dir()):
        return None
    if not _is_path_within(OUT_DIR, job_root):
        return None
    if _dir_has_known_outputs(job_root):
        return job_root

    reports: List[Path] = []
    for report_path in job_root.rglob("report.json"):
        if "_cache" in report_path.parts:
            continue
        if report_path.is_file():
            reports.append(report_path)
    reports.sort(
        key=lambda p: (p.stat().st_mtime if p.exists() else 0.0), reverse=True
    )

    for report_path in reports:
        try:
            report = json.loads(report_path.read_text())
        except Exception:
            report = {}
        if isinstance(report, dict):
            output_dir = report.get("output_dir")
            if isinstance(output_dir, str) and output_dir.strip():
                candidate = Path(output_dir).expanduser()
                if (
                    candidate.exists()
                    and candidate.is_dir()
                    and _is_path_within(OUT_DIR, candidate)
                ):
                    return candidate
        parent_dir = report_path.parent
        if parent_dir.is_dir() and _dir_has_known_outputs(parent_dir):
            return parent_dir

    for child in sorted(job_root.iterdir(), key=lambda p: p.name.lower()):
        if child.is_dir() and _dir_has_known_outputs(child):
            return child

    return None


def _collect_outputs(tile_dir: Path) -> Dict[str, Any]:
    if not tile_dir.exists():
        return {"dir": str(tile_dir), "files": []}
    files = [name for name in OUTPUT_ARTIFACT_CANDIDATES if (tile_dir / name).exists()]
    return {"dir": str(tile_dir), "files": files}


def _is_path_within(base_dir: Path, candidate: Path) -> bool:
    try:
        candidate.resolve().relative_to(base_dir.resolve())
        return True
    except Exception:
        return False


def _resolve_job_output_dir(job: Job) -> Optional[Path]:
    outputs = job.summary.get("outputs")
    if isinstance(outputs, dict):
        raw_dir = outputs.get("dir")
        if isinstance(raw_dir, str) and raw_dir.strip():
            candidate = Path(raw_dir).expanduser()
            if (
                candidate.exists()
                and candidate.is_dir()
                and _is_path_within(OUT_DIR, candidate)
            ):
                return candidate

    report_path = job.summary.get("report_path")
    if isinstance(report_path, str) and report_path:
        report_file = Path(report_path).expanduser()
        if report_file.exists() and report_file.is_file():
            candidate = report_file.parent
            if _is_path_within(OUT_DIR, candidate):
                return candidate

    default_dir = OUT_DIR / job.job_id
    discovered = _discover_output_dir_for_job(job.job_id)
    if discovered is not None:
        return discovered
    if (
        default_dir.exists()
        and default_dir.is_dir()
        and _is_path_within(OUT_DIR, default_dir)
    ):
        return default_dir
    return None


def _list_job_artifacts(job: Job) -> List[Dict[str, Any]]:
    output_dir = _resolve_job_output_dir(job)
    if output_dir is None:
        return []

    artifacts: List[Dict[str, Any]] = []
    seen: set[str] = set()
    outputs = job.summary.get("outputs")
    summary_files: List[str] = []
    if isinstance(outputs, dict) and isinstance(outputs.get("files"), list):
        for value in outputs.get("files"):
            if isinstance(value, str):
                summary_files.append(value.strip())

    for name in summary_files:
        if not name or "/" in name or "\\" in name or name in seen:
            continue
        path = output_dir / name
        if not path.is_file():
            continue
        stat = path.stat()
        artifacts.append(
            {"name": name, "size": int(stat.st_size), "mtime": float(stat.st_mtime)}
        )
        seen.add(name)

    # Ensure preview support files are available even for older summaries.
    for name in ("terrain.mtl", "combined.mtl"):
        if name in seen:
            continue
        path = output_dir / name
        if not path.is_file():
            continue
        stat = path.stat()
        artifacts.append(
            {"name": name, "size": int(stat.st_size), "mtime": float(stat.st_mtime)}
        )
        seen.add(name)

    if not artifacts:
        for path in sorted(output_dir.iterdir(), key=lambda p: p.name.lower()):
            if not path.is_file():
                continue
            name = path.name
            if name in seen:
                continue
            stat = path.stat()
            artifacts.append(
                {"name": name, "size": int(stat.st_size), "mtime": float(stat.st_mtime)}
            )
            seen.add(name)

    return artifacts


def _rehydrate_jobs_from_store() -> None:
    if JOB_REHYDRATE_LIMIT <= 0:
        return
    try:
        persisted = auth_store.list_recent_jobs(DB_PATH, limit=JOB_REHYDRATE_LIMIT)
    except Exception:
        return

    restored: List[Job] = []
    for item in persisted:
        job_id = str(item.get("job_id"))
        summary_raw = item.get("summary")
        summary = summary_raw if isinstance(summary_raw, dict) else {}

        artifacts_raw = item.get("artifacts")
        if isinstance(artifacts_raw, list) and artifacts_raw:
            outputs = summary.get("outputs")
            if not isinstance(outputs, dict):
                outputs = {}
            output_files = outputs.get("files")
            if not isinstance(output_files, list) or not output_files:
                outputs["files"] = [
                    str(entry.get("name"))
                    for entry in artifacts_raw
                    if isinstance(entry, dict) and str(entry.get("name") or "").strip()
                ]
            raw_dir = outputs.get("dir")
            if not isinstance(raw_dir, str) or not raw_dir.strip():
                outputs["dir"] = str(OUT_DIR / job_id)
            summary["outputs"] = outputs
        elif not isinstance(summary.get("outputs"), dict):
            discovered = _discover_output_dir_for_job(job_id)
            if discovered is not None:
                summary["outputs"] = _collect_outputs(discovered)

        created_at = item.get("created_at")
        if not isinstance(created_at, (int, float)):
            created_at = time.time()
        status = str(item.get("status") or "queued")
        raw_user_id = item.get("user_id")
        user_id = int(raw_user_id) if isinstance(raw_user_id, int) else None

        restored.append(
            Job(
                job_id=job_id,
                status=status,
                created_at=float(created_at),
                user_id=user_id,
                started_at=(
                    float(item["started_at"])
                    if isinstance(item.get("started_at"), (int, float))
                    else None
                ),
                finished_at=(
                    float(item["finished_at"])
                    if isinstance(item.get("finished_at"), (int, float))
                    else None
                ),
                exit_code=(
                    int(item["exit_code"])
                    if isinstance(item.get("exit_code"), int)
                    else None
                ),
                error=str(item["error"]) if item.get("error") is not None else None,
                summary=summary,
            )
        )

    restored.sort(key=lambda job: (job.created_at, job.job_id))
    with JOBS_LOCK:
        for job in restored:
            if job.job_id not in JOBS:
                JOBS[job.job_id] = job


def _persist_job_snapshot(job: Job) -> None:
    if not AUTH_ENABLED and not HMAC_KEYS and not JOB_HISTORY_ENABLED:
        return
    try:
        ensure_auth_store()
        summary = job.summary if isinstance(job.summary, dict) else {}
        auth_store.upsert_job_snapshot(
            DB_PATH,
            job.job_id,
            user_id=job.user_id,
            created_at=job.created_at,
            status=job.status,
            started_at=job.started_at,
            finished_at=job.finished_at,
            exit_code=job.exit_code,
            error=job.error,
            summary=summary,
        )
        auth_store.replace_job_artifacts(DB_PATH, job.job_id, _list_job_artifacts(job))
    except Exception:
        return


def _clerk_auth_ready() -> bool:
    return bool(CLERK_PUBLISHABLE_KEY and CLERK_SECRET_KEY)


@functools.lru_cache(maxsize=4)
def _clerk_jwk_client(jwks_url: str) -> jwt.PyJWKClient:
    return jwt.PyJWKClient(jwks_url)


def _resolve_clerk_jwks_url(unverified_claims: Dict[str, Any]) -> str:
    if CLERK_JWKS_URL:
        return CLERK_JWKS_URL
    iss = str(unverified_claims.get("iss") or "").strip()
    if not iss:
        return ""
    return iss.rstrip("/") + "/.well-known/jwks.json"


def _verify_clerk_session_token(raw_token: str) -> Dict[str, Any]:
    unverified = jwt.decode(
        raw_token,
        options={"verify_signature": False, "verify_exp": False},
        algorithms=["RS256", "HS256"],
    )
    jwks_url = _resolve_clerk_jwks_url(unverified)
    if not jwks_url:
        raise RuntimeError("Unable to determine Clerk JWKS URL.")
    jwk_client = _clerk_jwk_client(jwks_url)
    signing_key = jwk_client.get_signing_key_from_jwt(raw_token)
    issuer = CLERK_ISSUER or str(unverified.get("iss") or "")
    claims = jwt.decode(
        raw_token,
        signing_key.key,
        algorithms=["RS256"],
        options={"require": ["sub", "exp", "iat"]},
        issuer=issuer if issuer else None,
    )
    azp = str(claims.get("azp") or "")
    if CLERK_AUTHORIZED_PARTIES and azp not in CLERK_AUTHORIZED_PARTIES:
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
    if not CLERK_SECRET_KEY:
        raise RuntimeError("Missing VA_CLERK_SECRET_KEY.")
    resp = requests.get(
        f"{CLERK_API_URL.rstrip('/')}/users/{clerk_user_id}",
        headers={"Authorization": f"Bearer {CLERK_SECRET_KEY}"},
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

    if CLERK_ALLOWED_DOMAIN and not email.endswith("@" + CLERK_ALLOWED_DOMAIN):
        raise RuntimeError("Account domain is not allowed.")

    user = auth_store.find_user_by_email(DB_PATH, email)
    if REQUIRE_LOCAL_ALLOWLIST:
        if user is None or not user.get("is_active"):
            raise RuntimeError("Access denied for this account.")
        return user

    is_admin = bool(ADMIN_EMAIL and email == ADMIN_EMAIL)
    merged_admin = is_admin or bool(user and user.get("is_admin"))
    auth_store.upsert_user(DB_PATH, email, is_admin=merged_admin, is_active=True)
    user = auth_store.find_user_by_email(DB_PATH, email)
    if user is None:
        raise RuntimeError("Failed to initialize local user session.")
    return user


def snapshot_defaults() -> Dict[str, Any]:
    outputs = set(DEFAULT_OUTPUTS)
    return {
        "out": str(OUT_DIR),
        "units": "feet",
        "provider": "va",
        "provider_label": "VGIN (Virginia)",
        "center1": 37.5390116184146,
        "center2": -77.43353162833343,
        "job_name": "",
        "clip_size": 1500.0,
        "resolution": DEFAULT_RESOLUTION,
        "terrain_complexity": 5,
        "rotate_z": 0.0,
        "project_zero": DEFAULT_PROJECT_ZERO,
        "xyz_mode": DEFAULT_XYZ_MODE,
        "xyz_contour_spacing": 0.0,
        "dxf_contour_spacing": DEFAULT_DXF_CONTOUR_SPACING,
        "dxf_include_parcels": DEFAULT_DXF_INCLUDE_PARCELS,
        "dxf_include_buildings": DEFAULT_DXF_INCLUDE_BUILDINGS,
        "output_terrain": "terrain" in outputs,
        "output_buildings": "buildings" in outputs,
        "output_contours": "contours" in outputs,
        "output_naip": "naip" in outputs,
        "output_xyz": "xyz" in outputs,
        "min_height": DEFAULT_MIN_HEIGHT,
        "max_height": DEFAULT_MAX_HEIGHT,
        "random_min_height": DEFAULT_RANDOM_MIN_HEIGHT,
        "random_max_height": DEFAULT_RANDOM_MAX_HEIGHT,
        "contour_interval": 2.0,
        "image_quality": "standard",
    }


def _extract_form_defaults(
    *,
    coords: str,
    clip_size: float,
    units: str,
    terrain_complexity: int,
    rotate_z: float,
    project_zero: float,
    contour_interval: Optional[float],
    dxf_contour_spacing: Optional[float],
    dxf_include_parcels: bool,
    dxf_include_buildings: bool,
    xyz_mode: str,
    image_quality: str,
    random_min_height: float,
    random_max_height: float,
    output_terrain: bool,
    output_buildings: bool,
    output_contours: bool,
    output_naip: bool,
    output_xyz: bool,
    custom_name: str,
) -> Dict[str, Any]:
    return {
        "center1": coords.split(",")[0].strip() if "," in coords else coords,
        "center2": coords.split(",")[1].strip() if "," in coords else "",
        "job_name": custom_name,
        "clip_size": clip_size,
        "units": units,
        "terrain_complexity": terrain_complexity,
        "rotate_z": rotate_z,
        "project_zero": project_zero,
        "contour_interval": contour_interval if contour_interval is not None else 2.0,
        "dxf_contour_spacing": (
            dxf_contour_spacing
            if dxf_contour_spacing is not None
            else DEFAULT_DXF_CONTOUR_SPACING
        ),
        "dxf_include_parcels": dxf_include_parcels,
        "dxf_include_buildings": dxf_include_buildings,
        "xyz_mode": xyz_mode,
        "image_quality": image_quality,
        "random_min_height": random_min_height,
        "random_max_height": random_max_height,
        "output_terrain": output_terrain,
        "output_buildings": output_buildings,
        "output_contours": output_contours,
        "output_naip": output_naip,
        "output_xyz": output_xyz,
    }


def _merge_prefill_defaults(
    defaults: Dict[str, Any], saved: Optional[Dict[str, Any]]
) -> Dict[str, Any]:
    if not isinstance(saved, dict):
        return defaults
    allowed = {
        "center1",
        "center2",
        "job_name",
        "clip_size",
        "units",
        "terrain_complexity",
        "rotate_z",
        "project_zero",
        "contour_interval",
        "dxf_contour_spacing",
        "dxf_include_parcels",
        "dxf_include_buildings",
        "xyz_mode",
        "image_quality",
        "random_min_height",
        "random_max_height",
        "output_terrain",
        "output_buildings",
        "output_contours",
        "output_naip",
        "output_xyz",
    }
    for key in allowed:
        if key in saved:
            defaults[key] = saved[key]
    return defaults


def parcel_sources_payload() -> List[Dict[str, Any]]:
    sources = []
    for source in load_sources():
        payload = {"id": source.id, "name": source.name, "url": source.query_url}
        if source.coverage is not None:
            payload["coverage"] = {
                "xmin": source.coverage[0],
                "ymin": source.coverage[1],
                "xmax": source.coverage[2],
                "ymax": source.coverage[3],
            }
        if source.exclude:
            payload["exclude"] = [
                {"xmin": b[0], "ymin": b[1], "xmax": b[2], "ymax": b[3]}
                for b in source.exclude
            ]
        sources.append(payload)
    return sources


def _domain_key(url: str) -> str:
    return urlparse(url).netloc.lower()


def _base_service_url(url: str) -> str:
    parsed = urlparse(url)
    root = f"{parsed.scheme}://{parsed.netloc}"
    marker = "/arcgis/rest/services"
    idx = parsed.path.find(marker)
    if idx != -1:
        return root + marker
    return root


def data_sources_payload(parcel_sources: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    static_sources = [
        {
            "name": "VGIN LiDAR",
            "url": "https://vginmaps.vdem.virginia.gov/arcgis/rest/services/Download/Virginia_LiDAR_Downloads/MapServer/1",
        },
        {
            "name": "VGIN Footprints",
            "url": "https://vginmaps.vdem.virginia.gov/arcgis/rest/services/VA_Base_Layers/VA_Building_Footprints/FeatureServer/0",
        },
        {
            "name": "USGS 3DEP LiDAR",
            "url": "https://index.nationalmap.gov/arcgis/rest/services/3DEPElevationIndex/MapServer/8",
        },
        {
            "name": "Microsoft Footprints",
            "url": "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/MSBFP2/FeatureServer/0",
        },
        {
            "name": "NAIP Imagery",
            "url": "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer",
        },
    ]

    entries = list(static_sources)
    for source in parcel_sources:
        if source.get("url"):
            entries.append({"name": source["name"], "url": source["url"]})

    provider_labels = {
        "vginmaps.vdem.virginia.gov": "VGIN",
    }

    grouped: Dict[str, Dict[str, Any]] = {}
    order: List[str] = []
    for entry in entries:
        domain = _domain_key(entry["url"])
        if domain not in grouped:
            grouped[domain] = {
                "name": entry["name"],
                "url": entry["url"],
                "details": [],
            }
            order.append(domain)
        grouped[domain]["details"].append(entry["name"])

    sources = []
    for domain in order:
        group = grouped[domain]
        if len(group["details"]) > 1:
            name = provider_labels.get(domain, domain)
            url = _base_service_url(group["url"])
        else:
            name = group["name"]
            url = group["url"]
        sources.append(
            {
                "name": name,
                "url": url,
                "details": group["details"],
            }
        )
    return sources


@app.before_request
def _start_cleanup():
    ensure_cleanup_thread()
    ensure_auth_store()
    _ensure_logged_user_from_session()


@app.context_processor
def inject_user_context():
    return {
        "current_user": current_user(),
        "auth_enabled": AUTH_ENABLED,
        "desktop_mode": DESKTOP_MODE,
        "csrf_token": get_csrf_token,
    }


@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"})


@app.route("/auth/login")
def auth_login():
    if not AUTH_ENABLED:
        return redirect(url_for("index"))
    if not _clerk_auth_ready():
        return ("Clerk auth is not configured.", 500)
    next_path = request.args.get("next", "/")
    if not next_path.startswith("/"):
        next_path = "/"
    force_sign_out = request.args.get("logged_out", "").lower() in ("1", "true", "yes")
    return render_template(
        "auth_login.html",
        next_path=next_path,
        force_sign_out=force_sign_out,
        clerk_publishable_key=CLERK_PUBLISHABLE_KEY,
        clerk_sign_in_url=CLERK_SIGN_IN_URL,
        clerk_frontend_api_url=CLERK_FRONTEND_API_URL,
    )


@app.route("/auth/clerk/exchange", methods=["POST"])
def auth_clerk_exchange():
    if not AUTH_ENABLED:
        return redirect(url_for("index"))
    payload = request.get_json(silent=True) or {}
    raw_token = str(payload.get("token") or "").strip()
    next_path = str(payload.get("next") or "/").strip()
    if not next_path.startswith("/"):
        next_path = "/"
    if not raw_token:
        return jsonify({"error": "Missing Clerk session token."}), 400
    try:
        user = _exchange_clerk_token(raw_token)
    except Exception as exc:
        return jsonify({"error": f"Clerk auth failed: {exc}"}), 403

    sid = auth_store.create_session(DB_PATH, int(user["id"]), SESSION_TTL_SECONDS)
    session["sid"] = sid
    get_csrf_token()
    return jsonify({"ok": True, "next": next_path})


@app.route("/auth/callback")
def auth_callback():
    # Kept for compatibility with previously configured redirect URLs.
    return redirect(url_for("auth_login"))


@app.route("/auth/logout", methods=["POST"])
def auth_logout():
    if AUTH_ENABLED and not validate_csrf():
        return ("Invalid CSRF token.", 400)
    sid = session.get("sid")
    if sid:
        ensure_auth_store()
        auth_store.revoke_session(DB_PATH, str(sid))
    session.clear()
    if AUTH_ENABLED:
        return redirect(url_for("auth_login", next="/", logged_out=1))
    return redirect(url_for("index"))


@app.route("/")
def index():
    defaults = snapshot_defaults()
    prefill_job_id = (request.args.get("from_job") or "").strip()
    if prefill_job_id and _user_can_access_job(prefill_job_id):
        with JOBS_LOCK:
            prefill_job = JOBS.get(prefill_job_id)
        if prefill_job is not None:
            defaults = _merge_prefill_defaults(
                defaults, prefill_job.summary.get("form_defaults")
            )
    parcel_sources = parcel_sources_payload()
    data_sources = data_sources_payload(parcel_sources)
    user = current_user()
    can_build = (not AUTH_ENABLED) or (user is not None)
    with JOBS_LOCK:
        jobs = list(JOBS.values())
        if AUTH_ENABLED:
            if user is None:
                jobs = []
            else:
                jobs = [job for job in jobs if job.user_id == user["id"]]
        jobs = jobs[-8:][::-1]
    return render_template(
        "index.html",
        defaults=defaults,
        data_sources=data_sources,
        parcel_sources=parcel_sources,
        jobs=jobs,
        can_build=can_build,
        retention_days=RETENTION_DAYS,
        status_label=status_label,
        status_class=status_class,
    )


@app.route("/recent-jobs")
@require_login
def recent_jobs():
    user = current_user()
    with JOBS_LOCK:
        jobs = list(JOBS.values())
        if AUTH_ENABLED:
            if user is None:
                jobs = []
            else:
                jobs = [job for job in jobs if job.user_id == user["id"]]
        jobs = jobs[-8:][::-1]
    payload = [
        {
            "job_id": job.job_id,
            "name": str(job.summary.get("name") or job.job_id),
            "status": job.status,
            "status_label": status_label(job.status),
            "status_class": status_class(job.status),
            "preview_url": url_for("job_status", job_id=job.job_id, tab="preview"),
            "log_url": url_for("job_status", job_id=job.job_id),
        }
        for job in jobs
    ]
    for item, job in zip(payload, jobs):
        if job.status != "done":
            continue
        artifacts = _list_job_artifacts(job)
        if not artifacts:
            continue
        item["artifact_count"] = len(artifacts)
        item["download_all_url"] = url_for("job_download_all", job_id=job.job_id)
    return jsonify({"jobs": payload})


@app.route("/admin/users")
@require_admin
def admin_users():
    users = auth_store.list_users(DB_PATH)
    return render_template("admin_users.html", users=users)


@app.route("/admin/users", methods=["POST"])
@require_admin
def admin_users_upsert():
    if not validate_csrf():
        return ("Invalid CSRF token.", 400)
    email = (request.form.get("email") or "").strip().lower()
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return ("Invalid email.", 400)
    is_admin = request.form.get("is_admin") is not None
    is_active = request.form.get("is_active") is not None
    auth_store.upsert_user(DB_PATH, email, is_admin=is_admin, is_active=is_active)
    return redirect(url_for("admin_users"))


@app.route("/coverage")
def coverage():
    lon = parse_float(request.args.get("lon"))
    lat = parse_float(request.args.get("lat"))
    if lon is None or lat is None:
        return jsonify({"supported": None, "error": "Invalid coordinates"}), 400

    provider = resolve_provider(lat, lon)
    cache_key = _coverage_cache_key(lon, lat)
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

    payload = {"supported": supported, "provider": provider}
    if error:
        payload["error"] = error
    if supported is not None:
        with _coverage_cache_lock:
            _coverage_cache[cache_key] = (now, supported, provider)
    return jsonify(payload)


@app.route("/run", methods=["POST"])
@require_login
def run_job():
    if not validate_csrf():
        return jsonify({"error": "Invalid CSRF token."}), 400

    user = current_user()
    user_id = int(user["id"]) if user else None
    if AUTH_ENABLED and user_id is not None:
        limit_error = _enforce_rate_limits(user_id)
        if limit_error:
            return jsonify({"error": limit_error}), 429

    form = request.form
    custom_name = (form.get("job_name") or "").strip()
    if len(custom_name) > 120:
        return jsonify({"error": "Name must be 120 characters or fewer."}), 400
    out_dir = OUT_DIR
    ensure_dir(out_dir)
    units = form.get("units") or DEFAULT_UNITS
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
    if clip_size > MAX_CLIP_SIZE:
        return jsonify({"error": f"Clip size exceeds max ({MAX_CLIP_SIZE:g})."}), 400

    center = (lat, lon) if lat is not None and lon is not None else None

    resolution = DEFAULT_RESOLUTION
    terrain_complexity = parse_int(form.get("terrain_complexity"))
    if terrain_complexity is None:
        terrain_complexity = 2
    terrain_complexity = max(0, min(10, terrain_complexity))
    # Map 0-10 complexity to terrain_sample 11-1 (higher complexity -> smaller sample)
    terrain_sample = max(1, 11 - terrain_complexity)
    fill_dtm = True
    fill_hard = True
    fill_max_dist = DEFAULT_FILL_MAX_DIST
    fill_smoothing = DEFAULT_FILL_SMOOTHING

    percentile = DEFAULT_PERCENTILE
    min_height = parse_float(form.get("min_height"))
    if min_height is None:
        min_height = DEFAULT_MIN_HEIGHT
    max_height = parse_float(form.get("max_height"))
    if max_height is None:
        max_height = DEFAULT_MAX_HEIGHT
    floor_to_floor = DEFAULT_FLOOR_TO_FLOOR

    random_min = parse_float(form.get("random_min_height"))
    if random_min is None:
        random_min = DEFAULT_RANDOM_MIN_HEIGHT
    random_max = parse_float(form.get("random_max_height"))
    if random_max is None:
        random_max = DEFAULT_RANDOM_MAX_HEIGHT
    random_seed = None

    naip_pixel_size, naip_max_size, naip_tiled = resolve_image_quality(
        form.get("image_quality")
    )
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

    combine_output = parse_bool(form.get("output_combined"))
    if combine_output and not ("terrain" in outputs and "buildings" in outputs):
        return (
            jsonify({"error": "Combined output requires terrain + buildings."}),
            400,
        )

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
    dxf_contour_spacing = (
        parse_float(form.get("dxf_contour_spacing")) if contours_enabled else None
    )
    if dxf_contour_spacing is not None and dxf_contour_spacing <= 0:
        dxf_contour_spacing = None
    dxf_include_parcels = (
        parse_bool(form.get("dxf_include_parcels")) if contours_enabled else False
    )
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
    project_zero = parse_float(form.get("project_zero"))
    if project_zero is None:
        project_zero = DEFAULT_PROJECT_ZERO

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
        project_zero=project_zero,
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
        "form_defaults": _extract_form_defaults(
            coords=f"{lat},{lon}",
            clip_size=clip_size,
            units=units,
            terrain_complexity=terrain_complexity,
            rotate_z=rotate_z,
            project_zero=project_zero,
            contour_interval=contour_interval,
            dxf_contour_spacing=dxf_contour_spacing,
            dxf_include_parcels=dxf_include_parcels,
            dxf_include_buildings=dxf_include_buildings,
            xyz_mode=xyz_mode,
            image_quality=(form.get("image_quality") or "standard").strip().lower(),
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
    if AUTH_ENABLED:
        auth_store.record_job_owner(DB_PATH, job_id, user_id)
    if user_id is not None:
        auth_store.add_build_request(DB_PATH, user_id)
        auth_store.set_active_job(DB_PATH, job_id, user_id, status="queued")

    thread = threading.Thread(target=_run_build_job, args=(job, cfg), daemon=True)
    thread.start()

    if request.headers.get("X-Requested-With") == "fetch":
        return jsonify({"job_id": job_id})
    return redirect(url_for("job_status", job_id=job_id))


@app.route("/jobs/<job_id>")
@require_login
def job_status(job_id: str):
    if not _user_can_access_job(job_id):
        return _forbidden_response("Not allowed to access this job.")
    with JOBS_LOCK:
        job = JOBS.get(job_id)
    if job is None:
        return "Job not found", 404
    embed_mode = request.args.get("embed", "").strip().lower() in ("1", "true", "yes")
    return render_template_string(
        STATUS_TEMPLATE,
        job=job,
        status_label=status_label,
        status_class=status_class,
        embed_mode=embed_mode,
    )


@app.route("/logs/<job_id>")
@require_login
def job_logs(job_id: str):
    if not _user_can_access_job(job_id):
        return _forbidden_response("Not allowed to access this job.")
    offset = parse_int(request.args.get("offset")) or 0
    with JOBS_LOCK:
        job = JOBS.get(job_id)
        if job is None:
            return jsonify({"error": "Job not found"}), 404
        logs = job.logs[offset:]
        next_offset = offset + len(logs)
        payload = {
            "status": job.status,
            "logs": logs,
            "offset": next_offset,
            "error": job.error,
            "exit_code": job.exit_code,
            "summary": job.summary,
        }
    return jsonify(payload)


@app.route("/jobs/<job_id>/artifacts")
@require_login
def job_artifacts(job_id: str):
    if not _user_can_access_job(job_id):
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
            "download_url": url_for("job_download", job_id=job_id, name=item["name"]),
        }
        for item in artifacts
    ]
    return jsonify({"job_id": job_id, "files": payload})


@app.route("/jobs/<job_id>/download/<name>")
@require_login
def job_download(job_id: str, name: str):
    if "/" in name or "\\" in name:
        return jsonify({"error": "Invalid file name."}), 400
    if not _user_can_access_job(job_id):
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


@app.route("/jobs/<job_id>/download-all")
@require_login
def job_download_all(job_id: str):
    if not _user_can_access_job(job_id):
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


@app.route("/internal/worker/jobs/<job_id>/complete", methods=["POST"])
def worker_job_complete(job_id: str):
    if not _verify_hmac_request():
        return jsonify({"error": "Unauthorized callback."}), 401
    payload = request.get_json(silent=True) or {}
    with JOBS_LOCK:
        job = JOBS.get(job_id)
        if job is None:
            return jsonify({"error": "Job not found."}), 404
        job.status = payload.get("status", job.status)
        job.exit_code = payload.get("exit_code", job.exit_code)
        job.error = payload.get("error", job.error)
        summary = payload.get("summary")
        if isinstance(summary, dict):
            job.summary.update(summary)
    if AUTH_ENABLED and job.status in ("done", "error"):
        auth_store.set_job_status(DB_PATH, job_id, job.status)
        auth_store.finish_active_job(DB_PATH, job_id, job.status)
    _persist_job_snapshot(job)
    return jsonify({"ok": True})


def _run_build_job(job: Job, cfg: BuildConfig) -> None:
    job.status = "running"
    job.started_at = time.time()
    if AUTH_ENABLED:
        auth_store.set_job_status(DB_PATH, job.job_id, "running")
        if job.user_id is not None:
            auth_store.set_active_job(
                DB_PATH, job.job_id, job.user_id, status="running"
            )
    _persist_job_snapshot(job)
    logger = get_logger()
    handler = JobLogHandler(job)
    logger.addHandler(handler)
    try:
        job.exit_code = build_pipeline(cfg)
        if job.exit_code == 0:
            job.status = "done"
        else:
            job.status = "error"
    except Exception as exc:  # pragma: no cover - surface to UI
        job.status = "error"
        job.error = str(exc)
        logger.exception("Build failed")
    finally:
        job.finished_at = time.time()
        logger.removeHandler(handler)
        if AUTH_ENABLED:
            auth_store.set_job_status(DB_PATH, job.job_id, job.status)
            if job.user_id is not None:
                auth_store.finish_active_job(DB_PATH, job.job_id, job.status)

        report_path = _find_latest_report(cfg.out_dir, job.started_at or time.time())
        if report_path:
            try:
                report = json.loads(report_path.read_text())
                job.summary["report_path"] = str(report_path)
                job.summary["tile"] = report.get("tile")
                if report.get("output_dir"):
                    job.summary["out"] = report.get("output_dir")
                job.summary["job_id"] = report.get("job_id")
                job.summary["warnings"] = report.get("warnings")
                job.summary["source_type"] = report.get("source_type")
                job.summary["outputs"] = _collect_outputs(report_path.parent)
            except Exception:
                pass
        _persist_job_snapshot(job)


def main() -> int:
    default_host = DEFAULT_DESKTOP_HOST if DESKTOP_MODE else "127.0.0.1"
    default_port = DEFAULT_DESKTOP_PORT if DESKTOP_MODE else 5000
    parser = argparse.ArgumentParser(prog="va-lidar-context-web")
    parser.add_argument("--host", default=os.getenv("VA_WEB_HOST", default_host))
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("VA_WEB_PORT", str(default_port))),
    )
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    app.run(host=args.host, port=args.port, debug=args.debug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
