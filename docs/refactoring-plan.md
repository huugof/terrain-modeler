# Repository Refactoring Plan

Last updated: February 19, 2026

## Purpose

This is a living plan to clean up the codebase: remove dead code/files, simplify architecture, fix confirmed bugs, and improve long-term maintainability.

## Audit Snapshot

- Scope reviewed: `src/`, `tests/`, templates/CSS, docs, deploy files.
- Test run status: `pytest` unavailable in current environment, so full test execution is pending.
- Syntax check: `python3 -m compileall src tests` succeeded.
- Pre-existing local modification observed: `data/app.db`.

## Confirmed High-Priority Issues

### P0: Default CLI/build behavior is inconsistent and can fail immediately

- Evidence:
  - `src/va_lidar_context/config.py:43` sets `DEFAULT_OUTPUTS` to `("contours", "xyz")`.
  - `src/va_lidar_context/cli.py:45` uses `DEFAULT_OUTPUTS` when `--outputs` is omitted.
  - `src/va_lidar_context/pipeline/build.py:135` requires contour interval when contours are enabled.
  - `src/va_lidar_context/cli.py:222` help text still says defaults are buildings/terrain.
- Outcome:
  - A default run can raise `ValueError: Contours output requires --contours INTERVAL.`

### P0: Invalid numeric form/query input can trigger 500s

- Evidence:
  - `src/va_lidar_context/webapp.py:1294` (`parse_float`) raises on invalid input.
  - `src/va_lidar_context/webapp.py:1303` (`parse_int`) raises on invalid input.
- Outcome:
  - Bad user input is not consistently converted to user-facing 4xx responses.
- Fix approach:
  - Make parsers return `None` on non-numeric input (not raise), consistent with empty/None handling.
  - Do NOT add a try/except wrapper at the call site — fix the parsers directly.

### P0: Job logging can leak across concurrent jobs

- Evidence:
  - Global logger handler attachment in `src/va_lidar_context/webapp.py:2674`.
  - `get_logger()` in `util.py:10` returns the named `"va_lidar_context"` singleton.
- Outcome:
  - Concurrent jobs (up to 4 threads/worker in gunicorn) cross-contaminate log streams.
- Fix approach:
  - Create a child logger per job: `logging.getLogger(f"va_lidar_context.job.{job.job_id}")`
  - Set `propagate = False` on the child logger.
  - Attach `JobLogHandler` to the child logger, not the global one.

### P0: Job summary hydration can associate wrong report under concurrency

- Evidence:
  - Report discovery scans by mtime (`src/va_lidar_context/webapp.py:1369`).
  - Used after job execution (`src/va_lidar_context/webapp.py:2697`).
- Outcome:
  - Wrong report/output metadata can be attached when jobs finish close together.
- Fix approach:
  - Change `build_pipeline()` return type from `int` to a small result struct carrying `exit_code` + `output_dir` (or `Path | None`).
  - Use that explicit path in the job runner instead of calling `_find_latest_report`.
  - Delete `_find_latest_report` once the explicit path is plumbed through.

## Confirmed Medium-Priority Issues

### P1: Auth policy/documentation mismatch

- Evidence:
  - Owner-only access check in `src/va_lidar_context/webapp.py:326`.
  - README claims admins can download all jobs (`README.md:220`).

### P1: `project_zero` is currently a no-op

- Evidence:
  - Config/UI plumbing exists (`src/va_lidar_context/config.py:88`, `src/va_lidar_context/webapp.py:2382`).
  - No active use in pipeline behavior (`build.py` never reads `cfg.project_zero`).
- Decision needed: implement it, or delete config + webapp + form plumbing entirely.

### P1: Form/backend mismatch

- Backend reads fields not present in form:
  - `output_combined` (`src/va_lidar_context/webapp.py:2341`) — silently always `False`; dead path
  - `min_height` / `max_height` (`src/va_lidar_context/webapp.py:2300`, `2303`) — fall through to defaults
  - `xyz_contour_spacing` (`src/va_lidar_context/webapp.py:2358`)
- Form includes unused/deferred field:
  - `dxf_include_roads` (`src/va_lidar_context/templates/index.html:348`)
- Decision for `output_combined`: delete the backend path + config field, or add UI checkbox.

## Confirmed Dead Code

All items below have been verified by grep — zero callers outside the definition.

- `src/va_lidar_context/util.py:33` — `read_json` (unused)
- `src/va_lidar_context/providers/usgs_index.py:94` — `format_collect_date` (unused)
- `src/va_lidar_context/pipeline/types.py:14` — `ClipSpec` (exported but never imported externally)
- `src/va_lidar_context/pipeline/types.py:34` — `BuildArtifacts` (exported but never imported externally)
- `src/va_lidar_context/pipeline/types.py:49` — `BuildRequest = BuildConfig` (alias, never used)
- `src/va_lidar_context/core/mesh.py:515` — `export_contours_dxf` (needs grep confirmation before delete)
- `src/va_lidar_context/core/mesh.py:542` — `export_parcels_dxf` (needs grep confirmation before delete)
- `data/app.db` — runtime artifact committed to git

Note: `LidarSource` and `OutputKind` in `pipeline/types.py` ARE used — keep them.

---

## Task List

### Phase 1: Stabilize Critical Behavior (P0)

- [x] **1.1** Fix `parse_float` (`webapp.py:1294`) to return `None` on non-numeric input instead of raising `ValueError`.
- [x] **1.2** Fix `parse_int` (`webapp.py:1303`) to return `None` on non-numeric input instead of raising `ValueError`.
- [x] **1.3** Fix CLI default outputs: changed `DEFAULT_OUTPUTS` in `config.py:43` from `("contours", "xyz")` to `("buildings", "terrain")`.
- [x] **1.4** Fix CLI help text in `cli.py:222` to match actual defaults.
- [x] **1.5** Add regression test: default CLI run without `--outputs` does not raise. (`tests/test_cli_defaults.py`)
- [x] **1.6** Add regression test: invalid numeric input to `/run` returns 400, not 500. (`tests/test_parse_inputs.py`)
- [x] **1.7** Add regression test: contour/xyz validation combinations (contours without interval, xyz in contour mode without interval). (`tests/test_build_validation.py`)

### Phase 2: Make Job Lifecycle Deterministic

- [x] **2.1** Define `BuildResult(exit_code: int, output_dir: Path | None)` in `pipeline/types.py`.
- [x] **2.2** Updated `build()` in `build.py` to return `BuildResult` instead of bare `int`. Updated `cli.py` to use `.exit_code`.
- [x] **2.3** Updated job runner in `webapp.py` to use `result.output_dir` directly.
- [x] **2.4** Deleted `_find_latest_report` from `webapp.py`. Updated `tests/test_webapp_reports.py` to test the new path.
- [x] **2.5** Fixed per-job logging: job runner now uses `logging.getLogger(f"va_lidar_context.job.{job.job_id}")` with `propagate=False`.
- [x] **2.6** Added concurrency test: two jobs produce independent log streams. (`tests/test_job_concurrency.py`)
- [x] **2.7** Added concurrency test: two jobs finishing close together receive correct summaries. (`tests/test_job_concurrency.py`)

### Phase 3: Decompose Monoliths

*Do `STATUS_TEMPLATE` first — it's ~850 lines (31%) of `webapp.py` and the highest-value single extraction.*

- [x] **3.1** Move `STATUS_TEMPLATE` (inline HTML string, `webapp.py:442–1291`) into `src/va_lidar_context/templates/job_status.html` as a proper Jinja template.
- [x] **3.2** Move large inline JS in `src/va_lidar_context/templates/index.html` into `src/va_lidar_context/static/app.js`.
- [x] **3.3** Split `webapp.py` into submodules:
  - [x] **3.3a** `webapp/auth.py` — session management, CSRF, Clerk token exchange, `require_login`, `require_admin`
  - [x] **3.3b** `webapp/jobs.py` — `Job` dataclass, `JOBS` dict, job runner, `JobLogHandler`, notify helpers
  - [x] **3.3c** `webapp/routes.py` — all Flask route handlers
  - [x] **3.3d** `webapp/settings.py` — env var parsing (named settings to avoid clash with top-level config.py)
- [x] **3.4** Break `pipeline/build.py` into stage functions or sub-modules (e.g. `pipeline/stages/`).
- [x] **3.5** Evaluate `pipeline/report.py` (12 lines, single `json.dumps` wrapper): decide to inline into `build.py` or keep for testability.

### Phase 4: Remove Dead Code and Drift

*Safe to do before or alongside Phase 3 — reduces noise.*

- [x] **4.1** Deleted `read_json` from `util.py`.
- [x] **4.2** Deleted `format_collect_date` and unused `datetime` import from `usgs_index.py`.
- [x] **4.3** Deleted `ClipSpec`, `BuildArtifacts`, `BuildRequest`, unused `BuildConfig` import from `pipeline/types.py`; updated `pipeline/__init__.py` exports.
- [x] **4.4** Grep-confirmed no callers; deleted `export_contours_dxf` from `core/mesh.py`.
- [x] **4.5** Grep-confirmed no callers; deleted `export_parcels_dxf` from `core/mesh.py`.
- [x] **4.6** Deleted `project_zero` from `config.py`, `webapp.py` (form parse + BuildConfig call + _extract_form_defaults), and `templates/index.html`.
- [x] **4.7** Removed web form `output_combined` read from `webapp.py`; hardcoded `combine_output = False` with comment. CLI `--combine-output` flag and `build.py` pipeline logic retained (feature works via CLI).
- [x] **4.8** Removed `dxf_include_roads` button and hidden checkbox from `templates/index.html`.
- [x] **4.9** Removed `data/app.db` from git tracking (`git rm --cached`).
- [x] **4.10** Added `data/*.db` to `.gitignore`.

### Phase 5: Tooling, Tests, and Documentation Consistency

- [x] **5.1** Add explicit dev dependencies for test/lint tooling to `pyproject.toml` (pytest, ruff or flake8, mypy optional).
- [x] **5.2** Ensure CI runs `pytest` and lint checks on each push. Added `.github/workflows/ci.yml`.
- [x] **5.3** Normalize tests: remove any repeated `sys.path` bootstrapping; rely on `pyproject.toml` install.
- [x] **5.4** Reconcile README (`README.md:220`) with actual auth/ownership behavior (owner-only, not admin-accessible).
- [x] **5.5** Reconcile README with actual CLI defaults after Phase 1 fix. (No stale prose found; all examples use explicit `--outputs`.)
- [x] **5.6** Decide status of `SPEC.md` / `CONTINUE.md`: archive, merge into README, or remove. Moved both to `docs/`.
- [x] **5.7** Consider moving toward Flask app-factory pattern to make test setup less reliant on monkeypatching module-level globals (long-term, low urgency). Deferred — documented here as future work.

---

## Execution Order (Recommended)

1. Phase 1 (P0 bug fixes — unblock safe usage)
2. Phase 2 (job lifecycle determinism)
3. Phase 4 (dead code removal — clean up before decomposing)
4. Phase 3 (decompose monoliths)
5. Phase 5 (tooling and docs)

## Success Criteria

- Default CLI/web flows work without hidden required fields.
- No known concurrency-induced metadata/logging corruption.
- `webapp.py` and `pipeline/build.py` are materially smaller and easier to test.
- Dead code and runtime artifacts are removed from tracked source.
- Docs reflect actual behavior.
- `pytest` passes clean.

## Change Log

- 2026-02-19: Initial full-repo audit and baseline refactoring roadmap created.
- 2026-02-19: Revised with code-verified findings: confirmed dead code, P0 fix approaches, new findings (STATUS_TEMPLATE size, report.py triviality, gunicorn threading context, gitignore gap). Added numbered task list with specific file/line references.
- 2026-02-19: Phase 1 complete. Fixed parse_float/parse_int, DEFAULT_OUTPUTS, CLI help text. Added tests/test_cli_defaults.py, tests/test_parse_inputs.py, tests/test_build_validation.py.
- 2026-02-19: Phase 2 complete. Added BuildResult to pipeline/types.py; build() returns explicit output_dir; _find_latest_report deleted; per-job child logger replaces global handler. Added tests/test_webapp_reports.py (rewritten), tests/test_job_concurrency.py.
- 2026-02-19: Phase 4 complete. Deleted read_json, format_collect_date, ClipSpec, BuildArtifacts, BuildRequest, export_contours_dxf, export_parcels_dxf, project_zero plumbing, output_combined web form path, dxf_include_roads UI. Untracked data/app.db; added data/*.db to .gitignore.
- 2026-02-19: Phase 5 complete. Added [dev] extras (pytest, ruff) to pyproject.toml; added static/*.js to package-data; added .github/workflows/ci.yml; removed redundant sys.path bootstrap from tests/__init__.py and 3 test files; fixed README download-auth claim; moved SPEC.md and CONTINUE.md to docs/.
- 2026-02-19: Phase 3 complete. Moved STATUS_TEMPLATE to job_status.html; moved inline JS to static/app.js; split webapp.py into webapp/ package (settings, jobs, auth, forms, routes); extracted stage helpers from pipeline/build.py; inlined write_report and deleted pipeline/report.py.
