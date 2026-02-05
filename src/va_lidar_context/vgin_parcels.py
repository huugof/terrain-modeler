from __future__ import annotations

from typing import Any, Dict, List, Tuple

from .constants import MAX_RECORD_COUNT, VGIN_PARCELS_QUERY


def fetch_parcels_geojson(bbox: Tuple[float, float, float, float]) -> Dict[str, Any]:
    """
    Fetch parcel boundaries within the given bounding box.

    Args:
        bbox: (xmin, ymin, xmax, ymax) in WGS84

    Returns:
        GeoJSON FeatureCollection with parcel polygons
    """
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
            "outFields": "OBJECTID,VGIN_QPID,PARCELID,LOCALITY,Shape__Area",
            "returnGeometry": "true",
            "outSR": 4326,
            "f": "geojson",
            "resultRecordCount": MAX_RECORD_COUNT,
            "resultOffset": offset,
        }

        resp = requests.get(VGIN_PARCELS_QUERY, params=params, timeout=60)
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
