const VA_BOUNDS = { latMin: 36.5, latMax: 39.5, lonMin: -83.0, lonMax: -75.0 };
const CONUS_BOUNDS = {
  latMin: 24.5,
  latMax: 49.5,
  lonMin: -125.0,
  lonMax: -66.5,
};
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
const CLERK_PUBLISHABLE_KEY =
  (window.APP_CONFIG && window.APP_CONFIG.clerkPublishableKey) || "";
const CLERK_FRONTEND_API_URL =
  (window.APP_CONFIG && window.APP_CONFIG.clerkFrontendApiUrl) || "";
const LAST_PREVIEW_KEY = "terrain-last-preview-url";
let buildErrorMessage = "";
let coverageStatus = null;
let coverageKey = null;
let coverageTimer = null;
let coverageRequestId = 0;
let recentJobsVersion = 0;
let clerkReadyPromise = null;
let clerkListenerAttached = false;
let authExchangeInFlight = false;
let clerkDarkThemePromise = null;

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
    const resp = await fetch(`/coverage?lon=${coords.lon}&lat=${coords.lat}`, {
      cache: "no-store",
    });
    if (!resp.ok) throw new Error("coverage failed");
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
  const alertEl = document.getElementById("parcelAlert");
  if (!alertEl) return;
  if (!message) {
    alertEl.classList.add("hidden");
    alertEl.classList.remove("error");
    alertEl.textContent = "";
    return;
  }
  alertEl.textContent = message;
  alertEl.classList.remove("hidden");
  if (isError) {
    alertEl.classList.add("error");
  } else {
    alertEl.classList.remove("error");
  }
}

function updateAlerts() {
  const parcels = document.getElementById("dxf_include_parcels");
  const contours = document.getElementById("output_contours");
  const coordsInput = document.querySelector('input[name="coords"]');
  const coords = coordsInput ? parseCoords(coordsInput.value) : null;
  if (coordsInput && coordsInput.value.trim() && !coords) {
    setAlert('Coordinates are invalid. Use "lat, lon".', true);
    return;
  }
  if (coords && !isInConus(coords.lon, coords.lat)) {
    setAlert(
      "Coordinates are outside the supported area (contiguous US).",
      true,
    );
    return;
  }
  if (
    coverageStatus === false &&
    coords &&
    coverageKey === coverageKeyFor(coords.lon, coords.lat)
  ) {
    setAlert(
      "Coordinates are outside the supported area (contiguous US).",
      true,
    );
    return;
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

async function deleteRecentJob(deleteUrl, jobId) {
  if (!deleteUrl) return;
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
  } catch (err) {
    setAlert("Failed to delete job.", true);
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

function applyRecentJobPreview(previewUrl, formDefaults) {
  if (previewUrl) {
    setInlinePreview(previewUrl);
  }
  applyJobFormDefaults(formDefaults);
}

function renderRecentJobs(container, jobs) {
  container.innerHTML = "";
  if (!jobs || jobs.length === 0) {
    const empty = document.createElement("p");
    empty.className = "footer";
    empty.textContent = "No jobs yet.";
    container.appendChild(empty);
    return;
  }
  const list = document.createElement("ul");
  list.className = "recent-job-list";
  jobs.forEach((job) => {
    const item = document.createElement("li");
    item.className = "recent-job-row";
    const canAct = job.status === "done" || job.status === "error";
    const name = job.name || job.job_id;

    const meta = document.createElement("div");
    meta.className = "recent-job-meta";
    const title = document.createElement("div");
    title.className = "recent-job-title";
    title.textContent = name;
    meta.appendChild(title);
    if (!canAct && job.stage_label) {
      const stage = document.createElement("div");
      stage.className = "recent-job-stage";
      const progress = Number.isFinite(job.stage_progress)
        ? ` (${job.stage_progress}%)`
        : "";
      stage.textContent = `${job.stage_label}${progress}`;
      meta.appendChild(stage);
    }
    item.appendChild(meta);

    if (canAct) {
      const actions = document.createElement("div");
      actions.className = "recent-job-actions";
      if (job.preview_url) {
        const previewLink = document.createElement("a");
        previewLink.className = "recent-job-pill";
        previewLink.href = job.preview_url;
        previewLink.textContent = "Preview";
        previewLink.dataset.previewInline = "1";
        previewLink.dataset.previewUrl = job.preview_url;
        previewLink.dataset.formDefaults = JSON.stringify(
          job.form_defaults || {},
        );
        actions.appendChild(previewLink);
      }
      if (job.download_all_url) {
        const downloadLink = document.createElement("a");
        downloadLink.className = "recent-job-pill";
        downloadLink.href = job.download_all_url;
        downloadLink.setAttribute("aria-label", "Download job files");
        downloadLink.setAttribute("title", "Download job files");
        const icon = document.createElement("i");
        icon.setAttribute("data-lucide", "download");
        downloadLink.appendChild(icon);
        actions.appendChild(downloadLink);
      }
      if (job.delete_url) {
        const deleteBtn = document.createElement("button");
        deleteBtn.type = "button";
        deleteBtn.className = "recent-job-pill recent-job-pill-delete";
        const icon = document.createElement("i");
        icon.setAttribute("data-lucide", "trash-2");
        deleteBtn.appendChild(icon);
        deleteBtn.dataset.jobDeleteUrl = job.delete_url;
        deleteBtn.dataset.jobId = job.job_id;
        deleteBtn.setAttribute("aria-label", "Delete job");
        deleteBtn.setAttribute("title", "Delete job");
        actions.appendChild(deleteBtn);
      }
      item.appendChild(actions);
    }

    list.appendChild(item);
  });
  container.appendChild(list);
  if (window.lucide) {
    window.lucide.createIcons();
  }
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

function initPreviewModal() {
  document.addEventListener("click", (event) => {
    const deleteButton = event.target.closest("button[data-job-delete-url]");
    if (deleteButton) {
      event.preventDefault();
      deleteRecentJob(
        deleteButton.dataset.jobDeleteUrl,
        deleteButton.dataset.jobId,
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
      const profileButton = document.getElementById("menuButton");
      const profileDropdown = document.getElementById("menuDropdown");
      if (profileDropdown) {
        profileDropdown.classList.add("hidden");
      }
      if (profileButton) {
        profileButton.setAttribute("aria-expanded", "false");
      }
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
    }
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closePreviewModal();
  });
}

function _updateModalOpenClass() {
  const previewModal = document.getElementById("previewModal");
  const previewOpen =
    previewModal && !previewModal.classList.contains("hidden");
  document.body.classList.toggle("modal-open", Boolean(previewOpen));
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

function normalizeFrontendApiUrl(value) {
  const raw = String(value || "").trim();
  if (!raw) return "";
  if (raw.startsWith("http://") || raw.startsWith("https://")) {
    return raw.replace(/\/+$/, "");
  }
  return `https://${raw.replace(/\/+$/, "")}`;
}

function frontendApiFromPublishableKey(key) {
  const raw = String(key || "").trim();
  const firstUnderscore = raw.indexOf("_", raw.indexOf("_") + 1);
  if (firstUnderscore < 0) return "";
  const encoded = raw.slice(firstUnderscore + 1);
  if (!encoded) return "";
  let base64 = encoded.replace(/-/g, "+").replace(/_/g, "/");
  while (base64.length % 4 !== 0) base64 += "=";
  try {
    const decoded = atob(base64);
    const hostOrUrl = decoded.split("$")[0].trim();
    return normalizeFrontendApiUrl(hostOrUrl);
  } catch (err) {
    return "";
  }
}

function loadClerkGlobal() {
  return new Promise((resolve, reject) => {
    if (window.__terrainClerkGlobal) {
      resolve(window.__terrainClerkGlobal);
      return;
    }
    if (window.Clerk) {
      window.__terrainClerkGlobal = window.Clerk;
      resolve(window.__terrainClerkGlobal);
      return;
    }
    const CLERK_JS_VERSION = "5.124.0";
    const CLERK_JS_SRI_HASH =
      "sha384-y7Ljr3jTkMhkujAphmGaZq0PL89c4v37KtauA4YTAS768ejhGi/+TJ2J+rBZ71Ah";
    const frontendApi =
      normalizeFrontendApiUrl(CLERK_FRONTEND_API_URL) ||
      frontendApiFromPublishableKey(CLERK_PUBLISHABLE_KEY);
    const sources = [
      frontendApi
        ? {
            src: `${frontendApi}/npm/@clerk/clerk-js@${CLERK_JS_VERSION}/dist/clerk.browser.js`,
            integrity: CLERK_JS_SRI_HASH,
          }
        : null,
      {
        src: `https://cdn.jsdelivr.net/npm/@clerk/clerk-js@${CLERK_JS_VERSION}/dist/clerk.browser.js`,
        integrity: CLERK_JS_SRI_HASH,
      },
    ].filter(Boolean);
    if (!sources.length) {
      reject(new Error("Unable to determine Clerk JS source."));
      return;
    }
    const loaded = new Set();
    document.querySelectorAll("script[src]").forEach((node) => {
      if (node.src) loaded.add(node.src);
    });
    const loadFrom = (idx) => {
      if (idx >= sources.length) {
        reject(new Error("Failed to load Clerk browser bundle from CDN."));
        return;
      }
      const { src, integrity } = sources[idx];
      const script = document.createElement("script");
      script.src = src;
      if (loaded.has(script.src)) {
        if (window.Clerk) {
          window.__terrainClerkGlobal = window.Clerk;
          resolve(window.__terrainClerkGlobal);
          return;
        }
        loadFrom(idx + 1);
        return;
      }
      script.type = "text/javascript";
      script.setAttribute("data-clerk-publishable-key", CLERK_PUBLISHABLE_KEY);
      script.async = true;
      script.crossOrigin = "anonymous";
      if (integrity) script.integrity = integrity;
      script.onload = () => {
        if (!window.Clerk) {
          loadFrom(idx + 1);
          return;
        }
        window.__terrainClerkGlobal = window.Clerk;
        resolve(window.__terrainClerkGlobal);
      };
      script.onerror = () => loadFrom(idx + 1);
      document.head.appendChild(script);
    };
    loadFrom(0);
  });
}

async function loadClerkDarkTheme() {
  if (!clerkDarkThemePromise) {
    clerkDarkThemePromise = (async () => {
      const globalDark =
        window.Clerk && window.Clerk.themes && window.Clerk.themes.dark;
      if (globalDark) return globalDark;

      const moduleUrls = [
        "https://cdn.jsdelivr.net/npm/@clerk/themes@2/+esm",
        "https://unpkg.com/@clerk/themes@2?module",
      ];

      for (const url of moduleUrls) {
        try {
          const mod = await import(url);
          if (mod && mod.dark) return mod.dark;
          if (mod && mod.default && mod.default.dark) return mod.default.dark;
        } catch (err) {
          // Try the next source if this one fails.
        }
      }
      return null;
    })();
  }
  return clerkDarkThemePromise;
}

async function ensureClerkReady() {
  if (!AUTH_ENABLED) return null;
  if (!CLERK_PUBLISHABLE_KEY) {
    throw new Error("Missing CLERK_PUBLISHABLE_KEY.");
  }
  if (!clerkReadyPromise) {
    clerkReadyPromise = (async () => {
      const clerk = await loadClerkGlobal();
      const darkTheme = await loadClerkDarkTheme().catch(() => null);
      await clerk.load({
        appearance: {
          ...(darkTheme ? { baseTheme: darkTheme } : {}),
          captcha: { theme: "dark" },
        },
      });
      if (!clerkListenerAttached && typeof clerk.addListener === "function") {
        clerk.addListener((state) => {
          if (state && state.session) {
            const nextPath = `${window.location.pathname || "/"}${window.location.search || ""}`;
            finalizeClerkSession(clerk, nextPath);
          }
        });
        clerkListenerAttached = true;
      }
      return clerk;
    })();
  }
  return clerkReadyPromise;
}

async function finalizeClerkSession(clerk, nextPath = "/") {
  if (authExchangeInFlight || !clerk || !clerk.session) {
    return;
  }
  authExchangeInFlight = true;
  try {
    const token = await clerk.session.getToken();
    const resp = await fetch("/auth/clerk/exchange", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ token, next: nextPath }),
    });
    const data = await resp.json().catch(() => ({}));
    if (!resp.ok) {
      throw new Error(data.error || "Unable to establish session.");
    }
    window.location.href = data.next || nextPath || "/";
  } catch (err) {
    authExchangeInFlight = false;
    const message = String((err && err.message) || err || "").trim();
    setAlert(message || "Unable to sign in right now.", true);
  }
}

function openAuthModal(nextPath = "/") {
  if (!AUTH_ENABLED) return;
  const normalizedNext =
    typeof nextPath === "string" && nextPath.startsWith("/") ? nextPath : "/";
  ensureClerkReady()
    .then(async (clerk) => {
      if (!clerk) return;
      if (clerk.session) {
        await finalizeClerkSession(clerk, normalizedNext);
        return;
      }
      if (typeof clerk.openSignIn === "function") {
        clerk.openSignIn({
          afterSignInUrl: normalizedNext,
        });
        return;
      }
      window.location.href = _buildAuthLoginUrl(normalizedNext);
    })
    .catch(() => {
      window.location.href = _buildAuthLoginUrl(normalizedNext);
    });
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
      syncToggleButtons();
      updateAlerts();
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
  const form = event.target;
  const runBtn = document.getElementById("runBtn");
  if (!form || !runBtn) return;
  if (!CAN_BUILD) {
    const nextPath = `${window.location.pathname || "/"}${window.location.search || ""}`;
    openAuthModal(nextPath);
    return;
  }

  buildErrorMessage = "";
  updateAlerts();
  runBtn.disabled = true;
  const originalText = runBtn.textContent;
  runBtn.textContent = "Running...";
  setInlineBuildStatus("Queued...");
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
    runBtn.disabled = false;
    runBtn.textContent = originalText;
    setInlineBuildStatus("Build failed to start.");
    setInlineBuildingOverlay(false);
    return;
  }
  if (!resp.ok) {
    if (resp.status === 401 && AUTH_ENABLED) {
      const nextPath = `${window.location.pathname || "/"}${window.location.search || ""}`;
      openAuthModal(nextPath);
      runBtn.disabled = false;
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
    runBtn.disabled = false;
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
  runBtn.disabled = false;
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

function initInlinePreview() {
  const frame = document.getElementById("inlinePreviewFrame");
  if (!frame) return;
  // Prefer server-injected URL (most recent job from this session), then localStorage
  const serverUrl = window.APP_CONFIG && window.APP_CONFIG.initialPreviewUrl;
  const savedUrl = localStorage.getItem(LAST_PREVIEW_KEY);
  const previewUrl = serverUrl || savedUrl;
  if (previewUrl) {
    setInlinePreview(previewUrl);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  initPreviewModal();
  initAuthModal();
  const jobsMenuShell = document.getElementById("menuShell");
  const jobsMenuButton = document.getElementById("menuButton");
  const jobsMenuDropdown = document.getElementById("menuDropdown");
  if (jobsMenuShell && jobsMenuButton && jobsMenuDropdown) {
    const closeJobsMenu = () => {
      jobsMenuDropdown.classList.add("hidden");
      jobsMenuButton.setAttribute("aria-expanded", "false");
    };
    jobsMenuButton.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      const willOpen = jobsMenuDropdown.classList.contains("hidden");
      if (willOpen) {
        jobsMenuDropdown.classList.remove("hidden");
        jobsMenuButton.setAttribute("aria-expanded", "true");
      } else {
        closeJobsMenu();
      }
    });
    document.addEventListener("click", (event) => {
      if (!jobsMenuShell.contains(event.target)) {
        closeJobsMenu();
      }
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeJobsMenu();
      }
    });
  }
  const topProfileShell = document.getElementById("topProfileShell");
  const topProfileButton = document.getElementById("topProfileButton");
  const topProfileDropdown = document.getElementById("topProfileDropdown");
  const topRecentJobsLink = document.getElementById("topRecentJobsLink");
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
    if (topRecentJobsLink) {
      topRecentJobsLink.addEventListener("click", (event) => {
        event.preventDefault();
        closeTopProfileMenu();
        if (jobsMenuDropdown && jobsMenuButton) {
          jobsMenuDropdown.classList.remove("hidden");
          jobsMenuButton.setAttribute("aria-expanded", "true");
          jobsMenuButton.focus();
        }
      });
    }
  }

  initSegmentedControls();
  initToggleButtons();
  updateUnitLabels();
  updateUiToggles();
  if (window.lucide) {
    lucide.createIcons();
    setFaviconFromLucide();
  }
  const contours = document.getElementById("output_contours");
  const outTerrain = document.getElementById("output_terrain");
  const outBuildings = document.getElementById("output_buildings");
  const outImage = document.getElementById("output_naip");
  const outXyz = document.getElementById("output_xyz");
  const xyzMode = document.getElementById("xyz_mode");
  const dxfParcels = document.getElementById("dxf_include_parcels");
  const coords = document.querySelector('input[name="coords"]');
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
  if (units)
    units.addEventListener("change", () => {
      updateUnitLabels();
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
  initInlinePreview();
  scheduleCoverageCheck();
});
