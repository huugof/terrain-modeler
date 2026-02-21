const VA_BOUNDS = { latMin: 36.5, latMax: 39.5, lonMin: -83.0, lonMax: -75.0 };
const CONUS_BOUNDS = { latMin: 24.5, latMax: 49.5, lonMin: -125.0, lonMax: -66.5 };
const PARCEL_SOURCES = (window.APP_CONFIG && window.APP_CONFIG.parcelSources) || [];
const RECENT_JOBS_WAIT_SECONDS = 25;
const RECENT_JOBS_RETRY_MS = 1500;
const CAN_BUILD = Boolean(window.APP_CONFIG && window.APP_CONFIG.canBuild);
let buildErrorMessage = '';
let coverageStatus = null;
let coverageKey = null;
let coverageTimer = null;
let coverageRequestId = 0;
let recentJobsVersion = 0;

function setFaviconFromLucide() {
  const icon = document.getElementById('faviconSource');
  if (!icon || icon.tagName.toLowerCase() !== 'svg') return;
  const svg = icon.cloneNode(true);
  svg.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
  svg.setAttribute('width', '64');
  svg.setAttribute('height', '64');
  svg.style.color = '#e4e4e4';
  const encoded = encodeURIComponent(svg.outerHTML)
    .replace(/'/g, '%27')
    .replace(/"/g, '%22');
  const link = document.getElementById('favicon');
  if (link) {
    link.href = `data:image/svg+xml,${encoded}`;
  }
}

function parseCoords(value) {
  if (!value) return null;
  const parts = value.split(/[\s,]+/).map((p) => p.trim()).filter(Boolean);
  if (parts.length < 2) return null;
  const lat = Number(parts[0]);
  const lon = Number(parts[1]);
  if (!Number.isFinite(lat) || !Number.isFinite(lon)) return null;
  return { lat, lon };
}

function getCoords() {
  const coordsInput = document.querySelector('input[name="coords"]');
  if (!coordsInput) return null;
  return parseCoords(coordsInput.value);
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
  const coords = getCoords();
  if (!coords) {
    coverageStatus = null;
    coverageKey = null;
    updateAlerts();
    return;
  }
  const key = coverageKeyFor(coords.lon, coords.lat);
  const reqId = ++coverageRequestId;
  try {
    const resp = await fetch(`/coverage?lon=${coords.lon}&lat=${coords.lat}`, { cache: 'no-store' });
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
  const parcels = document.getElementById('dxf_include_parcels');
  const contours = document.getElementById('output_contours');
  const coordsInput = document.querySelector('input[name="coords"]');
  const coords = coordsInput ? parseCoords(coordsInput.value) : null;
  if (coordsInput && coordsInput.value.trim() && !coords) {
    setAlert('Coordinates are invalid. Use "lat, lon".', true);
    return;
  }
  if (coords && !isInConus(coords.lon, coords.lat)) {
    setAlert('Coordinates are outside the supported area (contiguous US).', true);
    return;
  }
  if (
    coverageStatus === false &&
    coords &&
    coverageKey === coverageKeyFor(coords.lon, coords.lat)
  ) {
    setAlert('Coordinates are outside the supported area (contiguous US).', true);
    return;
  }
  const parcelsRequested = Boolean(
    parcels &&
    contours &&
    contours.checked &&
    parcels.checked
  );
  if (parcelsRequested && coords && !hasParcelCoverage(coords.lon, coords.lat)) {
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
  list.className = 'recent-job-list';
  jobs.forEach((job) => {
    const item = document.createElement('li');
    item.className = 'recent-job-row';
    const isDone = job.status === 'done';
    const name = job.name || job.job_id;

    const title = document.createElement('div');
    title.className = 'recent-job-title';
    title.textContent = isDone ? name : 'Job running...';
    item.appendChild(title);

    if (isDone) {
      const actions = document.createElement('div');
      actions.className = 'recent-job-actions';
      if (job.preview_url) {
        const previewLink = document.createElement('a');
        previewLink.className = 'recent-job-pill';
        previewLink.href = job.preview_url;
        previewLink.textContent = 'Preview';
        previewLink.dataset.previewModal = '1';
        previewLink.dataset.previewUrl = job.preview_url;
        previewLink.dataset.previewTitle = name;
        actions.appendChild(previewLink);
      }
      if (job.download_all_url) {
        const downloadLink = document.createElement('a');
        downloadLink.className = 'recent-job-pill';
        downloadLink.href = job.download_all_url;
        downloadLink.textContent = 'Download';
        actions.appendChild(downloadLink);
      }
      const matchLink = document.createElement('a');
      matchLink.className = 'recent-job-pill';
      matchLink.href = job.match_settings_url || `/?from_job=${encodeURIComponent(job.job_id)}`;
      matchLink.textContent = 'Match Settings';
      actions.appendChild(matchLink);
      item.appendChild(actions);
    }

    list.appendChild(item);
  });
  container.appendChild(list);
}

function openPreviewModal(url) {
  const modal = document.getElementById('previewModal');
  const frame = document.getElementById('previewModalFrame');
  if (!modal || !frame) return;
  let embedUrl = url;
  try {
    const parsed = new URL(url, window.location.origin);
    parsed.searchParams.set('embed', '1');
    embedUrl = `${parsed.pathname}${parsed.search}${parsed.hash}`;
  } catch (err) {
    const separator = url && url.includes('?') ? '&' : '?';
    embedUrl = `${url}${separator}embed=1`;
  }
  frame.src = embedUrl;
  modal.classList.remove('hidden');
  modal.setAttribute('aria-hidden', 'false');
  document.body.classList.add('modal-open');
}

function closePreviewModal() {
  const modal = document.getElementById('previewModal');
  const frame = document.getElementById('previewModalFrame');
  if (!modal || !frame) return;
  modal.classList.add('hidden');
  modal.setAttribute('aria-hidden', 'true');
  frame.src = 'about:blank';
  document.body.classList.remove('modal-open');
}

function initPreviewModal() {
  document.addEventListener('click', (event) => {
    const previewLink = event.target.closest('a[data-preview-modal="1"]');
    if (previewLink) {
      event.preventDefault();
      const url = previewLink.dataset.previewUrl || previewLink.href;
      openPreviewModal(url);
      return;
    }
    const closeTarget = event.target.closest('[data-preview-close="1"]');
    if (closeTarget) {
      event.preventDefault();
      closePreviewModal();
    }
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closePreviewModal();
  });
}

async function refreshRecentJobs(options = {}) {
  if (!CAN_BUILD) return;
  const container = document.getElementById('recentJobs');
  if (!container) return;
  const waitSeconds = Number.isFinite(options.waitSeconds)
    ? Math.max(0, options.waitSeconds)
    : 0;
  const hasSince = Number.isFinite(options.sinceVersion);
  const params = new URLSearchParams();
  if (waitSeconds > 0) {
    params.set('wait', String(waitSeconds));
  }
  if (hasSince) {
    params.set('since', String(Math.max(0, options.sinceVersion)));
  }
  const path = params.toString() ? `/recent-jobs?${params.toString()}` : '/recent-jobs';
  try {
    const resp = await fetch(path, { cache: 'no-store' });
    if (!resp.ok) {
      if (resp.status === 401 || resp.status === 403) {
        return { ok: false, stop: true };
      }
      return { ok: false, stop: false };
    }
    const data = await resp.json();
    renderRecentJobs(container, data.jobs || []);
    if (typeof data.version === 'number') {
      recentJobsVersion = data.version;
    }
    return { ok: true, stop: false };
  } catch (err) {
    return { ok: false, stop: false };
  }
}

function startRecentJobsPolling() {
  if (window.__recentJobsPoll) return;
  window.__recentJobsPoll = true;
  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  (async () => {
    while (window.__recentJobsPoll) {
      const result = await refreshRecentJobs({
        waitSeconds: RECENT_JOBS_WAIT_SECONDS,
        sinceVersion: recentJobsVersion,
      });
      if (result && result.stop) break;
      if (!result || !result.ok) {
        await sleep(RECENT_JOBS_RETRY_MS);
      }
    }
    window.__recentJobsPoll = false;
  })();
}

function updateUnitLabels() {
  const unitsInput = document.querySelector('select[name="units"]');
  const unitValue = unitsInput ? unitsInput.value : 'feet';
  const label = unitValue === 'meters' ? 'meters' : 'feet';
  document.querySelectorAll('[data-unit-label]').forEach((el) => {
    el.textContent = label;
  });
}

function initSegmentedControls() {
  document.querySelectorAll('.segmented[data-target]').forEach((segmented) => {
    const inputId = segmented.dataset.target;
    const input = document.getElementById(inputId);
    const buttons = Array.from(segmented.querySelectorAll('button[data-value]'));
    if (!input || buttons.length === 0) return;
    const bound = segmented.dataset.bound === 'true';
    const values = buttons.map((btn) => btn.dataset.value);
    let current = input.value;
    if (!values.includes(current)) {
      if (inputId === 'contour_interval') {
        const numeric = Number(current);
        let best = values[0];
        let bestDelta = Infinity;
        values.forEach((value) => {
          const delta = Math.abs(Number(value) - numeric);
          if (delta < bestDelta) {
            bestDelta = delta;
            best = value;
          }
        });
        current = best;
      } else {
        current = values[0];
      }
      input.value = current;
    }
    const setActive = (value) => {
      input.value = value;
      buttons.forEach((btn) => {
        btn.classList.toggle('active', btn.dataset.value === value);
      });
    };
    setActive(current);
    if (!bound) {
      buttons.forEach((btn) => {
        btn.addEventListener('click', () => setActive(btn.dataset.value));
      });
      segmented.dataset.bound = 'true';
    }
  });
}

function syncToggleButtons() {
  document.querySelectorAll('button[data-input]').forEach((btn) => {
    const input = document.getElementById(btn.dataset.input);
    if (!input) return;
    btn.classList.toggle('active', input.checked);
    btn.setAttribute('aria-pressed', input.checked ? 'true' : 'false');
    btn.disabled = input.disabled;
  });
}

function initToggleButtons() {
  document.querySelectorAll('button[data-input]').forEach((btn) => {
    if (btn.dataset.bound === 'true') return;
    const input = document.getElementById(btn.dataset.input);
    if (!input) return;
    btn.addEventListener('click', () => {
      if (btn.disabled) return;
      input.checked = !input.checked;
      syncToggleButtons();
      updateAlerts();
    });
    btn.dataset.bound = 'true';
  });
  syncToggleButtons();
}

function setSectionLocked(sectionId, locked) {
  const section = document.getElementById(sectionId);
  if (!section) return;
  section.classList.toggle('locked', locked);
}

function updateUiToggles() {
  const contours = document.getElementById('output_contours');
  const outTerrain = document.getElementById('output_terrain');
  const outBuildings = document.getElementById('output_buildings');
  const outImage = document.getElementById('output_naip');
  const outXyz = document.getElementById('output_xyz');
  const xyzMode = document.getElementById('xyz_mode');
  const dxfParcels = document.getElementById('dxf_include_parcels');
  const dxfBuildings = document.getElementById('dxf_include_buildings');

  const contoursActive = contours && contours.checked;
  const xyzActive = outXyz && outXyz.checked;
  const terrainActive = outTerrain && outTerrain.checked;
  const buildingsActive = outBuildings && outBuildings.checked;
  const rotationActive = terrainActive || buildingsActive || contoursActive || xyzActive;
  const projectZeroActive = rotationActive;
  const xyzModeIsContours = xyzMode && xyzMode.value === 'contours';
  const showContourControls = contoursActive || (xyzActive && xyzModeIsContours);

  setSectionLocked('meshResolutionSection', false);
  setSectionLocked('buildingHeightsSection', !buildingsActive);
  setSectionLocked('contourIntervalSection', !showContourControls);
  setSectionLocked('contourLayersSection', !contoursActive);
  setSectionLocked('contourSmoothingSection', !contoursActive);
  setSectionLocked('xyzSamplingSection', !xyzActive);
  setSectionLocked('imageQualitySection', !(outImage && outImage.checked));
  setSectionLocked('rotationSection', !rotationActive);
  setSectionLocked('projectZeroSection', !projectZeroActive);

  if (dxfParcels) dxfParcels.disabled = !contoursActive;
  if (dxfBuildings) dxfBuildings.disabled = !contoursActive;
  const parcelsBtn = document.querySelector('button[data-input="dxf_include_parcels"]');
  const buildingsBtn = document.querySelector('button[data-input="dxf_include_buildings"]');
  if (parcelsBtn) parcelsBtn.disabled = !contoursActive;
  if (buildingsBtn) buildingsBtn.disabled = !contoursActive;

  const dxfRange = document.getElementById('dxfSpacingRange');
  const dxfValue = document.getElementById('dxfSpacingValue');
  if (dxfRange && dxfValue) {
    dxfRange.disabled = !contoursActive;
    dxfValue.textContent = dxfRange.value;
  }
  const complexityInput = document.querySelector('input[name="terrain_complexity"]');
  const complexityValue = document.getElementById('complexityValue');
  if (complexityInput && complexityValue) {
    complexityValue.textContent = complexityInput.value;
  }

  updateAlerts();
  syncToggleButtons();
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
    try {
      const payload = await resp.json();
      buildErrorMessage = payload.error || 'Build failed to start. Please check your inputs and try again.';
    } catch (err) {
      buildErrorMessage = 'Build failed to start. Please check your inputs and try again.';
    }
    updateAlerts();
    runBtn.disabled = false;
    runBtn.textContent = originalText;
    return;
  }
  const data = await resp.json();

  let offset = 0;
  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  while (true) {
    try {
      const logResp = await fetch(`/logs/${data.job_id}?offset=${offset}&wait=25`, {
        cache: 'no-store',
      });
      if (!logResp.ok) {
        if (logResp.status === 401 || logResp.status === 403 || logResp.status === 404) {
          buildErrorMessage = 'Build status is no longer available. Please refresh and try again.';
          updateAlerts();
          break;
        }
        await sleep(1500);
        continue;
      }
      const logData = await logResp.json();
      if (typeof logData.offset === 'number') {
        offset = logData.offset;
      }
      if (logData.status === 'running' || logData.status === 'queued') {
        continue;
      }
      if (logData.status === 'error') {
        const reason = logData.error ? ` ${logData.error}` : '';
        buildErrorMessage = `Build failed.${reason}`;
        updateAlerts();
      }
      break;
    } catch (err) {
      await sleep(1500);
    }
  }
  refreshRecentJobs();
  runBtn.disabled = false;
  runBtn.textContent = originalText;
}

document.addEventListener('DOMContentLoaded', () => {
  initPreviewModal();
  const profileShell = document.getElementById('profileShell');
  const profileButton = document.getElementById('profileButton');
  const profileDropdown = document.getElementById('profileDropdown');
  if (profileShell && profileButton && profileDropdown) {
    const closeProfileMenu = () => {
      profileDropdown.classList.add('hidden');
      profileButton.setAttribute('aria-expanded', 'false');
    };
    profileButton.addEventListener('click', (event) => {
      event.preventDefault();
      event.stopPropagation();
      const willOpen = profileDropdown.classList.contains('hidden');
      if (willOpen) {
        profileDropdown.classList.remove('hidden');
        profileButton.setAttribute('aria-expanded', 'true');
      } else {
        closeProfileMenu();
      }
    });
    document.addEventListener('click', (event) => {
      if (!profileShell.contains(event.target)) {
        closeProfileMenu();
      }
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        closeProfileMenu();
      }
    });
  }

  initSegmentedControls();
  initToggleButtons();
  updateUnitLabels();
  updateUiToggles();
  if (window.lucide) {
    lucide.createIcons();
    setFaviconFromLucide();
  }
  const contours = document.getElementById('output_contours');
  const outTerrain = document.getElementById('output_terrain');
  const outBuildings = document.getElementById('output_buildings');
  const outImage = document.getElementById('output_naip');
  const outXyz = document.getElementById('output_xyz');
  const xyzMode = document.getElementById('xyz_mode');
  const dxfParcels = document.getElementById('dxf_include_parcels');
  const coords = document.querySelector('input[name="coords"]');
  const units = document.querySelector('select[name="units"]');
  if (contours) contours.addEventListener('change', updateUiToggles);
  if (dxfParcels) dxfParcels.addEventListener('change', updateAlerts);
  if (outTerrain) outTerrain.addEventListener('change', updateUiToggles);
  if (outBuildings) outBuildings.addEventListener('change', updateUiToggles);
  if (outImage) outImage.addEventListener('change', updateUiToggles);
  if (outXyz) outXyz.addEventListener('change', updateUiToggles);
  if (xyzMode) xyzMode.addEventListener('change', updateUiToggles);
  if (coords) coords.addEventListener('input', () => {
    updateAlerts();
    scheduleCoverageCheck();
  });
  if (units) units.addEventListener('change', () => {
    updateUnitLabels();
  });
  const form = document.querySelector('form.card');
  if (form) {
    if (CAN_BUILD) {
      form.addEventListener('submit', runBuild);
    }
    form.addEventListener('reset', () => {
      setTimeout(() => {
        initSegmentedControls();
        initToggleButtons();
        updateUnitLabels();
        updateUiToggles();
        updateAlerts();
        scheduleCoverageCheck();
      }, 0);
    });
  }
  if (CAN_BUILD) {
    refreshRecentJobs();
    startRecentJobsPolling();
  }
  scheduleCoverageCheck();
  initThemeToggle();
});

function initThemeToggle() {
  const STORAGE_KEY = 'terrain-theme';
  const root = document.documentElement;
  const btn = document.getElementById('themeToggle');
  if (!btn) return;

  const saved = localStorage.getItem(STORAGE_KEY);
  if (saved === 'light') {
    root.setAttribute('data-theme', 'light');
  }

  btn.addEventListener('click', () => {
    const isLight = root.getAttribute('data-theme') === 'light';
    if (isLight) {
      root.removeAttribute('data-theme');
      localStorage.setItem(STORAGE_KEY, 'dark');
    } else {
      root.setAttribute('data-theme', 'light');
      localStorage.setItem(STORAGE_KEY, 'light');
    }
  });
}
