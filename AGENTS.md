# AGENTS.md

## Project Overview
- Builds terrain, building, contour, and parcel context models from LiDAR + GIS sources.
- CLI: `va-lidar-context`.
- Web UI: `va-lidar-context-web` (Flask app, also serves as a local desktop UI).

## Repo Layout
- `src/va_lidar_context/` — core Python package
  - `cli.py` — CLI entry point (`va-lidar-context` command)
  - `config.py` — `BuildConfig` frozen dataclass + `DEFAULT_*` constants
  - `constants.py` — URL constants, default preview job config
  - `util.py` — subprocess wrapper, cancel machinery, `get_logger()`, `download_file()`
  - `auth_store.py` — SQLite persistence for users, sessions, jobs, artifacts
  - `hmac_auth.py` — HMAC signing/verification primitives
  - `pipeline/` — build orchestration (`build.py`, `io.py`, `types.py`)
  - `webapp/` — Flask web app (`__init__.py`, `routes.py`, `jobs.py`, `auth.py`, `forms.py`, `settings.py`, `rate_limiter.py`)
  - `core/` — raster + mesh + geo helpers
  - `parcels/` — parcel registry + fetchers (`sources.json`)
  - `providers/` — data source adapters
- `out/` — output jobs (default, gitignored)
- `docs/` — project documentation (`DOCUMENTATION.md` is the primary reference)
- `tests/` — pytest suite
- `deploy/` — Caddyfile + blue/green deploy scripts
- `scripts/` — utility scripts

## Dev Environment
- Python 3.11+
- System deps (macOS via Homebrew): `pdal`, `gdal`, `geos`, `proj`
- Install Python deps: `pip install -e .`

## Common Commands
- Run CLI:
  - `va-lidar-context build --center <lat> <lon> --size 500 --out ./out`
- Run web UI:
  - `va-lidar-context-web`
  - or `python3 -m va_lidar_context.webapp`
- Run tests: `pytest`
- Run linter: `python -m ruff check src/ tests/`

## Key Entry Points
- `va-lidar-context` → `va_lidar_context.cli:main`
- `va-lidar-context-web` → `va_lidar_context.webapp:main`
- Docker/Gunicorn → `va_lidar_context.webapp:app`

## Outputs & Retention
- Output jobs are written to `./out/<job_id>/` by default.
- Controlled via env vars: `OUT_DIR`, `RETENTION_DAYS`, `CLEANUP_INTERVAL`.
- See `docs/DOCUMENTATION.md` for the full env var reference.

## Parcel Sources
- Parcel boundaries are sourced from `src/va_lidar_context/parcels/sources.json`.
- Resolver picks the first source whose `coverage` bbox intersects the request area.
- Only ArcGIS FeatureServer `query` endpoints are supported.

### Add a Parcel Source
1. Find a public ArcGIS FeatureServer layer that serves parcel polygons.
2. Add an entry to `src/va_lidar_context/parcels/sources.json`.
3. Set a `coverage` bbox in WGS84 (lon/lat) so we only query in-region.

Example entry:
```json
{
  "id": "state_or_county_parcels",
  "name": "State/County Parcels",
  "kind": "arcgis",
  "query_url": "https://example.gov/arcgis/rest/services/Parcels/FeatureServer/0/query",
  "out_fields": "OBJECTID,PARCELID",
  "max_record_count": 2000,
  "coverage": { "xmin": -120.0, "ymin": 32.0, "xmax": -114.0, "ymax": 42.0 },
  "notes": "Any licensing caveats or coverage notes."
}
```

## Conventions
- Prefer minimal, explicit changes.
- Keep outputs deterministic where possible.
- Update `docs/DOCUMENTATION.md` if behavior or user-facing flags change.
