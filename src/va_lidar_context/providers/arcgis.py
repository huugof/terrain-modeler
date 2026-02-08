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
) -> Dict[str, Any]:
    """Fetch an ArcGIS FeatureServer layer with paging and return GeoJSON."""

    xmin, ymin, xmax, ymax = bbox
    all_features: List[Dict[str, Any]] = []
    offset = 0

    while True:
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

    return {"type": "FeatureCollection", "features": all_features}
