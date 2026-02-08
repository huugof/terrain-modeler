from __future__ import annotations

import json
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
from shapely.geometry import shape

HOBU_BOUNDARIES_URL = "https://raw.githubusercontent.com/hobu/usgs-lidar/master/boundaries/resources.geojson"


def extract_year(name: str | None) -> Optional[int]:
    if not name:
        return None
    match = re.search(r"(19[9][0-9]|20[0-2][0-9])", name)
    if not match:
        return None
    try:
        return int(match.group(1))
    except ValueError:
        return None


def load_boundaries(
    cache_path: Path,
    *,
    force: bool = False,
    timeout: int = 60,
    logger=None,
) -> Dict[str, Any]:
    if cache_path.exists() and not force:
        return json.loads(cache_path.read_text())

    if logger:
        logger.info(f"Downloading Hobu EPT boundaries from {HOBU_BOUNDARIES_URL}")
    resp = requests.get(HOBU_BOUNDARIES_URL, timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    if data.get("type") != "FeatureCollection":
        raise ValueError("Hobu boundaries payload is not a FeatureCollection")

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(data))
    return data


def _dataset_url_from_properties(props: Dict[str, Any]) -> Optional[str]:
    url = props.get("url") or props.get("URL")
    if url:
        return url
    name = props.get("name") or props.get("Name")
    if not name:
        return None
    return f"https://usgs-lidar-public.s3.amazonaws.com/{name}/ept.json"


def find_intersections(
    boundaries: Dict[str, Any], aoi_geom, logger=None
) -> List[Dict[str, Any]]:
    features = boundaries.get("features", [])
    results: List[Dict[str, Any]] = []
    for feat in features:
        geom = feat.get("geometry")
        props = feat.get("properties", {})
        if not geom:
            continue
        try:
            geom_shape = shape(geom)
        except Exception:
            continue
        if not geom_shape.intersects(aoi_geom):
            continue

        name = props.get("name") or props.get("Name")
        url = _dataset_url_from_properties(props)
        results.append(
            {
                "name": name,
                "url": url,
                "year": props.get("year") or extract_year(name),
                "properties": props,
                "geometry": geom,
            }
        )

    if logger:
        logger.info(f"Hobu boundaries intersecting datasets: {len(results)}")
    return results


def sort_datasets(datasets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    def key(d):
        year = d.get("year")
        return (-(year or 0), d.get("name") or "")

    return sorted(datasets, key=key)
