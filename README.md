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
Each build also writes per-footprint height attributes to
`building_heights.geojson` and `building_heights.csv` (with QC fields).

## Web App

```bash
va-lidar-context-web
```

Opens at `http://127.0.0.1:5000`. To bind to all interfaces:

```bash
va-lidar-context-web --host 0.0.0.0 --port 8000
```

Default first-load form values are preconfigured to Grand Canyon:
- Center: `36.09841234052352, -112.0952885242688`
- Size: `3000` feet
- Satellite image (NAIP): enabled

To preload the matching first-load preview artifacts for live deployments:

```bash
python3 scripts/preload_grand_canyon_default.py --out ./out
```

The web UI will auto-seed this preloaded job from `./out/grand-canyon-default/`
for users with no existing jobs.

## Docker

**Production (Caddy + TLS + blue/green):**
```bash
# 1) Point your DNS A record to the droplet public IPv4 first.
#    Example: meshd.xyz -> 134.209.42.153

# 2) Create deployment env file.
cp .env.example .env
# edit .env and set APP_DOMAIN, ACME_EMAIL, VA_SESSION_SECRET
# generate a secret with: python3 -c "import secrets; print(secrets.token_hex(32))"

# 3) Prepare persistent volumes for the app container user (uid 10001).
mkdir -p /data/out /data/app
chown -R 10001:10001 /data/out /data/app

# 4) Validate env + compose + DNS before startup.
./deploy/preflight.sh

# 5) Start stack.
docker compose up -d --build
```
App is served through Caddy on `http://<host>/` (and `https://<domain>/` when DNS + ACME are configured).

Quick checks:
```bash
docker compose ps
docker compose logs --since=10m caddy
curl -I http://$APP_DOMAIN
curl -I https://$APP_DOMAIN
```

If you use `docker compose logs -f ...`, it will stream continuously until you stop it with `Ctrl+C`.

Blue/green deploy:
```bash
./deploy/deploy_green.sh <image-tag>
./deploy/switch_traffic.sh green
./deploy/rollback.sh   # if needed
```

See [DOCUMENTATION.md](docs/DOCUMENTATION.md) for all CLI flags, environment variables, auth configuration, output file reference, and parcel source setup.
