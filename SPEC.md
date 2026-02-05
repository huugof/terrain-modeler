Project spec: va-lidar-context CLI
Goal

Given a VGIN/USGS tile name (e.g. S13_4899_20), the CLI will:

resolve tile metadata + point cloud download URL

download the LAZ point cloud

download matching Virginia Building Footprints polygons

generate a context building mesh by extruding footprints using LiDAR-derived heights (fallback to footprint attributes)

export mesh to a standard format (OBJ default)

Inputs and outputs
Input

tile_name: S13_4899_20 (string)

Outputs (per tile)

tile.json (resolved metadata, URLs, bbox)

tile.laz (downloaded point cloud)

footprints.geojson (building footprints clipped to tile extent)

dtm.tif, dsm.tif, ndsm.tif (optional intermediate rasters)

buildings.obj (final extruded mesh)

report.json (counts, height stats, warnings)

External data sources
A) VGIN LiDAR Download Tile Grid (tile → LAZ URL + tile geometry)

REST layer (MapServer layer 1):

https://vginmaps.vdem.virginia.gov/arcgis/rest/services/Download/Virginia_LiDAR_Downloads/MapServer/1

Key fields (confirmable in layer metadata):

TileName, PointCloudDownload, VComment, ProjectYear, etc.

Supports JSON, geoJSON, PBF, MaxRecordCount=2000

B) VGIN Virginia Building Footprints (polygons + optional height/stories attributes)

FeatureServer root:

https://vginmaps.vdem.virginia.gov/arcgis/rest/services/VA_Base_Layers/VA_Building_Footprints/FeatureServer

Layer 0:

https://vginmaps.vdem.virginia.gov/arcgis/rest/services/VA_Base_Layers/VA_Building_Footprints/FeatureServer/0

Supported query formats: JSON, geoJSON, PBF

Useful fields:

BLDGHEIGHT, NUMSTORIES, BUILDINGCLASS, MUNICIPALITY, etc.

MaxRecordCount=2000 (requires pagination)

Coordinate systems

Both VGIN services report native spatial reference in Web Mercator (WKID 102100 / EPSG:3857).

For querying, use outSR=4326 to simplify bbox operations.

For overlay with LAZ, always read LAZ CRS from the file and reproject footprints into that CRS before raster sampling/extrusion.

Functional requirements
Tile resolution

Query tile grid by TileName and prefer VComment='Current' when present:

where=TileName='<tile>' AND VComment='Current'

Extract:

LAZ URL from the PointCloudDownload HTML string (href="...")

tile polygon geometry (returnGeometry=true)

derive WGS84 bbox (xmin/ymin/xmax/ymax)

Footprints download

Query building footprints by tile bbox (WGS84 envelope):

geometry=<xmin>,<ymin>,<xmax>,<ymax>

geometryType=esriGeometryEnvelope

spatialRel=esriSpatialRelIntersects

returnGeometry=true

f=geojson

Paginate using resultRecordCount=2000 and resultOffset=0,2000,4000,... until 0 features returned.

Edge case: clip spillover across tile boundaries

If a clip bbox extends beyond the selected tile bbox, current behavior still uses one tile only.
Rasters are clipped to the tile extent; footprints outside may have no raster samples and are dropped
or use fallback heights (warnings recorded in report.json).

Proposed multi-tile spillover handling (optional):
Detect spillover by comparing clip bbox to tile bbox.
Query tile grid by bbox (esriGeometryEnvelope, intersects) to get all intersecting tiles.
Download all LAZ files and merge with PDAL (filters.merge; reproject to a common CRS if needed).
Run DTM/DSM/nDSM on merged LAZ, then clip to requested size as usual.
Optionally gate behind --allow-multi-tile and record tiles used in report.json.

Height model (trees + buildings are class 1 in LAZ)

Use LiDAR only for surface height, not classification separation:

DTM: Classification==2 (ground)

DSM: Classification!=2 (everything above ground: trees+buildings)

nDSM = DSM − DTM

For each footprint polygon:

sample nDSM values inside polygon

choose height = P95 (configurable P90–P95)

clamp (e.g., 8–300 ft)

Fallbacks (if no samples inside polygon):

BLDGHEIGHT (if present)

NUMSTORIES * floor_to_floor_ft (default 10 ft)

skip building (log warning)

Mesh generation

Extrude each footprint polygon by computed height

Merge all extrusions into one mesh

Export:

OBJ (default)

optional GLB (if you add a GLTF exporter path)

Non-functional requirements

Deterministic output folder structure per tile

Caching:

don’t re-download LAZ/footprints if present unless --force

Logging:

progress per stage

warnings for missing tile, empty footprints, empty height samples, etc.

Performance:

keep rasters coarse enough for context (default resolution ~1.0 in LAZ linear units)

avoid per-point operations; use rasterization + polygon sampling

CLI design
Command

va-lidar-context build S13_4899_20 [options]

Options

--out <dir> (default ./out)

--force (re-download and regenerate)

--format obj|glb (default obj)

--units feet|meters (default feet, affects output scaling and clamps)

--resolution <float> (default 1.0)

--percentile 90|95 (default 95)

--min-height <float> (default 8)

--max-height <float> (default 300)

--floor-to-floor <float> (default 10)

--keep-rasters (default true or false, your call)

REST query templates
1) Tile lookup (tile → LAZ URL + geometry)

Endpoint:

.../Virginia_LiDAR_Downloads/MapServer/1/query

Example query params:

where=TileName='S13_4899_20' AND VComment='Current'

outFields=TileName,PointCloudDownload,VComment,ProjectYear

returnGeometry=true

outSR=4326

f=json

2) Footprints by bbox (tile bbox → footprints GeoJSON)

Endpoint:

.../VA_Building_Footprints/FeatureServer/0/query

Example query params:

where=1=1

geometry=<xmin>,<ymin>,<xmax>,<ymax>

geometryType=esriGeometryEnvelope

inSR=4326

spatialRel=esriSpatialRelIntersects

outFields=OBJECTID,BLDGHEIGHT,NUMSTORIES,BUILDINGCLASS,MUNICIPALITY

returnGeometry=true

outSR=4326

f=geojson

resultRecordCount=2000

resultOffset=0 (paginate)

Implementation plan
Phase 0: project scaffolding

Create repo + packaging (recommended: uv or pip-tools)

Choose CLI framework:

minimal: argparse

nicer: typer

Phase 1: data acquisition

Implement tile_lookup(tile_name) -> {laz_url, tile_polygon_wgs84, bbox_wgs84, attrs}

Implement download_file(url, dest, cache=True)

Implement fetch_footprints_geojson(bbox_wgs84) -> GeoJSON with pagination

Phase 2: LiDAR surfaces (PDAL)

Install dependency note:

PDAL binary via Homebrew

Python calls PDAL via subprocess (pdal pipeline)

Implement:

make_dtm(laz, dtm.tif) using Classification==2

make_dsm(laz, dsm.tif) using Classification!=2 and output_type=max

make_ndsm(dsm, dtm, ndsm.tif)

Phase 3: heights + extrusion

Reproject footprints from WGS84 to LAZ CRS (read from LAZ)

For each polygon:

sample nDSM raster values (mask + percentile)

apply fallbacks from attributes

Extrude polygons to meshes and merge

Phase 4: export + reporting

Export mesh to OBJ (and optionally GLB)

Write report.json:

number of footprints fetched

number extruded

percentile used

average/median/min/max heights

count of fallback heights used

warnings

Suggested repo structure

src/va_lidar_context/

cli.py

vgin_tile.py (tile grid queries + parsing PointCloudDownload href)

vgin_footprints.py (bbox queries + pagination)

pdal_surfaces.py (DTM/DSM/nDSM pipelines)

heights.py (sampling + fallbacks + unit conversion)

mesh.py (extrusion + merge + export)

util.py (http, caching, logging)

tests/ (start with parsing + bbox + pagination unit tests)

pyproject.toml

Dependencies (practical)

Python:

requests (HTTP)

shapely, geopandas, pyproj (geometry + reprojection)

rasterio, numpy (raster sampling + math)

trimesh (extrusion + export)

System:

pdal (for LAZ rasterization)

gdal/geos (often required by geopandas stack)

Acceptance criteria

Running va-lidar-context build S13_4899_20:

downloads LAZ via the URL returned by tile grid

downloads building footprints that overlay the tile extent

produces buildings.obj with nonzero number of extrusions

produces report.json with counts and basic height stats

Heights look plausible (spot check 3–5 buildings):

not near-zero

not canopy-driven spikes

consistent scale (feet)

Known risks / mitigations

Footprints query returns >2000 features: must paginate (resultOffset).

Tile name returns multiple records: filter VComment='Current' or pick max ProjectYear.

LAZ CRS missing/odd: fall back to keeping everything in 4326 for footprints download, but require LAZ CRS for final overlay (hard-fail with clear message).

DSM polluted by trees: percentile sampling + footprint masking is the primary mitigation; clamp heights.

If you want this to be “single command, zero manual install surprises” on macOS, the next step is defining the install doc for PDAL/GDAL + the Python env (one page), and deciding whether you want OBJ only or GLB as well.
