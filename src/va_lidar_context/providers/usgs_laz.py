from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import requests
from pyproj import CRS, Transformer

from ..util import ensure_dir, require_https_url, run_subprocess


@dataclass(frozen=True)
class LazTileInfo:
    url: str
    bbox_wgs84: Tuple[float, float, float, float]
    crs_wkt: str


def _download_links_url(lpc_link: str) -> str:
    return lpc_link.rstrip("/") + "/0_file_download_links.txt"


def list_laz_urls(
    lpc_link: str,
    *,
    timeout: int = 60,
    retries: int = 3,
    backoff: float = 2.0,
    logger=None,
) -> List[str]:
    """List LAZ/ LAS URLs from a USGS LPC link."""
    require_https_url(lpc_link)
    url = _download_links_url(lpc_link)
    last_exc: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
            urls = []
            for line in resp.text.splitlines():
                line = line.strip()
                if not line:
                    continue
                if line.lower().endswith(".laz") or line.lower().endswith(".las"):
                    urls.append(line)
            return urls
        except requests.RequestException as exc:
            last_exc = exc
            if logger:
                logger.warning(f"Failed to fetch LAZ list (attempt {attempt}/{retries}): {exc}")
            if attempt < retries:
                import time

                time.sleep(backoff * attempt)

    if last_exc:
        raise last_exc
    return []


def _extract_wkt(metadata: Dict[str, Any]) -> str | None:
    if metadata.get("comp_spatialreference"):
        return metadata.get("comp_spatialreference")
    if metadata.get("spatialreference"):
        return metadata.get("spatialreference")
    srs = metadata.get("srs")
    if isinstance(srs, dict):
        return srs.get("wkt") or srs.get("proj4")
    if isinstance(srs, str):
        return srs
    return None


def _pdal_info(url: str) -> Dict[str, Any]:
    require_https_url(url)
    proc = run_subprocess(
        ["pdal", "info", "--metadata", url],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(proc.stdout)


def _bbox_to_wgs84(
    bounds: Tuple[float, float, float, float],
    crs_wkt: str,
) -> Tuple[float, float, float, float]:
    crs = CRS.from_wkt(crs_wkt)
    transformer = Transformer.from_crs(crs, "EPSG:4326", always_xy=True)
    minx, miny, maxx, maxy = bounds
    corners = [
        (minx, miny),
        (minx, maxy),
        (maxx, miny),
        (maxx, maxy),
    ]
    xs = []
    ys = []
    for x, y in corners:
        lon, lat = transformer.transform(x, y)
        xs.append(lon)
        ys.append(lat)
    return (min(xs), min(ys), max(xs), max(ys))


def _load_index(path: Path) -> List[LazTileInfo]:
    data = json.loads(path.read_text())
    items = []
    for entry in data.get("tiles", []):
        items.append(
            LazTileInfo(
                url=entry["url"],
                bbox_wgs84=tuple(entry["bbox_wgs84"]),
                crs_wkt=entry["crs_wkt"],
            )
        )
    return items


def _save_index(path: Path, tiles: Iterable[LazTileInfo]) -> None:
    payload = {
        "tiles": [
            {
                "url": t.url,
                "bbox_wgs84": list(t.bbox_wgs84),
                "crs_wkt": t.crs_wkt,
            }
            for t in tiles
        ]
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True))


def build_laz_index(
    laz_urls: List[str],
    cache_path: Path,
    *,
    force: bool = False,
    logger=None,
) -> List[LazTileInfo]:
    """Build or load a cached LAZ tile index with bbox metadata."""
    if cache_path.exists() and not force:
        return _load_index(cache_path)

    ensure_dir(cache_path.parent)

    tiles: List[LazTileInfo] = []
    for idx, url in enumerate(laz_urls, start=1):
        if logger:
            logger.info(f"Indexing LAZ metadata {idx}/{len(laz_urls)}")
        data = _pdal_info(url)
        md = data.get("metadata", {})
        crs_wkt = _extract_wkt(md)
        if not crs_wkt:
            continue
        bounds = (md.get("minx"), md.get("miny"), md.get("maxx"), md.get("maxy"))
        if any(v is None for v in bounds):
            continue
        bbox_wgs84 = _bbox_to_wgs84(bounds, crs_wkt)
        tiles.append(LazTileInfo(url=url, bbox_wgs84=bbox_wgs84, crs_wkt=crs_wkt))

    _save_index(cache_path, tiles)
    return tiles


def _bbox_intersects(
    a: Tuple[float, float, float, float], b: Tuple[float, float, float, float]
) -> bool:
    return not (a[2] < b[0] or a[0] > b[2] or a[3] < b[1] or a[1] > b[3])


def select_laz_tiles(
    tiles: List[LazTileInfo],
    bbox_wgs84: Tuple[float, float, float, float],
) -> List[LazTileInfo]:
    """Select LAZ tiles that intersect a bbox."""
    return [t for t in tiles if _bbox_intersects(t.bbox_wgs84, bbox_wgs84)]
