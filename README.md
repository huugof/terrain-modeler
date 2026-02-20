# va-lidar-context

Generate 3D terrain and building meshes from LiDAR data. Outputs OBJ files (terrain, buildings, combined), DXF contours, parcel overlays, and NAIP aerial imagery. Works with Virginia state LiDAR or national USGS 3DEP coverage.

## Setup

**macOS:**
```bash
brew install pdal gdal geos proj
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
```

**Ubuntu:**
```bash
sudo apt update && sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable
sudo apt update && sudo apt install -y pdal gdal-bin libgdal-dev libgeos-dev proj-bin
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
```

## CLI

Build by tile ID (Virginia):
```bash
va-lidar-context build S13_4899_20 \
  --out ./out \
  --outputs buildings,terrain,naip \
  --terrain-sample 10 \
  --random-heights 15 40 \
  --fill-dtm --fill-hard \
  --naip-flip-v \
  --combine-output
```

Build by coordinates (500 ft clip, any provider):
```bash
va-lidar-context build \
  --center 38.0334 -78.4645 \
  --size 500 \
  --out ./out \
  --outputs buildings,terrain,contours,parcels \
  --terrain-sample 10 \
  --random-heights 15 40 \
  --fill-dtm --fill-hard \
  --contours 2 \
  --allow-multi-tile \
  --combine-output
```

National mode (USGS 3DEP + Microsoft footprints):
```bash
va-lidar-context build \
  --provider national --ept-only \
  --center 38.0334 -78.4645 \
  --size 500 \
  --out ./out
```

`--center` takes `lat lon` (Google Maps order). Outputs land in `./out/<job_id>/`.

## Web App

```bash
va-lidar-context-web
```

Opens at `http://127.0.0.1:5000`. To bind to all interfaces:

```bash
va-lidar-context-web --host 0.0.0.0 --port 8000
```

## Docker

**Dev / local:**
```bash
mkdir -p /data/out
docker compose up -d --build
```
App runs on `http://localhost:8000`.

**Production (Caddy + TLS + blue/green):**
```bash
# Required env vars: APP_DOMAIN, ACME_EMAIL, APP_IMAGE, VA_SESSION_SECRET
docker compose -f docker-compose.prod.yml up -d
```

Blue/green deploy:
```bash
./deploy/deploy_green.sh <image-tag>
./deploy/switch_traffic.sh green
./deploy/rollback.sh   # if needed
```

See [DOCUMENTATION.md](docs/DOCUMENTATION.md) for all CLI flags, environment variables, auth configuration, output file reference, and parcel source setup.
