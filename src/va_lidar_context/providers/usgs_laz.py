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


def _metadata_from_local_laz(path: Path) -> Dict[str, Any]:
    with laspy.open(path) as reader:
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


def _download_laz_header_bytes(
    url: str, *, max_bytes: int = 256 * 1024, timeout: int = 180
) -> bytes:
    headers = {"Range": f"bytes=0-{max_bytes - 1}"}
    with requests.get(url, headers=headers, stream=True, timeout=timeout) as resp:
        resp.raise_for_status()
        chunks: List[bytes] = []
        total = 0
        for chunk in resp.iter_content(chunk_size=64 * 1024):
            if not chunk:
                continue
            remaining = max_bytes - total
            if remaining <= 0:
                break
            piece = chunk[:remaining]
            chunks.append(piece)
            total += len(piece)
            if total >= max_bytes:
                break
    return b"".join(chunks)


def _header_metadata(url: str, *, allow_full_fallback: bool = True) -> Dict[str, Any]:
    suffix = Path(urlparse(url).path).suffix or ".laz"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        # Fast path: fetch only the leading bytes where LAS header + VLRs live.
        for max_bytes in (256 * 1024, 1024 * 1024, 4 * 1024 * 1024):
            try:
                header_bytes = _download_laz_header_bytes(url, max_bytes=max_bytes)
                if not header_bytes:
                    continue
                tmp_path.write_bytes(header_bytes)
                metadata = _metadata_from_local_laz(tmp_path)
                if _extract_wkt(metadata):
                    return metadata
            except Exception:
                continue

        if not allow_full_fallback:
            raise ValueError("CRS not found in LAZ header bytes")

        # Fallback: fetch full file for datasets that don't expose CRS up front.
        with requests.get(url, stream=True, timeout=180) as resp:
            resp.raise_for_status()
            with tmp_path.open("wb") as out:
                for chunk in resp.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        out.write(chunk)
        return _metadata_from_local_laz(tmp_path)
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
    allow_full_fallback: bool = True,
    logger=None,
) -> List[LazTileInfo]:
    """Build or load a cached LAZ tile index with bbox metadata."""
    if cache_path.exists() and not force:
        return _load_index(cache_path)

    ensure_dir(cache_path.parent)

    tiles: List[LazTileInfo] = []
    failures = 0
    total = len(laz_urls)
    for idx, url in enumerate(laz_urls, start=1):
        if logger and (idx == 1 or idx == total or idx % 10 == 0):
            logger.info(f"Indexing LAZ metadata {idx}/{len(laz_urls)}")
        try:
            md = _header_metadata(url, allow_full_fallback=allow_full_fallback)
            crs_wkt = _extract_wkt(md)
            if not crs_wkt:
                continue
            bounds = (md.get("minx"), md.get("miny"), md.get("maxx"), md.get("maxy"))
            if any(v is None for v in bounds):
                continue
            bbox_wgs84 = _bbox_to_wgs84(bounds, crs_wkt)
            tiles.append(LazTileInfo(url=url, bbox_wgs84=bbox_wgs84, crs_wkt=crs_wkt))
        except Exception as exc:
            failures += 1
            if logger:
                logger.warning(f"Skipping LAZ metadata {idx}/{total}: {exc}")
            continue

    _save_index(cache_path, tiles)
    if logger and failures:
        logger.warning(
            f"LAZ metadata index completed with {failures} skipped file(s); "
            f"indexed {len(tiles)}/{total} files"
        )
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
