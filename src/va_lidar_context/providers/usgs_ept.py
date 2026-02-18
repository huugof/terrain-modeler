from __future__ import annotations

from typing import Any, Dict, Tuple

import requests

from ..constants import USGS_LIDAR_PUBLIC_BUCKET
from ..pipeline.types import LidarSource
from .hobu_boundaries import find_intersections, load_boundaries, sort_datasets
from .usgs_index import query_for_bbox, query_for_point, sort_features


def _ept_url(workunit: str, name: str = "ept.json") -> str:
    return f"{USGS_LIDAR_PUBLIC_BUCKET}/{workunit}/{name}"


def _boundary_url(workunit: str) -> str:
    return f"{USGS_LIDAR_PUBLIC_BUCKET}/{workunit}/boundary.json"


def _ept_exists(url: str) -> bool:
    try:
        resp = requests.head(url, timeout=30)
        if resp.status_code == 200:
            return True
        if resp.status_code in (403, 404):
            return False
    except requests.RequestException:
        pass

    try:
        resp = requests.get(url, stream=True, timeout=30)
        if resp.status_code == 200:
            return True
        if resp.status_code in (403, 404):
            return False
    except requests.RequestException:
        return False

    return False


def _extract_wkt(srs: Dict[str, Any]) -> str | None:
    if not srs:
        return None
    if isinstance(srs, str):
        return srs
    return (
        srs.get("wkt")
        or srs.get("compoundwkt")
        or srs.get("comp_spatialreference")
        or srs.get("proj4")
    )


def _fetch_ept_metadata(url: str) -> Dict[str, Any]:
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    return resp.json()


def _fetch_boundary_bbox(workunit: str) -> Dict[str, float] | None:
    url = _boundary_url(workunit)
    try:
        resp = requests.get(url, timeout=60)
        if resp.status_code != 200:
            return None
        data = resp.json()
    except requests.RequestException:
        return None

    coords = []
    if data.get("type") == "MultiPolygon":
        for poly in data.get("coordinates", []):
            for ring in poly:
                coords.extend(ring)
    elif data.get("type") == "Polygon":
        for ring in data.get("coordinates", []):
            coords.extend(ring)
    if not coords:
        return None

    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    return {"xmin": min(xs), "ymin": min(ys), "xmax": max(xs), "ymax": max(ys)}


def resolve_ept_from_point(
    lon: float, lat: float, logger=None, cache_dir=None
) -> LidarSource | None:
    # Preferred: Hobu boundaries (authoritative for EPT coverage)
    if cache_dir is not None:
        try:
            from shapely.geometry import Point

            cache_path = cache_dir / "hobu_boundaries.geojson"
            boundaries = load_boundaries(cache_path, logger=logger)
            datasets = sort_datasets(
                find_intersections(boundaries, Point(lon, lat), logger=logger)
            )
            for ds in datasets:
                base_url = ds.get("url")
                if not base_url:
                    continue
                for name in ("ept.json", "ept-1.json"):
                    url = base_url.replace("ept.json", name)
                    if logger:
                        logger.info(
                            f"Checking EPT (Hobu): dataset={ds.get('name')} file={name}"
                        )
                    if not _ept_exists(url):
                        continue
                    ept = _fetch_ept_metadata(url)
                    wkt = _extract_wkt(ept.get("srs", {}))
                    if logger:
                        logger.info(
                            f"Using EPT (Hobu): dataset={ds.get('name')} file={name}"
                        )
                    return LidarSource(
                        source_type="ept",
                        uri=url,
                        bbox_wgs84=(lon, lat, lon, lat),
                        crs_wkt=wkt,
                        metadata={
                            "dataset": ds.get("name"),
                            "year": ds.get("year"),
                            "ept_name": name,
                            "source": "hobu_boundaries",
                        },
                    )
        except Exception:
            pass

    # Fallback: USGS index workunits
    features = query_for_point(lon, lat)
    if not features:
        return None
    for feature in sort_features(features):
        attrs = feature.get("attributes", {})
        workunit = attrs.get("workunit")
        if not workunit:
            continue

        for name in ("ept.json", "ept-1.json"):
            if logger:
                logger.info(f"Checking EPT: workunit={workunit} file={name}")
            url = _ept_url(workunit, name=name)
            if not _ept_exists(url):
                continue

            ept = _fetch_ept_metadata(url)
            wkt = _extract_wkt(ept.get("srs", {}))
            bbox = _fetch_boundary_bbox(workunit)

            if logger:
                logger.info(f"Using EPT: workunit={workunit} file={name}")
            return LidarSource(
                source_type="ept",
                uri=url,
                bbox_wgs84=(
                    bbox["xmin"],
                    bbox["ymin"],
                    bbox["xmax"],
                    bbox["ymax"],
                )
                if bbox
                else (lon, lat, lon, lat),
                crs_wkt=wkt,
                metadata={
                    "workunit": workunit,
                    "project": attrs.get("project"),
                    "ql": attrs.get("ql"),
                    "collect_start": attrs.get("collect_start"),
                    "collect_end": attrs.get("collect_end"),
                    "lpc_link": attrs.get("lpc_link"),
                    "metadata_link": attrs.get("metadata_link"),
                    "ept_name": name,
                },
            )

    if logger:
        logger.warning("No EPT coverage found for location")
    return None


def resolve_ept_from_bbox(
    bbox: Tuple[float, float, float, float], logger=None, cache_dir=None
) -> LidarSource | None:
    # Preferred: Hobu boundaries
    if cache_dir is not None:
        try:
            from shapely.geometry import box as shp_box
            from shapely.geometry import shape as shp_shape

            def _safe_shape(geom):
                if not geom:
                    return None
                try:
                    return shp_shape(geom)
                except Exception:
                    return None

            def _coverage_ratio(geom, aoi_geom):
                try:
                    if aoi_geom.area == 0:
                        return None
                    if geom.covers(aoi_geom):
                        return 1.0
                    inter = geom.intersection(aoi_geom)
                    if inter.is_empty:
                        return 0.0
                    return inter.area / aoi_geom.area
                except Exception:
                    return None

            cache_path = cache_dir / "hobu_boundaries.geojson"
            boundaries = load_boundaries(cache_path, logger=logger)
            aoi_geom = shp_box(*bbox)
            datasets = sort_datasets(
                find_intersections(boundaries, aoi_geom, logger=logger)
            )
            enriched: list[dict[str, Any]] = []
            covering: list[dict[str, Any]] = []
            for ds in datasets:
                geom = _safe_shape(ds.get("geometry"))
                ds = dict(ds)
                ds["_geom"] = geom
                enriched.append(ds)
                if geom and geom.covers(aoi_geom):
                    covering.append(ds)
            candidates = covering or enriched
            if covering and logger:
                logger.info(
                    f"Hobu boundaries: {len(covering)} dataset(s) fully cover AOI"
                )

            for ds in candidates:
                base_url = ds.get("url")
                if not base_url:
                    continue
                for name in ("ept.json", "ept-1.json"):
                    url = base_url.replace("ept.json", name)
                    if logger:
                        logger.info(
                            f"Checking EPT (Hobu): dataset={ds.get('name')} file={name}"
                        )
                    if not _ept_exists(url):
                        continue
                    ept = _fetch_ept_metadata(url)
                    wkt = _extract_wkt(ept.get("srs", {}))
                    coverage_ratio = _coverage_ratio(ds.get("_geom"), aoi_geom)
                    coverage_status = None
                    if coverage_ratio is not None:
                        coverage_status = (
                            "full" if coverage_ratio >= 0.99 else "partial"
                        )
                    if logger:
                        logger.info(
                            f"Using EPT (Hobu): dataset={ds.get('name')} file={name}"
                        )
                    return LidarSource(
                        source_type="ept",
                        uri=url,
                        bbox_wgs84=bbox,
                        crs_wkt=wkt,
                        metadata={
                            "dataset": ds.get("name"),
                            "year": ds.get("year"),
                            "ept_name": name,
                            "source": "hobu_boundaries",
                            "coverage_ratio": coverage_ratio,
                            "coverage_status": coverage_status,
                            "coverage_source": "hobu_boundaries",
                        },
                    )
        except Exception:
            pass

    # Fallback: USGS index
    features = query_for_bbox(bbox)
    if not features:
        return None
    for feature in sort_features(features):
        attrs = feature.get("attributes", {})
        workunit = attrs.get("workunit")
        if not workunit:
            continue

        for name in ("ept.json", "ept-1.json"):
            if logger:
                logger.info(f"Checking EPT: workunit={workunit} file={name}")
            url = _ept_url(workunit, name=name)
            if not _ept_exists(url):
                continue

            ept = _fetch_ept_metadata(url)
            wkt = _extract_wkt(ept.get("srs", {}))
            boundary = _fetch_boundary_bbox(workunit)
            bbox_wgs84 = (
                (
                    boundary["xmin"],
                    boundary["ymin"],
                    boundary["xmax"],
                    boundary["ymax"],
                )
                if boundary
                else bbox
            )

            if logger:
                logger.info(f"Using EPT: workunit={workunit} file={name}")
            return LidarSource(
                source_type="ept",
                uri=url,
                bbox_wgs84=bbox_wgs84,
                crs_wkt=wkt,
                metadata={
                    "workunit": workunit,
                    "project": attrs.get("project"),
                    "ql": attrs.get("ql"),
                    "collect_start": attrs.get("collect_start"),
                    "collect_end": attrs.get("collect_end"),
                    "lpc_link": attrs.get("lpc_link"),
                    "metadata_link": attrs.get("metadata_link"),
                    "ept_name": name,
                },
            )

    if logger:
        logger.warning("No EPT coverage found for bbox")
    return None
