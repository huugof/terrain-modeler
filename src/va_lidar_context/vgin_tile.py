from __future__ import annotations

import html
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
    current = [f for f in features if f.get("attributes", {}).get("VComment") == "Current"]
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
    attrs = feature.get("attributes", {})
    geometry = feature.get("geometry")

    laz_url = parse_laz_url(attrs.get("PointCloudDownload", ""))
    if not laz_url:
        raise ValueError("Failed to parse LAZ download URL")

    bbox = _geometry_to_bbox(geometry)

    return {
        "tile_name": attrs.get("TileName", tile_name),
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
