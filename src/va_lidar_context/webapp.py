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

from flask import Flask, jsonify, redirect, render_template_string, request, url_for

from .cli import build_command
from .config import (
    DEFAULT_ALLOW_MULTI_TILE,
    DEFAULT_CLIP_SIZE,
    DEFAULT_COMBINE_OUTPUT,
    DEFAULT_EPT_ONLY,
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
    DEFAULT_PROVIDER,
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
from .parcels.registry import load_sources
from .providers.usgs_lidar_index import query_for_point
from .util import ensure_dir, generate_job_id, get_logger
from .vgin_tile import normalize_coordinates

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


INDEX_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Terrain Modeler</title>
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
        padding-left: calc((100vw - 100%) / 2);
        padding-right: calc((100vw - 100%) / 2);
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
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 16px;
      }
      main > * {
        width: min(600px, 100%);
      }
      .card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.35);
      }
      .app-card {
        height: 800px;
        display: flex;
        flex-direction: column;
      }
      .form-body {
        flex: 1;
        overflow: auto;
        padding-right: 4px;
      }
      .form-footer {
        margin-top: auto;
        display: flex;
        flex-direction: column;
        gap: 12px;
      }
      .advanced-controls {
        margin-top: 12px;
      }
      .form-actions {
        display: flex;
        gap: 12px;
        align-items: center;
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
      .inline-note {
        font-size: 12px;
        color: var(--muted);
        margin-top: 6px;
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
      .status {
        margin: 0;
        padding: 10px 12px;
        border-radius: 8px;
        background: #2f2f2f;
        color: var(--muted);
        font-size: 13px;
      }
      .status.success {
        color: #b8f2c9;
        background: #203328;
      }
      .status.error {
        color: #ffd4d4;
        background: #3b1f1f;
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
      <h1>Terrain Modeler</h1>
      <p class="sub">Generate site context and contour models for anywhere in the USA.</p>
    </header>
    <main>

      <form class="card app-card" method="post" action="{{ url_for('run_job') }}">
        <div class="form-body">
          <div class="section-title">Location</div>
          <div class="grid">
            <div style="grid-column: 1 / -1;">
              <label>Coordinates</label>
              <input type="text" name="coords" value="{{ defaults.center1 }}, {{ defaults.center2 }}" placeholder="lat, lon" />
            </div>
            <div>
              <label>Map Size (Square)</label>
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

          <div class="section-title" style="margin-top:16px;">Outputs</div>
          <div class="check-row">
            <label class="check"><input type="checkbox" id="out_terrain" name="out_terrain" {% if defaults.out_terrain %}checked{% endif %} /> Terrain Mesh</label>
            <label class="check"><input type="checkbox" id="out_buildings" name="out_buildings" {% if defaults.out_buildings %}checked{% endif %} /> Buildings</label>
          </div>
          <div class="check-row" style="margin-top:6px;">
            <label class="check"><input type="checkbox" id="contours" name="contours" {% if defaults.contours %}checked{% endif %} /> Contours</label>
            <label class="check"><input type="checkbox" id="parcels" name="parcels" {% if defaults.parcels %}checked{% endif %} /> Parcels</label>
            <label class="check"><input type="checkbox" id="out_image" name="out_image" {% if defaults.out_image %}checked{% endif %} /> Image</label>
          </div>

          <div id="advancedControls" class="advanced-controls">
            <div id="meshResolutionSection">
              <div class="section-title" style="margin-top:16px;">Mesh Resolution</div>
              <div class="grid" style="margin-top:6px;">
                <div style="grid-column: 1 / -1; display:flex; align-items:center; gap:12px;">
                  <input type="range" min="0" max="10" step="1" name="terrain_complexity" value="{{ defaults.terrain_complexity }}" oninput="document.getElementById('complexityValue').textContent = this.value; updateComplexityEstimate();" />
                  <div id="complexityValue" style="min-width:20px; text-align:right;">{{ defaults.terrain_complexity }}</div>
                </div>
              </div>
              <div class="note" id="complexityEstimate" style="margin-top:6px;"></div>
            </div>

            <div id="buildingHeightsSection">
              <div class="section-title" style="margin-top:16px;">Building Heights</div>
              <div class="grid" style="margin-top:6px;">
                <div>
                  <label>Random Min Height</label>
                  <input type="number" step="any" name="random_min_height" value="{{ defaults.random_min_height }}" />
                </div>
                <div>
                  <label>Random Max Height</label>
                  <input type="number" step="any" name="random_max_height" value="{{ defaults.random_max_height }}" />
                </div>
              </div>
            </div>

            <div id="contourIntervalSection">
              <div class="section-title" style="margin-top:16px;">Contour Interval</div>
              <div class="grid" id="contourIntervalRow">
                <div>
                  <input type="number" step="any" name="contour_interval" value="{{ defaults.contour_interval }}" />
                </div>
              </div>
            </div>

            <div id="imageQualitySection">
              <div class="section-title" style="margin-top:16px;">Image Quality</div>
              <div class="grid" style="margin-top:6px;">
                <div>
                  <select id="image_quality" name="image_quality">
                    <option value="standard" {% if defaults.image_quality == 'standard' %}selected{% endif %}>Standard</option>
                    <option value="high" {% if defaults.image_quality == 'high' %}selected{% endif %}>High</option>
                    <option value="ultra" {% if defaults.image_quality == 'ultra' %}selected{% endif %}>Ultra</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="form-footer">
          <div id="parcelAlert" class="status hidden"></div>
          <div class="form-actions">
            <button class="btn" id="runBtn" type="submit">Build</button>
            <button class="btn secondary" type="reset">Reset</button>
          </div>
        </div>
      </form>
      <div class="note" style="margin-top:20px; text-align:center;">
        Data sources: VGIN LiDAR/Footprints (VA mode), USGS 3DEP LiDAR + Microsoft Footprints (National mode), and NAIP imagery.
      </div>


      <div class="card">
        <div class="section-title">Recent Jobs</div>
        <div id="recentJobs">
          {% if jobs %}
            <ul>
              {% for job in jobs %}
                <li>
                  <a href="{{ url_for('job_status', job_id=job.job_id) }}">{{ job.job_id }}</a>
                  — {{ status_label(job.status) }}
                </li>
              {% endfor %}
            </ul>
          {% else %}
            <p class="footer">No jobs yet.</p>
          {% endif %}
        </div>
      </div>
    </main>
    <script>
      const VA_BOUNDS = { latMin: 36.5, latMax: 39.5, lonMin: -83.0, lonMax: -75.0 };
      const CONUS_BOUNDS = { latMin: 24.5, latMax: 49.5, lonMin: -125.0, lonMax: -66.5 };
      const PARCEL_SOURCES = {{ parcel_sources | tojson }};
      const RECENT_JOBS_POLL_MS = 5000;
      let buildErrorMessage = '';
      let coverageStatus = null;
      let coverageKey = null;
      let coverageTimer = null;
      let coverageRequestId = 0;

      function parseCoords(value) {
        if (!value) return null;
        const parts = value.split(/[\\s,]+/).map((p) => p.trim()).filter(Boolean);
        if (parts.length < 2) return null;
        const c1 = Number(parts[0]);
        const c2 = Number(parts[1]);
        if (!Number.isFinite(c1) || !Number.isFinite(c2)) return null;
        return [c1, c2];
      }

      function normalizeCoords(c1, c2) {
        const c1Lat = c1 >= -90 && c1 <= 90;
        const c2Lat = c2 >= -90 && c2 <= 90;
        if (c1Lat && !c2Lat) return { lon: c2, lat: c1 };
        if (c2Lat && !c1Lat) return { lon: c1, lat: c2 };
        if (c1Lat && c2Lat) {
          if (c1 < 0 && c2 > 0) return { lon: c1, lat: c2 };
          if (c2 < 0 && c1 > 0) return { lon: c2, lat: c1 };
          return { lon: c2, lat: c1 };
        }
        return null;
      }

      function getNormalizedCoords() {
        const coordsInput = document.querySelector('input[name="coords"]');
        if (!coordsInput) return null;
        const parsed = parseCoords(coordsInput.value);
        if (!parsed) return null;
        return normalizeCoords(parsed[0], parsed[1]);
      }

      function coverageKeyFor(lon, lat) {
        return `${lon.toFixed(4)},${lat.toFixed(4)}`;
      }

      function isInVirginia(lon, lat) {
        return (
          lon >= VA_BOUNDS.lonMin &&
          lon <= VA_BOUNDS.lonMax &&
          lat >= VA_BOUNDS.latMin &&
          lat <= VA_BOUNDS.latMax
        );
      }

      function updateProviderLabel() {
        const providerEl = document.getElementById('providerValue');
        if (!providerEl) return;
        const normalized = getNormalizedCoords();
        if (!normalized) {
          providerEl.textContent = 'VGIN (Virginia)';
          return;
        }
        providerEl.textContent = isInVirginia(normalized.lon, normalized.lat)
          ? 'VGIN (Virginia)'
          : 'USGS 3DEP (National)';
      }

      function hasParcelCoverage(lon, lat) {
        if (!Array.isArray(PARCEL_SOURCES) || PARCEL_SOURCES.length === 0) {
          return false;
        }
        const inBBox = (bbox) => (
          lon >= bbox.xmin &&
          lon <= bbox.xmax &&
          lat >= bbox.ymin &&
          lat <= bbox.ymax
        );
        return PARCEL_SOURCES.some((source) => {
          if (Array.isArray(source.exclude)) {
            for (const ex of source.exclude) {
              if (inBBox(ex)) return false;
            }
          }
          const cov = source.coverage;
          if (!cov) return true;
          return inBBox(cov);
        });
      }

      function isInConus(lon, lat) {
        return (
          lon >= CONUS_BOUNDS.lonMin &&
          lon <= CONUS_BOUNDS.lonMax &&
          lat >= CONUS_BOUNDS.latMin &&
          lat <= CONUS_BOUNDS.latMax
        );
      }

      async function checkCoverage() {
        const normalized = getNormalizedCoords();
        if (!normalized) {
          coverageStatus = null;
          coverageKey = null;
          updateAlerts();
          return;
        }
        const key = coverageKeyFor(normalized.lon, normalized.lat);
        const reqId = ++coverageRequestId;
        try {
          const resp = await fetch(`/coverage?lon=${normalized.lon}&lat=${normalized.lat}`, { cache: 'no-store' });
          if (!resp.ok) throw new Error('coverage failed');
          const data = await resp.json();
          if (reqId !== coverageRequestId) return;
          if (data.supported === true) {
            coverageStatus = true;
          } else if (data.supported === false) {
            coverageStatus = false;
          } else {
            coverageStatus = null;
          }
          coverageKey = key;
        } catch (err) {
          if (reqId !== coverageRequestId) return;
          coverageStatus = null;
          coverageKey = null;
        }
        updateAlerts();
      }

      function scheduleCoverageCheck() {
        if (coverageTimer) {
          clearTimeout(coverageTimer);
        }
        coverageTimer = setTimeout(checkCoverage, 400);
      }

      function setAlert(message, isError) {
        const alertEl = document.getElementById('parcelAlert');
        if (!alertEl) return;
        if (!message) {
          alertEl.classList.add('hidden');
          alertEl.classList.remove('error');
          alertEl.textContent = '';
          return;
        }
        alertEl.textContent = message;
        alertEl.classList.remove('hidden');
        if (isError) {
          alertEl.classList.add('error');
        } else {
          alertEl.classList.remove('error');
        }
      }

      function updateAlerts() {
        const parcels = document.getElementById('parcels');
        if (!parcels) {
          setAlert('', false);
          return;
        }
        const coordsInput = document.querySelector('input[name="coords"]');
        const parsed = coordsInput ? parseCoords(coordsInput.value) : null;
        const normalized = parsed ? normalizeCoords(parsed[0], parsed[1]) : null;
        if ((parsed && !normalized) || (normalized && !isInConus(normalized.lon, normalized.lat))) {
          setAlert('Coordinates are outside the supported area (contiguous US).', true);
          return;
        }
        if (
          coverageStatus === false &&
          normalized &&
          coverageKey === coverageKeyFor(normalized.lon, normalized.lat)
        ) {
          setAlert('Coordinates are outside the supported area (contiguous US).', true);
          return;
        }
        if (
          parcels.checked &&
          normalized &&
          !hasParcelCoverage(normalized.lon, normalized.lat)
        ) {
          setAlert('No parcel data available for this location.', true);
          return;
        }
        if (buildErrorMessage) {
          setAlert(buildErrorMessage, true);
          return;
        }
        setAlert('', false);
      }

      function renderRecentJobs(container, jobs) {
        container.innerHTML = '';
        if (!jobs || jobs.length === 0) {
          const empty = document.createElement('p');
          empty.className = 'footer';
          empty.textContent = 'No jobs yet.';
          container.appendChild(empty);
          return;
        }
        const list = document.createElement('ul');
        jobs.forEach((job) => {
          const item = document.createElement('li');
          const link = document.createElement('a');
          link.href = `/jobs/${job.job_id}`;
          link.textContent = job.job_id;
          item.appendChild(link);
          const label = job.status_label || job.status;
          item.appendChild(document.createTextNode(` — ${label}`));
          list.appendChild(item);
        });
        container.appendChild(list);
      }

      async function refreshRecentJobs() {
        const container = document.getElementById('recentJobs');
        if (!container) return;
        try {
          const resp = await fetch('/recent-jobs', { cache: 'no-store' });
          if (!resp.ok) return;
          const data = await resp.json();
          renderRecentJobs(container, data.jobs || []);
        } catch (err) {
          return;
        }
      }

      function startRecentJobsPolling() {
        if (window.__recentJobsPoll) return;
        window.__recentJobsPoll = setInterval(refreshRecentJobs, RECENT_JOBS_POLL_MS);
      }

      function formatCount(value) {
        if (value >= 1e6) return `${(value / 1e6).toFixed(1)}M`;
        if (value >= 1e3) return `${Math.round(value / 1e3)}k`;
        return `${Math.round(value)}`;
      }

      function updateComplexityEstimate() {
        const estimateEl = document.getElementById('complexityEstimate');
        const sizeInput = document.querySelector('input[name="size"]');
        const unitsInput = document.querySelector('select[name="units"]');
        const complexityInput = document.querySelector('input[name="terrain_complexity"]');
        const outTerrain = document.getElementById('out_terrain');
        if (!estimateEl || !sizeInput || !complexityInput || !outTerrain) return;

        if (!outTerrain.checked) {
          estimateEl.textContent = '';
          return;
        }

        const size = Number(sizeInput.value);
        const complexityValue = Number(complexityInput.value || 0);
        const units = unitsInput ? unitsInput.value : 'feet';
        if (!Number.isFinite(size) || size <= 0) {
          estimateEl.textContent = 'Estimated terrain faces: —';
          return;
        }

        const terrainSample = Math.max(1, 11 - Math.round(complexityValue));
        const baseResolution = Number({{ defaults.resolution }}) || 1;
        const metersToFeet = 3.28084;
        let cellSize = baseResolution * terrainSample;
        if (units === 'feet') {
          cellSize *= metersToFeet;
        }
        if (!Number.isFinite(cellSize) || cellSize <= 0) {
          estimateEl.textContent = 'Estimated terrain faces: —';
          return;
        }
        const samplesPerSide = Math.max(2, Math.floor(size / cellSize));
        const faces = 2 * Math.pow(samplesPerSide - 1, 2);
        const resolutionLabel = units === 'feet'
          ? `${(baseResolution * metersToFeet).toFixed(2)} ft`
          : `${baseResolution.toFixed(2)} m`;
        estimateEl.textContent = `Estimated terrain faces: ~${formatCount(faces)} (assumes ${resolutionLabel} raster)`;
      }

      const advancedState = {};

      function setAdvancedVisibility(sectionId, checked) {
        const section = document.getElementById(sectionId);
        const container = document.getElementById('advancedControls');
        if (!section || !container) return;
        const prev = advancedState[sectionId];
        if (checked) {
          section.classList.remove('hidden');
          if (!prev) {
            container.appendChild(section);
          }
        } else {
          section.classList.add('hidden');
        }
        advancedState[sectionId] = checked;
      }

      function updateUiToggles() {
        const contours = document.getElementById('contours');
        const parcels = document.getElementById('parcels');
        const outTerrain = document.getElementById('out_terrain');
        const outBuildings = document.getElementById('out_buildings');
        const outImage = document.getElementById('out_image');
        if (outTerrain) setAdvancedVisibility('meshResolutionSection', outTerrain.checked);
        if (outBuildings) setAdvancedVisibility('buildingHeightsSection', outBuildings.checked);
        if (contours) setAdvancedVisibility('contourIntervalSection', contours.checked);
        if (outImage) setAdvancedVisibility('imageQualitySection', outImage.checked);
        if (parcels) updateAlerts();
        updateComplexityEstimate();
        updateProviderLabel();
      }

      async function runBuild(event) {
        event.preventDefault();
        const form = event.target;
        const runBtn = document.getElementById('runBtn');
        if (!form || !runBtn) return;

        buildErrorMessage = '';
        updateAlerts();
        runBtn.disabled = true;
        const originalText = runBtn.textContent;
        runBtn.textContent = 'Running...';

        const formData = new FormData(form);
        const resp = await fetch(form.action, {
          method: 'POST',
          body: formData,
          headers: { 'X-Requested-With': 'fetch' },
        });
        if (!resp.ok) {
          buildErrorMessage = 'Build failed to start. Please check your inputs and try again.';
          updateAlerts();
          runBtn.disabled = false;
          runBtn.textContent = originalText;
          return;
        }
        const data = await resp.json();

        let offset = 0;
        async function poll() {
          const logResp = await fetch(`/logs/${data.job_id}?offset=${offset}`);
          if (!logResp.ok) return;
          const logData = await logResp.json();
          offset = logData.offset;
          if (logData.status === 'running') {
            setTimeout(poll, 1500);
          } else {
            if (logData.status === 'error') {
              const reason = logData.error ? ` ${logData.error}` : '';
              buildErrorMessage = `Build failed.${reason}`;
              updateAlerts();
            }
            refreshRecentJobs();
            runBtn.disabled = false;
            runBtn.textContent = originalText;
          }
        }
        poll();
      }

      document.addEventListener('DOMContentLoaded', () => {
        updateUiToggles();
        const contours = document.getElementById('contours');
        const parcels = document.getElementById('parcels');
        const outTerrain = document.getElementById('out_terrain');
        const outBuildings = document.getElementById('out_buildings');
        const outImage = document.getElementById('out_image');
        const coords = document.querySelector('input[name="coords"]');
        const size = document.querySelector('input[name="size"]');
        const units = document.querySelector('select[name="units"]');
        if (contours) contours.addEventListener('change', updateUiToggles);
        if (parcels) parcels.addEventListener('change', updateAlerts);
        if (outTerrain) outTerrain.addEventListener('change', updateUiToggles);
        if (outBuildings) outBuildings.addEventListener('change', updateUiToggles);
        if (outImage) outImage.addEventListener('change', updateUiToggles);
        if (coords) coords.addEventListener('input', () => {
          updateProviderLabel();
          updateAlerts();
          scheduleCoverageCheck();
        });
        if (size) size.addEventListener('input', updateComplexityEstimate);
        if (units) units.addEventListener('change', updateComplexityEstimate);
        const form = document.querySelector('form.card');
        if (form) {
          form.addEventListener('submit', runBuild);
          form.addEventListener('reset', () => {
            setTimeout(() => {
              updateUiToggles();
              updateAlerts();
              scheduleCoverageCheck();
            }, 0);
          });
        }
        refreshRecentJobs();
        startRecentJobsPolling();
        scheduleCoverageCheck();
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


def resolve_provider(center1: float | None, center2: float | None) -> str:
    if center1 is None or center2 is None:
        return DEFAULT_PROVIDER
    try:
        lon, lat = normalize_coordinates(center1, center2)
    except Exception:
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
        "trees.obj",
    ]
    files = [name for name in candidates if (tile_dir / name).exists()]
    return {"dir": str(tile_dir), "files": files}


def snapshot_defaults() -> Dict[str, Any]:
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
        "out_terrain": True,
        "out_buildings": True,
        "trees": False,
        "min_height": DEFAULT_MIN_HEIGHT,
        "max_height": DEFAULT_MAX_HEIGHT,
        "random_min_height": DEFAULT_RANDOM_MIN_HEIGHT,
        "random_max_height": DEFAULT_RANDOM_MAX_HEIGHT,
        "contours": True,
        "contour_interval": 2.0,
        "parcels": False,
        "out_image": True,
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
    return render_template_string(
        INDEX_TEMPLATE,
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

    provider = resolve_provider(lon, lat)
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
    tile_name = None
    out_dir = OUT_DIR
    ensure_dir(out_dir)
    units = form.get("units") or DEFAULT_UNITS
    center_mode = "auto"
    coords = form.get("coords") or ""
    parts = [p for p in re.split(r"[ ,]+", coords.strip()) if p]
    center1 = parse_float(parts[0]) if len(parts) > 0 else None
    center2 = parse_float(parts[1]) if len(parts) > 1 else None
    provider = resolve_provider(center1, center2)
    ept_only = False
    clip_size = parse_float(form.get("size"))
    if provider == "national" and clip_size is None:
        return jsonify({"error": "National provider requires a clip size."}), 400

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

    naip_texture = parse_bool(form.get("out_image"))
    naip_pixel_size, naip_max_size, naip_tiled = resolve_image_quality(
        form.get("image_quality")
    )
    naip_flip_u = DEFAULT_NAIP_FLIP_U
    naip_flip_v = DEFAULT_NAIP_FLIP_V

    export_terrain = parse_bool(form.get("out_terrain"))
    export_buildings = parse_bool(form.get("out_buildings"))
    combine_output = export_terrain and export_buildings
    contours_enabled = parse_bool(form.get("contours"))
    contour_interval = (
        (parse_float(form.get("contour_interval")) or 2.0) if contours_enabled else None
    )
    parcels = parse_bool(form.get("parcels"))
    trees = parse_bool(form.get("trees"))
    keep_rasters = False

    trees_resolution = DEFAULT_TREES_RESOLUTION
    trees_sample = DEFAULT_TREES_SAMPLE
    trees_min_height = DEFAULT_TREES_MIN_HEIGHT
    trees_max_height = DEFAULT_TREES_MAX_HEIGHT
    trees_radius = DEFAULT_TREES_RADIUS

    flip_x = False
    flip_y = False
    terrain_flip_y = False
    rotate_z = 0.0

    allow_multi_tile = True
    force = False

    job_id = generate_job_id(
        (center1, center2) if center1 is not None and center2 is not None else None,
        clip_size,
        units,
    )
    cfg = BuildConfig(
        tile_name=tile_name,
        job_id=job_id,
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
        naip_tiled=naip_tiled,
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
        export_terrain=export_terrain,
        prefer_ept=True,
        flip_y=flip_y,
        flip_x=flip_x,
        terrain_flip_y=terrain_flip_y,
        rotate_z=rotate_z,
        provider=provider,
        ept_only=ept_only,
        cleanup_intermediates=True,
    )

    target_summary = None
    if center1 is not None and center2 is not None:
        target_summary = f"{center_mode}:{center1},{center2} size={clip_size}"

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
