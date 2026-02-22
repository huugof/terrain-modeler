from __future__ import annotations

from typing import Any, Dict, List, Tuple

import requests

from ..constants import MAX_RECORD_COUNT

BBoxWGS84 = Tuple[float, float, float, float]


def paged_query_geojson(
    query_url: str,
    bbox: BBoxWGS84,
    *,
    out_fields: str,
    max_record_count: int = MAX_RECORD_COUNT,
    where: str = "1=1",
    timeout: int = 60,
    max_pages: int = 500,
) -> Dict[str, Any]:
    """Fetch an ArcGIS FeatureServer layer with paging and return GeoJSON.

    Raises RuntimeError if the server returns more than *max_pages* pages,
    which prevents an infinite loop against a misbehaving endpoint.
    """

    xmin, ymin, xmax, ymax = bbox
    all_features: List[Dict[str, Any]] = []
    offset = 0
    pages_fetched = 0

    while True:
        if pages_fetched >= max_pages:
            raise RuntimeError(
                f"ArcGIS paged query exceeded {max_pages} pages at {query_url!r}; "
                "the server may not be honoring resultOffset pagination correctly."
            )
        params = {
            "where": where,
            "geometry": f"{xmin},{ymin},{xmax},{ymax}",
            "geometryType": "esriGeometryEnvelope",
            "inSR": 4326,
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": out_fields,
            "returnGeometry": "true",
            "outSR": 4326,
            "f": "geojson",
            "resultRecordCount": max_record_count,
            "resultOffset": offset,
        }

        resp = requests.get(query_url, params=params, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        features = data.get("features", [])
        if not features:
            break
        all_features.extend(features)
        offset += max_record_count
        pages_fetched += 1

    return {"type": "FeatureCollection", "features": all_features}
