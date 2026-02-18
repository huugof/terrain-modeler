from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import laspy
import numpy as np
import tifffile
from matplotlib.path import Path as MplPath
from pyproj import CRS, Transformer
from shapely.geometry import MultiPolygon, Polygon


@dataclass(frozen=True)
class RasterMeta:
    transform: tuple[float, float, float, float, float, float]
    width: int
    height: int
    crs_wkt: str
    nodata: float = -9999.0


def _meta_path(path: Path) -> Path:
    return path.with_suffix(path.suffix + ".meta.json")


def save_raster_meta(path: Path, meta: RasterMeta) -> None:
    _meta_path(path).write_text(json.dumps(asdict(meta), indent=2, sort_keys=True))


def load_raster_meta(path: Path) -> RasterMeta:
    payload = json.loads(_meta_path(path).read_text())
    transform = payload.get("transform")
    if not isinstance(transform, list) or len(transform) != 6:
        raise ValueError(f"Invalid raster transform metadata for {path}")
    return RasterMeta(
        transform=tuple(float(v) for v in transform),
        width=int(payload["width"]),
        height=int(payload["height"]),
        crs_wkt=str(payload.get("crs_wkt", "")),
        nodata=float(payload.get("nodata", -9999.0)),
    )


def write_raster(path: Path, data: np.ndarray, meta: RasterMeta) -> Path:
    array = np.asarray(data, dtype=np.float32)
    if array.ndim != 2:
        raise ValueError("Raster array must be 2D")
    if array.shape[0] != meta.height or array.shape[1] != meta.width:
        raise ValueError("Raster data shape does not match metadata dimensions")
    path.parent.mkdir(parents=True, exist_ok=True)
    a, _b, c, _d, e, f = meta.transform
    pixel_scale = (abs(float(a)), abs(float(e)), 0.0)
    tiepoint = (0.0, 0.0, 0.0, float(c), float(f), 0.0)
    nodata_text = f"{meta.nodata}\x00"
    tifffile.imwrite(
        path,
        array,
        metadata=None,
        photometric="minisblack",
        extratags=[
            (33550, "d", 3, pixel_scale, False),  # ModelPixelScaleTag
            (33922, "d", 6, tiepoint, False),  # ModelTiepointTag
            (42113, "s", len(nodata_text), nodata_text, False),  # GDAL_NODATA
        ],
    )
    save_raster_meta(path, meta)
    return path


def read_raster(path: Path) -> np.ndarray:
    data = tifffile.imread(path)
    if data.ndim == 3:
        data = data[0]
    return np.asarray(data, dtype=np.float32)


def read_raster_with_meta(
    path: Path, meta: RasterMeta | None = None
) -> tuple[np.ndarray, RasterMeta]:
    resolved_meta = meta if meta is not None else load_raster_meta(path)
    data = read_raster(path)
    if data.shape != (resolved_meta.height, resolved_meta.width):
        raise ValueError(f"Raster shape mismatch for {path}")
    return data, resolved_meta


def raster_bounds(meta: RasterMeta) -> tuple[float, float, float, float]:
    a, b, c, d, e, f = meta.transform
    corners = [
        (0.0, 0.0),
        (0.0, float(meta.height)),
        (float(meta.width), 0.0),
        (float(meta.width), float(meta.height)),
    ]
    xs: list[float] = []
    ys: list[float] = []
    for col, row in corners:
        xs.append(a * col + b * row + c)
        ys.append(d * col + e * row + f)
    return (min(xs), min(ys), max(xs), max(ys))


def world_to_pixel(
    transform: tuple[float, float, float, float, float, float],
    x: np.ndarray | float,
    y: np.ndarray | float,
) -> tuple[np.ndarray | float, np.ndarray | float]:
    a, b, c, d, e, f = transform
    det = a * e - b * d
    if abs(det) < 1e-12:
        raise ValueError("Non-invertible affine transform")
    dx = np.asarray(x) - c
    dy = np.asarray(y) - f
    col = (e * dx - b * dy) / det
    row = (-d * dx + a * dy) / det
    if np.isscalar(x) and np.isscalar(y):
        return float(col), float(row)
    return col, row


def _laz_crs_wkt(las: laspy.LasData) -> str:
    parsed = las.header.parse_crs()
    if parsed is not None:
        try:
            return parsed.to_wkt()
        except Exception:
            pass
    records = list(las.header.vlrs)
    try:
        records.extend(list(las.header.evlrs or []))
    except Exception:
        pass
    for vlr in records:
        if getattr(vlr, "string", None):
            text = str(vlr.string).strip()
            if "GEOGCS" in text or "PROJCRS" in text or "COMPD_CS" in text:
                return text
        raw = getattr(vlr, "record_data", None)
        if isinstance(raw, bytes):
            try:
                text = raw.decode("utf-8", errors="ignore").strip()
            except Exception:
                continue
            if "GEOGCS" in text or "PROJCRS" in text or "COMPD_CS" in text:
                return text
    raise ValueError("LAZ CRS not found in header")


def _las_crs(las: laspy.LasData) -> CRS | None:
    parsed = las.header.parse_crs()
    if parsed is not None:
        return parsed
    try:
        return CRS.from_wkt(_laz_crs_wkt(las))
    except Exception:
        return None


def fill_nodata_raster(
    in_path: Path,
    out_path: Path,
    max_distance: float = 10.0,
    smoothing_iterations: int = 0,
    hard_fill: bool = False,
) -> tuple[Path, RasterMeta]:
    data, meta = read_raster_with_meta(in_path)
    nodata = float(meta.nodata)
    filled = data.copy()
    valid = np.isfinite(filled) & (filled != nodata)

    def _fill_iteration(arr: np.ndarray, valid_mask: np.ndarray) -> int:
        count = np.zeros(arr.shape, dtype=np.uint8)
        total = np.zeros(arr.shape, dtype=np.float64)

        src = valid_mask[:-1, :]
        dst = ~valid_mask[1:, :]
        sel = src & dst
        if np.any(sel):
            dst_total = total[1:, :]
            dst_count = count[1:, :]
            src_vals = arr[:-1, :]
            dst_total[sel] += src_vals[sel]
            dst_count[sel] += 1

        src = valid_mask[1:, :]
        dst = ~valid_mask[:-1, :]
        sel = src & dst
        if np.any(sel):
            dst_total = total[:-1, :]
            dst_count = count[:-1, :]
            src_vals = arr[1:, :]
            dst_total[sel] += src_vals[sel]
            dst_count[sel] += 1

        src = valid_mask[:, :-1]
        dst = ~valid_mask[:, 1:]
        sel = src & dst
        if np.any(sel):
            dst_total = total[:, 1:]
            dst_count = count[:, 1:]
            src_vals = arr[:, :-1]
            dst_total[sel] += src_vals[sel]
            dst_count[sel] += 1

        src = valid_mask[:, 1:]
        dst = ~valid_mask[:, :-1]
        sel = src & dst
        if np.any(sel):
            dst_total = total[:, :-1]
            dst_count = count[:, :-1]
            src_vals = arr[:, 1:]
            dst_total[sel] += src_vals[sel]
            dst_count[sel] += 1

        fill_mask = (~valid_mask) & (count > 0)
        if not np.any(fill_mask):
            return 0
        arr[fill_mask] = (total[fill_mask] / count[fill_mask]).astype(np.float32)
        valid_mask[fill_mask] = True
        return int(np.count_nonzero(fill_mask))

    max_steps = max(0, int(math.ceil(max_distance)))
    steps = 0
    while steps < max_steps:
        if _fill_iteration(filled, valid) == 0:
            break
        steps += 1

    if hard_fill:
        while True:
            if _fill_iteration(filled, valid) == 0:
                break

    if smoothing_iterations > 0:
        for _ in range(max(0, smoothing_iterations)):
            total = np.zeros(filled.shape, dtype=np.float64)
            count = np.zeros(filled.shape, dtype=np.uint8)
            for src_rows, src_cols, dst_rows, dst_cols in (
                (slice(None, -1), slice(None), slice(1, None), slice(None)),
                (slice(1, None), slice(None), slice(None, -1), slice(None)),
                (slice(None), slice(None, -1), slice(None), slice(1, None)),
                (slice(None), slice(1, None), slice(None), slice(None, -1)),
            ):
                src_valid = valid[src_rows, src_cols]
                total[dst_rows, dst_cols][src_valid] += filled[src_rows, src_cols][
                    src_valid
                ]
                count[dst_rows, dst_cols][src_valid] += 1
            smooth_mask = valid & (count > 0)
            filled[smooth_mask] = (total[smooth_mask] / count[smooth_mask]).astype(
                np.float32
            )

    filled[~valid] = nodata
    write_raster(out_path, filled.astype(np.float32), meta)
    return out_path, meta


def clip_raster(
    in_path: Path,
    out_path: Path,
    polygon,
) -> tuple[Path, RasterMeta]:
    data, meta = read_raster_with_meta(in_path)
    a, b, c, d, e, f = meta.transform
    nodata = float(meta.nodata)

    minx, miny, maxx, maxy = polygon.bounds
    bbox_cols: list[float] = []
    bbox_rows: list[float] = []
    for x, y in ((minx, miny), (minx, maxy), (maxx, miny), (maxx, maxy)):
        col, row = world_to_pixel(meta.transform, x, y)
        bbox_cols.append(float(col))
        bbox_rows.append(float(row))

    col_min = max(0, int(math.floor(min(bbox_cols))) - 1)
    row_min = max(0, int(math.floor(min(bbox_rows))) - 1)
    col_max = min(meta.width, int(math.ceil(max(bbox_cols))) + 2)
    row_max = min(meta.height, int(math.ceil(max(bbox_rows))) + 2)

    if col_min >= col_max or row_min >= row_max:
        raise ValueError("Clip polygon does not overlap raster bounds")

    crop = data[row_min:row_max, col_min:col_max].copy()
    cols = np.arange(col_min, col_max, dtype=np.float64) + 0.5
    rows = np.arange(row_min, row_max, dtype=np.float64) + 0.5
    col_grid, row_grid = np.meshgrid(cols, rows)
    xs = a * col_grid + b * row_grid + c
    ys = d * col_grid + e * row_grid + f
    points = np.column_stack((xs.ravel(), ys.ravel()))

    def _contains_points(poly: Polygon, pts: np.ndarray) -> np.ndarray:
        exterior = MplPath(np.asarray(poly.exterior.coords))
        inside = exterior.contains_points(pts)
        for ring in poly.interiors:
            hole = MplPath(np.asarray(ring.coords))
            inside &= ~hole.contains_points(pts)
        return inside

    mask_inside = np.zeros(points.shape[0], dtype=bool)
    if isinstance(polygon, Polygon):
        mask_inside |= _contains_points(polygon, points)
    elif isinstance(polygon, MultiPolygon):
        for poly in polygon.geoms:
            mask_inside |= _contains_points(poly, points)
    else:
        raise ValueError("Unsupported clip geometry type")
    mask_inside = mask_inside.reshape(crop.shape)
    if not np.any(mask_inside):
        raise ValueError("Clip polygon does not overlap raster bounds")
    crop[~mask_inside] = nodata

    new_transform = (
        a,
        b,
        a * col_min + b * row_min + c,
        d,
        e,
        d * col_min + e * row_min + f,
    )
    new_meta = RasterMeta(
        transform=new_transform,
        width=crop.shape[1],
        height=crop.shape[0],
        crs_wkt=meta.crs_wkt,
        nodata=nodata,
    )
    write_raster(out_path, crop.astype(np.float32), new_meta)
    return out_path, new_meta


def _classification_array(las: laspy.LasData) -> np.ndarray | None:
    try:
        return np.asarray(las.classification, dtype=np.uint8)
    except Exception:
        return None


def _rasterize_laz(
    laz_path: Path,
    out_path: Path,
    resolution: float,
    *,
    kind: str,
    crs_wkt_fallback: str | None = None,
) -> tuple[Path, RasterMeta]:
    if resolution <= 0:
        raise ValueError("resolution must be > 0")
    las = laspy.read(laz_path)
    x_all = np.asarray(las.x, dtype=np.float64)
    y_all = np.asarray(las.y, dtype=np.float64)
    z_all = np.asarray(las.z, dtype=np.float64)
    if x_all.size == 0:
        raise ValueError(f"No points found in {laz_path}")

    finite_all = np.isfinite(x_all) & np.isfinite(y_all) & np.isfinite(z_all)
    if not np.any(finite_all):
        raise ValueError(f"No finite points found in {laz_path}")

    x_all = x_all[finite_all]
    y_all = y_all[finite_all]
    z_all = z_all[finite_all]

    x_min = math.floor(float(np.min(x_all)) / resolution) * resolution
    y_top = math.ceil(float(np.max(y_all)) / resolution) * resolution
    col_all = ((x_all - x_min) / resolution).astype(np.int64)
    row_all = ((y_top - y_all) / resolution).astype(np.int64)
    width = int(np.max(col_all)) + 1
    height = int(np.max(row_all)) + 1

    mask = np.ones(x_all.shape[0], dtype=bool)
    classification = _classification_array(las)
    if kind == "ground":
        if classification is None:
            mask &= False
        else:
            cls = classification[finite_all]
            mask &= cls == 2
        agg = "min"
    elif kind == "dtm_unclassified":
        agg = "min"
    elif kind == "dsm":
        if classification is not None:
            cls = classification[finite_all]
            mask &= cls != 2
        agg = "max"
    else:
        raise ValueError(f"Unsupported rasterization kind: {kind}")

    nodata = -9999.0
    if agg == "min":
        grid = np.full((height, width), np.inf, dtype=np.float32)
    else:
        grid = np.full((height, width), -np.inf, dtype=np.float32)
    if np.any(mask):
        cols = col_all[mask]
        rows = row_all[mask]
        vals = z_all[mask].astype(np.float32)
        valid_idx = (
            (rows >= 0)
            & (rows < height)
            & (cols >= 0)
            & (cols < width)
            & np.isfinite(vals)
        )
        rows = rows[valid_idx]
        cols = cols[valid_idx]
        vals = vals[valid_idx]
        if vals.size:
            if agg == "min":
                np.minimum.at(grid, (rows, cols), vals)
            else:
                np.maximum.at(grid, (rows, cols), vals)

    if agg == "min":
        untouched = ~np.isfinite(grid)
    else:
        untouched = ~np.isfinite(grid)
    grid[untouched] = nodata

    try:
        crs_wkt = _laz_crs_wkt(las)
    except ValueError:
        if crs_wkt_fallback:
            crs_wkt = crs_wkt_fallback
        else:
            raise

    meta = RasterMeta(
        transform=(resolution, 0.0, x_min, 0.0, -resolution, y_top),
        width=width,
        height=height,
        crs_wkt=crs_wkt,
        nodata=nodata,
    )
    write_raster(out_path, grid, meta)
    return out_path, meta


def make_dtm(
    laz_path: Path,
    dtm_path: Path,
    resolution: float,
    *,
    crs_wkt_fallback: str | None = None,
) -> tuple[Path, RasterMeta]:
    return _rasterize_laz(
        laz_path,
        dtm_path,
        resolution,
        kind="ground",
        crs_wkt_fallback=crs_wkt_fallback,
    )


def make_dtm_unclassified(
    laz_path: Path,
    dtm_path: Path,
    resolution: float,
    *,
    crs_wkt_fallback: str | None = None,
) -> tuple[Path, RasterMeta]:
    return _rasterize_laz(
        laz_path,
        dtm_path,
        resolution,
        kind="dtm_unclassified",
        crs_wkt_fallback=crs_wkt_fallback,
    )


def raster_has_data(path: Path, meta: RasterMeta | None = None) -> bool:
    data, resolved_meta = read_raster_with_meta(path, meta=meta)
    nodata = float(resolved_meta.nodata)
    return bool(np.any((data != nodata) & np.isfinite(data)))


def make_dsm(
    laz_path: Path,
    dsm_path: Path,
    resolution: float,
    *,
    crs_wkt_fallback: str | None = None,
) -> tuple[Path, RasterMeta]:
    return _rasterize_laz(
        laz_path,
        dsm_path,
        resolution,
        kind="dsm",
        crs_wkt_fallback=crs_wkt_fallback,
    )


def make_ndsm(
    dsm_path: Path,
    dtm_path: Path,
    ndsm_path: Path,
    *,
    dsm_meta: RasterMeta | None = None,
    dtm_meta: RasterMeta | None = None,
) -> tuple[Path, RasterMeta]:
    dsm, dsm_resolved_meta = read_raster_with_meta(dsm_path, dsm_meta)
    dtm, dtm_resolved_meta = read_raster_with_meta(dtm_path, dtm_meta)
    if dsm.shape != dtm.shape:
        raise ValueError(
            f"DSM/DTM shape mismatch: dsm={dsm.shape} dtm={dtm.shape}; expected identical grids"
        )
    if dsm_resolved_meta.transform != dtm_resolved_meta.transform:
        raise ValueError("DSM/DTM transform mismatch; expected identical grids")
    nodata = float(dsm_resolved_meta.nodata)
    dtm_nodata = float(dtm_resolved_meta.nodata)
    mask = (dsm == nodata) | (dtm == dtm_nodata) | ~np.isfinite(dsm) | ~np.isfinite(dtm)
    ndsm = (dsm - dtm).astype(np.float32)
    ndsm[mask] = nodata
    out_meta = RasterMeta(
        transform=dsm_resolved_meta.transform,
        width=dsm_resolved_meta.width,
        height=dsm_resolved_meta.height,
        crs_wkt=dsm_resolved_meta.crs_wkt,
        nodata=nodata,
    )
    write_raster(ndsm_path, ndsm, out_meta)
    return ndsm_path, out_meta


def _merged_scales(
    xs: np.ndarray, ys: np.ndarray, zs: np.ndarray
) -> tuple[float, float, float]:
    int_limit = 2_000_000_000.0
    span_x = max(1.0, float(np.max(xs) - np.min(xs)))
    span_y = max(1.0, float(np.max(ys) - np.min(ys)))
    span_z = max(1.0, float(np.max(zs) - np.min(zs)))
    sx = max(0.001, span_x / int_limit)
    sy = max(0.001, span_y / int_limit)
    sz = max(0.001, span_z / int_limit)
    return (sx, sy, sz)


def merge_lazs(
    laz_paths: list[Path],
    merged_path: Path,
    target_srs: str | None = None,
) -> Path:
    if not laz_paths:
        raise ValueError("No LAZ files provided for merge")
    if len(laz_paths) == 1:
        return laz_paths[0]

    target_crs: CRS | None = CRS.from_wkt(target_srs) if target_srs else None
    merged_x: list[np.ndarray] = []
    merged_y: list[np.ndarray] = []
    merged_z: list[np.ndarray] = []
    merged_cls: list[np.ndarray] = []
    source_crs_for_output: CRS | None = target_crs

    for laz_path in laz_paths:
        las = laspy.read(laz_path)
        x = np.asarray(las.x, dtype=np.float64)
        y = np.asarray(las.y, dtype=np.float64)
        z = np.asarray(las.z, dtype=np.float64)
        src_crs = _las_crs(las)
        if source_crs_for_output is None and src_crs is not None:
            source_crs_for_output = src_crs
        if (
            target_crs is not None
            and src_crs is not None
            and not src_crs.equals(target_crs)
        ):
            transformer = Transformer.from_crs(src_crs, target_crs, always_xy=True)
            x, y, z = transformer.transform(x, y, z)
        cls = _classification_array(las)
        if cls is None:
            cls = np.zeros(x.shape[0], dtype=np.uint8)
        merged_x.append(x)
        merged_y.append(y)
        merged_z.append(z)
        merged_cls.append(cls.astype(np.uint8, copy=False))

    xs = np.concatenate(merged_x)
    ys = np.concatenate(merged_y)
    zs = np.concatenate(merged_z)
    clss = np.concatenate(merged_cls)

    header = laspy.LasHeader(point_format=3, version="1.2")
    header.offsets = np.array([float(np.min(xs)), float(np.min(ys)), float(np.min(zs))])
    header.scales = np.array(_merged_scales(xs, ys, zs))
    if source_crs_for_output is not None:
        try:
            header.add_crs(source_crs_for_output)
        except Exception:
            pass
    merged = laspy.LasData(header)
    merged.x = xs
    merged.y = ys
    merged.z = zs
    merged.classification = clss
    merged.write(merged_path)
    return merged_path
