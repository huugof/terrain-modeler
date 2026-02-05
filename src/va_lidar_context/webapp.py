from __future__ import annotations

import argparse
import logging
import os
import re
import shutil
import threading
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from flask import Flask, jsonify, redirect, render_template_string, request, url_for

from .cli import build_command
from .config import (
    DEFAULT_ALLOW_MULTI_TILE,
    DEFAULT_CLIP_SIZE,
    DEFAULT_COMBINE_OUTPUT,
    DEFAULT_FILL_DTM,
    DEFAULT_FILL_HARD,
    DEFAULT_FILL_MAX_DIST,
    DEFAULT_FILL_SMOOTHING,
    DEFAULT_FLIP_X,
    DEFAULT_FLIP_Y,
    DEFAULT_FLOOR_TO_FLOOR,
    DEFAULT_FORMAT,
    DEFAULT_MAX_HEIGHT,
    DEFAULT_MIN_HEIGHT,
    DEFAULT_NAIP_FLIP_U,
    DEFAULT_NAIP_FLIP_V,
    DEFAULT_NAIP_MAX_SIZE,
    DEFAULT_NAIP_PIXEL_SIZE,
    DEFAULT_OUT_DIR,
    DEFAULT_PERCENTILE,
    DEFAULT_RANDOM_SEED,
    DEFAULT_RESOLUTION,
    DEFAULT_TERRAIN_FLIP_Y,
    DEFAULT_TERRAIN_SAMPLE,
    DEFAULT_TREES_ENABLED,
    DEFAULT_TREES_MAX_HEIGHT,
    DEFAULT_TREES_MIN_HEIGHT,
    DEFAULT_TREES_RADIUS,
    DEFAULT_TREES_RESOLUTION,
    DEFAULT_TREES_SAMPLE,
    DEFAULT_UNITS,
    BuildConfig,
)
from .util import ensure_dir, get_logger

app = Flask(__name__)


OUT_DIR = Path(os.getenv("VA_OUT_DIR", "./out"))
RETENTION_DAYS = int(os.getenv("VA_RETENTION_DAYS", "7"))
CLEANUP_INTERVAL_SECONDS = int(os.getenv("VA_CLEANUP_INTERVAL", "3600"))

_cleanup_started = False
_cleanup_lock = threading.Lock()


@dataclass
class Job:
    job_id: str
    status: str
    created_at: float
    started_at: Optional[float] = None
    finished_at: Optional[float] = None
    exit_code: Optional[int] = None
    error: Optional[str] = None
    logs: List[str] = field(default_factory=list)
    summary: Dict[str, Any] = field(default_factory=dict)


JOBS: Dict[str, Job] = {}
JOBS_LOCK = threading.Lock()


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


INDEX_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>VA Site Mesh Builder</title>
    <style>
      :root {
        --bg: #2C2C2C;
        --ink: #E4E4E4;
        --muted: #bcbcbc;
        --accent: #A8DADC;
        --accent-2: #FFC1CC;
        --card: #353535;
        --border: #444444;
      }
      * { box-sizing: border-box; }
      body {
        margin: 0;
        font-family: "Avenir Next", "Avenir", "Futura", "Trebuchet MS", sans-serif;
        color: var(--ink);
        background: var(--bg);
      }
      header {
        padding: 28px 24px 8px;
        text-align: center;
      }
      h1 {
        margin: 0 0 6px;
        font-size: 24px;
        letter-spacing: 0.4px;
      }
      p.sub {
        margin: 0;
        color: var(--muted);
      }
      main {
        padding: 16px 24px 40px;
        display: grid;
        gap: 16px;
        justify-content: center;
      }
      main > * {
        width: min(700px, 100%);
      }
      .card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.35);
      }
      .grid {
        display: grid;
        gap: 12px;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      }
      label {
        display: block;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: var(--muted);
        margin-bottom: 6px;
      }
      input[type="text"],
      input[type="number"],
      input[type="range"],
      select {
        width: 100%;
        padding: 10px 12px;
        border-radius: 8px;
        border: 1px solid var(--border);
        font-size: 14px;
      }
      .check-row {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
      }
      .check {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 14px;
      }
      .section-title {
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 0.16em;
        color: var(--accent);
        margin: 0 0 10px;
      }
      .note {
        font-size: 12px;
        color: var(--muted);
        margin-top: 8px;
      }
      .btn {
        background: #B39CD0;
        color: #fff;
        border: none;
        padding: 12px 18px;
        font-size: 14px;
        border-radius: 10px;
        cursor: pointer;
      }
      .btn.secondary {
        background: #3a3a3a;
      }
      .footer {
        color: var(--muted);
        font-size: 12px;
      }
      a {
        color: #B39CD0;
        text-decoration: none;
      }
      a:visited {
        color: #B39CD0;
      }

          .hidden {
        display: none;
      }
          input[type="range"] {
        -webkit-appearance: none;
        width: 100%;
        height: 6px;
        border-radius: 999px;
        background: #3f3f3f;
        outline: none;
      }
      input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: #B39CD0;
        border: none;
      }
      input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: #B39CD0;
        border: none;
      }
      select {
        appearance: none;
      }
      .hidden {
        display: none;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>VA Site Mesh Builder</h1>
      <p class="sub">Generate site, building footprints, and contour models.</p>
    </header>
    <main>

      <form class="card" method="post" action="{{ url_for('run_job') }}">
        <div class="section-title">Outputs</div>
        <div class="check-row">
          <label class="check"><input type="checkbox" name="out_terrain" checked disabled /> Terrain</label>
          <label class="check"><input type="checkbox" id="out_buildings" name="out_buildings" {% if defaults.out_buildings %}checked{% endif %} /> Buildings</label>
          <label class="check"><input type="checkbox" id="combine_output" name="combine_output" {% if defaults.combine_output %}checked{% endif %} /> Combined</label>
        </div>
        <div class="check-row" style="margin-top:6px;">
          <label class="check"><input type="checkbox" id="contours" name="contours" {% if defaults.contours %}checked{% endif %} /> Contours</label>
          <label class="check"><input type="checkbox" name="trees" {% if defaults.trees %}checked{% endif %} /> Trees</label>
        </div>

        <div class="section-title" style="margin-top:16px;">Location</div>
        <div class="grid">
          <div style="grid-column: 1 / -1;">
            <label>Coordinates</label>
            <input type="text" name="coords" value="{{ defaults.center1 }}, {{ defaults.center2 }}" placeholder="lat, lon" />
          </div>
          <div>
            <label>Clip Size (square)</label>
            <input type="number" step="any" name="size" value="{{ defaults.clip_size }}" />
          </div>
          <div>
            <label>Units</label>
            <select name="units">
              <option value="feet" {% if defaults.units == 'feet' %}selected{% endif %}>feet</option>
              <option value="meters" {% if defaults.units == 'meters' %}selected{% endif %}>meters</option>
            </select>
          </div>
        </div>

        <div class="section-title" style="margin-top:16px;">Complexity</div>
        <div class="note">Higher = more polygons / slower export.</div>
        <div class="grid" style="margin-top:6px;">
          <div style="grid-column: 1 / -1; display:flex; align-items:center; gap:12px;">
            <input type="range" min="0" max="10" step="1" name="terrain_complexity" value="{{ defaults.terrain_complexity }}" oninput="document.getElementById('complexityValue').textContent = this.value;" />
            <div id="complexityValue" style="min-width:20px; text-align:right;">{{ defaults.terrain_complexity }}</div>
          </div>
        </div>

        <div class="section-title" style="margin-top:16px;">Contour Interval</div>
        <div class="grid" id="contourIntervalRow">
          <div>
            <input type="number" step="any" name="contour_interval" value="{{ defaults.contour_interval }}" />
          </div>
        </div>

        <div style="margin-top:16px; display:flex; gap:12px; align-items:center;">
          <button class="btn" type="submit">Build</button>
          <button class="btn secondary" type="reset">Reset</button>
        </div>
      </form>
      <div class="note" style="margin-top:20px; text-align:center;">All data gathered from <a href="https://vgin.vdem.virginia.gov/documents/VGIN::vbmp-digitial-terrain-models-dtm/about" target="_blank" rel="noreferrer">VBMP DTM</a> and <a href="https://www.usgs.gov/centers/eros/science/usgs-eros-archive-aerial-photography-national-agriculture-imagery-program-naip" target="_blank" rel="noreferrer">NAIP</a>.</div>


      <div class="card">
        <div class="section-title">Recent Jobs</div>
        {% if jobs %}
          <ul>
            {% for job in jobs %}
              <li>
                <a href="{{ url_for('job_status', job_id=job.job_id) }}">{{ job.job_id }}</a>
                — {{ job.status }}
              </li>
            {% endfor %}
          </ul>
        {% else %}
          <p class="footer">No jobs yet.</p>
        {% endif %}
      </div>
    </main>
    <script>
      function updateUiToggles() {
        const contours = document.getElementById('contours');
        const contourRow = document.getElementById('contourIntervalRow');
        if (contours && contourRow) {
          contourRow.classList.toggle('hidden', !contours.checked);
        }
        const buildings = document.getElementById('out_buildings');
        const combined = document.getElementById('combine_output');
        if (buildings && combined) {
          if (!buildings.checked) {
            combined.checked = false;
            combined.disabled = true;
          } else {
            combined.disabled = false;
          }
        }
      }

      async function runBuild(event) {
        event.preventDefault();
        const form = event.target;
        const runBtn = document.getElementById('runBtn');
        const status = document.getElementById('jobStatus');
        const logsEl = document.getElementById('jobLogs');
        if (!form || !runBtn || !status || !logsEl) return;

        runBtn.disabled = true;
        const originalText = runBtn.textContent;
        runBtn.textContent = 'Running...';
        status.textContent = 'Starting build...';
        logsEl.style.display = 'none';
        logsEl.textContent = '';

        const formData = new FormData(form);
        const resp = await fetch(form.action, {
          method: 'POST',
          body: formData,
          headers: { 'X-Requested-With': 'fetch' },
        });
        if (!resp.ok) {
          status.textContent = 'Failed to start build.';
          runBtn.disabled = false;
          runBtn.textContent = originalText;
          return;
        }
        const data = await resp.json();
        status.textContent = `Job ${data.job_id} started.`;
        logsEl.style.display = 'block';

        let offset = 0;
        async function poll() {
          const logResp = await fetch(`/logs/${data.job_id}?offset=${offset}`);
          if (!logResp.ok) return;
          const logData = await logResp.json();
          if (logData.logs && logData.logs.length) {
            logsEl.textContent += logData.logs.join('
') + '
';
            logsEl.scrollTop = logsEl.scrollHeight;
            offset = logData.offset;
          }
          if (logData.status === 'running') {
            setTimeout(poll, 1500);
          } else {
            status.textContent = `Job ${data.job_id}: ${logData.status}`;
            runBtn.disabled = false;
            runBtn.textContent = originalText;
          }
        }
        poll();
      }

      document.addEventListener('DOMContentLoaded', () => {
        updateUiToggles();
        const contours = document.getElementById('contours');
        const buildings = document.getElementById('out_buildings');
        if (contours) contours.addEventListener('change', updateUiToggles);
        if (buildings) buildings.addEventListener('change', updateUiToggles);
        const form = document.querySelector('form.card');
        const runBtn = document.getElementById('runBtn');
        if (runBtn && form) {
          runBtn.addEventListener('click', (e) => runBuild({ preventDefault: () => {}, target: form }));
        }
      });
    </script>
  </body>
</html>
"""


STATUS_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Job {{ job.job_id }}</title>
    <style>
      body { margin: 0; font-family: "Avenir Next", "Avenir", "Futura", sans-serif; background:#f7f4ef; color:#1f1f1f; }
      header { padding: 20px 24px; }
      main { padding: 0 24px 32px; }
      .card { background:#fff; border:1px solid #e4ded4; border-radius:12px; padding:16px; margin-bottom:16px; }
      pre { background:#0f1410; color:#bde7c0; padding:14px; border-radius:8px; height:420px; overflow:auto; }
      a {
        color: #B39CD0;
        text-decoration: none;
      }
      .meta {
        color: #B39CD0;
        text-decoration: none;
      }
          .hidden {
        display: none;
      }
          input[type="range"] {
        -webkit-appearance: none;
        width: 100%;
        height: 6px;
        border-radius: 999px;
        background: #3f3f3f;
        outline: none;
      }
      input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: #B39CD0;
        border: none;
      }
      input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: #B39CD0;
        border: none;
      }
      select {
        appearance: none;
      }
      .hidden {
        display: none;
      }
    </style>
  </head>
  <body>
    <header>
      <h2>Job {{ job.job_id }}</h2>
      <div class="meta">Status: <span id="status">{{ job.status }}</span></div>
      <div class="meta">Output: {{ job.summary.get('out') }}</div>
      <div class="meta">Tile/Center: {{ job.summary.get('target') }}</div>
      <div class="meta"><a href="{{ url_for('index') }}">Back to form</a></div>
    </header>
    <main>
      <div class="card">
        <h3>Logs</h3>
        <pre id="logs"></pre>
      </div>
    </main>
    <script>
      function updateUiToggles() {
        const contours = document.getElementById('contours');
        const contourRow = document.getElementById('contourIntervalRow');
        if (contours && contourRow) {
          contourRow.classList.toggle('hidden', !contours.checked);
        }
        const buildings = document.getElementById('out_buildings');
        const combined = document.getElementById('combine_output');
        if (buildings && combined) {
          if (!buildings.checked) {
            combined.checked = false;
            combined.disabled = true;
          } else {
            combined.disabled = false;
          }
        }
      }

      async function runBuild(event) {
        event.preventDefault();
        const form = event.target;
        const runBtn = document.getElementById('runBtn');
        const status = document.getElementById('jobStatus');
        const logsEl = document.getElementById('jobLogs');
        if (!form || !runBtn || !status || !logsEl) return;

        runBtn.disabled = true;
        const originalText = runBtn.textContent;
        runBtn.textContent = 'Running...';
        status.textContent = 'Starting build...';
        logsEl.style.display = 'none';
        logsEl.textContent = '';

        const formData = new FormData(form);
        const resp = await fetch(form.action, {
          method: 'POST',
          body: formData,
          headers: { 'X-Requested-With': 'fetch' },
        });
        if (!resp.ok) {
          status.textContent = 'Failed to start build.';
          runBtn.disabled = false;
          runBtn.textContent = originalText;
          return;
        }
        const data = await resp.json();
        status.textContent = `Job ${data.job_id} started.`;
        logsEl.style.display = 'block';

        let offset = 0;
        async function poll() {
          const logResp = await fetch(`/logs/${data.job_id}?offset=${offset}`);
          if (!logResp.ok) return;
          const logData = await logResp.json();
          if (logData.logs && logData.logs.length) {
            logsEl.textContent += logData.logs.join('
') + '
';
            logsEl.scrollTop = logsEl.scrollHeight;
            offset = logData.offset;
          }
          if (logData.status === 'running') {
            setTimeout(poll, 1500);
          } else {
            status.textContent = `Job ${data.job_id}: ${logData.status}`;
            runBtn.disabled = false;
            runBtn.textContent = originalText;
          }
        }
        poll();
      }

      document.addEventListener('DOMContentLoaded', () => {
        updateUiToggles();
        const contours = document.getElementById('contours');
        const buildings = document.getElementById('out_buildings');
        if (contours) contours.addEventListener('change', updateUiToggles);
        if (buildings) buildings.addEventListener('change', updateUiToggles);
        const form = document.querySelector('form.card');
        const runBtn = document.getElementById('runBtn');
        if (runBtn && form) {
          runBtn.addEventListener('click', (e) => runBuild({ preventDefault: () => {}, target: form }));
        }
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


def snapshot_defaults() -> Dict[str, Any]:
    return {
        "out": str(OUT_DIR),
        "units": "feet",
        "center1": 37.5390116184146,
        "center2": -77.43353162833343,
        "clip_size": 1000.0,
        "terrain_complexity": 6,
        "combine_output": True,
        "out_buildings": True,
        "trees": False,
        "contours": True,
        "contour_interval": 2.0,
    }


@app.before_request
def _start_cleanup():
    ensure_cleanup_thread()


@app.route("/")
def index():
    defaults = snapshot_defaults()
    with JOBS_LOCK:
        jobs = list(JOBS.values())[-8:][::-1]
    return render_template_string(
        INDEX_TEMPLATE, defaults=defaults, jobs=jobs, retention_days=RETENTION_DAYS
    )


@app.route("/run", methods=["POST"])
def run_job():
    form = request.form
    tile_name = None
    out_dir = OUT_DIR
    ensure_dir(out_dir)
    units = form.get("units") or DEFAULT_UNITS
    center_mode = "auto"
    coords = form.get("coords") or ""
    parts = [p for p in re.split(r"[ ,]+", coords.strip()) if p]
    center1 = parse_float(parts[0]) if len(parts) > 0 else None
    center2 = parse_float(parts[1]) if len(parts) > 1 else None
    clip_size = parse_float(form.get("size"))

    center_coords = None
    center_lonlat = None
    center_latlon = None
    center_xy = None

    if center1 is not None and center2 is not None:
        if center_mode == "auto":
            center_coords = (center1, center2)
        elif center_mode == "lonlat":
            center_lonlat = (center1, center2)
        elif center_mode == "latlon":
            center_latlon = (center1, center2)
        elif center_mode == "xy":
            center_xy = (center1, center2)

    resolution = DEFAULT_RESOLUTION
    terrain_complexity = parse_int(form.get("terrain_complexity"))
    if terrain_complexity is None:
        terrain_complexity = 6
    terrain_complexity = max(0, min(10, terrain_complexity))
    # Map 0-10 complexity to terrain_sample 11-1 (higher complexity -> smaller sample)
    terrain_sample = max(1, 11 - terrain_complexity)
    fill_dtm = True
    fill_hard = True
    fill_max_dist = DEFAULT_FILL_MAX_DIST
    fill_smoothing = DEFAULT_FILL_SMOOTHING

    percentile = DEFAULT_PERCENTILE
    min_height = DEFAULT_MIN_HEIGHT
    max_height = DEFAULT_MAX_HEIGHT
    floor_to_floor = DEFAULT_FLOOR_TO_FLOOR

    random_min = 15.0
    random_max = 40.0
    random_seed = None

    naip_texture = True
    naip_pixel_size = DEFAULT_NAIP_PIXEL_SIZE
    naip_max_size = DEFAULT_NAIP_MAX_SIZE
    naip_flip_u = DEFAULT_NAIP_FLIP_U
    naip_flip_v = DEFAULT_NAIP_FLIP_V

    combine_output = parse_bool(form.get("combine_output"))
    export_buildings = parse_bool(form.get("out_buildings"))
    contours_enabled = parse_bool(form.get("contours"))
    contour_interval = (
        (parse_float(form.get("contour_interval")) or 2.0) if contours_enabled else None
    )
    parcels = False
    trees = parse_bool(form.get("trees"))
    keep_rasters = False

    trees_resolution = DEFAULT_TREES_RESOLUTION
    trees_sample = DEFAULT_TREES_SAMPLE
    trees_min_height = DEFAULT_TREES_MIN_HEIGHT
    trees_max_height = DEFAULT_TREES_MAX_HEIGHT
    trees_radius = DEFAULT_TREES_RADIUS

    flip_x = False
    flip_y = False
    terrain_flip_y = True
    rotate_z = 0.0

    allow_multi_tile = True
    force = False

    cfg = BuildConfig(
        tile_name=tile_name,
        center_coords=center_coords,
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
        naip_texture=naip_texture,
        naip_pixel_size=naip_pixel_size,
        naip_max_size=naip_max_size,
        naip_flip_u=naip_flip_u,
        naip_flip_v=naip_flip_v,
        combine_output=combine_output,
        trees=trees,
        trees_resolution=trees_resolution,
        trees_sample=trees_sample,
        trees_min_height=trees_min_height,
        trees_max_height=trees_max_height,
        trees_radius=trees_radius,
        contour_interval=contour_interval,
        parcels=parcels,
        clip_center_lonlat=center_lonlat,
        clip_center_latlon=center_latlon,
        clip_center_xy=center_xy,
        clip_size=clip_size,
        allow_multi_tile=allow_multi_tile,
        export_buildings=export_buildings,
        flip_y=flip_y,
        flip_x=flip_x,
        terrain_flip_y=terrain_flip_y,
        rotate_z=rotate_z,
    )

    target_summary = None
    if center1 is not None and center2 is not None:
        target_summary = f"{center_mode}:{center1},{center2} size={clip_size}"

    summary = {
        "out": str(out_dir),
        "target": target_summary or "(tile lookup)",
    }

    job_id = uuid.uuid4().hex[:8]
    job = Job(job_id=job_id, status="queued", created_at=time.time(), summary=summary)

    with JOBS_LOCK:
        JOBS[job_id] = job

    thread = threading.Thread(target=_run_build_job, args=(job, cfg), daemon=True)
    thread.start()

    if request.headers.get("X-Requested-With") == "fetch":
        return jsonify({"job_id": job_id})
    return redirect(url_for("job_status", job_id=job_id))


@app.route("/jobs/<job_id>")
def job_status(job_id: str):
    with JOBS_LOCK:
        job = JOBS.get(job_id)
    if job is None:
        return "Job not found", 404
    return render_template_string(STATUS_TEMPLATE, job=job)


@app.route("/logs/<job_id>")
def job_logs(job_id: str):
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
        }
    return jsonify(payload)


def _run_build_job(job: Job, cfg: BuildConfig) -> None:
    job.status = "running"
    job.started_at = time.time()
    logger = get_logger()
    handler = JobLogHandler(job)
    logger.addHandler(handler)
    try:
        job.exit_code = build_command(cfg)
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


def main() -> int:
    parser = argparse.ArgumentParser(prog="va-lidar-context-web")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    app.run(host=args.host, port=args.port, debug=args.debug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
