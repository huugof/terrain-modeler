from __future__ import annotations

import json
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple
from urllib.parse import urlparse

import laspy
import requests
from pyproj import CRS, Transformer

from ..util import ensure_dir


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
                logger.warning(
                    f"Failed to fetch LAZ list (attempt {attempt}/{retries}): {exc}"
                )
            if attempt < retries:
                import time

                time.sleep(backoff * attempt)

    if last_exc:
        raise last_exc
    return []


def _extract_wkt(metadata: Dict[str, Any]) -> str | None:
    parsed = metadata.get("parsed_crs")
    if parsed is not None:
        try:
            return parsed.to_wkt()
        except Exception:
            pass
    vlr_text = metadata.get("vlr_wkt")
    if isinstance(vlr_text, str) and vlr_text.strip():
        return vlr_text.strip()
    return None


def _header_metadata(url: str) -> Dict[str, Any]:
    suffix = Path(urlparse(url).path).suffix or ".laz"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        with requests.get(url, stream=True, timeout=180) as resp:
            resp.raise_for_status()
            with tmp_path.open("wb") as out:
                for chunk in resp.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        out.write(chunk)
        with laspy.open(tmp_path) as reader:
            header = reader.header
            metadata: Dict[str, Any] = {
                "minx": float(header.mins[0]),
                "miny": float(header.mins[1]),
                "maxx": float(header.maxs[0]),
                "maxy": float(header.maxs[1]),
                "parsed_crs": header.parse_crs(),
            }
            for vlr in header.vlrs:
                if getattr(vlr, "string", None):
                    text = str(vlr.string).strip()
                    if text:
                        metadata["vlr_wkt"] = text
                        break
                raw = getattr(vlr, "record_data", None)
                if isinstance(raw, bytes):
                    text = raw.decode("utf-8", errors="ignore").strip()
                    if text and (
                        "GEOGCS" in text or "PROJCRS" in text or "COMPD_CS" in text
                    ):
                        metadata["vlr_wkt"] = text
                        break
            return metadata
    finally:
        tmp_path.unlink(missing_ok=True)


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
        md = _header_metadata(url)
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
