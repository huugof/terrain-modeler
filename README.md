# va-lidar-context

CLI to build context building meshes from Virginia LiDAR and building footprints.

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

## Outputs
Per tile in `./out/<tile_name>/`:
- `tile.json`
- `tile.laz`
- `footprints.geojson`
- `buildings.obj`
- `terrain.obj`, `terrain.mtl`, `terrain.png`
- `scene.obj` (if `--combine-output`)
- `scene.mtl` (if `--combine-output` and `--naip-texture`)
- `trees.obj`
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
