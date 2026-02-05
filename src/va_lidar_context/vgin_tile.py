from __future__ import annotations

import html
import json
import re
from typing import Any, Dict, List, Optional, Tuple

from .constants import VGIN_LIDAR_QUERY
from .util import http_get_json

HREF_RE = re.compile(r"href=\"([^\"]+)\"")


def parse_laz_url(pointcloud_download: str) -> Optional[str]:
    if not pointcloud_download:
        return None
    match = HREF_RE.search(pointcloud_download)
    if not match:
        return None
    return html.unescape(match.group(1))


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

    # fallback: pick highest ProjectYear if present
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


def normalize_coordinates(coord1: float, coord2: float) -> Tuple[float, float]:
    """
    Auto-detect coordinate order and return (lon, lat).

    Latitude is always between -90 and 90.
    Longitude can be between -180 and 180.

    For Virginia, coordinates are roughly:
    - Latitude: 36.5 to 39.5
    - Longitude: -83 to -75

    This function checks which value is a valid latitude and returns (lon, lat).
    """
    # Latitude must be between -90 and 90
    c1_valid_lat = -90 <= coord1 <= 90
    c2_valid_lat = -90 <= coord2 <= 90

    if c1_valid_lat and not c2_valid_lat:
        # coord1 is latitude, coord2 is longitude
        return (coord2, coord1)
    elif c2_valid_lat and not c1_valid_lat:
        # coord2 is latitude, coord1 is longitude
        return (coord1, coord2)
    elif c1_valid_lat and c2_valid_lat:
        # Both could be latitude - use Virginia-specific heuristics
        # Virginia latitudes are ~36.5-39.5, longitudes are ~-83 to -75
        # If one is negative and the other positive, negative is likely longitude
        if coord1 < 0 and coord2 > 0:
            return (coord1, coord2)  # coord1=lon, coord2=lat
        elif coord2 < 0 and coord1 > 0:
            return (coord2, coord1)  # coord2=lon, coord1=lat
        else:
            # Both same sign - assume lat, lon order (Google Maps style)
            return (coord2, coord1)
    else:
        raise ValueError(
            f"Cannot determine coordinate order: neither {coord1} nor {coord2} "
            "is a valid latitude (must be between -90 and 90)"
        )


def tiles_for_point(lon: float, lat: float) -> List[Dict[str, Any]]:
    """
    Find all tiles that contain the given point (lon, lat in WGS84).
    Returns a list of tile info dicts, preferring 'Current' versions.
    """
    # Use a point geometry for the spatial query
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

    # Group by tile name and pick best version for each
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
    """
    Find all tiles that intersect the given bbox (WGS84).
    Returns a list of tile info dicts, preferring 'Current' versions.
    """
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
        # fallback query without VComment
        params["where"] = f"TileName='{tile_name}'"
        data = http_get_json(VGIN_LIDAR_QUERY, params)
        features = data.get("features", [])

    feature = _select_best_feature(features)
    return _feature_to_tile_info(feature, name_fallback=tile_name)
