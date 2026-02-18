# Web/Job UX + Auth/Ownership + Browser Preview Implementation Write-Up

## Goals

1. Keep build submission on one main page, with immediate feedback and recent job actions (`Preview`, `Download`, `Log`) on the same screen.
2. Provide a dedicated job page where `Preview` and `Activity Log` are tabbed in one card.
3. Enforce strict per-user job access so users can only see/download their own jobs.
4. Enable in-browser 3D preview of generated OBJ/MTL/texture artifacts, with no desktop viewer dependency.

## Scope and Primary Files

- Backend/UI orchestration: `src/va_lidar_context/webapp.py`
- Auth and ownership persistence: `src/va_lidar_context/auth_store.py`
- Main UI + recent jobs + popup preview: `src/va_lidar_context/templates/index.html`
- Main UI styles and status/modal styling: `src/va_lidar_context/static/app.css`

## Runtime Model

- Jobs are represented by `Job` dataclass and tracked in-memory in `JOBS`.
- Build requests are accepted by `/run`, validated, and queued.
- A background thread executes the build (`_run_build_job`) and streams log lines into each job’s in-memory `logs` list via `JobLogHandler`.
- Build summary metadata (outputs, warnings, report path) is added back to `job.summary` after completion.

## Auth, Sessions, and Ownership

### Auth mode and session model

- Auth is optional and enabled when `VA_AUTH_PROVIDER=clerk` (and not in desktop mode).
- Clerk token exchange creates a local session (`sessions` table) and stores session id in Flask session cookie.
- User identity is resolved from local session on each request.

### Authorization model

- `require_login` protects user-facing job endpoints.
- Ownership check is centralized in `_user_can_access_job(job_id)`.
- When auth is enabled, access is granted only when `jobs.user_id == current_user.id`.

### Ownership persistence

- Job owner is recorded at queue time in `auth_store.record_job_owner(...)`.
- Job status transitions are persisted in `jobs` table.
- Rate limiting state is persisted via `build_requests` and `active_jobs` tables.

### DB schema responsibilities

- `users`: local user registry and admin flag.
- `sessions`: auth session lifecycle.
- `jobs`: job ownership and status.
- `build_requests`: hourly/daily request counts.
- `active_jobs`: active concurrency control.
- `used_nonces`: replay protection for internal callback auth.

## Job APIs

### Main user APIs

- `POST /run`
- `GET /recent-jobs`
- `GET /jobs/<job_id>`
- `GET /logs/<job_id>?offset=<n>`
- `GET /jobs/<job_id>/artifacts`
- `GET /jobs/<job_id>/download/<name>`
- `GET /jobs/<job_id>/download-all`

### Internal callback API

- `POST /internal/worker/jobs/<job_id>/complete`
- Protected by worker token or HMAC headers + nonce replay protection.

## Main Page UX (`index.html`)

### Build form behavior

- Submits via `fetch` to `/run` with `X-Requested-With: fetch`.
- Immediately starts polling `/logs/<job_id>` for progress.
- Displays inline errors without full-page reload.

### Recent Jobs list behavior

- Shows entries as `<name> - <status>`.
- Actions per row:
  - `Preview` (opens modal iframe to job page preview tab)
  - `Download` (single ZIP of all artifacts, only shown when done and artifacts exist)
  - `Log` (job page)
- Polls `/recent-jobs` every 5 seconds to keep status/action links fresh.

### Preview popup behavior

- Modal contains iframe, loading `/jobs/<job_id>?tab=preview`.
- Closed by backdrop, close button, or Escape.
- Keeps preview implementation centralized on job page (no duplicate renderer code on main page).

## Job Page UX (`STATUS_TEMPLATE` in `webapp.py`)

### Unified card with tabs

- One card with `Preview` and `Activity Log` tabs.
- Status badge color-coded:
  - queued/running: `status-running`
  - done: `status-done`
  - error: `status-error`

### Log stream

- Polls `/logs/<job_id>` with incremental `offset`.
- Appends only new log lines and auto-scrolls.
- Updates status badge continuously.

### Preview activation

- If job is done: activates preview immediately.
- If queued/running: shows waiting message until completion.
- If error: shows failed/unavailable message.

## Browser 3D Preview Pipeline

### Artifact discovery

- Calls `/jobs/<job_id>/artifacts` to discover output files.
- Builds available model options dynamically:
  - `Terrain + Buildings`
  - `Combined`
  - `Terrain`
  - `Buildings`

### Renderer setup

- Three.js + `OrbitControls` + `OBJLoader` + `MTLLoader` loaded from CDN.
- Camera configured as Z-up (`camera.up.set(0,0,1)`).
- Scene lighting is ambient + directional.

### Model loading

- OBJ/MTL fetched as text, parsed in browser.
- `LoadingManager.setURLModifier` remaps relative MTL texture references to authorized artifact download URLs.
- `inline=1` is used on download URLs so browser can request files without attachment behavior.

### Interaction controls

- `Wireframe` toggle.
- `Reset View` (reframes camera based on current model bounds).
- Model selector dropdown switches between available model groups.

## Artifact and File Safety

- Output directory is resolved from job summary/report/default path, then constrained with `_is_path_within(OUT_DIR, candidate)`.
- Download endpoint rejects path separators in filenames.
- Artifact listing prefers known output list and adds MTL support files for preview compatibility.

## Rate Limits and Multi-User Guardrails

- Hourly and daily per-user build request caps.
- Max active jobs per user.
- If exceeded, `/run` returns HTTP `429` with specific reason.

## Reuse Settings Flow

- Job page provides `Reuse settings in main form` link (`/?from_job=<job_id>`).
- Main form merges saved `form_defaults` from job summary when access is allowed.

## How to Split This Feature Out Separately

1. Extract backend job/auth endpoints and helpers from `webapp.py` as one module.
2. Keep `auth_store.py` intact as the persistence layer.
3. Extract frontend pieces:
   - main-page recent jobs + modal preview logic
   - job-page preview/log tab renderer logic
4. Preserve endpoint contracts first (`/run`, `/logs`, `/recent-jobs`, `/artifacts`, `/download`, `/download-all`) to avoid coupling breakage.
5. After extraction, add integration tests around:
   - ownership restrictions
   - download authorization
   - recent jobs filtering by user
   - preview artifact discovery and inline serving
