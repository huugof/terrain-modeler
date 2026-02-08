from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple, Literal

from ..constants import MAX_RECORD_COUNT

BBoxWGS84 = Tuple[float, float, float, float]


@dataclass(frozen=True)
class ParcelSource:
    id: str
    name: str
    kind: Literal["arcgis"]
    query_url: str
    out_fields: str
    max_record_count: int = MAX_RECORD_COUNT
    coverage: Optional[BBoxWGS84] = None
    exclude: Optional[List[BBoxWGS84]] = None
    notes: Optional[str] = None


def _sources_path() -> Path:
    return Path(__file__).with_name("sources.json")


def load_sources() -> List[ParcelSource]:
    path = _sources_path()
    data = json.loads(path.read_text())
    sources: List[ParcelSource] = []
    for item in data:
        coverage = None
        if item.get("coverage"):
            cov = item["coverage"]
            coverage = (
                float(cov["xmin"]),
                float(cov["ymin"]),
                float(cov["xmax"]),
                float(cov["ymax"]),
            )
        exclude = None
        if item.get("exclude"):
            exclude = []
            for entry in item["exclude"]:
                exclude.append(
                    (
                        float(entry["xmin"]),
                        float(entry["ymin"]),
                        float(entry["xmax"]),
                        float(entry["ymax"]),
                    )
                )
        sources.append(
            ParcelSource(
                id=item["id"],
                name=item["name"],
                kind=item["kind"],
                query_url=item["query_url"],
                out_fields=item.get("out_fields", "OBJECTID"),
                max_record_count=int(item.get("max_record_count", MAX_RECORD_COUNT)),
                coverage=coverage,
                exclude=exclude,
                notes=item.get("notes"),
            )
        )
    return sources


def _bbox_intersects(a: BBoxWGS84, b: BBoxWGS84) -> bool:
    return not (a[2] < b[0] or a[0] > b[2] or a[3] < b[1] or a[1] > b[3])


def _point_in_bbox(point: tuple[float, float], bbox: BBoxWGS84) -> bool:
    x, y = point
    return bbox[0] <= x <= bbox[2] and bbox[1] <= y <= bbox[3]


def resolve_source(bbox_wgs84: BBoxWGS84, sources: Iterable[ParcelSource]) -> Optional[ParcelSource]:
    center = ((bbox_wgs84[0] + bbox_wgs84[2]) / 2.0, (bbox_wgs84[1] + bbox_wgs84[3]) / 2.0)
    for source in sources:
        if source.exclude and any(_point_in_bbox(center, ex) for ex in source.exclude):
            continue
        if source.coverage is None:
            return source
        if _bbox_intersects(bbox_wgs84, source.coverage):
            return source
    return None


def fetch_parcels_geojson(bbox: BBoxWGS84, source: ParcelSource) -> Dict[str, Any]:
    if source.kind != "arcgis":
        raise ValueError(f"Unsupported parcel source kind: {source.kind}")

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
            "outFields": source.out_fields,
            "returnGeometry": "true",
            "outSR": 4326,
            "f": "geojson",
            "resultRecordCount": source.max_record_count,
            "resultOffset": offset,
        }

        resp = requests.get(source.query_url, params=params, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        features = data.get("features", [])
        if not features:
            break
        all_features.extend(features)
        offset += source.max_record_count

    return {
        "type": "FeatureCollection",
        "features": all_features,
    }


def fetch_parcels_for_bbox(bbox_wgs84: BBoxWGS84) -> Tuple[Optional[ParcelSource], Optional[Dict[str, Any]]]:
    sources = load_sources()
    source = resolve_source(bbox_wgs84, sources)
    if source is None:
        return None, None
    return source, fetch_parcels_geojson(bbox_wgs84, source)
