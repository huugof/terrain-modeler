from __future__ import annotations

from typing import Any, Dict, List, Tuple

import requests

from ..constants import MAX_RECORD_COUNT, MSBFP2_QUERY


def fetch_footprints_geojson(
    bbox: Tuple[float, float, float, float],
    *,
    max_records: int = MAX_RECORD_COUNT,
) -> Dict[str, Any]:
    """
    Fetch Microsoft US Building Footprints from the Esri-hosted FeatureServer.

    Args:
        bbox: (xmin, ymin, xmax, ymax) in WGS84 (EPSG:4326)
        max_records: pagination size (server max record count)

    Returns:
        GeoJSON FeatureCollection with building polygons
    """
    xmin, ymin, xmax, ymax = bbox
    all_features: List[Dict[str, Any]] = []
    offset = 0

    while True:
        params = {
            "where": "1=1",
            "geometry": f"{xmin},{ymin},{xmax},{ymax}",
            "geometryType": "esriGeometryEnvelope",
            "inSR": 4326,
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": "OBJECTID",
            "returnGeometry": "true",
            "outSR": 4326,
            "f": "geojson",
            "resultRecordCount": max_records,
            "resultOffset": offset,
        }

        resp = requests.get(MSBFP2_QUERY, params=params, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        features = data.get("features", [])
        if not features:
            break
        all_features.extend(features)
        offset += max_records

    return {
        "type": "FeatureCollection",
        "features": all_features,
    }
