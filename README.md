# va-lidar-context

CLI to build context building meshes from Virginia LiDAR and building footprints, with optional national USGS 3DEP support.

**Primary example (current default workflow):**
```bash
va-lidar-context build S13_4899_20 \
  --out ./out \
  --terrain-sample 10 \
  --random-heights 15 40 \
  --fill-dtm --fill-hard \
  --naip-texture --naip-flip-v \
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
  --naip-texture \
  --combine-output \
  --contours 2 \
  --parcels \
  --resolution 0.5
```

**National mode (USGS 3DEP LiDAR + Microsoft building footprints):**
```bash
va-lidar-context build \
  --provider national \
  --ept-only \
  --center 38.03344644806424 -78.46451371473545 \
  --size 500 \
  --out ./out \
  --resolution 1
```

Parcels are resolved from a small registry of public parcel sources in
`src/va_lidar_context/parcels/sources.json`. If no source matches the clip area,
parcels are skipped and the web UI shows an alert when Parcels is checked.
Use `--ept-only` if the USGS LAZ host is unreachable (will fail if EPT is missing).

If you only have lat/lon order, use:
```
--center-latlon 38.0275 -78.4662
```

## Requirements
- macOS
- Python 3.11+
- Homebrew
- System deps: `pdal`, `gdal`, `geos`, `proj`
- Python deps installed via `pip install -e .` (includes `mapbox-earcut`)

## Setup
```bash
brew install pdal gdal geos proj
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Run
```bash
va-lidar-context build S13_4899_20 \
  --out ./out \
  --terrain-sample 10 \
  --random-heights 15 40 \
  --fill-dtm --fill-hard \
  --naip-texture --naip-flip-v \
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


## Deploy (DigitalOcean)
**Recommended**: Docker on a small Ubuntu droplet.

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

### Output retention
Outputs are stored in `/data/out` and cleaned automatically.
Default retention: **7 days**.
Override with env vars:
- `VA_OUT_DIR=/data/out`
- `VA_RETENTION_DAYS=7`
- `VA_CLEANUP_INTERVAL=3600`

## Outputs
Per run in `./out/<job_id>/` (job id is a hash of center coords + size + time):
- `tile.json`
- `tile.laz`
- `footprints.geojson`
- `buildings.obj`
- `terrain.obj`, `terrain.mtl`, `terrain.png`
- `combined.obj` (if `--combine-output`)
- `combined.mtl` (if `--combine-output` and `--naip-texture`)
- `contours.dxf` (if contours/parcels/exported)
- `trees.obj`
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
- Tree blobs are derived from LAZ **classification 1**.

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
