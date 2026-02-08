from __future__ import annotations

import json
import re
from datetime import datetime
from typing import Any, Dict, List, Tuple

from ..constants import USGS_LIDAR_INDEX_QUERY
from ..util import http_get_json


def _query(params: Dict[str, Any]) -> List[Dict[str, Any]]:
    data = http_get_json(USGS_LIDAR_INDEX_QUERY, params)
    return data.get("features", [])


def query_for_point(lon: float, lat: float) -> List[Dict[str, Any]]:
    geometry = json.dumps({"x": lon, "y": lat, "spatialReference": {"wkid": 4326}})
    params = {
        "geometry": geometry,
        "geometryType": "esriGeometryPoint",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "workunit,project,ql,collect_start,collect_end,lpc_link,metadata_link",
        "returnGeometry": "false",
        "outSR": 4326,
        "f": "json",
    }
    return _query(params)


def query_for_bbox(bbox: Tuple[float, float, float, float]) -> List[Dict[str, Any]]:
    xmin, ymin, xmax, ymax = bbox
    params = {
        "geometry": f"{xmin},{ymin},{xmax},{ymax}",
        "geometryType": "esriGeometryEnvelope",
        "inSR": 4326,
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "workunit,project,ql,collect_start,collect_end,lpc_link,metadata_link",
        "returnGeometry": "false",
        "outSR": 4326,
        "f": "json",
    }
    return _query(params)


def _ql_rank(ql: str | None) -> int:
    if not ql:
        return 99
    match = re.search(r"(\d+)", ql)
    if not match:
        return 99
    try:
        return int(match.group(1))
    except ValueError:
        return 99


def _collect_end_ms(feature: Dict[str, Any]) -> int:
    val = feature.get("attributes", {}).get("collect_end")
    try:
        return int(val) if val is not None else 0
    except (TypeError, ValueError):
        return 0


def select_best_feature(features: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not features:
        raise ValueError("No LiDAR features returned")

    def sort_key(f: Dict[str, Any]) -> tuple[int, int]:
        ql = _ql_rank(f.get("attributes", {}).get("ql"))
        end_ms = _collect_end_ms(f)
        return (ql, -end_ms)

    return sorted(features, key=sort_key)[0]


def sort_features(features: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not features:
        return []

    def sort_key(f: Dict[str, Any]) -> tuple[int, int]:
        ql = _ql_rank(f.get("attributes", {}).get("ql"))
        end_ms = _collect_end_ms(f)
        return (ql, -end_ms)

    return sorted(features, key=sort_key)


def format_collect_date(feature: Dict[str, Any]) -> str | None:
    end_ms = _collect_end_ms(feature)
    if not end_ms:
        return None
    try:
        return datetime.utcfromtimestamp(end_ms / 1000).date().isoformat()
    except Exception:
        return None
