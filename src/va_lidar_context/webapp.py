from __future__ import annotations

import argparse
import json
import logging
import os
import re
import shutil
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from flask import Flask, jsonify, redirect, render_template, request, url_for

from .pipeline.build import build as build_pipeline
from .config import (
    DEFAULT_COMBINE_OUTPUT,
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
    DEFAULT_PROVIDER,
    DEFAULT_RESOLUTION,
    DEFAULT_UNITS,
    BuildConfig,
)
from .parcels.registry import load_sources
from .providers.usgs_index import query_for_point
from .pipeline.io import generate_job_id
from .util import ensure_dir, get_logger

app = Flask(__name__)


OUT_DIR = Path(os.getenv("VA_OUT_DIR", str(DEFAULT_OUT_DIR)))
RETENTION_DAYS = int(os.getenv("VA_RETENTION_DAYS", "7"))
CLEANUP_INTERVAL_SECONDS = int(os.getenv("VA_CLEANUP_INTERVAL", "3600"))
DEFAULT_RANDOM_MIN_HEIGHT = 15.0
DEFAULT_RANDOM_MAX_HEIGHT = 40.0
COVERAGE_CACHE_TTL_SECONDS = int(os.getenv("VA_COVERAGE_CACHE_TTL", "600"))

_cleanup_started = False
_cleanup_lock = threading.Lock()
_coverage_cache: Dict[str, tuple[float, Optional[bool], str]] = {}
_coverage_cache_lock = threading.Lock()


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
      <div class="meta">Status: <span id="status">{{ status_label(job.status) }}</span></div>
      <div class="meta">Provider: {{ job.summary.get('provider_label') or job.summary.get('provider') }}</div>
      <div class="meta">Output folder: {{ job.summary.get('out') }}</div>
      <div class="meta">Target: {{ job.summary.get('target') }}</div>
      {% if job.summary.get('tile') %}
        <div class="meta">Tile: {{ job.summary.get('tile') }}</div>
      {% endif %}
      <div class="meta"><a href="{{ url_for('index') }}">Back to form</a></div>
    </header>
    <main>
      {% if job.error or job.summary.get('coverage') or job.summary.get('warnings') %}
      <div class="card">
        <h3>Job Notes</h3>
        {% if job.error %}
          <p><strong>This job did not complete.</strong> {{ job.error }}</p>
        {% endif %}
        {% if job.summary.get('coverage') %}
          {% set coverage = job.summary.get('coverage') %}
          {% if coverage.get('status') %}
            <p><strong>EPT coverage:</strong> {{ coverage.get('status') }}
              {% if coverage.get('ratio') is not none %}
                (~{{ '%.1f'|format(coverage.get('ratio') * 100) }}%)
              {% endif %}
            </p>
          {% endif %}
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
      <div class="card">
        <h3>Activity Log</h3>
        <pre id="logs"></pre>
      </div>
    </main>
    <script>
      const STATUS_LABELS = {
        queued: 'Queued',
        running: 'Running',
        done: 'Completed',
        error: 'Failed',
      };

      async function pollLogs(jobId) {
        const logsEl = document.getElementById('logs');
        const statusEl = document.getElementById('status');
        if (!logsEl || !statusEl) return;
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
          statusEl.textContent = STATUS_LABELS[logData.status] || logData.status;
          if (logData.status === 'running' || logData.status === 'queued') {
            setTimeout(poll, 1500);
          }
        }
        poll();
      }

      document.addEventListener('DOMContentLoaded', () => {
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


def _collect_outputs(tile_dir: Path) -> Dict[str, Any]:
    if not tile_dir.exists():
        return {"dir": str(tile_dir), "files": []}
    candidates = [
        "terrain.obj",
        "buildings.obj",
        "combined.obj",
        "terrain.png",
        "contours.dxf",
    ]
    files = [name for name in candidates if (tile_dir / name).exists()]
    return {"dir": str(tile_dir), "files": files}


def snapshot_defaults() -> Dict[str, Any]:
    outputs = set(DEFAULT_OUTPUTS)
    return {
        "out": str(OUT_DIR),
        "units": "feet",
        "provider": "va",
        "provider_label": "VGIN (Virginia)",
        "center1": 37.5390116184146,
        "center2": -77.43353162833343,
        "clip_size": 1000.0,
        "resolution": DEFAULT_RESOLUTION,
        "terrain_complexity": 2,
        "output_terrain": "terrain" in outputs,
        "output_buildings": "buildings" in outputs,
        "output_contours": "contours" in outputs,
        "output_parcels": "parcels" in outputs,
        "output_naip": "naip" in outputs,
        "output_combined": DEFAULT_COMBINE_OUTPUT,
        "min_height": DEFAULT_MIN_HEIGHT,
        "max_height": DEFAULT_MAX_HEIGHT,
        "random_min_height": DEFAULT_RANDOM_MIN_HEIGHT,
        "random_max_height": DEFAULT_RANDOM_MAX_HEIGHT,
        "contour_interval": 2.0,
        "image_quality": "standard",
    }


def parcel_sources_payload() -> List[Dict[str, Any]]:
    sources = []
    for source in load_sources():
        payload = {"id": source.id, "name": source.name}
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


@app.before_request
def _start_cleanup():
    ensure_cleanup_thread()


@app.route("/")
def index():
    defaults = snapshot_defaults()
    parcel_sources = parcel_sources_payload()
    with JOBS_LOCK:
        jobs = list(JOBS.values())[-8:][::-1]
    return render_template(
        "index.html",
        defaults=defaults,
        parcel_sources=parcel_sources,
        jobs=jobs,
        retention_days=RETENTION_DAYS,
        status_label=status_label,
    )


@app.route("/recent-jobs")
def recent_jobs():
    with JOBS_LOCK:
        jobs = list(JOBS.values())[-8:][::-1]
    payload = [
        {
            "job_id": job.job_id,
            "status": job.status,
            "status_label": status_label(job.status),
        }
        for job in jobs
    ]
    return jsonify({"jobs": payload})


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
                    {"supported": supported_cached, "provider": provider, "cached": True}
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
def run_job():
    form = request.form
    out_dir = OUT_DIR
    ensure_dir(out_dir)
    units = form.get("units") or DEFAULT_UNITS
    coords = form.get("coords") or ""
    parts = [p for p in re.split(r"[ ,]+", coords.strip()) if p]
    lat = parse_float(parts[0]) if len(parts) > 0 else None
    lon = parse_float(parts[1]) if len(parts) > 1 else None
    provider = resolve_provider(lat, lon)
    ept_only = False
    clip_size = parse_float(form.get("size"))
    if lat is None or lon is None:
        return jsonify({"error": "Provide coordinates as lat, lon."}), 400
    if clip_size is None:
        return jsonify({"error": "Provide a clip size."}), 400

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
    if parse_bool(form.get("output_parcels")):
        outputs.append("parcels")
    if parse_bool(form.get("output_naip")):
        outputs.append("naip")
    if not outputs:
        return jsonify({"error": "Select at least one output."}), 400

    combine_output = parse_bool(form.get("output_combined"))
    if combine_output and not (
        "terrain" in outputs and "buildings" in outputs
    ):
        return (
            jsonify({"error": "Combined output requires terrain + buildings."}),
            400,
        )

    contours_enabled = "contours" in outputs
    contour_interval = (
        (parse_float(form.get("contour_interval")) or 2.0) if contours_enabled else None
    )
    keep_rasters = False

    flip_x = False
    flip_y = False
    terrain_flip_y = False
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
        prefer_ept=True,
        flip_y=flip_y,
        flip_x=flip_x,
        terrain_flip_y=terrain_flip_y,
        rotate_z=rotate_z,
        provider=provider,
        ept_only=ept_only,
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
    }

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
    return render_template_string(STATUS_TEMPLATE, job=job, status_label=status_label)


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
            "summary": job.summary,
        }
    return jsonify(payload)


def _run_build_job(job: Job, cfg: BuildConfig) -> None:
    job.status = "running"
    job.started_at = time.time()
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

        report_path = _find_latest_report(cfg.out_dir, job.started_at or time.time())
        if report_path:
            try:
                report = json.loads(report_path.read_text())
                job.summary["report_path"] = str(report_path)
                job.summary["tile"] = report.get("tile")
                if report.get("output_dir"):
                    job.summary["out"] = report.get("output_dir")
                job.summary["job_id"] = report.get("job_id")
                job.summary["coverage"] = report.get("coverage")
                job.summary["warnings"] = report.get("warnings")
                job.summary["source_type"] = report.get("source_type")
                job.summary["outputs"] = _collect_outputs(report_path.parent)
            except Exception:
                pass


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
