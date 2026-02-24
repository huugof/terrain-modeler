const VA_BOUNDS = { latMin: 36.5, latMax: 39.5, lonMin: -83.0, lonMax: -75.0 };
const CONUS_BOUNDS = {
  latMin: 24.5,
  latMax: 49.5,
  lonMin: -125.0,
  lonMax: -66.5,
};
const LARGE_MAP_SIZE_WARNING_FEET = 5000;
const PARCEL_SOURCES =
  (window.APP_CONFIG && window.APP_CONFIG.parcelSources) || [];
const RECENT_JOBS_WAIT_SECONDS = 25;
const RECENT_JOBS_RETRY_MS = 1500;
const CAN_BUILD = Boolean(window.APP_CONFIG && window.APP_CONFIG.canBuild);
const AUTH_ENABLED = Boolean(
  window.APP_CONFIG && window.APP_CONFIG.authEnabled,
);
const AUTH_LOGIN_URL =
  (window.APP_CONFIG && window.APP_CONFIG.authLoginUrl) || "/auth/login";
const LAST_PREVIEW_KEY = "terrain-last-preview-url";
let buildErrorMessage = "";
let coverageStatus = null;
let coverageKey = null;
let coverageProvider = null;
let coverageError = "";
let coverageTimer = null;
let coverageRequestId = 0;
let recentJobsVersion = 0;
let recentJobsData = [];
let currentPreviewPath = "";
let formRecordMode = false;
let projectNamePromptResolver = null;
let deleteJobPromptResolver = null;

function setFaviconFromLucide() {
  const icon = document.getElementById("faviconSource");
  if (!icon || icon.tagName.toLowerCase() !== "svg") return;
  const svg = icon.cloneNode(true);
  svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  svg.setAttribute("width", "64");
  svg.setAttribute("height", "64");
  svg.style.color = "#e4e4e4";
  const encoded = encodeURIComponent(svg.outerHTML)
    .replace(/'/g, "%27")
    .replace(/"/g, "%22");
  const link = document.getElementById("favicon");
  if (link) {
    link.href = `data:image/svg+xml,${encoded}`;
  }
}

function normalizePreviewPath(value) {
  if (!value) return "";
  try {
    const parsed = new URL(String(value), window.location.origin);
    return `${parsed.pathname}${parsed.search}`;
  } catch (err) {
    return String(value || "").trim();
  }
}

function getPreviewJobs() {
  if (!Array.isArray(recentJobsData)) return [];
  return recentJobsData.filter((job) => {
    return Boolean(
      job && typeof job.preview_url === "string" && job.preview_url,
    );
  });
}

function getActivePreviewPath(jobs = recentJobsData) {
  if (!Array.isArray(jobs) || jobs.length === 0) return "";
  const previewPaths = jobs
    .filter(
      (job) => job && typeof job.preview_url === "string" && job.preview_url,
    )
    .map((job) => normalizePreviewPath(job.preview_url))
    .filter(Boolean);
  if (!previewPaths.length) return "";
  const current = normalizePreviewPath(currentPreviewPath);
  if (current && previewPaths.includes(current)) return current;
  return previewPaths[0];
}

function updateRecentJobsMeta(count) {
  const meta = document.getElementById("recentJobsMeta");
  if (!meta) return;
  const limit = Number(
    window.APP_CONFIG && Number(window.APP_CONFIG.recentJobsLimit),
  );
  if (Number.isFinite(limit) && limit > 0) {
    meta.textContent = `(${count}/${limit} shown)`;
    return;
  }
  meta.textContent = `(${count} shown)`;
}

function getActiveDownloadJob() {
  if (!Array.isArray(recentJobsData) || recentJobsData.length === 0) {
    return null;
  }
  const current = normalizePreviewPath(currentPreviewPath);
  if (current) {
    const matched = recentJobsData.find((job) => {
      if (!job || !job.preview_url || !job.download_all_url) return false;
      return normalizePreviewPath(job.preview_url) === current;
    });
    if (matched) return matched;
  }
  return (
    recentJobsData.find(
      (job) =>
        job && typeof job.download_all_url === "string" && job.download_all_url,
    ) || null
  );
}

function updatePreviewDownloadButton() {
  const downloadBtn = document.getElementById("previewDownloadButton");
  if (!downloadBtn) return;
  const activeJob = getActiveDownloadJob();
  const url =
    activeJob && typeof activeJob.download_all_url === "string"
      ? activeJob.download_all_url
      : "";
  if (!url) {
    downloadBtn.disabled = true;
    delete downloadBtn.dataset.downloadUrl;
    return;
  }
  downloadBtn.disabled = false;
  downloadBtn.dataset.downloadUrl = url;
}

function updatePreviewNavButtons() {
  const prevBtn = document.getElementById("previewPrevButton");
  const nextBtn = document.getElementById("previewNextButton");
  if (!prevBtn || !nextBtn) {
    updatePreviewDownloadButton();
    return;
  }
  const previewJobs = getPreviewJobs();
  if (previewJobs.length < 2) {
    prevBtn.disabled = true;
    nextBtn.disabled = true;
    updatePreviewDownloadButton();
    return;
  }
  const normalizedPaths = previewJobs.map((job) =>
    normalizePreviewPath(job.preview_url),
  );
  const current = normalizePreviewPath(currentPreviewPath);
  const currentIndex = normalizedPaths.indexOf(current);
  if (currentIndex < 0) {
    prevBtn.disabled = false;
    nextBtn.disabled = false;
    updatePreviewDownloadButton();
    return;
  }
  // Left button moves down the list (older), right button moves to newer.
  prevBtn.disabled = currentIndex >= normalizedPaths.length - 1;
  nextBtn.disabled = currentIndex <= 0;
  updatePreviewDownloadButton();
}

function navigatePreview(direction) {
  const previewJobs = getPreviewJobs();
  if (previewJobs.length < 2) return;
  const normalizedPaths = previewJobs.map((job) =>
    normalizePreviewPath(job.preview_url),
  );
  const current = normalizePreviewPath(currentPreviewPath);
  const currentIndex = normalizedPaths.indexOf(current);
  let targetIndex = 0;
  if (currentIndex >= 0) {
    targetIndex = currentIndex + direction;
  } else {
    targetIndex = direction > 0 ? 0 : previewJobs.length - 1;
  }
  if (targetIndex < 0 || targetIndex >= previewJobs.length) {
    return;
  }
  const targetJob = previewJobs[targetIndex];
  if (!targetJob || !targetJob.preview_url) return;
  applyRecentJobPreview(targetJob.preview_url, targetJob.form_defaults || {});
}

function parseCoords(value) {
  if (!value) return null;
  const parts = value
    .split(/[\s,]+/)
    .map((p) => p.trim())
    .filter(Boolean);
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

function coverageKeyFor(lon, lat, size, units) {
  const sizeNum = Number(size);
  const sizeKey =
    Number.isFinite(sizeNum) && sizeNum > 0 ? sizeNum.toFixed(2) : "none";
  const unitsKey = units === "meters" ? "meters" : "feet";
  return `${lon.toFixed(4)},${lat.toFixed(4)},${sizeKey},${unitsKey}`;
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
  const inBBox = (bbox) =>
    lon >= bbox.xmin &&
    lon <= bbox.xmax &&
    lat >= bbox.ymin &&
    lat <= bbox.ymax;
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

function mapSizeFeet(sizeValue, unitsValue) {
  const size = Number(sizeValue);
  if (!Number.isFinite(size) || size <= 0) return null;
  return unitsValue === "meters" ? size * 3.28084 : size;
}

async function checkCoverage() {
  if (formRecordMode) {
    coverageStatus = null;
    coverageKey = null;
    coverageProvider = null;
    coverageError = "";
    updateAlerts();
    return;
  }
  const coords = getCoords();
  const sizeInput = document.querySelector('input[name="size"]');
  const unitsInput = document.querySelector('select[name="units"]');
  const sizeRaw = Number(sizeInput ? sizeInput.value : "");
  const size = Number.isFinite(sizeRaw) && sizeRaw > 0 ? sizeRaw : null;
  const units = unitsInput && unitsInput.value === "meters" ? "meters" : "feet";
  if (!coords) {
    coverageStatus = null;
    coverageKey = null;
    coverageProvider = null;
    coverageError = "";
    updateAlerts();
    return;
  }
  const key = coverageKeyFor(coords.lon, coords.lat, size, units);
  const reqId = ++coverageRequestId;
  try {
    const params = new URLSearchParams({
      lon: String(coords.lon),
      lat: String(coords.lat),
    });
    if (size !== null) {
      params.set("size", String(size));
      params.set("units", units);
    }
    const resp = await fetch(`/coverage?${params.toString()}`, {
      cache: "no-store",
    });
    if (!resp.ok) throw new Error("coverage failed");
    const data = await resp.json();
    if (reqId !== coverageRequestId) return;
    coverageProvider = typeof data.provider === "string" ? data.provider : null;
    coverageError = typeof data.error === "string" ? data.error : "";
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
    coverageProvider = null;
    coverageError = "";
  }
  updateAlerts();
}

function scheduleCoverageCheck() {
  if (formRecordMode) {
    if (coverageTimer) {
      clearTimeout(coverageTimer);
      coverageTimer = null;
    }
    return;
  }
  if (coverageTimer) {
    clearTimeout(coverageTimer);
  }
  coverageTimer = setTimeout(checkCoverage, 400);
}

function setAlert(message, tone) {
  const alertEl = document.getElementById("parcelAlert");
  if (!alertEl) return;
  const isError = tone === true || tone === "error";
  const isWarning = tone === "warning";
  if (!message) {
    alertEl.classList.add("hidden");
    alertEl.classList.remove("error");
    alertEl.classList.remove("warning");
    alertEl.textContent = "";
    return;
  }
  alertEl.textContent = message;
  alertEl.classList.remove("hidden");
  alertEl.classList.toggle("error", isError);
  alertEl.classList.toggle("warning", isWarning);
}

function updateAlerts() {
  const parcels = document.getElementById("dxf_include_parcels");
  const contours = document.getElementById("output_contours");
  const outBuildings = document.getElementById("output_buildings");
  const inlinePreviewDemo = document.getElementById("inlinePreviewDemo");
  const suppressCoverageWarnings = Boolean(
    inlinePreviewDemo && !inlinePreviewDemo.classList.contains("hidden"),
  );
  if (formRecordMode) {
    setAlert("", false);
    return;
  }
  const coordsInput = document.querySelector('input[name="coords"]');
  const sizeInput = document.querySelector('input[name="size"]');
  const unitsInput = document.querySelector('select[name="units"]');
  const sizeFeet = mapSizeFeet(
    sizeInput ? sizeInput.value : "",
    unitsInput ? unitsInput.value : "feet",
  );
  const coverageSizeRaw = Number(sizeInput ? sizeInput.value : "");
  const coverageSize =
    Number.isFinite(coverageSizeRaw) && coverageSizeRaw > 0
      ? coverageSizeRaw
      : null;
  const coverageUnits =
    unitsInput && unitsInput.value === "meters" ? "meters" : "feet";
  const coords = coordsInput ? parseCoords(coordsInput.value) : null;
  const currentCoverageKey = coords
    ? coverageKeyFor(coords.lon, coords.lat, coverageSize, coverageUnits)
    : null;
  if (coordsInput && coordsInput.value.trim() && !coords) {
    setAlert('Coordinates are invalid. Use "lat, lon".', true);
    return;
  }
  if (coords && !isInConus(coords.lon, coords.lat)) {
    setAlert(
      "Coordinates are outside the supported area (contiguous U.S. only).",
      true,
    );
    return;
  }
  if (
    coverageStatus === false &&
    coords &&
    coverageKey === currentCoverageKey
  ) {
    if (!suppressCoverageWarnings) {
      if (coverageProvider === "national") {
        setAlert(
          "Coverage pre-check could not confirm USGS 3DEP LiDAR for this map area. You can still try a build.",
          "warning",
        );
      } else {
        setAlert("No LiDAR coverage was found at this location.", true);
      }
      return;
    }
  }
  if (
    coverageStatus === null &&
    coverageError &&
    coords &&
    coverageKey === currentCoverageKey
  ) {
    if (!suppressCoverageWarnings) {
      setAlert(
        "Could not verify coverage right now. You can still try a build, but it may fail.",
        "warning",
      );
      return;
    }
  }
  const parcelsRequested = Boolean(
    parcels && contours && contours.checked && parcels.checked,
  );
  if (
    parcelsRequested &&
    coords &&
    !hasParcelCoverage(coords.lon, coords.lat)
  ) {
    setAlert("No parcel data available for this location.", true);
    return;
  }
  if (buildErrorMessage) {
    setAlert(buildErrorMessage, true);
    return;
  }
  if (sizeFeet !== null && sizeFeet > LARGE_MAP_SIZE_WARNING_FEET) {
    setAlert(
      "Map sizes over 5,000 feet will significantly increase build time.",
      "warning",
    );
    return;
  }
  if (outBuildings && outBuildings.checked) {
    setAlert(
      "Enabling buildings significantly increases build time. Building heights can be inaccurate in some areas.",
      "warning",
    );
    return;
  }
  setAlert("", false);
}

function parseBoolish(value) {
  if (typeof value === "boolean") return value;
  if (typeof value === "number") return value !== 0;
  if (typeof value === "string") {
    const normalized = value.trim().toLowerCase();
    return (
      normalized === "1" ||
      normalized === "true" ||
      normalized === "yes" ||
      normalized === "on"
    );
  }
  return false;
}

function parseJsonObject(raw) {
  if (!raw) return null;
  try {
    const parsed = JSON.parse(raw);
    if (parsed && typeof parsed === "object") {
      return parsed;
    }
  } catch (err) {
    return null;
  }
  return null;
}

function getCsrfToken() {
  const input = document.querySelector('input[name="csrf_token"]');
  return input ? input.value : "";
}

async function deleteRecentJob(deleteUrl, jobId, jobName) {
  if (!deleteUrl) return;
  const confirmed = await promptForDeleteJob(jobName || jobId || "");
  if (!confirmed) return;
  const previewToken = jobId ? `/jobs/${encodeURIComponent(jobId)}` : "";
  const deletingActivePreview =
    Boolean(previewToken) &&
    normalizePreviewPath(currentPreviewPath).includes(previewToken);
  const csrfToken = getCsrfToken();
  try {
    const resp = await fetch(deleteUrl, {
      method: "POST",
      headers: {
        "X-Requested-With": "fetch",
        "X-CSRF-Token": csrfToken,
      },
    });
    const payload = await resp.json().catch(() => ({}));
    if (!resp.ok) {
      const message =
        (payload && payload.error) || `Failed to delete job ${jobId || ""}.`;
      setAlert(message, true);
      return;
    }
    if (buildErrorMessage) {
      buildErrorMessage = "";
      updateAlerts();
    }
    await refreshRecentJobs();
    if (deletingActivePreview) {
      const nextPreviewPath = getActivePreviewPath(recentJobsData);
      if (nextPreviewPath) {
        const nextJob = getPreviewJobs().find(
          (job) => normalizePreviewPath(job.preview_url) === nextPreviewPath,
        );
        if (nextJob && nextJob.preview_url) {
          setInlinePreview(nextJob.preview_url);
        } else {
          setInlinePreview(nextPreviewPath);
        }
      } else {
        const frame = document.getElementById("inlinePreviewFrame");
        const demo = document.getElementById("inlinePreviewDemo");
        if (frame) {
          frame.onload = null;
          frame.classList.remove("loaded");
          frame.src = "about:blank";
        }
        if (demo) demo.classList.remove("hidden");
        currentPreviewPath = "";
        try {
          localStorage.removeItem(LAST_PREVIEW_KEY);
        } catch (e) {}
        syncPreviewToggleButtons();
        updatePreviewNavButtons();
      }
    }
  } catch (err) {
    setAlert("Failed to delete job.", true);
  }
}

async function cancelRecentJob(cancelUrl, jobId) {
  if (!cancelUrl) return;
  const confirmed = window.confirm(
    "Force cancel this build? Any partial outputs may be incomplete.",
  );
  if (!confirmed) return;
  const csrfToken = getCsrfToken();
  try {
    const resp = await fetch(cancelUrl, {
      method: "POST",
      headers: {
        "X-Requested-With": "fetch",
        "X-CSRF-Token": csrfToken,
      },
    });
    const payload = await resp.json().catch(() => ({}));
    if (!resp.ok) {
      const message =
        (payload && payload.error) || `Failed to cancel job ${jobId || ""}.`;
      setAlert(message, true);
      return;
    }
    if (buildErrorMessage) {
      buildErrorMessage = "";
      updateAlerts();
    }
    await refreshRecentJobs();
  } catch (err) {
    setAlert("Failed to cancel job.", true);
  }
}

async function renameRecentJob(renameUrl, jobId, currentName) {
  if (!renameUrl) return;
  const initialName = String(currentName || "").trim();
  const next = await promptForProjectName(initialName);
  if (next === null) return;
  const name = String(next || "").trim();
  if (!name) {
    setAlert("Project name is required.", true);
    return;
  }
  if (name.length > 120) {
    setAlert("Name must be 120 characters or fewer.", true);
    return;
  }
  const csrfToken = getCsrfToken();
  const formData = new FormData();
  formData.set("name", name);
  try {
    const resp = await fetch(renameUrl, {
      method: "POST",
      headers: {
        "X-Requested-With": "fetch",
        "X-CSRF-Token": csrfToken,
      },
      body: formData,
    });
    const payload = await resp.json().catch(() => ({}));
    if (!resp.ok) {
      const message =
        (payload && payload.error) || `Failed to rename job ${jobId || ""}.`;
      setAlert(message, true);
      return;
    }
    if (buildErrorMessage) {
      buildErrorMessage = "";
      updateAlerts();
    }
    const hiddenName = document.querySelector('input[name="job_name"]');
    if (
      hiddenName &&
      jobId &&
      normalizePreviewPath(currentPreviewPath).includes(
        `/jobs/${encodeURIComponent(jobId)}`,
      )
    ) {
      hiddenName.value = name;
    }
    await refreshRecentJobs();
  } catch (err) {
    setAlert("Failed to rename job.", true);
  }
}

function applyJobFormDefaults(formDefaults) {
  if (!formDefaults || typeof formDefaults !== "object") return;
  const setValue = (selector, value) => {
    if (value === undefined || value === null) return;
    const input = document.querySelector(selector);
    if (!input) return;
    input.value = String(value);
  };
  const setSelect = (selector, value) => {
    if (value === undefined || value === null) return;
    const select = document.querySelector(selector);
    if (!select) return;
    const asString = String(value);
    const hasOption = Array.from(select.options).some(
      (option) => option.value === asString,
    );
    if (hasOption) {
      select.value = asString;
    }
  };
  const setCheckbox = (id, value) => {
    if (value === undefined || value === null) return;
    const input = document.getElementById(id);
    if (!input) return;
    input.checked = parseBoolish(value);
  };

  const coordsInput = document.querySelector('input[name="coords"]');
  const hasCenter1 =
    formDefaults.center1 !== undefined && formDefaults.center1 !== null;
  const hasCenter2 =
    formDefaults.center2 !== undefined && formDefaults.center2 !== null;
  if (coordsInput && hasCenter1 && hasCenter2) {
    coordsInput.value = `${formDefaults.center1}, ${formDefaults.center2}`;
  }

  setValue('input[name="job_name"]', formDefaults.job_name);
  setValue('input[name="size"]', formDefaults.clip_size);
  setSelect('select[name="units"]', formDefaults.units);
  setValue('input[name="terrain_complexity"]', formDefaults.terrain_complexity);
  setValue('input[name="rotate_z"]', formDefaults.rotate_z);
  setValue("#contour_interval", formDefaults.contour_interval);
  setValue(
    'input[name="dxf_contour_spacing"]',
    formDefaults.dxf_contour_spacing,
  );
  setCheckbox("dxf_include_parcels", formDefaults.dxf_include_parcels);
  setCheckbox("dxf_include_buildings", formDefaults.dxf_include_buildings);
  setSelect("#xyz_mode", formDefaults.xyz_mode);
  setValue("#image_quality", formDefaults.image_quality);
  setCheckbox("output_terrain", formDefaults.output_terrain);
  setCheckbox("output_buildings", formDefaults.output_buildings);
  setCheckbox("output_contours", formDefaults.output_contours);
  setCheckbox("output_naip", formDefaults.output_naip);
  setCheckbox("output_xyz", formDefaults.output_xyz);

  buildErrorMessage = "";
  initSegmentedControls();
  initToggleButtons();
  updateUnitLabels();
  updateUiToggles();
  updateAlerts();
  scheduleCoverageCheck();
}

function setFormRecordMode(locked) {
  formRecordMode = Boolean(locked);
  const disable = (selector) => {
    document.querySelectorAll(selector).forEach((el) => {
      el.disabled = formRecordMode;
    });
  };
  disable(
    'input[name="coords"], input[name="size"], select[name="units"], input[name="terrain_complexity"], input[name="rotate_z"], input[name="dxf_contour_spacing"], #xyz_mode, #runBtn',
  );
  disable(
    "#output_terrain, #output_buildings, #output_contours, #output_naip, #output_xyz, #dxf_include_parcels, #dxf_include_buildings",
  );
  document
    .querySelectorAll(
      "button[data-input], .segmented[data-target] button[data-value]",
    )
    .forEach((btn) => {
      btn.disabled = formRecordMode;
    });
  const runBtn = document.getElementById("runBtn");
  if (runBtn) {
    runBtn.disabled = formRecordMode;
    runBtn.textContent = formRecordMode ? "Locked" : "Build";
    runBtn.classList.toggle("locked", formRecordMode);
  }
  const form = document.querySelector("form.card");
  if (form) {
    form.classList.toggle("record-mode", formRecordMode);
  }
  if (formRecordMode) {
    if (coverageTimer) {
      clearTimeout(coverageTimer);
      coverageTimer = null;
    }
    coverageStatus = null;
    coverageKey = null;
    coverageProvider = null;
    coverageError = "";
    setAlert("", false);
  }
}

function applyNewBuildDefaults() {
  setFormRecordMode(false);
  const coordsInput = document.querySelector('input[name="coords"]');
  if (coordsInput) coordsInput.value = "";
  const jobNameInput = document.querySelector('input[name="job_name"]');
  if (jobNameInput) jobNameInput.value = "";

  const setChecked = (id, value) => {
    const input = document.getElementById(id);
    if (input) input.checked = Boolean(value);
  };
  setChecked("output_contours", true);
  setChecked("output_xyz", true);
  setChecked("output_naip", true);
  setChecked("output_terrain", true);
  setChecked("output_buildings", false);
  setChecked("dxf_include_parcels", true);
  setChecked("dxf_include_buildings", true);

  const complexityInput = document.querySelector(
    'input[name="terrain_complexity"]',
  );
  if (complexityInput) complexityInput.value = "5";
  const northInput = document.querySelector('input[name="rotate_z"]');
  if (northInput) northInput.value = "0";
  const dxfSmoothingInput = document.querySelector(
    'input[name="dxf_contour_spacing"]',
  );
  if (dxfSmoothingInput) dxfSmoothingInput.value = "2";
  const contourIntervalInput = document.getElementById("contour_interval");
  if (contourIntervalInput) contourIntervalInput.value = "2";
  const xyzModeInput = document.getElementById("xyz_mode");
  if (xyzModeInput) xyzModeInput.value = "grid";
  const imageQualityInput = document.getElementById("image_quality");
  if (imageQualityInput) imageQualityInput.value = "standard";

  buildErrorMessage = "";
  initSegmentedControls();
  initToggleButtons();
  updateUnitLabels();
  updateUiToggles();
  updateAlerts();
  scheduleCoverageCheck();
}

function applyRecentJobPreview(previewUrl, formDefaults) {
  setFormRecordMode(true);
  if (previewUrl) {
    setInlinePreview(previewUrl);
  }
  applyJobFormDefaults(formDefaults);
  setFormRecordMode(true);
}

function initPreviewNavButtons() {
  const prevBtn = document.getElementById("previewPrevButton");
  const nextBtn = document.getElementById("previewNextButton");
  const downloadBtn = document.getElementById("previewDownloadButton");
  if (prevBtn) {
    prevBtn.addEventListener("click", () => navigatePreview(1));
  }
  if (nextBtn) {
    nextBtn.addEventListener("click", () => navigatePreview(-1));
  }
  if (downloadBtn) {
    downloadBtn.addEventListener("click", () => {
      const downloadUrl = downloadBtn.dataset.downloadUrl;
      if (!downloadUrl) return;
      window.location.href = downloadUrl;
    });
  }
  updatePreviewNavButtons();
}

function renderRecentJobs(container, jobs) {
  container.innerHTML = "";
  updateRecentJobsMeta(Array.isArray(jobs) ? jobs.length : 0);
  if (!jobs || jobs.length === 0) {
    const empty = document.createElement("p");
    empty.className = "footer";
    empty.textContent = "no jobs yet.";
    container.appendChild(empty);
    return;
  }
  const list = document.createElement("ul");
  list.className = "recent-job-list";
  const activePreviewPath = getActivePreviewPath(jobs);
  jobs.forEach((job) => {
    const item = document.createElement("li");
    item.className = "recent-job-row";
    const canAct =
      job.status === "done" ||
      job.status === "error" ||
      job.status === "canceled";
    const name = job.name || job.job_id;
    const displayName = job.display_name || name;

    const meta = document.createElement("div");
    meta.className = "recent-job-meta";
    let title;
    if (job.preview_url) {
      title = document.createElement("a");
      title.className = "recent-job-title recent-job-title-link";
      title.href = job.preview_url;
      title.dataset.previewInline = "1";
      title.dataset.previewUrl = job.preview_url;
      title.dataset.formDefaults = JSON.stringify(job.form_defaults || {});
    } else {
      title = document.createElement("div");
      title.className = "recent-job-title";
    }
    const titleText = document.createElement("span");
    titleText.textContent = displayName;
    title.appendChild(titleText);
    const isActive =
      Boolean(job.preview_url) &&
      normalizePreviewPath(job.preview_url) === activePreviewPath;
    if (isActive) {
      const activeTag = document.createElement("span");
      activeTag.className = "recent-job-active-tag";
      activeTag.textContent = "(active)";
      title.appendChild(activeTag);
    }
    meta.appendChild(title);
    if (!canAct && job.stage_label) {
      const stageWrap = document.createElement("div");
      stageWrap.className = "recent-job-stage-wrap";
      const stage = document.createElement("div");
      stage.className = "recent-job-stage";
      const progress = Number.isFinite(job.stage_progress)
        ? ` (${job.stage_progress}%)`
        : "";
      stage.textContent = `${job.stage_label}${progress}`;
      stageWrap.appendChild(stage);
      if (job.cancel_url) {
        const cancelBtn = document.createElement("button");
        cancelBtn.type = "button";
        cancelBtn.className = "recent-job-cancel-btn";
        cancelBtn.textContent = "cancel --force";
        cancelBtn.dataset.jobCancelUrl = job.cancel_url;
        cancelBtn.dataset.jobId = job.job_id;
        stageWrap.appendChild(cancelBtn);
      }
      meta.appendChild(stageWrap);
    }
    item.appendChild(meta);

    if (canAct) {
      const actions = document.createElement("div");
      actions.className = "recent-job-actions";
      let hasActions = false;
      if (job.download_all_url) {
        const downloadLink = document.createElement("a");
        downloadLink.className = "recent-job-pill recent-job-pill-download";
        downloadLink.href = job.download_all_url;
        downloadLink.setAttribute("aria-label", "Download job files");
        downloadLink.setAttribute("title", "Download job files");
        const icon = document.createElement("i");
        icon.setAttribute("data-lucide", "download");
        downloadLink.appendChild(icon);
        actions.appendChild(downloadLink);
        hasActions = true;
      }
      if (job.delete_url) {
        const deleteBtn = document.createElement("button");
        deleteBtn.type = "button";
        deleteBtn.className = "recent-job-pill recent-job-pill-delete";
        const icon = document.createElement("i");
        icon.setAttribute("data-lucide", "x");
        deleteBtn.appendChild(icon);
        deleteBtn.dataset.jobDeleteUrl = job.delete_url;
        deleteBtn.dataset.jobId = job.job_id;
        deleteBtn.dataset.jobName = displayName;
        deleteBtn.setAttribute("aria-label", "Delete job");
        deleteBtn.setAttribute("title", "Delete job");
        actions.appendChild(deleteBtn);
        hasActions = true;
      }
      if (job.rename_url) {
        const renameBtn = document.createElement("button");
        renameBtn.type = "button";
        renameBtn.className = "recent-job-pill recent-job-pill-edit";
        const icon = document.createElement("i");
        icon.setAttribute("data-lucide", "pencil");
        renameBtn.appendChild(icon);
        renameBtn.dataset.jobRenameUrl = job.rename_url;
        renameBtn.dataset.jobId = job.job_id;
        renameBtn.dataset.jobName = job.name || job.job_id;
        renameBtn.setAttribute("aria-label", "Edit job name");
        renameBtn.setAttribute("title", "Edit job name");
        actions.appendChild(renameBtn);
        hasActions = true;
      }
      if (hasActions) {
        meta.appendChild(actions);
      }
    }

    list.appendChild(item);
  });
  container.appendChild(list);
  if (window.lucide) {
    window.lucide.createIcons();
  }
  recentJobsData = jobs || [];
  updatePreviewNavButtons();
}

function rerenderRecentJobsIfMounted() {
  const container = document.getElementById("recentJobs");
  if (!container || !Array.isArray(recentJobsData)) return;
  renderRecentJobs(container, recentJobsData);
}

function openPreviewModal(url) {
  const modal = document.getElementById("previewModal");
  const frame = document.getElementById("previewModalFrame");
  if (!modal || !frame) return;
  let embedUrl = url;
  try {
    const parsed = new URL(url, window.location.origin);
    parsed.searchParams.set("embed", "1");
    embedUrl = `${parsed.pathname}${parsed.search}${parsed.hash}`;
  } catch (err) {
    const separator = url && url.includes("?") ? "&" : "?";
    embedUrl = `${url}${separator}embed=1`;
  }
  frame.src = embedUrl;
  modal.classList.remove("hidden");
  modal.setAttribute("aria-hidden", "false");
  _updateModalOpenClass();
}

function closePreviewModal() {
  const modal = document.getElementById("previewModal");
  const frame = document.getElementById("previewModalFrame");
  if (!modal || !frame) return;
  modal.classList.add("hidden");
  modal.setAttribute("aria-hidden", "true");
  frame.src = "about:blank";
  _updateModalOpenClass();
}

function closeProjectNameModal(value = null) {
  const modal = document.getElementById("projectNameModal");
  if (!modal) return;
  const resolver = projectNamePromptResolver;
  projectNamePromptResolver = null;
  modal.classList.add("hidden");
  modal.setAttribute("aria-hidden", "true");
  _updateModalOpenClass();
  if (resolver) resolver(value);
}

function closeDeleteJobModal(confirmed = false) {
  const modal = document.getElementById("deleteJobModal");
  if (!modal) return;
  const resolver = deleteJobPromptResolver;
  deleteJobPromptResolver = null;
  modal.classList.add("hidden");
  modal.setAttribute("aria-hidden", "true");
  _updateModalOpenClass();
  if (resolver) resolver(Boolean(confirmed));
}

function promptForProjectName(initialValue = "") {
  return new Promise((resolve) => {
    const modal = document.getElementById("projectNameModal");
    const input = document.getElementById("projectNameInput");
    if (!modal || !input) {
      const fallback = window.prompt(
        "Project name",
        String(initialValue || ""),
      );
      resolve(fallback === null ? null : String(fallback || ""));
      return;
    }
    if (projectNamePromptResolver) {
      closeProjectNameModal(null);
    }
    projectNamePromptResolver = resolve;
    input.value = String(initialValue || "");
    modal.classList.remove("hidden");
    modal.setAttribute("aria-hidden", "false");
    _updateModalOpenClass();
    setTimeout(() => {
      input.focus();
      input.select();
    }, 0);
  });
}

function promptForDeleteJob(jobName = "") {
  return new Promise((resolve) => {
    const modal = document.getElementById("deleteJobModal");
    const message = document.getElementById("deleteJobMessage");
    const label = String(jobName || "").trim();
    if (!modal || !message) {
      const fallback = window.confirm(
        label
          ? `Delete "${label}" permanently? This removes job files and history.`
          : "Delete this job permanently? This removes job files and history.",
      );
      resolve(Boolean(fallback));
      return;
    }
    if (deleteJobPromptResolver) {
      closeDeleteJobModal(false);
    }
    deleteJobPromptResolver = resolve;
    message.textContent = label
      ? `Delete "${label}" permanently? This removes job files and history.`
      : "Delete this job permanently? This removes job files and history.";
    modal.classList.remove("hidden");
    modal.setAttribute("aria-hidden", "false");
    _updateModalOpenClass();
    setTimeout(() => {
      const btn = document.getElementById("deleteJobConfirm");
      if (btn) btn.focus();
    }, 0);
  });
}

function initProjectNameModal() {
  const form = document.getElementById("projectNameForm");
  const input = document.getElementById("projectNameInput");
  const cancelBtn = document.getElementById("projectNameCancel");
  if (!form || !input) return;
  if (form.dataset.bound === "true") return;
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    closeProjectNameModal(String(input.value || "").trim());
  });
  if (cancelBtn) {
    cancelBtn.addEventListener("click", (event) => {
      event.preventDefault();
      closeProjectNameModal(null);
    });
  }
  form.dataset.bound = "true";
}

function initDeleteJobModal() {
  const form = document.getElementById("deleteJobForm");
  const cancelBtn = document.getElementById("deleteJobCancel");
  if (!form) return;
  if (form.dataset.bound === "true") return;
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    closeDeleteJobModal(true);
  });
  if (cancelBtn) {
    cancelBtn.addEventListener("click", (event) => {
      event.preventDefault();
      closeDeleteJobModal(false);
    });
  }
  form.dataset.bound = "true";
}

function initPreviewModal() {
  document.addEventListener("click", (event) => {
    const deleteButton = event.target.closest("button[data-job-delete-url]");
    if (deleteButton) {
      event.preventDefault();
      deleteRecentJob(
        deleteButton.dataset.jobDeleteUrl,
        deleteButton.dataset.jobId,
        deleteButton.dataset.jobName,
      );
      return;
    }
    const renameButton = event.target.closest("button[data-job-rename-url]");
    if (renameButton) {
      event.preventDefault();
      renameRecentJob(
        renameButton.dataset.jobRenameUrl,
        renameButton.dataset.jobId,
        renameButton.dataset.jobName,
      );
      return;
    }
    const cancelButton = event.target.closest("button[data-job-cancel-url]");
    if (cancelButton) {
      event.preventDefault();
      cancelRecentJob(
        cancelButton.dataset.jobCancelUrl,
        cancelButton.dataset.jobId,
      );
      return;
    }
    const previewInlineLink = event.target.closest(
      'a[data-preview-inline="1"]',
    );
    if (previewInlineLink) {
      event.preventDefault();
      const url =
        previewInlineLink.dataset.previewUrl || previewInlineLink.href;
      const formDefaults = parseJsonObject(
        previewInlineLink.dataset.formDefaults,
      );
      applyRecentJobPreview(url, formDefaults);
      return;
    }
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
      return;
    }
    const projectNameCloseTarget = event.target.closest(
      '[data-project-name-close="1"]',
    );
    if (projectNameCloseTarget) {
      event.preventDefault();
      closeProjectNameModal(null);
      return;
    }
    const deleteJobCloseTarget = event.target.closest(
      '[data-delete-job-close="1"]',
    );
    if (deleteJobCloseTarget) {
      event.preventDefault();
      closeDeleteJobModal(false);
    }
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closePreviewModal();
      closeProjectNameModal(null);
      closeDeleteJobModal(false);
    }
  });
}

function _updateModalOpenClass() {
  const previewModal = document.getElementById("previewModal");
  const projectNameModal = document.getElementById("projectNameModal");
  const deleteJobModal = document.getElementById("deleteJobModal");
  const previewOpen =
    previewModal && !previewModal.classList.contains("hidden");
  const projectNameOpen =
    projectNameModal && !projectNameModal.classList.contains("hidden");
  const deleteJobOpen =
    deleteJobModal && !deleteJobModal.classList.contains("hidden");
  document.body.classList.toggle(
    "modal-open",
    Boolean(previewOpen || projectNameOpen || deleteJobOpen),
  );
}

function _buildAuthLoginUrl(nextPath) {
  const normalizedNext =
    typeof nextPath === "string" && nextPath.startsWith("/") ? nextPath : "/";
  try {
    const parsed = new URL(AUTH_LOGIN_URL, window.location.origin);
    parsed.searchParams.set("next", normalizedNext);
    return `${parsed.pathname}${parsed.search}${parsed.hash}`;
  } catch (err) {
    const separator = AUTH_LOGIN_URL.includes("?") ? "&" : "?";
    return `${AUTH_LOGIN_URL}${separator}next=${encodeURIComponent(normalizedNext)}`;
  }
}

function openAuthModal(nextPath = "/") {
  if (!AUTH_ENABLED) return;
  const normalizedNext =
    typeof nextPath === "string" && nextPath.startsWith("/") ? nextPath : "/";
  // Route all interactive sign-in flows through /auth/login. The dedicated page
  // mounts Clerk SignIn and reliably completes /auth/clerk/exchange.
  window.location.href = _buildAuthLoginUrl(normalizedNext);
}

function initAuthModal() {
  document.addEventListener("click", (event) => {
    const openTarget = event.target.closest('[data-auth-open="1"]');
    if (openTarget) {
      if (AUTH_ENABLED) {
        event.preventDefault();
        const nextPath = `${window.location.pathname || "/"}${window.location.search || ""}`;
        openAuthModal(nextPath);
      }
    }
  });
}

async function refreshRecentJobs(options = {}) {
  if (!CAN_BUILD) return;
  const container = document.getElementById("recentJobs");
  if (!container) return;
  const waitSeconds = Number.isFinite(options.waitSeconds)
    ? Math.max(0, options.waitSeconds)
    : 0;
  const hasSince = Number.isFinite(options.sinceVersion);
  const params = new URLSearchParams();
  if (waitSeconds > 0) {
    params.set("wait", String(waitSeconds));
  }
  if (hasSince) {
    params.set("since", String(Math.max(0, options.sinceVersion)));
  }
  const path = params.toString()
    ? `/recent-jobs?${params.toString()}`
    : "/recent-jobs";
  try {
    const resp = await fetch(path, { cache: "no-store" });
    if (!resp.ok) {
      if (resp.status === 401 || resp.status === 403) {
        return { ok: false, stop: true };
      }
      return { ok: false, stop: false };
    }
    const data = await resp.json();
    renderRecentJobs(container, data.jobs || []);
    recentJobsData = data.jobs || [];
    updatePreviewNavButtons();
    if (typeof data.version === "number") {
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
  const unitValue = unitsInput ? unitsInput.value : "feet";
  const label = unitValue === "meters" ? "meters" : "feet";
  document.querySelectorAll("[data-unit-label]").forEach((el) => {
    el.textContent = label;
  });
}

function initSegmentedControls() {
  document.querySelectorAll(".segmented[data-target]").forEach((segmented) => {
    const inputId = segmented.dataset.target;
    const input = document.getElementById(inputId);
    const buttons = Array.from(
      segmented.querySelectorAll("button[data-value]"),
    );
    if (!input || buttons.length === 0) return;
    const bound = segmented.dataset.bound === "true";
    const values = buttons.map((btn) => btn.dataset.value);
    let current = input.value;
    if (!values.includes(current)) {
      if (inputId === "contour_interval") {
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
        btn.classList.toggle("active", btn.dataset.value === value);
      });
    };
    setActive(current);
    if (!bound) {
      buttons.forEach((btn) => {
        btn.addEventListener("click", () => setActive(btn.dataset.value));
      });
      segmented.dataset.bound = "true";
    }
  });
}

function syncToggleButtons() {
  document.querySelectorAll("button[data-input]").forEach((btn) => {
    const input = document.getElementById(btn.dataset.input);
    if (!input) return;
    btn.classList.toggle("active", input.checked);
    btn.setAttribute("aria-pressed", input.checked ? "true" : "false");
    btn.disabled = input.disabled;
  });
}

function initToggleButtons() {
  document.querySelectorAll("button[data-input]").forEach((btn) => {
    if (btn.dataset.bound === "true") return;
    const input = document.getElementById(btn.dataset.input);
    if (!input) return;
    btn.addEventListener("click", () => {
      if (btn.disabled) return;
      input.checked = !input.checked;
      input.dispatchEvent(new Event("change", { bubbles: true }));
      syncToggleButtons();
    });
    btn.dataset.bound = "true";
  });
  syncToggleButtons();
}

function setSectionLocked(sectionId, locked) {
  const section = document.getElementById(sectionId);
  if (!section) return;
  section.classList.toggle("locked", locked);
}

function updateUiToggles() {
  const contours = document.getElementById("output_contours");
  const outTerrain = document.getElementById("output_terrain");
  const outBuildings = document.getElementById("output_buildings");
  const outImage = document.getElementById("output_naip");
  const outXyz = document.getElementById("output_xyz");
  const xyzMode = document.getElementById("xyz_mode");
  const dxfParcels = document.getElementById("dxf_include_parcels");
  const dxfBuildings = document.getElementById("dxf_include_buildings");

  const contoursActive = contours && contours.checked;
  const xyzActive = outXyz && outXyz.checked;
  const terrainActive = outTerrain && outTerrain.checked;
  const buildingsActive = outBuildings && outBuildings.checked;
  const rotationActive =
    terrainActive || buildingsActive || contoursActive || xyzActive;
  const projectZeroActive = rotationActive;
  const xyzModeIsContours = xyzMode && xyzMode.value === "contours";
  const showContourControls =
    contoursActive || (xyzActive && xyzModeIsContours);

  setSectionLocked("meshResolutionSection", false);
  setSectionLocked("buildingHeightsSection", !buildingsActive);
  setSectionLocked("contourIntervalSection", !showContourControls);
  setSectionLocked("contourLayersSection", !contoursActive);
  setSectionLocked("contourSmoothingSection", !contoursActive);
  setSectionLocked("xyzSamplingSection", !xyzActive);
  setSectionLocked("imageQualitySection", !(outImage && outImage.checked));
  setSectionLocked("rotationSection", !rotationActive);
  setSectionLocked("projectZeroSection", !projectZeroActive);

  if (dxfParcels) dxfParcels.disabled = !contoursActive;
  if (dxfBuildings) dxfBuildings.disabled = !contoursActive;
  const parcelsBtn = document.querySelector(
    'button[data-input="dxf_include_parcels"]',
  );
  const buildingsBtn = document.querySelector(
    'button[data-input="dxf_include_buildings"]',
  );
  if (parcelsBtn) parcelsBtn.disabled = !contoursActive;
  if (buildingsBtn) buildingsBtn.disabled = !contoursActive;

  const dxfRange = document.getElementById("dxfSpacingRange");
  const dxfValue = document.getElementById("dxfSpacingValue");
  if (dxfRange && dxfValue) {
    dxfRange.disabled = !contoursActive;
    dxfValue.textContent = dxfRange.value;
  }
  const complexityInput = document.querySelector(
    'input[name="terrain_complexity"]',
  );
  const complexityValue = document.getElementById("complexityValue");
  if (complexityInput && complexityValue) {
    complexityValue.textContent = complexityInput.value;
  }

  updateAlerts();
  syncToggleButtons();
}

async function runBuild(event) {
  event.preventDefault();
  if (formRecordMode) return;
  const form = event.target;
  const runBtn = document.getElementById("runBtn");
  if (!form || !runBtn) return;
  if (!CAN_BUILD) {
    const nextPath = `${window.location.pathname || "/"}${window.location.search || ""}`;
    openAuthModal(nextPath);
    return;
  }

  const jobNameInput = form.querySelector('input[name="job_name"]');
  if (jobNameInput) {
    const current = String(jobNameInput.value || "").trim();
    let nextName = current;
    if (!nextName) {
      const prompted = await promptForProjectName(current);
      if (prompted === null) return;
      nextName = String(prompted || "").trim();
    }
    if (!nextName) {
      setAlert("Project name is required.", true);
      return;
    }
    if (nextName.length > 120) {
      setAlert("Name must be 120 characters or fewer.", true);
      return;
    }
    jobNameInput.value = nextName;
  }

  buildErrorMessage = "";
  updateAlerts();
  runBtn.disabled = true;
  const originalText = runBtn.textContent;
  runBtn.textContent = "Building...";
  setInlineBuildStatus("Building...");
  setInlineBuildingOverlay(true);

  const formData = new FormData(form);
  let resp;
  try {
    resp = await fetch(form.action, {
      method: "POST",
      body: formData,
      headers: { "X-Requested-With": "fetch" },
    });
  } catch (err) {
    buildErrorMessage =
      "Build failed to start. Please check your inputs and try again.";
    updateAlerts();
    runBtn.disabled = formRecordMode;
    runBtn.textContent = originalText;
    setInlineBuildStatus("Build failed to start.");
    setInlineBuildingOverlay(false);
    return;
  }
  if (!resp.ok) {
    if (resp.status === 401 && AUTH_ENABLED) {
      const nextPath = `${window.location.pathname || "/"}${window.location.search || ""}`;
      openAuthModal(nextPath);
      runBtn.disabled = formRecordMode;
      runBtn.textContent = originalText;
      setInlineBuildStatus("Sign in required.");
      setInlineBuildingOverlay(false);
      return;
    }
    try {
      const payload = await resp.json();
      buildErrorMessage =
        payload.error ||
        "Build failed to start. Please check your inputs and try again.";
    } catch (err) {
      buildErrorMessage =
        "Build failed to start. Please check your inputs and try again.";
    }
    updateAlerts();
    runBtn.disabled = formRecordMode;
    runBtn.textContent = originalText;
    setInlineBuildStatus("Build failed to start.");
    setInlineBuildingOverlay(false);
    return;
  }
  const data = await resp.json();

  let offset = 0;
  let buildSucceeded = false;
  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  while (true) {
    try {
      const logResp = await fetch(
        `/logs/${data.job_id}?offset=${offset}&wait=25`,
        {
          cache: "no-store",
        },
      );
      if (!logResp.ok) {
        if (
          logResp.status === 401 ||
          logResp.status === 403 ||
          logResp.status === 404
        ) {
          buildErrorMessage =
            "Build status is no longer available. Please refresh and try again.";
          updateAlerts();
          break;
        }
        await sleep(1500);
        continue;
      }
      const logData = await logResp.json();
      if (typeof logData.offset === "number") {
        offset = logData.offset;
      }
      if (logData.stage_label) {
        const progress = Number.isFinite(logData.stage_progress)
          ? ` (${logData.stage_progress}%)`
          : "";
        setInlineBuildStatus(`${logData.stage_label}${progress}`);
      } else if (logData.status === "queued") {
        setInlineBuildStatus("Queued...");
      } else if (logData.status === "running") {
        setInlineBuildStatus("Running...");
      }
      if (logData.status === "running" || logData.status === "queued") {
        continue;
      }
      if (logData.status === "error") {
        const reason = logData.error ? ` ${logData.error}` : "";
        buildErrorMessage = `Build failed.${reason}`;
        setInlineBuildStatus("Build failed.");
        updateAlerts();
      } else if (logData.status === "canceled") {
        buildErrorMessage = "Build canceled.";
        setInlineBuildStatus("Build canceled.");
        updateAlerts();
      } else if (logData.status === "done") {
        setInlineBuildStatus("Build complete.");
        buildSucceeded = true;
      }
      break;
    } catch (err) {
      await sleep(1500);
    }
  }
  setInlineBuildingOverlay(false);
  if (buildSucceeded && data && data.job_id) {
    const jobPreviewUrl = `/jobs/${encodeURIComponent(data.job_id)}?tab=preview`;
    setInlinePreview(jobPreviewUrl);
  }
  await refreshRecentJobs();
  runBtn.disabled = formRecordMode;
  runBtn.textContent = originalText;
}

// ---- Inline preview panel ----

function _makeEmbedUrl(url) {
  try {
    const parsed = new URL(url, window.location.origin);
    parsed.searchParams.set("embed", "1");
    return `${parsed.pathname}${parsed.search}${parsed.hash}`;
  } catch (err) {
    const sep = url && url.includes("?") ? "&" : "?";
    return `${url}${sep}embed=1`;
  }
}

function _setWireframeToggleState(enabled, active) {
  const btn = document.getElementById("wireframeToggle");
  if (!btn) return;
  btn.disabled = !enabled;
  btn.classList.toggle("is-active", Boolean(active));
  btn.setAttribute("aria-pressed", active ? "true" : "false");
}

function _setBuildingsToggleState(enabled, active) {
  const btn = document.getElementById("buildingsToggle");
  if (!btn) return;
  btn.disabled = !enabled;
  btn.classList.toggle("is-active", Boolean(active));
  btn.setAttribute("aria-pressed", active ? "true" : "false");
}

function _getInlinePreviewWindow() {
  const frame = document.getElementById("inlinePreviewFrame");
  if (!frame || !frame.contentWindow) return null;
  return frame.contentWindow;
}

function syncWireframeToggleFromInlinePreview() {
  const frame = document.getElementById("inlinePreviewFrame");
  if (!frame || !frame.src || frame.src === "about:blank") {
    _setWireframeToggleState(false, false);
    return;
  }
  const frameWin = _getInlinePreviewWindow();
  if (!frameWin) {
    _setWireframeToggleState(false, false);
    return;
  }
  try {
    const enabled = typeof frameWin.toggleWireframe === "function";
    const innerBtn = frameWin.document.getElementById("preview-wireframe-btn");
    const active = Boolean(
      innerBtn && innerBtn.classList.contains("is-active"),
    );
    _setWireframeToggleState(enabled, active);
  } catch (err) {
    _setWireframeToggleState(false, false);
  }
}

function syncBuildingsToggleFromInlinePreview() {
  const frame = document.getElementById("inlinePreviewFrame");
  if (!frame || !frame.src || frame.src === "about:blank") {
    _setBuildingsToggleState(false, false);
    return;
  }
  const frameWin = _getInlinePreviewWindow();
  if (!frameWin) {
    _setBuildingsToggleState(false, false);
    return;
  }
  try {
    const hasToggleFn =
      typeof frameWin.toggleBuildingsVisibility === "function";
    const enabled =
      hasToggleFn &&
      typeof frameWin.buildingsToggleAvailable === "function" &&
      Boolean(frameWin.buildingsToggleAvailable());
    let active = false;
    if (enabled && typeof frameWin.buildingsVisible === "function") {
      // Purple means buildings are enabled/visible.
      active = frameWin.buildingsVisible() !== false;
    }
    _setBuildingsToggleState(enabled, active);
  } catch (err) {
    _setBuildingsToggleState(false, false);
  }
}

function syncPreviewToggleButtons() {
  syncWireframeToggleFromInlinePreview();
  syncBuildingsToggleFromInlinePreview();
}
window.syncPreviewToggleButtons = syncPreviewToggleButtons;

function initWireframeToggle() {
  const btn = document.getElementById("wireframeToggle");
  if (!btn) return;
  _setWireframeToggleState(false, false);
  btn.addEventListener("click", () => {
    const frameWin = _getInlinePreviewWindow();
    if (!frameWin || typeof frameWin.toggleWireframe !== "function") return;
    try {
      frameWin.toggleWireframe();
    } catch (err) {
      return;
    }
    syncPreviewToggleButtons();
  });
}

function initBuildingsToggle() {
  const btn = document.getElementById("buildingsToggle");
  if (!btn) return;
  _setBuildingsToggleState(false, false);
  btn.addEventListener("click", () => {
    const frameWin = _getInlinePreviewWindow();
    if (!frameWin || typeof frameWin.toggleBuildingsVisibility !== "function") {
      return;
    }
    try {
      frameWin.toggleBuildingsVisibility();
    } catch (err) {
      return;
    }
    syncPreviewToggleButtons();
  });
}

function setInlinePreview(previewUrl) {
  const frame = document.getElementById("inlinePreviewFrame");
  const demo = document.getElementById("inlinePreviewDemo");
  if (!frame) return;
  const embedUrl = _makeEmbedUrl(previewUrl);
  currentPreviewPath = normalizePreviewPath(previewUrl);
  let nextHref = embedUrl;
  let currentHref = frame.src || "";
  try {
    nextHref = new URL(embedUrl, window.location.origin).href;
  } catch (err) {}
  try {
    currentHref = new URL(currentHref, window.location.origin).href;
  } catch (err) {}
  if (currentHref === nextHref) {
    if (demo) demo.classList.add("hidden");
    syncPreviewToggleButtons();
    updatePreviewNavButtons();
    rerenderRecentJobsIfMounted();
    return;
  }
  _setWireframeToggleState(false, false);
  _setBuildingsToggleState(false, false);
  frame.classList.remove("loaded");
  frame.onload = () => {
    if (frame.src && frame.src !== "about:blank") {
      frame.classList.add("loaded");
    }
    syncPreviewToggleButtons();
  };
  frame.src = embedUrl;
  if (demo) demo.classList.add("hidden");
  try {
    localStorage.setItem(LAST_PREVIEW_KEY, previewUrl);
  } catch (e) {}
  updatePreviewNavButtons();
  rerenderRecentJobsIfMounted();
}

function setInlineBuildingOverlay(active) {
  const overlay = document.getElementById("inlinePreviewBuilding");
  if (!overlay) return;
  overlay.classList.toggle("active", active);
  overlay.setAttribute("aria-hidden", active ? "false" : "true");
  if (!active) {
    setInlineBuildStatus("Building...");
  }
}

function setInlineBuildStatus(message) {
  const statusEl = document.getElementById("inlinePreviewBuildStatus");
  if (!statusEl) return;
  statusEl.textContent = String(message || "Building...");
}

function findRecentJobFormDefaultsByPreviewUrl(previewUrl) {
  if (!previewUrl) return null;
  const targetPath = normalizePreviewPath(previewUrl);
  const links = document.querySelectorAll('a[data-preview-inline="1"]');
  for (const link of links) {
    const linkUrl = link.dataset.previewUrl || link.getAttribute("href") || "";
    if (!linkUrl) continue;
    if (normalizePreviewPath(linkUrl) !== targetPath) continue;
    return parseJsonObject(link.dataset.formDefaults);
  }
  return null;
}

function initInlinePreview() {
  const frame = document.getElementById("inlinePreviewFrame");
  if (!frame) return;
  // Prefer server-injected URL (most recent job from this session), then localStorage
  const serverUrl = window.APP_CONFIG && window.APP_CONFIG.initialPreviewUrl;
  const savedUrl = localStorage.getItem(LAST_PREVIEW_KEY);
  const previewUrl = serverUrl || savedUrl;
  if (previewUrl) {
    const formDefaults = findRecentJobFormDefaultsByPreviewUrl(previewUrl);
    if (formDefaults) {
      applyRecentJobPreview(previewUrl, formDefaults);
      return;
    }
    setInlinePreview(previewUrl);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  initPreviewModal();
  initProjectNameModal();
  initDeleteJobModal();
  initAuthModal();
  const newJobButton = document.getElementById("newJobButton");
  if (newJobButton) {
    newJobButton.addEventListener("click", (event) => {
      event.preventDefault();
      applyNewBuildDefaults();
    });
  }
  const jobsPanel = document.getElementById("recentJobsPanel");
  const jobsButton = document.getElementById("menuButton");
  if (jobsPanel && jobsButton) {
    const setJobsPanelOpenState = (open) => {
      document.body.classList.toggle("jobs-panel-open", Boolean(open));
    };
    const closeJobsPanel = () => {
      jobsPanel.classList.add("hidden");
      jobsButton.setAttribute("aria-expanded", "false");
      setJobsPanelOpenState(false);
    };
    const openJobsPanel = () => {
      jobsPanel.classList.remove("hidden");
      jobsButton.setAttribute("aria-expanded", "true");
      setJobsPanelOpenState(true);
    };
    jobsButton.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      const willOpen = jobsPanel.classList.contains("hidden");
      if (willOpen) {
        openJobsPanel();
      } else {
        closeJobsPanel();
      }
    });
    document.addEventListener("click", (event) => {
      const target = event.target;
      if (
        target &&
        typeof target.closest === "function" &&
        target.closest("#deleteJobModal, #projectNameModal, #previewModal")
      ) {
        return;
      }
      if (!jobsPanel.contains(target) && !jobsButton.contains(target)) {
        closeJobsPanel();
      }
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeJobsPanel();
      }
    });
    const previewFrames = [
      document.getElementById("inlinePreviewFrame"),
      document.getElementById("previewModalFrame"),
    ].filter(Boolean);
    window.addEventListener("blur", () => {
      const active = document.activeElement;
      if (active && previewFrames.includes(active)) {
        closeJobsPanel();
      }
    });
    previewFrames.forEach((frame) => {
      frame.addEventListener("load", () => {
        try {
          const frameDoc = frame.contentWindow && frame.contentWindow.document;
          if (!frameDoc || frame.dataset.jobsCloseBound === "true") return;
          frameDoc.addEventListener("pointerdown", () => {
            closeJobsPanel();
          });
          frame.dataset.jobsCloseBound = "true";
        } catch (err) {
          // Ignore cross-document access failures.
        }
      });
    });
    setJobsPanelOpenState(false);
  }
  const topProfileShell = document.getElementById("topProfileShell");
  const topProfileButton = document.getElementById("topProfileButton");
  const topProfileDropdown = document.getElementById("topProfileDropdown");
  if (topProfileShell && topProfileButton && topProfileDropdown) {
    const closeTopProfileMenu = () => {
      topProfileDropdown.classList.add("hidden");
      topProfileButton.setAttribute("aria-expanded", "false");
    };
    topProfileButton.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      const willOpen = topProfileDropdown.classList.contains("hidden");
      if (willOpen) {
        topProfileDropdown.classList.remove("hidden");
        topProfileButton.setAttribute("aria-expanded", "true");
      } else {
        closeTopProfileMenu();
      }
    });
    document.addEventListener("click", (event) => {
      if (!topProfileShell.contains(event.target)) {
        closeTopProfileMenu();
      }
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeTopProfileMenu();
      }
    });
  }

  initSegmentedControls();
  initToggleButtons();
  updateUnitLabels();
  updateUiToggles();
  if (window.lucide) {
    lucide.createIcons();
  }
  const contours = document.getElementById("output_contours");
  const outTerrain = document.getElementById("output_terrain");
  const outBuildings = document.getElementById("output_buildings");
  const outImage = document.getElementById("output_naip");
  const outXyz = document.getElementById("output_xyz");
  const xyzMode = document.getElementById("xyz_mode");
  const dxfParcels = document.getElementById("dxf_include_parcels");
  const coords = document.querySelector('input[name="coords"]');
  const mapSizeInput = document.querySelector('input[name="size"]');
  const units = document.querySelector('select[name="units"]');
  if (contours) contours.addEventListener("change", updateUiToggles);
  if (dxfParcels) dxfParcels.addEventListener("change", updateAlerts);
  if (outTerrain) outTerrain.addEventListener("change", updateUiToggles);
  if (outBuildings) outBuildings.addEventListener("change", updateUiToggles);
  if (outImage) outImage.addEventListener("change", updateUiToggles);
  if (outXyz) outXyz.addEventListener("change", updateUiToggles);
  if (xyzMode) xyzMode.addEventListener("change", updateUiToggles);
  if (coords)
    coords.addEventListener("input", () => {
      updateAlerts();
      scheduleCoverageCheck();
    });
  if (mapSizeInput)
    mapSizeInput.addEventListener("input", () => {
      updateAlerts();
      scheduleCoverageCheck();
    });
  if (units)
    units.addEventListener("change", () => {
      updateUnitLabels();
      updateAlerts();
      scheduleCoverageCheck();
    });
  const form = document.querySelector("form.card");
  if (form) {
    form.addEventListener("submit", runBuild);
    form.addEventListener("reset", () => {
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
  initWireframeToggle();
  initBuildingsToggle();
  initPreviewNavButtons();
  initInlinePreview();
  scheduleCoverageCheck();
});
