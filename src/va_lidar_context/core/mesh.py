from __future__ import annotations

import math
from typing import List, Optional, Tuple

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def export_terrain_xyz(
    raster_path: str,
    output_path: str,
    xy_scale: float = 1.0,
    z_scale: float = 1.0,
    sample: int = 1,
    origin: Optional[tuple[float, float]] = None,
    rotate_deg: float = 0.0,
) -> int:
    """Export terrain grid points to an XYZ point cloud file.

    Reads the DTM raster and writes one ``X Y Z`` line per valid cell.
    When *origin* ``(x, y)`` is given (in **scaled** output units) it is
    subtracted from every point so the file is centred on that location.
    Returns the number of points written.
    """
    import rasterio

    if sample < 1:
        raise ValueError("sample must be >= 1")

    with rasterio.open(raster_path) as ds:
        data = ds.read(1)
        nodata = ds.nodata if ds.nodata is not None else -9999
        transform = ds.transform

    if sample > 1:
        data = data[::sample, ::sample]
        transform = transform * rasterio.Affine.scale(sample, sample)

    rows, cols = data.shape
    mask_valid = (data != nodata) & np.isfinite(data)

    col_idx = np.arange(cols, dtype=np.float64)
    row_idx = np.arange(rows, dtype=np.float64)
    col_grid, row_grid = np.meshgrid(col_idx, row_idx)

    x_all = transform.a * (col_grid + 0.5) + transform.b * (row_grid + 0.5) + transform.c
    y_all = transform.d * (col_grid + 0.5) + transform.e * (row_grid + 0.5) + transform.f

    flat_mask = mask_valid.ravel()
    x = x_all.ravel()[flat_mask] * xy_scale
    y = y_all.ravel()[flat_mask] * xy_scale
    z = data.ravel()[flat_mask].astype(np.float64) * z_scale

    ox = origin[0] if origin else 0.0
    oy = origin[1] if origin else 0.0
    x -= ox
    y -= oy

    if rotate_deg:
        theta = math.radians(rotate_deg)
        c, s = math.cos(theta), math.sin(theta)
        x, y = x * c - y * s, x * s + y * c

    np.savetxt(output_path, np.column_stack([x, y, z]), fmt="%.4f")
    return int(flat_mask.sum())


def generate_contours_from_raster(
    raster_path: str,
    interval: float,
    xy_scale: float = 1.0,
    z_scale: float = 1.0,
    sample: int = 1,
    origin: Optional[tuple[float, float]] = None,
    rotate_deg: float = 0.0,
) -> List[Tuple[float, List[np.ndarray]]]:
    """Generate contour polylines from a raster at the given interval.

    When *origin* ``(x, y)`` is given (in **scaled** output units) it is
    subtracted from every point so the output is centred on that location.
    Returns a list of (elevation, [polylines]) tuples.
    """
    import rasterio

    with rasterio.open(raster_path) as ds:
        data = ds.read(1)
        nodata = ds.nodata if ds.nodata is not None else -9999
        transform = ds.transform

    if sample > 1:
        data = data[::sample, ::sample]
        transform = transform * rasterio.Affine.scale(sample, sample)

    data = np.where((data == nodata) | ~np.isfinite(data), np.nan, data)

    rows, cols = data.shape
    if rows < 2 or cols < 2:
        return []

    col_indices = np.arange(cols)
    row_indices = np.arange(rows)
    col_grid, row_grid = np.meshgrid(col_indices, row_indices)

    x_grid = (
        transform.a * (col_grid + 0.5) + transform.b * (row_grid + 0.5) + transform.c
    )
    y_grid = (
        transform.d * (col_grid + 0.5) + transform.e * (row_grid + 0.5) + transform.f
    )

    valid_data = data[np.isfinite(data)]
    if valid_data.size == 0:
        return []

    z_min = float(np.floor(valid_data.min() / interval) * interval)
    z_max = float(np.ceil(valid_data.max() / interval) * interval)
    levels = np.arange(z_min, z_max + interval, interval)

    fig, ax = plt.subplots()
    cs = ax.contour(x_grid, y_grid, data, levels=levels)
    plt.close(fig)

    results: List[Tuple[float, List[np.ndarray]]] = []
    theta = math.radians(rotate_deg)
    c = math.cos(theta)
    s = math.sin(theta)
    for level_idx, level in enumerate(cs.levels):
        polylines: List[np.ndarray] = []
        for path in cs.allsegs[level_idx]:
            if len(path) < 2:
                continue
            ox = origin[0] if origin else 0.0
            oy = origin[1] if origin else 0.0
            scaled = np.zeros((len(path), 3))
            px = path[:, 0] * xy_scale - ox
            py = path[:, 1] * xy_scale - oy
            if rotate_deg:
                scaled[:, 0] = px * c - py * s
                scaled[:, 1] = px * s + py * c
            else:
                scaled[:, 0] = px
                scaled[:, 1] = py
            scaled[:, 2] = level * z_scale
            polylines.append(scaled)
        if polylines:
            results.append((level * z_scale, polylines))

    return results


def _resample_polyline(
    points: np.ndarray, spacing: float
) -> list[tuple[float, float, float]]:
    if spacing <= 0 or len(points) < 2:
        return [tuple(p) for p in points]

    pts = np.asarray(points, dtype=float)
    seg = np.diff(pts[:, :2], axis=0)
    seg_len = np.hypot(seg[:, 0], seg[:, 1])
    total = float(seg_len.sum())
    if total == 0.0:
        return [tuple(pts[0])]

    cum = np.concatenate(([0.0], np.cumsum(seg_len)))
    targets = np.arange(0.0, total, spacing)
    if total - targets[-1] > 1e-6:
        targets = np.append(targets, total)

    out: list[tuple[float, float, float]] = []
    for t in targets:
        idx = int(np.searchsorted(cum, t, side="right") - 1)
        if idx >= len(seg_len):
            idx = len(seg_len) - 1
        seg_total = seg_len[idx]
        if seg_total == 0.0:
            pt = pts[idx]
        else:
            ratio = (t - cum[idx]) / seg_total
            pt = pts[idx] + (pts[idx + 1] - pts[idx]) * ratio
        out.append((float(pt[0]), float(pt[1]), float(pt[2])))
    return out


def export_contours_xyz(
    contours: List[Tuple[float, List[np.ndarray]]],
    output_path: str,
    spacing: float | None = None,
) -> int:
    """Export contour polylines as XYZ points.

    When spacing is provided (> 0), resample points uniformly along each contour.
    """
    count = 0
    spacing_value = spacing or 0.0
    with open(output_path, "w") as f:
        for _elevation, polylines in contours:
            for polyline in polylines:
                if spacing_value > 0:
                    points = _resample_polyline(polyline, spacing_value)
                else:
                    points = [tuple(p) for p in polyline]
                for x, y, z in points:
                    f.write(f"{x} {y} {z}\n")
                    count += 1
    return count


def resample_contours(
    contours: List[Tuple[float, List[np.ndarray]]],
    spacing: float,
) -> List[Tuple[float, List[np.ndarray]]]:
    """Resample contour polylines to a uniform spacing in XY."""
    if spacing <= 0:
        return contours
    results: List[Tuple[float, List[np.ndarray]]] = []
    for elevation, polylines in contours:
        resampled: List[np.ndarray] = []
        for polyline in polylines:
            points = _resample_polyline(polyline, spacing)
            if len(points) < 2:
                continue
            resampled.append(np.array(points, dtype=float))
        if resampled:
            results.append((elevation, resampled))
    return results


class DxfExporter:
    """Unified DXF exporter — writes raw DXF R12 (AC1009) for maximum speed."""

    def __init__(self):
        self._layers: dict[str, int] = {}
        self._chunks: list[str] = []
        self._layer_colors = {
            "CONTOURS": 8,
            "PARCELS": 3,
            "BUILDINGS": 5,
            "origin": 1,
            "north": 2,
        }

    def _ensure_layer(self, name: str, color: int = None) -> None:
        if name not in self._layers:
            self._layers[name] = color or self._layer_colors.get(name, 7)

    def _add_polyline3d(self, layer: str, points: list, close: bool = False) -> None:
        flag = 9 if close else 8  # bit 0=closed, bit 3=3D polyline
        parts = [f"  0\nPOLYLINE\n  8\n{layer}\n 66\n     1\n 70\n     {flag}\n"]
        for x, y, z in points:
            parts.append(
                f"  0\nVERTEX\n  8\n{layer}\n"
                f" 10\n{x:.4f}\n 20\n{y:.4f}\n 30\n{z:.4f}\n 70\n    32\n"
            )
        parts.append(f"  0\nSEQEND\n  8\n{layer}\n")
        self._chunks.append("".join(parts))

    def _add_line(self, layer: str, p1: tuple, p2: tuple) -> None:
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        self._chunks.append(
            f"  0\nLINE\n  8\n{layer}\n"
            f" 10\n{x1:.4f}\n 20\n{y1:.4f}\n 30\n{z1:.4f}\n"
            f" 11\n{x2:.4f}\n 21\n{y2:.4f}\n 31\n{z2:.4f}\n"
        )

    def add_contours(
        self,
        contours: List[Tuple[float, List[np.ndarray]]],
        layer_prefix: str = "CONTOUR",
        major_interval: float = None,
    ) -> int:
        """Add contour lines to the DXF. Returns total polylines added."""
        count = 0
        for elevation, polylines in contours:
            if major_interval and abs(elevation % major_interval) < 0.01:
                layer_name = f"{layer_prefix}_MAJOR"
                color = 7
            else:
                layer_name = f"{layer_prefix}_MINOR"
                color = 8
            self._ensure_layer(layer_name, color)
            for polyline in polylines:
                self._add_polyline3d(layer_name, [(p[0], p[1], p[2]) for p in polyline])
                count += 1
        return count

    def add_polygons_from_geojson(
        self,
        geojson: dict,
        layer_name: str,
        xy_scale: float = 1.0,
        transform_func=None,
        z_value: float = 0.0,
        color: int = None,
        origin: Optional[tuple[float, float]] = None,
        clip_boundary=None,
        rotate_deg: float = 0.0,
    ) -> int:
        """Add polygons from a GeoJSON FeatureCollection. Returns count added."""
        from shapely.geometry import GeometryCollection, MultiPolygon, Polygon, shape
        from shapely.ops import transform as shp_transform

        self._ensure_layer(layer_name, color)

        count = 0
        theta = math.radians(rotate_deg)
        c = math.cos(theta)
        s = math.sin(theta)
        for feature in geojson.get("features", []):
            try:
                geom = shape(feature["geometry"])
            except Exception:
                continue

            if geom.geom_type == "Polygon":
                polygons = [geom]
            elif geom.geom_type == "MultiPolygon":
                polygons = list(geom.geoms)
            else:
                continue

            for poly in polygons:
                geom = poly
                if transform_func:
                    try:
                        geom = shp_transform(
                            lambda x, y, z=None: transform_func(x, y), geom
                        )
                    except Exception:
                        continue

                if clip_boundary is not None:
                    try:
                        geom = geom.intersection(clip_boundary)
                    except Exception:
                        continue

                if geom.is_empty:
                    continue

                if isinstance(geom, Polygon):
                    clipped_polys = [geom]
                elif isinstance(geom, MultiPolygon):
                    clipped_polys = list(geom.geoms)
                elif isinstance(geom, GeometryCollection):
                    clipped_polys = [g for g in geom.geoms if isinstance(g, Polygon)]
                else:
                    continue

                for clipped in clipped_polys:
                    coords = list(clipped.exterior.coords)
                    ox = origin[0] if origin else 0.0
                    oy = origin[1] if origin else 0.0
                    points = []
                    for cx, cy in coords:
                        px = cx * xy_scale - ox
                        py = cy * xy_scale - oy
                        if rotate_deg:
                            rx = px * c - py * s
                            ry = px * s + py * c
                        else:
                            rx, ry = px, py
                        points.append((rx, ry, z_value))
                    if len(points) >= 3:
                        self._add_polyline3d(layer_name, points, close=True)
                        count += 1

        return count

    def add_cross(
        self,
        center: tuple[float, float, float],
        size: float = 50.0,
        layer_name: str = "origin",
        color: int | None = None,
    ) -> None:
        """Add a simple cross marker centered at the given point."""
        self._ensure_layer(layer_name, color)
        x, y, z = center
        half = size / 2.0
        self._add_line(layer_name, (x - half, y, z), (x + half, y, z))
        self._add_line(layer_name, (x, y - half, z), (x, y + half, z))

    def add_north_arrow(
        self,
        base: tuple[float, float, float],
        length: float = 75.0,
        head_length: float = 15.0,
        head_angle_deg: float = 25.0,
        layer_name: str = "north",
        color: int | None = None,
    ) -> None:
        """Add a one-sided north arrow pointing +Y."""
        self._ensure_layer(layer_name, color)
        x, y, z = base
        tip = (x, y + length, z)
        self._add_line(layer_name, (x, y, z), tip)
        angle = math.radians(head_angle_deg)
        dx = head_length * math.sin(angle)
        dy = head_length * math.cos(angle)
        left = (tip[0] - dx, tip[1] - dy, z)
        right = (tip[0] + dx, tip[1] - dy, z)
        self._add_line(layer_name, tip, left)
        self._add_line(layer_name, tip, right)

    def save(self, output_path: str) -> None:
        """Write DXF R12 file directly as text — no ezdxf object model overhead."""
        with open(output_path, "w", buffering=8 * 1024 * 1024) as f:
            f.write(
                "  0\nSECTION\n  2\nHEADER\n"
                "  9\n$ACADVER\n  1\nAC1009\n"
                "  0\nENDSEC\n"
                f"  0\nSECTION\n  2\nTABLES\n"
                f"  0\nTABLE\n  2\nLAYER\n 70\n{len(self._layers)}\n"
            )
            for name, color in self._layers.items():
                f.write(
                    f"  0\nLAYER\n  2\n{name}\n 70\n0\n 62\n{color}\n  6\nContinuous\n"
                )
            f.write("  0\nENDTAB\n  0\nENDSEC\n  0\nSECTION\n  2\nENTITIES\n")
            for chunk in self._chunks:
                f.write(chunk)
            f.write("  0\nENDSEC\n  0\nEOF\n")
