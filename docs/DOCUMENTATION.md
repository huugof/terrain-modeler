# Documentation

## CLI Flags

`va-lidar-context build [TILE_ID] [OPTIONS]`

| Flag | Description |
|---|---|
| `TILE_ID` | Virginia tile ID (e.g. `S13_4899_20`). Omit to use `--center`. |
| `--center LAT LON` | Clip center in lat/lon (Google Maps order). |
| `--size N` | Clip size in feet (default 500). Use `--units meters` for metric. |
| `--out DIR` | Output directory (required). |
| `--outputs LIST` | Comma-separated: `buildings`, `terrain`, `contours`, `parcels`, `naip`, `xyz`. |
| `--provider` | `virginia` (default) or `national` (USGS 3DEP + Microsoft footprints). |
| `--ept-only` | Skip LAZ download, use EPT stream only (national mode). |
| `--allow-multi-tile` | Merge adjacent tiles when clip crosses a boundary. |
| `--resolution N` | Point cloud resolution in meters (default 0.5). |
| `--terrain-sample N` | Terrain mesh simplification factor. |
| `--random-heights MIN MAX` | Random building height range when no height data is available. |
| `--fill-dtm` | Fill DTM voids. |
| `--fill-hard` | Use hard fill (no interpolation). |
| `--combine-output` | Merge terrain + buildings into `combined.obj`. |
| `--contours N` | Contour interval in feet (required when `contours` in `--outputs`). |
| `--units` | `feet` (default) or `meters`. |
| `--keep-rasters` | Retain intermediate `dtm.tif`, `dsm.tif`, `ndsm.tif`. |
| `--naip-flip-u` / `--naip-flip-v` | Fix horizontally/vertically mirrored NAIP imagery. |
| `--flip-x` / `--flip-y` | Mirror output geometry on X or Y axis. |
| `--rotate-z DEG` | Rotate output around the center point (applies to DXF/XYZ too). |
| `--xyz-mode` | `contours` (default) or `grid`. |
| `--xyz-contour-spacing N` | Resample XYZ contour vertices at this interval. |
| `--dxf-contour-spacing N` | Resample DXF contour vertices at this interval. |

## Output Files

All outputs land in `./out/<job_id>/` where job_id is a hash of the inputs.

| File | Condition |
|---|---|
| `tile.json`, `tile.laz` | Always |
| `footprints.geojson` | Always |
| `terrain.obj`, `terrain.mtl`, `terrain.png` | When `terrain` in outputs |
| `buildings.obj` | When `buildings` in outputs |
| `building_heights.geojson`, `building_heights.csv` | When `buildings` in outputs |
| `combined.obj`, `combined.mtl` | When `--combine-output` |
| `contours.dxf` | When `contours` or `parcels` in outputs |
| `terrain.xyz` | When `xyz` in outputs |
| `report.json`, `README.txt` | Always |
| `dtm.tif`, `dsm.tif`, `ndsm.tif` | Only with `--keep-rasters` |
| `tiles_merged.laz`, `tiles/<tile>.laz` | Only with `--allow-multi-tile` |

**Units note:** OBJ is unitless. Default output is in feet (~5000×5000 units per 500 ft clip). In Rhino, set document units to **Feet**. To import into a mm document, scale by **304.8**.

## Environment Variables

### Session / core

| Variable | Default | Description |
|---|---|---|
| `VA_SESSION_SECRET` | required in server mode | Flask session signing key. Startup fails in server mode when unset. |
| `VA_OUT_DIR` | `./out` | Where job outputs are written. |
| `VA_RETENTION_DAYS` | `7` | Days before outputs are cleaned up. |
| `VA_CLEANUP_INTERVAL` | `3600` | Cleanup loop interval in seconds. |
| `VA_DB_PATH` | `./data/app.db` | SQLite database path. In Docker: `/data/app/app.db`. |
| `VA_JOB_HISTORY_ENABLED` | `1` | Persist job metadata across restarts. |
| `VA_JOB_REHYDRATE_LIMIT` | `500` | Max jobs loaded from DB on startup. |

### Docker / Caddy deployment

| Variable | Default | Description |
|---|---|---|
| `APP_DOMAIN` | none | Public domain Caddy should serve (required in compose deployment). |
| `ACME_EMAIL` | none | Contact email used for ACME/TLS account registration (required). |
| `APP_IMAGE` | `va-lidar-context:latest` | Image tag for blue/green services. |

### Auth (Clerk)

| Variable | Description |
|---|---|
| `VA_AUTH_PROVIDER=clerk` | Enables Clerk authentication. |
| `VA_CLERK_PUBLISHABLE_KEY` | Clerk publishable key. |
| `VA_CLERK_SECRET_KEY` | Clerk secret key. |
| `VA_CLERK_FRONTEND_API_URL` | Recommended. E.g. `https://<your-frontend-api>`. |
| `VA_CLERK_SIGN_IN_URL` | Optional fallback link to hosted sign-in page. |
| `VA_CLERK_JWKS_URL` | Optional override if not inferable from token `iss`. |
| `VA_CLERK_ISSUER` | Optional strict issuer check. |
| `VA_CLERK_API_URL` | Default `https://api.clerk.com/v1`. |
| `VA_CLERK_ALLOWED_DOMAIN` | Restrict sign-in to this email domain. |
| `VA_CLERK_AUTHORIZED_PARTIES` | Comma-separated allowed `azp` values. |
| `VA_REQUIRE_LOCAL_ALLOWLIST` | `0` — set `1` to require local allowlist membership. |
| `VA_ADMIN_EMAIL` | Bootstraps first admin user in the local allowlist. |

### Rate limiting

| Variable | Default | Description |
|---|---|---|
| `VA_RATE_LIMIT_HOURLY` | `3` | Max builds per user per hour. |
| `VA_RATE_LIMIT_DAILY` | `10` | Max builds per user per day. |
| `VA_MAX_ACTIVE_JOBS_PER_USER` | `1` | Max concurrent jobs per user. |

### Worker callback auth (optional)

Secure the `/internal/worker/jobs/<job_id>/complete` endpoint with either:

- `VA_WORKER_SHARED_TOKEN` — simple shared token sent as `X-Worker-Token`.
- `VA_HMAC_KEYS_JSON` — JSON object of key-id → secret, e.g. `{"k1":"secret"}`. Request must include `X-Key-Id`, `X-Signature`, `X-Timestamp`, `X-Nonce` headers.

## Authentication Behaviour

With `VA_AUTH_PROVIDER=clerk`:
- The main form is publicly browseable; **Build** requires login.
- Unauthenticated users see a **Login to Build** button instead.
- Any authenticated Clerk user can sign in by default.
- Set `VA_REQUIRE_LOCAL_ALLOWLIST=1` to restrict to an explicit allowlist managed at `/admin/users`.
- Job downloads are owner-only. Programmatic access: `GET /jobs/<job_id>/artifacts` and `GET /jobs/<job_id>/download/<name>`.

## Parcel Sources

Parcel boundaries are fetched from public ArcGIS FeatureServer layers registered in `src/va_lidar_context/parcels/sources.json`. The resolver picks the first source whose `coverage` bbox intersects the clip area. If none match, parcels are silently skipped.

### Add a source

1. Find a public ArcGIS FeatureServer layer serving parcel polygons.
2. Confirm it returns `esriGeometryPolygon` GeoJSON and supports pagination (`?f=pjson`).
3. Add an entry to `sources.json`:

```json
{
  "id": "county_parcels",
  "name": "County Parcels",
  "kind": "arcgis",
  "query_url": "https://example.gov/arcgis/rest/services/Parcels/FeatureServer/0/query",
  "out_fields": "OBJECTID,PARCELID",
  "max_record_count": 2000,
  "coverage": { "xmin": -120.0, "ymin": 32.0, "xmax": -114.0, "ymax": 42.0 },
  "notes": "Optional licensing or coverage notes."
}
```

To find layers: browse `https://<domain>/arcgis/rest/services` and look for services named `Parcels`, `Cadastre`, `TaxParcel`, or `Assessment`.

## Notes

- If your clip crosses a tile boundary, add `--allow-multi-tile`.
- `--ept-only` skips the LAZ download and streams via EPT — use if the USGS LAZ host is unreachable (will fail if EPT is also unavailable).
- `--naip-flip-u`/`--naip-flip-v` fix mirrored aerial imagery.
- `--rotate-z` rotates DXF and XYZ outputs around `--center`; it does not affect `terrain.png`.
- XYZ output defaults to contour vertices; use `--xyz-mode grid` for a full uniform grid.
