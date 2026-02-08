# AGENTS.md

## Project Overview
- Builds terrain, building, contour, and parcel context models from LiDAR + GIS sources.
- CLI: `va-lidar-context`.
- Web UI: `va-lidar-context-web` (local Flask app).

## Repo Layout
- `src/va_lidar_context/` core Python package
- `src/va_lidar_context/cli.py` CLI entry point
- `src/va_lidar_context/webapp.py` local web UI
- `src/va_lidar_context/core/` raster + mesh + geo helpers
- `src/va_lidar_context/parcels/` parcel registry + fetchers
- `src/va_lidar_context/pipeline/` build orchestration
- `src/va_lidar_context/providers/` data source adapters
- `out/` output jobs (default)
- `docs/references/` research notes and links
- `tests/` pytest suite

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

## Outputs & Retention
- Output jobs are written to `./out/<job_id>/` by default.
- Web UI cleanup is controlled by env vars:
  - `VA_OUT_DIR`, `VA_RETENTION_DAYS`, `VA_CLEANUP_INTERVAL`

## Parcel Sources
- Parcel boundaries are sourced from `src/va_lidar_context/parcels/sources.json`.
- Resolver picks the first source whose `coverage` bbox intersects the request area.
- Only ArcGIS FeatureServer `query` endpoints are supported right now.

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

### Finding Parcel Layers (Quick Checklist)
- Start at the GIS server root: `https://<domain>/arcgis/rest/services`.
- Look for folders/services named `Parcels`, `Cadastre`, `TaxParcel`, or `Assessment`.
- Open the service, then the `FeatureServer` layer list.
- Use the layer’s `/query` endpoint as `query_url`.
- Confirm geometry type via `?f=pjson` (`esriGeometryPolygon`).

## Testing
- Run all tests: `pytest`
- Some tests may touch networked services; prefer running a targeted test if needed.

## Conventions
- Prefer minimal, explicit changes.
- Keep outputs deterministic where possible.
- Update README if behavior or user-facing flags change.
