"""Provider for Microsoft Global ML Building Footprints with height estimates.

Tiles are organized by Bing Maps quadkey at zoom 9. Each tile is a
gzip-compressed newline-delimited GeoJSON file (.csv.gz) containing building
polygons with a ``height`` property in metres (-1 means no height estimate).

Tile URLs are looked up from a published index CSV. The index is cached locally
for 7 days. Individual tiles are cached permanently — they are large (up to
~100 MB for dense cities) and change infrequently.
"""
from __future__ import annotations

import csv
import gzip
import hashlib
import io
import json
import math
import threading
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests

from ..constants import MS_GLOBAL_BUILDINGS_INDEX_URL

_INDEX_TTL_SECONDS = 7 * 86400

_index_lock = threading.Lock()
_index_cache: Optional[Dict[str, str]] = None  # quadkey → tile URL


# ---------------------------------------------------------------------------
# Quadkey helpers
# ---------------------------------------------------------------------------

def _lat_lon_to_quadkey(lat: float, lon: float, zoom: int = 9) -> str:
    x = int((lon + 180) / 360 * (2 ** zoom))
    lat_rad = math.radians(lat)
    y = int(
        (1 - math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi)
        / 2
        * (2 ** zoom)
    )
    qk = ""
    for i in range(zoom, 0, -1):
        digit = 0
        mask = 1 << (i - 1)
        if x & mask:
            digit += 1
        if y & mask:
            digit += 2
        qk += str(digit)
    return qk


def _bbox_quadkeys(bbox: Tuple[float, float, float, float], zoom: int = 9) -> List[str]:
    """Return unique quadkeys covering all corners + centre of the bbox."""
    xmin, ymin, xmax, ymax = bbox
    candidates = [
        (ymin, xmin), (ymin, xmax),
        (ymax, xmin), (ymax, xmax),
        ((ymin + ymax) / 2, (xmin + xmax) / 2),
    ]
    seen: set[str] = set()
    result: List[str] = []
    for lat, lon in candidates:
        qk = _lat_lon_to_quadkey(lat, lon, zoom)
        if qk not in seen:
            seen.add(qk)
            result.append(qk)
    return result


# ---------------------------------------------------------------------------
# Index CSV
# ---------------------------------------------------------------------------

def _load_index(cache_dir: Path) -> Dict[str, str]:
    """Return the quadkey→url mapping. Thread-safe; cached in-process and on disk."""
    global _index_cache
    with _index_lock:
        if _index_cache is not None:
            return _index_cache

        index_path = cache_dir / "_cache" / "ms_buildings" / "index.csv"
        index_path.parent.mkdir(parents=True, exist_ok=True)

        stale = (
            not index_path.exists()
            or (time.time() - index_path.stat().st_mtime) > _INDEX_TTL_SECONDS
        )
        if stale:
            resp = requests.get(MS_GLOBAL_BUILDINGS_INDEX_URL, timeout=60)
            resp.raise_for_status()
            index_path.write_bytes(resp.content)

        text = index_path.read_text(encoding="utf-8-sig")
        reader = csv.DictReader(io.StringIO(text))
        _index_cache = {row["QuadKey"]: row["Url"] for row in reader}
        return _index_cache


# ---------------------------------------------------------------------------
# Tile download & filtering
# ---------------------------------------------------------------------------

def _download_tile(quadkey: str, url: str, cache_dir: Path) -> Path:
    """Download and cache a tile. Returns path to the cached .csv.gz file."""
    tile_path = cache_dir / "_cache" / "ms_buildings" / f"{quadkey}.csv.gz"
    if not tile_path.exists():
        tile_path.parent.mkdir(parents=True, exist_ok=True)
        with requests.get(url, timeout=300, stream=True) as resp:
            resp.raise_for_status()
            with tile_path.open("wb") as fh:
                for chunk in resp.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        fh.write(chunk)
    return tile_path


def _filter_tile(
    tile_path: Path,
    bbox: Tuple[float, float, float, float],
) -> List[Dict[str, Any]]:
    """Stream-decompress a tile and return features whose footprint intersects bbox."""
    xmin, ymin, xmax, ymax = bbox
    features: List[Dict[str, Any]] = []
    with gzip.open(tile_path, "rt", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                feature = json.loads(line)
            except json.JSONDecodeError:
                continue
            coords = feature.get("geometry", {}).get("coordinates")
            if not coords:
                continue
            ring = coords[0]
            if any(xmin <= v[0] <= xmax and ymin <= v[1] <= ymax for v in ring):
                features.append(feature)
    return features


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def fetch_buildings_with_heights(
    bbox_wgs84: Tuple[float, float, float, float],
    cache_dir: Path,
) -> Dict[str, Any]:
    """Return a GeoJSON FeatureCollection of buildings within *bbox_wgs84*.

    Each feature has ``properties.height_m`` (float metres) or ``None`` when
    the dataset has no height estimate for that building.  Results are cached
    per bbox to avoid re-decompressing large tile files on repeated calls.
    """
    xmin, ymin, xmax, ymax = bbox_wgs84
    bbox_key = hashlib.md5(
        f"{xmin:.6f}_{ymin:.6f}_{xmax:.6f}_{ymax:.6f}".encode()
    ).hexdigest()
    filtered_path = (
        cache_dir / "_cache" / "ms_buildings_filtered" / f"{bbox_key}.geojson.gz"
    )

    if filtered_path.exists():
        with gzip.open(filtered_path, "rt", encoding="utf-8") as fh:
            return json.loads(fh.read())

    index = _load_index(cache_dir)
    quadkeys = _bbox_quadkeys(bbox_wgs84)

    raw_features: List[Dict[str, Any]] = []
    for qk in quadkeys:
        if qk not in index:
            continue
        tile_path = _download_tile(qk, index[qk], cache_dir)
        raw_features.extend(_filter_tile(tile_path, bbox_wgs84))

    features = [
        {
            "type": "Feature",
            "geometry": f["geometry"],
            "properties": {
                "height_m": (
                    h if (h := f.get("properties", {}).get("height")) is not None
                    and h > 0
                    else None
                ),
            },
        }
        for f in raw_features
    ]

    result: Dict[str, Any] = {"type": "FeatureCollection", "features": features}

    filtered_path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(filtered_path, "wt", encoding="utf-8") as fh:
        fh.write(json.dumps(result))

    return result
