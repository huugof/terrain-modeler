from __future__ import annotations

import html
import json
import re
from typing import Any, Dict, List, Optional, Tuple

from ..constants import VGIN_FOOTPRINTS_QUERY, VGIN_LIDAR_QUERY
from ..util import http_get_json
from .arcgis import paged_query_geojson

HREF_RE = re.compile(r"href=\"([^\"]+)\"")


def parse_laz_url(pointcloud_download: str) -> Optional[str]:
    """Extract a LAZ URL from the VGIN HTML download field."""

    if not pointcloud_download:
        return None
    match = HREF_RE.search(pointcloud_download)
    if not match:
        return None
    return html.unescape(match.group(1))


def fetch_footprints_geojson(bbox: Tuple[float, float, float, float]) -> Dict[str, Any]:
    """Fetch VGIN building footprints in GeoJSON for the given bbox."""

    return paged_query_geojson(
        VGIN_FOOTPRINTS_QUERY,
        bbox,
        out_fields="OBJECTID,BLDGHEIGHT,NUMSTORIES,BUILDINGCLASS,MUNICIPALITY",
    )


def tiles_for_point(lon: float, lat: float) -> List[Dict[str, Any]]:
    """Find all VGIN tiles that contain the given point (lon, lat in WGS84)."""

    geometry = json.dumps({"x": lon, "y": lat, "spatialReference": {"wkid": 4326}})
    params = {
        "geometry": geometry,
        "geometryType": "esriGeometryPoint",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "TileName,PointCloudDownload,VComment,ProjectYear",
        "returnGeometry": "true",
        "outSR": 4326,
        "f": "json",
    }
    data = http_get_json(VGIN_LIDAR_QUERY, params)
    features = data.get("features", [])

    if not features:
        raise ValueError(f"No tiles found containing point ({lon}, {lat})")

    tiles_by_name: Dict[str, List[Dict[str, Any]]] = {}
    for f in features:
        name = f.get("attributes", {}).get("TileName", "")
        if name:
            tiles_by_name.setdefault(name, []).append(f)

    results = []
    for name, tile_features in tiles_by_name.items():
        feature = _select_best_feature(tile_features)
        try:
            results.append(_feature_to_tile_info(feature, name_fallback=name))
        except ValueError:
            continue

    if not results:
        raise ValueError(f"No valid tiles with LAZ URLs found for point ({lon}, {lat})")

    return results


def tiles_for_bbox(
    bbox: Tuple[float, float, float, float],
) -> List[Dict[str, Any]]:
    """Find all VGIN tiles intersecting the bbox (WGS84)."""

    xmin, ymin, xmax, ymax = bbox
    params = {
        "geometry": f"{xmin},{ymin},{xmax},{ymax}",
        "geometryType": "esriGeometryEnvelope",
        "inSR": 4326,
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "TileName,PointCloudDownload,VComment,ProjectYear",
        "returnGeometry": "true",
        "outSR": 4326,
        "f": "json",
    }
    data = http_get_json(VGIN_LIDAR_QUERY, params)
    features = data.get("features", [])

    if not features:
        raise ValueError("No tiles found intersecting bbox")

    tiles_by_name: Dict[str, List[Dict[str, Any]]] = {}
    for f in features:
        name = f.get("attributes", {}).get("TileName", "")
        if name:
            tiles_by_name.setdefault(name, []).append(f)

    results = []
    for name, tile_features in tiles_by_name.items():
        feature = _select_best_feature(tile_features)
        try:
            results.append(_feature_to_tile_info(feature, name_fallback=name))
        except ValueError:
            continue

    if not results:
        raise ValueError("No valid tiles with LAZ URLs found for bbox")

    return sorted(results, key=lambda t: t.get("tile_name", ""))


def tile_lookup(tile_name: str) -> Dict[str, Any]:
    """Resolve a single VGIN tile by name and return tile metadata."""

    params = {
        "where": f"TileName='{tile_name}' AND VComment='Current'",
        "outFields": "TileName,PointCloudDownload,VComment,ProjectYear",
        "returnGeometry": "true",
        "outSR": 4326,
        "f": "json",
    }
    data = http_get_json(VGIN_LIDAR_QUERY, params)
    features = data.get("features", [])

    if not features:
        params["where"] = f"TileName='{tile_name}'"
        data = http_get_json(VGIN_LIDAR_QUERY, params)
        features = data.get("features", [])

    feature = _select_best_feature(features)
    return _feature_to_tile_info(feature, name_fallback=tile_name)


def _geometry_to_bbox(geometry: Dict[str, Any]) -> Tuple[float, float, float, float]:
    if not geometry:
        raise ValueError("Missing geometry for tile")

    coords: List[Tuple[float, float]] = []
    if "rings" in geometry:
        for ring in geometry["rings"]:
            coords.extend([(pt[0], pt[1]) for pt in ring])
    elif "paths" in geometry:
        for path in geometry["paths"]:
            coords.extend([(pt[0], pt[1]) for pt in path])
    elif "x" in geometry and "y" in geometry:
        coords.append((geometry["x"], geometry["y"]))
    else:
        raise ValueError("Unsupported geometry type for tile")

    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    return min(xs), min(ys), max(xs), max(ys)


def _select_best_feature(features: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not features:
        raise ValueError("No tile features returned")
    current = [
        f for f in features if f.get("attributes", {}).get("VComment") == "Current"
    ]
    if current:
        return current[0]

    def year_key(f: Dict[str, Any]) -> int:
        year = f.get("attributes", {}).get("ProjectYear")
        try:
            return int(year) if year is not None else -1
        except ValueError:
            return -1

    return sorted(features, key=year_key, reverse=True)[0]


def _feature_to_tile_info(
    feature: Dict[str, Any], name_fallback: str = ""
) -> Dict[str, Any]:
    attrs = feature.get("attributes", {})
    geometry = feature.get("geometry")

    laz_url = parse_laz_url(attrs.get("PointCloudDownload", ""))
    if not laz_url:
        raise ValueError("Failed to parse LAZ download URL")

    bbox = _geometry_to_bbox(geometry)
    return {
        "tile_name": attrs.get("TileName", name_fallback),
        "laz_url": laz_url,
        "vcomment": attrs.get("VComment"),
        "project_year": attrs.get("ProjectYear"),
        "geometry": geometry,
        "bbox_wgs84": {
            "xmin": bbox[0],
            "ymin": bbox[1],
            "xmax": bbox[2],
            "ymax": bbox[3],
        },
    }
