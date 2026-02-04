from __future__ import annotations

from typing import Any, Dict, List, Tuple

from .constants import MAX_RECORD_COUNT, VGIN_FOOTPRINTS_QUERY


def fetch_footprints_geojson(bbox: Tuple[float, float, float, float]) -> Dict[str, Any]:
    import requests

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
            "outFields": "OBJECTID,BLDGHEIGHT,NUMSTORIES,BUILDINGCLASS,MUNICIPALITY",
            "returnGeometry": "true",
            "outSR": 4326,
            "f": "geojson",
            "resultRecordCount": MAX_RECORD_COUNT,
            "resultOffset": offset,
        }

        resp = requests.get(VGIN_FOOTPRINTS_QUERY, params=params, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        features = data.get("features", [])
        if not features:
            break
        all_features.extend(features)
        offset += MAX_RECORD_COUNT

    return {
        "type": "FeatureCollection",
        "features": all_features,
    }
