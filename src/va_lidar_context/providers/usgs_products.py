from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

from ..constants import USGS_TNM_PRODUCTS_API
from ..util import http_get_json


def _bbox_tuple(raw: Dict[str, Any]) -> Optional[Tuple[float, float, float, float]]:
    try:
        minx = float(raw["minX"])
        miny = float(raw["minY"])
        maxx = float(raw["maxX"])
        maxy = float(raw["maxY"])
        return (minx, miny, maxx, maxy)
    except Exception:
        return None


def query_laz_for_bbox(
    bbox: Tuple[float, float, float, float],
    *,
    page_size: int = 200,
    max_pages: int = 5,
    timeout: int = 60,
) -> List[Dict[str, Any]]:
    """Query TNM products API for LPC LAZ items intersecting a bbox."""
    xmin, ymin, xmax, ymax = bbox
    bbox_param = f"{xmin},{ymin},{xmax},{ymax}"
    offset = 0
    seen: set[str] = set()
    results: List[Dict[str, Any]] = []

    for _ in range(max_pages):
        params = {
            "bbox": bbox_param,
            "datasets": "Lidar Point Cloud (LPC)",
            "outputFormat": "JSON",
            "max": page_size,
            "offset": offset,
        }
        data = http_get_json(USGS_TNM_PRODUCTS_API, params, timeout=timeout)
        items = data.get("items") or []
        if not isinstance(items, list) or not items:
            break

        for item in items:
            if not isinstance(item, dict):
                continue
            urls = item.get("urls")
            url = (
                item.get("downloadLazURL")
                or item.get("downloadURL")
                or (urls.get("LAZ") if isinstance(urls, dict) else None)
            )
            if not isinstance(url, str):
                continue
            lower = url.lower()
            if not (lower.endswith(".laz") or lower.endswith(".las")):
                continue
            if url in seen:
                continue
            seen.add(url)
            results.append(
                {
                    "url": url,
                    "bbox_wgs84": _bbox_tuple(item.get("boundingBox") or {}),
                    "title": item.get("title"),
                    "publication_date": item.get("publicationDate"),
                }
            )

        total = int(data.get("total") or 0)
        offset += len(items)
        if offset >= total:
            break

    return results
