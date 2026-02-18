# va-lidar-context

CLI to build context building meshes from Virginia LiDAR and building footprints, with optional national USGS 3DEP support.

**Primary example (current default workflow):**
```bash
va-lidar-context build S13_4899_20 \
  --out ./out \
  --terrain-sample 10 \
  --random-heights 15 40 \
  --fill-dtm --fill-hard \
  --outputs buildings,terrain,naip \
  --naip-flip-v \
  --combine-output
```

**Clip to a smaller region (square, feet) centered on a lon/lat:**
```bash
va-lidar-context build \
  --out ./out \
  --center 38.03344644806424 -78.46451371473545 \
  --size 500 \
  --allow-multi-tile \
  --terrain-sample 10 \
  --random-heights 15 40 \
  --fill-dtm --fill-hard \
  --outputs buildings,terrain,naip,contours,parcels \
  --combine-output \
  --contours 2 \
  --resolution 0.5
```

**National mode (USGS 3DEP LiDAR + Microsoft building footprints):**
```bash
va-lidar-context build \
  --provider national \
  --center 38.03344644806424 -78.46451371473545 \
  --size 500 \
  --out ./out \
  --resolution 1
```
National mode defaults to EPT-first with LAZ fallback.
- `--ept-only` requires EPT coverage and fails fast if unavailable.
- `--no-prefer-ept` skips EPT and uses LAZ workflow.

Parcels are resolved from a small registry of public parcel sources in
`src/va_lidar_context/parcels/sources.json`. If no source matches the clip area,
parcels are skipped and the web UI shows an alert when Parcels is checked.

Note: `--center` expects `lat, lon` (Google Maps order).

## Requirements
- macOS
- Python 3.11+
- PDAL (`pdal` on PATH) for EPT streaming in national mode
- Python deps installed via `pip install -e .` (includes `mapbox-earcut`)

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Ubuntu/Droplet Setup (No Docker)
If you are installing directly on Ubuntu (for example a DigitalOcean droplet):

### 1) Install Python + virtual environment
For Ubuntu 24.04 (default Python 3.12):
```bash
sudo apt install -y python3-venv python3-pip
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

### 2) (Optional) Use Python 3.11 specifically
```bash
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3-pip
python3.11 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

## Run
```bash
va-lidar-context build S13_4899_20 \
  --out ./out \
  --terrain-sample 10 \
  --random-heights 15 40 \
  --fill-dtm --fill-hard \
  --outputs buildings,terrain,naip \
  --naip-flip-v \
  --combine-output
```


## Web UI (Local)
Run a small local web app with a form UI for all CLI arguments:
```bash
va-lidar-context-web
```
Or:
```bash
python3 -m va_lidar_context.webapp
```
Then open `http://127.0.0.1:5000` in your browser.
On a remote host, bind to all interfaces:
```bash
va-lidar-context-web --host 0.0.0.0 --port 8000
```

## Desktop App (macOS, Tauri + Python sidecar)
Desktop mode runs the same Flask app locally with auth/rate limits disabled and
defaults output to `~/Documents/TerrainModeler`.

### Build sidecar binary
```bash
./desktop/build-sidecar.sh
```

### Build Tauri shell
```bash
cd desktop
npm install
npm run tauri:build
```

For a local verification build (macOS app only, skips DMG packaging):
```bash
cd desktop
npm run tauri:build:app
```

Desktop runtime env behavior:
- `VA_DESKTOP_MODE=1` (set by the Tauri shell)
- Default port `8000`
- Default retention `0` (no automatic cleanup)
- Default out dir `~/Documents/TerrainModeler`


## Deploy (DigitalOcean)
**Recommended**: Docker on a small Ubuntu droplet.
Running in a Python venv is fine for local/dev testing, but use Docker + Gunicorn + Caddy for production.

### Setup
```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
sudo usermod -aG docker $USER
```
Log out/in so Docker works without sudo.

### Run
```bash
mkdir -p /data/out
# from your repo
sudo docker compose up -d --build
```
App is on `http://<droplet-ip>:8000`.

## Production Deploy (Caddy + Blue/Green)
For production, use `docker-compose.prod.yml` and `deploy/Caddyfile`.

### Required environment
- `APP_DOMAIN` (DNS name routed to this VPS)
- `ACME_EMAIL` (for TLS cert registration)
- `APP_IMAGE` (container image tag)
- `VA_SESSION_SECRET` (random secret for session signing)

### Optional auth/abuse controls
- `VA_AUTH_PROVIDER=clerk`
- `VA_CLERK_PUBLISHABLE_KEY`
- `VA_CLERK_SECRET_KEY`
- `VA_CLERK_FRONTEND_API_URL` (recommended; e.g. `https://<your-frontend-api>`)
- `VA_CLERK_SIGN_IN_URL` (optional fallback link to hosted sign-in)
- `VA_CLERK_JWKS_URL` (optional override if not inferable from token `iss`)
- `VA_CLERK_ISSUER` (optional strict issuer check)
- `VA_CLERK_API_URL` (default `https://api.clerk.com/v1`)
- `VA_CLERK_ALLOWED_DOMAIN` (optional domain restriction)
- `VA_CLERK_AUTHORIZED_PARTIES` (comma-separated allowed `azp` values)
- `VA_REQUIRE_LOCAL_ALLOWLIST` (default `0`; set `1` to require local allowlist membership)
- `VA_ADMIN_EMAIL` (bootstraps first admin allowlisted user)
- `VA_RATE_LIMIT_HOURLY` (default `3`)
- `VA_RATE_LIMIT_DAILY` (default `10`)
- `VA_MAX_ACTIVE_JOBS_PER_USER` (default `1`)
- `VA_DB_PATH` (default `./data/app.db`, set `/data/app/app.db` in container)

### Start production stack
```bash
docker compose -f docker-compose.prod.yml up -d
```

### Blue/green workflow
```bash
./deploy/deploy_green.sh <image-tag>
./deploy/switch_traffic.sh green
# rollback if needed
./deploy/rollback.sh
```

### Output retention
Outputs are stored in `/data/out` and cleaned automatically.
Default retention: **7 days**.
Override with env vars:
- `VA_OUT_DIR=/data/out`
- `VA_RETENTION_DAYS=7`
- `VA_CLEANUP_INTERVAL=3600`

## Authentication and Access
- `VA_AUTH_PROVIDER=clerk` enables Clerk login.
- With auth enabled, the main UI is browseable and Build requires login.
- For unauthenticated users, the main action changes to `Login to Build`.
- By default, any successfully authenticated Clerk user can sign in.
- Set `VA_REQUIRE_LOCAL_ALLOWLIST=1` to require membership in the local allowlist table.
- Admin users can manage the local allowlist from `/admin/users`.
- When auth is enabled, build creation enforces:
  - Hourly per-user limit (`VA_RATE_LIMIT_HOURLY`)
  - Daily per-user limit (`VA_RATE_LIMIT_DAILY`)
  - Max active jobs per user (`VA_MAX_ACTIVE_JOBS_PER_USER`)

## Downloading Outputs
- Completed jobs show direct download links in **Recent Jobs**.
- Downloads are authorized per user: users can download only their own jobs, admins can download all jobs.
- Programmatic endpoints:
  - `GET /jobs/<job_id>/artifacts`
  - `GET /jobs/<job_id>/download/<name>`

## Internal Callback Auth
`/internal/worker/jobs/<job_id>/complete` accepts either:
- `X-Worker-Token` if `VA_WORKER_SHARED_TOKEN` is set.
- HMAC headers if configured:
  - `X-Key-Id`
  - `X-Signature`
  - `X-Timestamp`
  - `X-Nonce`

HMAC keys are configured as JSON in `VA_HMAC_KEYS_JSON`, for example:
```json
{"k1":"super-secret-value"}
```

## Outputs
Per run in `./out/<job_id>/` (job id is a hash of center coords + size + time):
- `tile.json`
- `tile.laz`
- `footprints.geojson`
- `buildings.obj`
- `terrain.obj`, `terrain.mtl`, `terrain.png`
- `combined.obj` (if `--combine-output`)
- `combined.mtl` (if `--combine-output` and `naip` output)
- `contours.dxf` (if contours/parcels/exported)
- `README.txt` (run metadata: center coords + size)
- `report.json`
- `dtm.tif`, `dsm.tif`, `ndsm.tif` (only if `--keep-rasters`)
- `tiles_merged.laz` (only if `--allow-multi-tile` and the clip spans tiles)
- `tiles/<tile>.laz` (only if `--allow-multi-tile` and extra tiles are downloaded)

## Notes
- OBJ is unitless. The tile is ~5000 x 5000 in **feet** by default.
- In Rhino, set document units to **Feet** before import. If you must import into mm, scale by **304.8**.
- Use `--units meters` if you want metric output.
- If your clip crosses a tile boundary, add `--allow-multi-tile` to merge adjacent tiles.
- `--naip-flip-u`/`--naip-flip-v` fix mirrored imagery.
- If the geometry is mirrored or rotated, use `--flip-x`, `--flip-y`, and/or `--rotate-z`.
- XYZ output defaults to a uniform grid; use `--xyz-mode contours` for contour sampling.
- `--rotate-z` also rotates DXF/XYZ outputs around the `--center` point (it does not affect `terrain.png`).
- `terrain.xyz` defaults to contour vertices; use `--xyz-mode grid` for a full grid and
  `--xyz-contour-spacing` to resample along contours.
- Use `--dxf-contour-spacing` to resample DXF contour vertices.
- `--outputs` controls which outputs are generated: `buildings`, `terrain`, `contours`, `parcels`, `naip`, `xyz`.

## Parcel Sources
Parcel boundaries are pulled from public ArcGIS FeatureServer layers listed in
`src/va_lidar_context/parcels/sources.json`. The resolver picks the first source
whose `coverage` bbox intersects the requested clip area.

### Add a Parcel Source
1. Find a public ArcGIS FeatureServer layer that serves parcel polygons.
2. Add a new entry to `src/va_lidar_context/parcels/sources.json`.
3. Set a `coverage` bbox in WGS84 (lon/lat) so we only hit that source in-region.

### Find Parcel Layers (Quick Checklist)
1. Locate the GIS server root: `https://<domain>/arcgis/rest/services`
2. Open it in a browser and search for folders/services named `Parcels`, `Cadastre`,
   `TaxParcel`, or `Assessment`.
3. Click a promising service, then open the `FeatureServer` (or `MapServer`) layer list.
4. Use the layer’s `/query` endpoint as `query_url`, for example:
   `.../FeatureServer/0/query`
5. Confirm the layer returns polygons in GeoJSON by loading `?f=pjson` and
   checking `geometryType` (should be `esriGeometryPolygon`) and
   `supportsPagination`/`maxRecordCount` for paging.

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
