from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Tuple

import requests
from pyproj import CRS, Transformer

USGS_3DEP_URL = (
    "https://elevation.nationalmap.gov/arcgis/rest/services/"
    "3DEPElevation/ImageServer/exportImage"
)


def _utm_epsg(lat: float, lon: float) -> int:
    zone = int((lon + 180) / 6) + 1
    return 32600 + zone if lat >= 0 else 32700 + zone


def fetch_dtm(
    bbox_wgs84: Tuple[float, float, float, float],
    cache_dir: Path,
    resolution: float = 1.0,
) -> Tuple[Path, CRS]:
    """Fetch a DTM GeoTIFF from USGS 3DEP for the given WGS84 bbox.

    Results are cached by bbox + resolution. Returns (path, utm_crs).
    """
    xmin, ymin, xmax, ymax = bbox_wgs84
    lat = (ymin + ymax) / 2.0
    lon = (xmin + xmax) / 2.0
    epsg = _utm_epsg(lat, lon)
    utm_crs = CRS.from_epsg(epsg)

    to_utm = Transformer.from_crs("EPSG:4326", utm_crs, always_xy=True)
    x1, y1 = to_utm.transform(xmin, ymin)
    x2, y2 = to_utm.transform(xmax, ymax)
    utm_xmin = min(x1, x2)
    utm_xmax = max(x1, x2)
    utm_ymin = min(y1, y2)
    utm_ymax = max(y1, y2)

    width_m = utm_xmax - utm_xmin
    height_m = utm_ymax - utm_ymin
    width_px = max(1, int(width_m / resolution))
    height_px = max(1, int(height_m / resolution))

    key = hashlib.md5(
        f"{xmin:.6f}_{ymin:.6f}_{xmax:.6f}_{ymax:.6f}_{resolution:.4f}_{epsg}".encode()
    ).hexdigest()
    cache_path = cache_dir / "_cache" / "3dep" / f"{key}.tif"

    if not cache_path.exists():
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        params = {
            "bbox": f"{utm_xmin},{utm_ymin},{utm_xmax},{utm_ymax}",
            "bboxSR": str(epsg),
            "size": f"{width_px},{height_px}",
            "imageSR": str(epsg),
            "format": "tiff",
            "pixelType": "F32",
            "noData": "-9999",
            "f": "image",
        }
        with requests.get(USGS_3DEP_URL, params=params, timeout=180, stream=True) as resp:
            resp.raise_for_status()
            content_type = resp.headers.get("Content-Type", "").lower()
            if "image" not in content_type and "tiff" not in content_type:
                text = resp.text[:400]
                raise RuntimeError(
                    f"3DEP exportImage returned non-image response: {content_type!r} {text}"
                )
            with cache_path.open("wb") as f:
                for chunk in resp.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)

    return cache_path, utm_crs


ESRI_IMAGERY_URL = (
    "https://server.arcgisonline.com/arcgis/rest/services/"
    "World_Imagery/MapServer/export"
)


def fetch_satellite(
    bbox_wgs84: Tuple[float, float, float, float],
    cache_dir: Path,
    px: int = 256,
) -> Path:
    """Fetch a satellite PNG from ESRI World Imagery for the given WGS84 bbox.

    Results are cached by bbox + px size. Returns path to cached PNG.
    """
    xmin, ymin, xmax, ymax = bbox_wgs84
    key = hashlib.md5(
        f"{xmin:.6f}_{ymin:.6f}_{xmax:.6f}_{ymax:.6f}_{px}".encode()
    ).hexdigest()
    cache_path = cache_dir / "_cache" / "satellite" / f"{key}.png"

    if not cache_path.exists():
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        params = {
            "bbox": f"{xmin},{ymin},{xmax},{ymax}",
            "bboxSR": "4326",
            "size": f"{px},{px}",
            "format": "png",
            "f": "image",
        }
        with requests.get(ESRI_IMAGERY_URL, params=params, timeout=60, stream=True) as resp:
            resp.raise_for_status()
            content_type = resp.headers.get("Content-Type", "").lower()
            if "image" not in content_type and "png" not in content_type:
                text = resp.text[:400]
                raise RuntimeError(
                    f"ESRI imagery returned non-image response: {content_type!r} {text}"
                )
            with cache_path.open("wb") as f:
                for chunk in resp.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)

    return cache_path
