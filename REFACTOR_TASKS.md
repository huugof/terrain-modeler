# Refactor Task List

## Phase A — File & Directory Cleanup

- [x] **Step 7:** Delete unnecessary files and directories
  - `git rm` `.zed/debug.json`, `TODO.md`, `docs/CONTINUE.md`, `docs/refactoring-plan.md`, `docs/SPEC.md`, `docs/README.md`, `docs/output-resolution-concurrency-contour-smoothing-review.md`, `docs/references/`
  - Add `.zed/` to `.gitignore`
  - Delete untracked `docs/output-resolution-processing-change.md`

- [x] **Step 8:** Update `AGENTS.md`
  - Rewrite to reflect current `webapp/` package structure and correct env var names

- [x] **Step 9:** Fix `scripts/preload_grand_canyon_default.py` bug
  - `result.get("output_dir")` → `result.output_dir`

## Phase B — Code Refactor

- [x] **Step 1:** Unify output validation (D1)
  - Moved `parse_outputs()` into `pipeline/build.py` alongside `OUTPUT_CHOICES`
  - `_validate_outputs()` now delegates to `parse_outputs()`
  - `cli.py` imports from new location; own copy removed

- [x] **Step 2:** Fix `OutputKind` type alias (B2)
  - Added `"xyz"` to the `Literal` in `pipeline/types.py`

- [x] **Step 3:** Simplify `webapp/__init__.py:main()` dead code (B1)
  - Removed unreachable `default_host`/`default_port` variables; use `settings.DESKTOP_HOST`/`settings.DESKTOP_PORT` directly

- [x] **Step 4:** Trim `webapp/__init__.py` re-exports (C1)
  - Reduced re-exports to only names actually used by tests/callers
  - Uses explicit `name as name` re-export pattern for ruff compliance

- [x] **Step 5:** Remove redundant `output_*` bools in `routes.py:run_job()` (D3)
  - Eliminated `output_terrain`/`output_buildings`/etc. — replaced with inline `"terrain" in outputs` checks

- [x] **Step 6:** Deduplicate `_ImmediateThread` in tests (D2)
  - Extracted to module-level class in `test_parse_inputs.py`

## Verification

- [x] Run tests: 169/169 passed
- [x] Run linter: `ruff check src/ tests/` — all checks passed
- [ ] Spot-check CLI: `va-lidar-context build --help`
- [ ] Verify imports: `python -c "from va_lidar_context.webapp import app, create_app, Job, JOBS, JOBS_LOCK, settings"`
- [ ] Verify sub-module imports: `python -c "import va_lidar_context.cli; import va_lidar_context.webapp.routes"`
