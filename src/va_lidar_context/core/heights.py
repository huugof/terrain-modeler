from __future__ import annotations

import csv
import hashlib
import json
import os
import random
import subprocess
import tempfile
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    import numpy as np
except Exception:  # pragma: no cover
    np = None

try:
    import rasterio
    from rasterio.mask import mask
except Exception:  # pragma: no cover
    rasterio = None
    mask = None

try:
    from pyproj import CRS, Transformer
except Exception:  # pragma: no cover
    CRS = None
    Transformer = None

try:
    from shapely import contains_xy
    from shapely.geometry import mapping, shape
    from shapely.ops import transform, unary_union
    from shapely.strtree import STRtree
    from shapely.validation import make_valid
except Exception:  # pragma: no cover
    contains_xy = None
    mapping = None
    shape = None
    transform = None
    unary_union = None
    STRtree = None
    make_valid = None


FEET_PER_METER = 3.28084


@dataclass
class FootprintHeight:
    geometry: Any
    height: float
    source: str
    base_z: float = 0.0
    building_id: str | None = None
    qc: Dict[str, Any] | None = None


def get_laz_crs_wkt(laz_path: str) -> str:
    """Read LAZ CRS WKT from PDAL metadata."""
    proc = subprocess.run(
        ["pdal", "info", "--metadata", laz_path],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)
    srs = data.get("metadata", {}).get("srs", {})
    wkt = (
        srs.get("wkt")
        or srs.get("compoundwkt")
        or srs.get("comp_spatialreference")
        or srs.get("proj4")
    )
    if not wkt:
        raise ValueError("LAZ CRS not found in PDAL metadata")
    return wkt


def get_unit_scale(crs: CRS, output_units: str, latitude: float | None = None) -> float:
    """Return a multiplier to convert CRS units to desired output units.

    When *latitude* is provided and the CRS is Web Mercator (EPSG:3857),
    the scale is corrected for Mercator distortion so that output
    coordinates represent true ground distances.
    """
    import math

    axis = crs.axis_info[0] if crs.axis_info else None
    to_meters = axis.unit_conversion_factor if axis and axis.unit_conversion_factor else 1.0
    # Web Mercator metres are not true metres — correct with cos(lat).
    if latitude is not None:
        try:
            epsg = crs.to_epsg()
        except Exception:
            epsg = None
        if epsg == 3857:
            to_meters *= math.cos(math.radians(latitude))
    if output_units == "meters":
        return to_meters
    if output_units == "feet":
        return to_meters * FEET_PER_METER
    raise ValueError(f"Unsupported units: {output_units}")


def reproject_features(
    geojson: Dict[str, Any],
    dst_crs: CRS,
    src_crs: CRS | str = "EPSG:4326",
) -> List[Dict[str, Any]]:
    """Reproject GeoJSON features into the target CRS."""
    if Transformer is None or shape is None or transform is None:
        raise RuntimeError("pyproj and shapely are required for reprojection")
    transformer = Transformer.from_crs(src_crs, dst_crs, always_xy=True)

    def _transform_geom(geom):
        return transform(transformer.transform, geom)

    features = []
    for feat in geojson.get("features", []):
        geom = shape(feat.get("geometry"))
        if geom.is_empty:
            continue
        geom = _transform_geom(geom)
        features.append(
            {
                "geometry": geom,
                "properties": feat.get("properties", {}),
            }
        )
    return features


def sample_raster_values(raster_path: str, polygon) -> np.ndarray:
    """Sample raster values within a polygon footprint."""
    if rasterio is None or mask is None:
        raise RuntimeError("rasterio is required for raster sampling")
    with rasterio.open(raster_path) as ds:
        nodata = ds.nodata if ds.nodata is not None else -9999
        try:
            out_image, _ = mask(ds, [polygon], crop=True, all_touched=False)
        except ValueError:
            # Polygon doesn't overlap raster (e.g., building outside clip region)
            return np.array([])
        data = out_image[0]
        values = data[(data != nodata) & np.isfinite(data)]
        return values


def compute_height(
    values: np.ndarray,
    percentile: int,
    min_height: float,
    max_height: float,
) -> Optional[float]:
    """Compute a clamped percentile height from raster samples."""
    if np is None:
        raise RuntimeError("numpy is required for height computation")
    if values.size == 0:
        return None
    h = float(np.percentile(values, percentile))
    return float(max(min_height, min(max_height, h)))


def compute_base(values: np.ndarray) -> Optional[float]:
    """Compute a base elevation using the median of raster samples."""
    if np is None:
        raise RuntimeError("numpy is required for base height computation")
    if values.size == 0:
        return None
    return float(np.percentile(values, 50))


def fallback_height(
    properties: Dict[str, Any], floor_to_floor: float
) -> Optional[Tuple[float, str]]:
    """Fallback to attribute-derived heights when raster samples are missing."""
    if properties.get("BLDGHEIGHT") is not None:
        try:
            return float(properties["BLDGHEIGHT"]), "BLDGHEIGHT"
        except (TypeError, ValueError):
            pass
    if properties.get("NUMSTORIES") is not None:
        try:
            return float(properties["NUMSTORIES"]) * floor_to_floor, "NUMSTORIES"
        except (TypeError, ValueError):
            pass
    return None


def derive_heights(
    ndsm_path: str | None,
    dtm_path: str,
    features: Iterable[Dict[str, Any]],
    percentile: int,
    min_height: float,
    max_height: float,
    floor_to_floor: float,
    override_height_range: Tuple[float, float] | None = None,
    rng: random.Random | None = None,
) -> Tuple[List[FootprintHeight], List[str]]:
    """Derive per-footprint heights and return any warnings."""
    results: List[FootprintHeight] = []
    warnings: List[str] = []

    if override_height_range and rng is None:
        rng = random.Random()

    for feat in features:
        geom = feat["geometry"]
        props = feat.get("properties", {})
        if override_height_range is None and ndsm_path is None:
            raise RuntimeError("nDSM path is required when not overriding heights")

        base_values = sample_raster_values(dtm_path, geom)

        base_z = compute_base(base_values)
        if base_z is None:
            base_z = 0.0
            warnings.append("No DTM samples for footprint; using base_z=0")

        if override_height_range is not None:
            h = rng.uniform(override_height_range[0], override_height_range[1])
            results.append(
                FootprintHeight(
                    geometry=geom,
                    height=h,
                    source="RANDOM",
                    base_z=base_z,
                )
            )
            continue

        ndsm_values = sample_raster_values(ndsm_path, geom)
        height = compute_height(ndsm_values, percentile, min_height, max_height)
        if height is not None:
            results.append(
                FootprintHeight(
                    geometry=geom,
                    height=height,
                    source=f"P{percentile}",
                    base_z=base_z,
                )
            )
            continue

        fallback = fallback_height(props, floor_to_floor)
        if fallback:
            h, source = fallback
            h = float(max(min_height, min(max_height, h)))
            results.append(
                FootprintHeight(
                    geometry=geom,
                    height=h,
                    source=source,
                    base_z=base_z,
                )
            )
            continue

        warnings.append("No height samples and no fallback attributes")

    return results, warnings


def _format_bounds(bounds: tuple[float, float, float, float]) -> str:
    minx, miny, maxx, maxy = bounds
    return f"([{minx},{maxx}],[{miny},{maxy}])"


def _read_points_csv(csv_path: str, has_classification: bool) -> tuple[np.ndarray, ...]:
    xs: list[float] = []
    ys: list[float] = []
    zs: list[float] = []
    classes: list[int] = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                x = float(row.get("X", "nan"))
                y = float(row.get("Y", "nan"))
                z = float(row.get("Z", "nan"))
            except (TypeError, ValueError):
                continue
            if not np.isfinite(x) or not np.isfinite(y) or not np.isfinite(z):
                continue
            xs.append(x)
            ys.append(y)
            zs.append(z)
            if has_classification:
                raw = row.get("Classification")
                try:
                    classes.append(int(float(raw)) if raw not in (None, "") else 0)
                except (TypeError, ValueError):
                    classes.append(0)

    x = np.asarray(xs, dtype=np.float64)
    y = np.asarray(ys, dtype=np.float64)
    z = np.asarray(zs, dtype=np.float64)
    if has_classification:
        cls = np.asarray(classes, dtype=np.int16)
    else:
        cls = np.zeros(x.shape[0], dtype=np.int16)
    return x, y, z, cls


def _extract_laz_points(
    laz_path: str,
    bounds: tuple[float, float, float, float] | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    def _run_extract(order: str) -> str:
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
            csv_path = tmp.name
        pipeline = {"pipeline": [str(laz_path)]}
        if bounds is not None:
            pipeline["pipeline"].append({"type": "filters.crop", "bounds": _format_bounds(bounds)})
        pipeline["pipeline"].append(
            {
                "type": "writers.text",
                "filename": csv_path,
                "order": order,
            }
        )
        subprocess.run(
            ["pdal", "pipeline", "--stdin"],
            input=json.dumps(pipeline).encode("utf-8"),
            check=True,
            capture_output=True,
        )
        return csv_path

    csv_path: str | None = None
    has_classification = True
    try:
        try:
            csv_path = _run_extract("X,Y,Z,Classification")
        except subprocess.CalledProcessError:
            has_classification = False
            csv_path = _run_extract("X,Y,Z")
        return _read_points_csv(csv_path, has_classification=has_classification)
    finally:
        if csv_path and os.path.exists(csv_path):
            os.unlink(csv_path)


def _deterministic_building_id(geom: Any) -> str:
    if geom is None:
        raise ValueError("Geometry is required to derive deterministic building_id")
    try:
        normalized = geom.normalize()
    except Exception:
        normalized = geom
    digest = hashlib.sha1(normalized.wkb).hexdigest()
    return digest[:16]


def _building_id(properties: Dict[str, Any], geom: Any) -> str:
    for key in (
        "building_id",
        "BUILDING_ID",
        "id",
        "ID",
        "fid",
        "FID",
        "OBJECTID",
        "objectid",
    ):
        value = properties.get(key)
        if value is None:
            continue
        text = str(value).strip()
        if text:
            return text
    return _deterministic_building_id(geom)


def _bbox_indices(
    x_sorted: np.ndarray,
    sort_idx: np.ndarray,
    y: np.ndarray,
    bbox: tuple[float, float, float, float],
) -> np.ndarray:
    minx, miny, maxx, maxy = bbox
    left = int(np.searchsorted(x_sorted, minx, side="left"))
    right = int(np.searchsorted(x_sorted, maxx, side="right"))
    if right <= left:
        return np.empty((0,), dtype=np.int64)
    cand = sort_idx[left:right]
    mask = (y[cand] >= miny) & (y[cand] <= maxy)
    return cand[mask]


def _ground_estimate(
    ring_z: np.ndarray,
    ring_cls: np.ndarray,
    dtm_path: str,
    ring_geom: Any,
    *,
    min_ground_pts: int,
) -> Dict[str, Any]:
    if ring_z.size == 0:
        if ring_geom is not None:
            dtm_values = sample_raster_values(dtm_path, ring_geom)
            if dtm_values.size > 0:
                return {
                    "ground": float(np.percentile(dtm_values, 50)),
                    "method": "dtm_median",
                    "n_ground_pts": int(dtm_values.size),
                    "ground_median": float(np.percentile(dtm_values, 50)),
                    "ground_iqr": float(
                        np.percentile(dtm_values, 75) - np.percentile(dtm_values, 25)
                    ),
                }
        return {
            "ground": None,
            "method": "none",
            "n_ground_pts": 0,
            "ground_median": None,
            "ground_iqr": None,
        }

    ground_class = ring_z[ring_cls == 2]
    if ground_class.size >= min_ground_pts:
        return {
            "ground": float(np.percentile(ground_class, 50)),
            "method": "class2_median",
            "n_ground_pts": int(ground_class.size),
            "ground_median": float(np.percentile(ground_class, 50)),
            "ground_iqr": float(np.percentile(ground_class, 75) - np.percentile(ground_class, 25)),
        }

    if ground_class.size >= 6:
        return {
            "ground": float(np.percentile(ground_class, 25)),
            "method": "class2_p25",
            "n_ground_pts": int(ground_class.size),
            "ground_median": float(np.percentile(ground_class, 50)),
            "ground_iqr": float(np.percentile(ground_class, 75) - np.percentile(ground_class, 25)),
        }

    med = float(np.percentile(ring_z, 50))
    mad = float(np.percentile(np.abs(ring_z - med), 50))
    if mad > 0.0:
        sigma = 1.4826 * mad
        filtered = ring_z[ring_z <= med + (3.0 * sigma)]
    else:
        filtered = ring_z

    if filtered.size >= 6:
        return {
            "ground": float(np.percentile(filtered, 10)),
            "method": "ring_p10_mad",
            "n_ground_pts": int(filtered.size),
            "ground_median": float(np.percentile(filtered, 50)),
            "ground_iqr": float(np.percentile(filtered, 75) - np.percentile(filtered, 25)),
        }

    dtm_values = sample_raster_values(dtm_path, ring_geom)
    if dtm_values.size > 0:
        return {
            "ground": float(np.percentile(dtm_values, 50)),
            "method": "dtm_median",
            "n_ground_pts": int(dtm_values.size),
            "ground_median": float(np.percentile(dtm_values, 50)),
            "ground_iqr": float(np.percentile(dtm_values, 75) - np.percentile(dtm_values, 25)),
        }

    return {
        "ground": None,
        "method": "none",
        "n_ground_pts": 0,
        "ground_median": None,
        "ground_iqr": None,
    }


def _fallback_height_for_feature(
    *,
    geom: Any,
    properties: Dict[str, Any],
    ndsm_path: str | None,
    dtm_path: str,
    percentile: int,
    min_height: float,
    max_height: float,
    floor_to_floor: float,
    building_id: str,
    extra_qc: Dict[str, Any],
) -> tuple[FootprintHeight | None, str | None]:
    base_values = sample_raster_values(dtm_path, geom)
    base_z = compute_base(base_values)
    if base_z is None:
        base_z = 0.0

    if ndsm_path is not None:
        ndsm_values = sample_raster_values(ndsm_path, geom)
        height = compute_height(ndsm_values, percentile, min_height, max_height)
        if height is not None:
            qc = dict(extra_qc)
            qc["fallback"] = True
            flags = list(qc.get("flags", []))
            flags.append("used_ndsm_fallback")
            qc["flags"] = sorted(set(flags))
            return (
                FootprintHeight(
                    geometry=geom,
                    height=height,
                    source=f"P{percentile}",
                    base_z=base_z,
                    building_id=building_id,
                    qc=qc,
                ),
                None,
            )

    fallback = fallback_height(properties, floor_to_floor)
    if fallback:
        h, source = fallback
        h = float(max(min_height, min(max_height, h)))
        qc = dict(extra_qc)
        qc["fallback"] = True
        flags = list(qc.get("flags", []))
        flags.append("used_attribute_fallback")
        qc["flags"] = sorted(set(flags))
        return (
            FootprintHeight(
                geometry=geom,
                height=h,
                source=source,
                base_z=base_z,
                building_id=building_id,
                qc=qc,
            ),
            None,
        )

    return None, f"Missing point-cloud and fallback height for building_id={building_id}"


def derive_heights_from_point_cloud(
    laz_path: str,
    dtm_path: str,
    features: Iterable[Dict[str, Any]],
    percentile: int,
    min_height: float,
    max_height: float,
    floor_to_floor: float,
    z_to_meters: float,
    ndsm_path: str | None = None,
    clip_bounds: tuple[float, float, float, float] | None = None,
    roof_erode: float = 0.5,
    ground_ring_inner: float = 1.0,
    ground_ring_outer: float = 5.0,
    near_ground_cutoff_m: float = 2.0,
    min_ground_pts: int = 12,
    min_roof_pts: int = 15,
) -> tuple[List[FootprintHeight], List[str]]:
    if np is None:
        raise RuntimeError("numpy is required for point-cloud height extraction")
    if contains_xy is None or STRtree is None or unary_union is None:
        raise RuntimeError("shapely>=2 is required for point-cloud height extraction")

    warnings: List[str] = []
    records: list[dict[str, Any]] = []
    for feat in features:
        geom = feat.get("geometry")
        if geom is None:
            continue
        if make_valid is not None and not geom.is_valid:
            geom = make_valid(geom)
        if geom.is_empty:
            continue
        if geom.geom_type not in ("Polygon", "MultiPolygon"):
            continue
        props = feat.get("properties", {})
        core_geom = geom.buffer(-roof_erode)
        if core_geom.is_empty:
            core_geom = geom
        ring_geom = geom.buffer(ground_ring_outer).difference(geom.buffer(ground_ring_inner))
        query_geom = geom.buffer(ground_ring_outer)
        records.append(
            {
                "geometry": geom,
                "properties": props,
                "building_id": _building_id(props, geom),
                "core_geom": core_geom,
                "ring_geom": ring_geom,
                "query_bbox": query_geom.bounds,
            }
        )

    if not records:
        return [], ["No polygon footprints available for height extraction"]

    if len(records) > 1:
        geoms = [r["geometry"] for r in records]
        tree = STRtree(geoms)
        for idx, record in enumerate(records):
            ring_geom = record["ring_geom"]
            if ring_geom.is_empty:
                continue
            neighbor_idx = tree.query(ring_geom)
            neighbors = [geoms[i] for i in neighbor_idx if int(i) != idx]
            if neighbors:
                record["ring_geom"] = ring_geom.difference(unary_union(neighbors))

    minx = min(r["query_bbox"][0] for r in records)
    miny = min(r["query_bbox"][1] for r in records)
    maxx = max(r["query_bbox"][2] for r in records)
    maxy = max(r["query_bbox"][3] for r in records)
    point_bounds = (minx, miny, maxx, maxy)
    if clip_bounds is not None:
        point_bounds = (
            max(point_bounds[0], clip_bounds[0]),
            max(point_bounds[1], clip_bounds[1]),
            min(point_bounds[2], clip_bounds[2]),
            min(point_bounds[3], clip_bounds[3]),
        )
    if point_bounds[0] >= point_bounds[2] or point_bounds[1] >= point_bounds[3]:
        point_bounds = None

    x, y, z, cls = _extract_laz_points(laz_path, bounds=point_bounds)
    if x.size == 0:
        warnings.append("Point-cloud crop returned zero points; using fallback heights")
        results: list[FootprintHeight] = []
        for record in records:
            fallback, msg = _fallback_height_for_feature(
                geom=record["geometry"],
                properties=record["properties"],
                ndsm_path=ndsm_path,
                dtm_path=dtm_path,
                percentile=percentile,
                min_height=min_height,
                max_height=max_height,
                floor_to_floor=floor_to_floor,
                building_id=record["building_id"],
                extra_qc={"flags": ["no_lidar_points"]},
            )
            if fallback is not None:
                results.append(fallback)
            if msg:
                warnings.append(msg)
        return results, warnings

    sort_idx = np.argsort(x)
    x_sorted = x[sort_idx]
    near_ground_cutoff = near_ground_cutoff_m / z_to_meters if z_to_meters > 0 else 2.0

    results: list[FootprintHeight] = []
    for record in records:
        geom = record["geometry"]
        props = record["properties"]
        building_id = record["building_id"]
        cand_idx = _bbox_indices(x_sorted, sort_idx, y, record["query_bbox"])

        flags: list[str] = []
        if cand_idx.size == 0:
            flags.append("no_points_in_bbox")
            fallback, msg = _fallback_height_for_feature(
                geom=geom,
                properties=props,
                ndsm_path=ndsm_path,
                dtm_path=dtm_path,
                percentile=percentile,
                min_height=min_height,
                max_height=max_height,
                floor_to_floor=floor_to_floor,
                building_id=building_id,
                extra_qc={"flags": flags},
            )
            if fallback is not None:
                results.append(fallback)
            if msg:
                warnings.append(msg)
            continue

        px = x[cand_idx]
        py = y[cand_idx]
        pz = z[cand_idx]
        pc = cls[cand_idx]

        in_ring = np.asarray(contains_xy(record["ring_geom"], px, py), dtype=bool)
        ring_z = pz[in_ring]
        ring_cls = pc[in_ring]

        ground_info = _ground_estimate(
            ring_z,
            ring_cls,
            dtm_path=dtm_path,
            ring_geom=record["ring_geom"],
            min_ground_pts=min_ground_pts,
        )
        ground = ground_info["ground"]
        n_ground_pts = int(ground_info["n_ground_pts"])
        ground_method = str(ground_info["method"])
        if n_ground_pts < min_ground_pts:
            flags.append("low_ground_pts")
        if ground_method not in {"class2_median", "class2_p25"}:
            flags.append("used_ground_fallback")

        in_core = np.asarray(contains_xy(record["core_geom"], px, py), dtype=bool)
        core_z = pz[in_core]
        core_cls = pc[in_core]
        raw_roof_count = int(core_z.size)

        in_footprint = np.asarray(contains_xy(geom, px, py), dtype=bool)
        shell_count = int(np.count_nonzero(in_footprint & ~in_core))
        shell_ratio = (
            float(shell_count) / float(max(1, shell_count + raw_roof_count))
            if (shell_count + raw_roof_count) > 0
            else 0.0
        )
        if shell_ratio > 0.6:
            flags.append("possible_misalignment")

        if ground is not None:
            roof_mask = core_z > (ground + near_ground_cutoff)
        else:
            roof_mask = np.ones(core_z.shape[0], dtype=bool)
        if core_cls.size:
            roof_mask &= ~np.isin(core_cls, np.array([3, 4, 5], dtype=core_cls.dtype))
        roof_z = core_z[roof_mask]
        n_roof_pts = int(roof_z.size)
        if n_roof_pts < min_roof_pts:
            flags.append("low_roof_pts")

        roof_p95 = float(np.percentile(roof_z, 95)) if n_roof_pts else None
        roof_p99 = float(np.percentile(roof_z, 99)) if n_roof_pts else None
        roof_iqr = (
            float(np.percentile(roof_z, 75) - np.percentile(roof_z, 25))
            if n_roof_pts >= 4
            else None
        )

        height = None
        if roof_p95 is not None and ground is not None:
            height = roof_p95 - ground
            if height < 0:
                height = 0.0
                flags.append("negative_clamped")

        if roof_p95 is not None and roof_p99 is not None:
            if (roof_p99 - roof_p95) * z_to_meters > 2.5:
                flags.append("possible_tree_contamination")
        if ground_info["ground_iqr"] is not None:
            if float(ground_info["ground_iqr"]) * z_to_meters > 1.5:
                flags.append("steep_ground")

        if height is None:
            flags.append("insufficient_point_samples")
            fallback, msg = _fallback_height_for_feature(
                geom=geom,
                properties=props,
                ndsm_path=ndsm_path,
                dtm_path=dtm_path,
                percentile=percentile,
                min_height=min_height,
                max_height=max_height,
                floor_to_floor=floor_to_floor,
                building_id=building_id,
                extra_qc={
                    "flags": sorted(set(flags)),
                    "n_ground_pts": n_ground_pts,
                    "n_roof_pts": n_roof_pts,
                    "ground_method": ground_method,
                },
            )
            if fallback is not None:
                results.append(fallback)
            if msg:
                warnings.append(msg)
            continue

        height_m = height * z_to_meters
        if height_m < 2.0 or height_m > 120.0:
            flags.append("suspicious_height")

        results.append(
            FootprintHeight(
                geometry=geom,
                height=float(height),
                source="POINT_ROOF_P95",
                base_z=float(ground),
                building_id=building_id,
                qc={
                    "n_ground_pts": n_ground_pts,
                    "n_roof_pts": n_roof_pts,
                    "ground_method": ground_method,
                    "ground_median": ground_info["ground_median"],
                    "ground_iqr": ground_info["ground_iqr"],
                    "roof_p95": roof_p95,
                    "roof_p99": roof_p99,
                    "roof_iqr": roof_iqr,
                    "shell_ratio": shell_ratio,
                    "flags": sorted(set(flags)),
                },
            )
        )

    return results, warnings


def heights_to_geojson(
    heights: Iterable[FootprintHeight],
    *,
    z_to_meters: float,
) -> Dict[str, Any]:
    if mapping is None:
        raise RuntimeError("shapely is required for GeoJSON height export")
    features: list[dict[str, Any]] = []
    for row in heights:
        qc = row.qc or {}
        flags = qc.get("flags") or []
        if isinstance(flags, str):
            flags = [flags]

        roof_p95 = qc.get("roof_p95")
        roof_p99 = qc.get("roof_p99")
        ground_median = qc.get("ground_median")
        roof_iqr = qc.get("roof_iqr")
        ground_iqr = qc.get("ground_iqr")

        height_m = row.height * z_to_meters
        properties = {
            "building_id": row.building_id or _deterministic_building_id(row.geometry),
            "height_m": height_m,
            "height_ft": height_m * FEET_PER_METER,
            "ground_elev_m": row.base_z * z_to_meters,
            "roof_p95_m": (roof_p95 * z_to_meters) if roof_p95 is not None else None,
            "roof_p99_m": (roof_p99 * z_to_meters) if roof_p99 is not None else None,
            "ground_median_m": (ground_median * z_to_meters) if ground_median is not None else None,
            "roof_iqr_m": (roof_iqr * z_to_meters) if roof_iqr is not None else None,
            "ground_iqr_m": (ground_iqr * z_to_meters) if ground_iqr is not None else None,
            "n_roof_pts": qc.get("n_roof_pts"),
            "n_ground_pts": qc.get("n_ground_pts"),
            "ground_method": qc.get("ground_method"),
            "qc_flags": ";".join(sorted(set(flags))),
            "height_source": row.source,
        }
        features.append(
            {
                "type": "Feature",
                "geometry": mapping(row.geometry),
                "properties": properties,
            }
        )
    return {"type": "FeatureCollection", "features": features}


def write_heights_geojson(
    path: str,
    heights: Iterable[FootprintHeight],
    *,
    z_to_meters: float,
) -> None:
    collection = heights_to_geojson(heights, z_to_meters=z_to_meters)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(collection, f, indent=2, sort_keys=True)


def write_heights_csv(
    path: str,
    heights: Iterable[FootprintHeight],
    *,
    z_to_meters: float,
) -> None:
    fieldnames = [
        "building_id",
        "height_m",
        "height_ft",
        "ground_elev_m",
        "roof_p95_m",
        "roof_p99_m",
        "ground_median_m",
        "roof_iqr_m",
        "ground_iqr_m",
        "n_roof_pts",
        "n_ground_pts",
        "ground_method",
        "qc_flags",
        "height_source",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in heights:
            qc = row.qc or {}
            flags = qc.get("flags") or []
            if isinstance(flags, str):
                flags = [flags]
            roof_p95 = qc.get("roof_p95")
            roof_p99 = qc.get("roof_p99")
            ground_median = qc.get("ground_median")
            roof_iqr = qc.get("roof_iqr")
            ground_iqr = qc.get("ground_iqr")
            height_m = row.height * z_to_meters
            writer.writerow(
                {
                    "building_id": row.building_id or _deterministic_building_id(row.geometry),
                    "height_m": height_m,
                    "height_ft": height_m * FEET_PER_METER,
                    "ground_elev_m": row.base_z * z_to_meters,
                    "roof_p95_m": (roof_p95 * z_to_meters) if roof_p95 is not None else None,
                    "roof_p99_m": (roof_p99 * z_to_meters) if roof_p99 is not None else None,
                    "ground_median_m": (ground_median * z_to_meters)
                    if ground_median is not None
                    else None,
                    "roof_iqr_m": (roof_iqr * z_to_meters) if roof_iqr is not None else None,
                    "ground_iqr_m": (ground_iqr * z_to_meters) if ground_iqr is not None else None,
                    "n_roof_pts": qc.get("n_roof_pts"),
                    "n_ground_pts": qc.get("n_ground_pts"),
                    "ground_method": qc.get("ground_method"),
                    "qc_flags": ";".join(sorted(set(flags))),
                    "height_source": row.source,
                }
            )
