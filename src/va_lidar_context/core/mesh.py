from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import trimesh
from shapely.affinity import scale as scale_geom
from shapely.validation import make_valid

from .heights import FootprintHeight


def extrude_footprints(
    footprints: Iterable[FootprintHeight],
    xy_scale: float = 1.0,
    z_scale: float = 1.0,
) -> Optional[trimesh.Trimesh]:
    """Extrude footprint polygons into a combined trimesh mesh."""
    try:
        import mapbox_earcut  # noqa: F401

        engine = "earcut"
    except Exception:  # pragma: no cover
        engine = None

    meshes: List[trimesh.Trimesh] = []
    for fp in footprints:
        geom = fp.geometry
        if xy_scale != 1.0:
            geom = scale_geom(geom, xfact=xy_scale, yfact=xy_scale, origin=(0, 0))
        if not geom.is_valid:
            geom = make_valid(geom)
        if geom.is_empty:
            continue
        height = fp.height * z_scale
        base_z = fp.base_z * z_scale
        if geom.geom_type == "Polygon":
            geoms = [geom]
        elif geom.geom_type == "MultiPolygon":
            geoms = list(geom.geoms)
        else:
            continue
        for g in geoms:
            try:
                mesh = trimesh.creation.extrude_polygon(g, height, engine=engine)
            except Exception:
                continue
            if base_z != 0.0:
                mesh.apply_translation((0.0, 0.0, base_z))
            meshes.append(mesh)
    if not meshes:
        return None
    return trimesh.util.concatenate(meshes)


def export_mesh(mesh: trimesh.Trimesh, path: str) -> None:
    """Export a mesh to the given path."""
    mesh.export(path)


def combine_meshes(meshes: List[trimesh.Trimesh]) -> Optional[trimesh.Trimesh]:
    """Concatenate multiple meshes into one."""
    valid = [m for m in meshes if m is not None]
    if not valid:
        return None
    return trimesh.util.concatenate(valid)


def apply_scene_transform(
    mesh: Optional[trimesh.Trimesh],
    center_x: float,
    center_y: float,
    flip_x: bool = False,
    flip_y: bool = False,
    rotate_deg: float = 0.0,
) -> None:
    """Apply flip/rotate transforms around a scene center."""
    if mesh is None:
        return

    to_origin = np.array(
        [
            [1.0, 0.0, 0.0, -center_x],
            [0.0, 1.0, 0.0, -center_y],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        dtype=float,
    )

    sx = -1.0 if flip_x else 1.0
    sy = -1.0 if flip_y else 1.0
    scale = np.array(
        [
            [sx, 0.0, 0.0, 0.0],
            [0.0, sy, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        dtype=float,
    )

    theta = np.deg2rad(rotate_deg)
    c = float(np.cos(theta))
    s = float(np.sin(theta))
    rot = np.array(
        [
            [c, -s, 0.0, 0.0],
            [s, c, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        dtype=float,
    )

    from_origin = np.array(
        [
            [1.0, 0.0, 0.0, center_x],
            [0.0, 1.0, 0.0, center_y],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        dtype=float,
    )

    transform = from_origin @ rot @ scale @ to_origin
    mesh.apply_transform(transform)


def terrain_mesh_from_raster(
    raster_path: str,
    xy_scale: float = 1.0,
    z_scale: float = 1.0,
    sample: int = 1,
) -> Optional[trimesh.Trimesh]:
    """Generate a terrain mesh from a raster heightmap."""
    try:
        import numpy as np
        import rasterio
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("numpy and rasterio are required for terrain mesh") from exc

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
    if rows < 2 or cols < 2:
        return None

    mask_valid = (data != nodata) & np.isfinite(data)

    idx_grid = -np.ones((rows, cols), dtype=int)
    vertices: List[List[float]] = []

    for r in range(rows):
        for c in range(cols):
            if not mask_valid[r, c]:
                continue
            x = transform.a * (c + 0.5) + transform.b * (r + 0.5) + transform.c
            y = transform.d * (c + 0.5) + transform.e * (r + 0.5) + transform.f
            z = float(data[r, c])
            vertices.append([x * xy_scale, y * xy_scale, z * z_scale])
            idx_grid[r, c] = len(vertices) - 1

    faces: List[List[int]] = []
    for r in range(rows - 1):
        for c in range(cols - 1):
            v00 = idx_grid[r, c]
            v10 = idx_grid[r, c + 1]
            v01 = idx_grid[r + 1, c]
            v11 = idx_grid[r + 1, c + 1]
            if v00 < 0 or v10 < 0 or v01 < 0 or v11 < 0:
                continue
            faces.append([v00, v10, v01])
            faces.append([v10, v11, v01])

    if not faces:
        return None

    return trimesh.Trimesh(vertices=vertices, faces=faces, process=False)


def export_obj_with_uv(
    mesh: trimesh.Trimesh,
    uv: "list[list[float]]",
    obj_path: str,
    mtl_path: str,
    texture_filename: str,
) -> None:
    """Export an OBJ with UV coordinates and an MTL texture reference."""
    with open(obj_path, "w") as f:
        f.write(f"mtllib {Path(mtl_path).name}\n")
        f.write("o terrain\n")
        for v in mesh.vertices:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for t in uv:
            f.write(f"vt {t[0]} {t[1]}\n")
        f.write("usemtl material0\n")
        for face in mesh.faces:
            v1, v2, v3 = face
            f.write(f"f {v1 + 1}/{v1 + 1} {v2 + 1}/{v2 + 1} {v3 + 1}/{v3 + 1}\n")

    with open(mtl_path, "w") as m:
        m.write("newmtl material0\n")
        m.write("Ka 1.000 1.000 1.000\n")
        m.write("Kd 1.000 1.000 1.000\n")
        m.write("Ks 0.000 0.000 0.000\n")
        m.write(f"map_Kd {texture_filename}\n")


def export_scene_with_terrain_texture(
    terrain_mesh: trimesh.Trimesh,
    terrain_uv: "list[list[float]]",
    buildings_mesh: Optional[trimesh.Trimesh],
    obj_path: str,
    mtl_path: str,
    texture_filename: str,
) -> None:
    """Export a combined terrain + buildings scene with terrain UVs."""
    t_verts = terrain_mesh.vertices
    t_faces = terrain_mesh.faces
    b_verts = buildings_mesh.vertices if buildings_mesh is not None else []
    b_faces = buildings_mesh.faces if buildings_mesh is not None else []
    t_count = len(t_verts)

    with open(obj_path, "w") as f:
        f.write(f"mtllib {Path(mtl_path).name}\n")
        f.write("o terrain\n")
        for v in t_verts:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for v in b_verts:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for t in terrain_uv:
            f.write(f"vt {t[0]} {t[1]}\n")
        if len(b_verts):
            # Provide dummy UVs for buildings to keep face formats consistent
            for _ in b_verts:
                f.write("vt 0.0 0.0\n")
        f.write("usemtl terrain\n")
        for face in t_faces:
            v1, v2, v3 = face
            f.write(f"f {v1 + 1}/{v1 + 1} {v2 + 1}/{v2 + 1} {v3 + 1}/{v3 + 1}\n")
        if len(b_faces):
            f.write("o buildings\n")
            f.write("usemtl buildings\n")
            for face in b_faces:
                v1, v2, v3 = face
                f.write(
                    f"f {v1 + 1 + t_count}/{v1 + 1 + t_count} "
                    f"{v2 + 1 + t_count}/{v2 + 1 + t_count} "
                    f"{v3 + 1 + t_count}/{v3 + 1 + t_count}\n"
                )

    with open(mtl_path, "w") as m:
        m.write("newmtl terrain\n")
        m.write("Ka 1.000 1.000 1.000\n")
        m.write("Kd 1.000 1.000 1.000\n")
        m.write("Ks 0.000 0.000 0.000\n")
        m.write(f"map_Kd {texture_filename}\n")
        m.write("newmtl buildings\n")
        m.write("Ka 0.800 0.800 0.800\n")
        m.write("Kd 0.800 0.800 0.800\n")
        m.write("Ks 0.000 0.000 0.000\n")


def generate_contours_from_raster(
    raster_path: str,
    interval: float,
    xy_scale: float = 1.0,
    z_scale: float = 1.0,
    sample: int = 1,
) -> List[Tuple[float, List[np.ndarray]]]:
    """
    Generate contour polylines from a raster at the given interval.

    Returns a list of (elevation, [polylines]) tuples where each polyline
    is an Nx2 or Nx3 numpy array of coordinates.
    """
    import rasterio

    with rasterio.open(raster_path) as ds:
        data = ds.read(1)
        nodata = ds.nodata if ds.nodata is not None else -9999
        transform = ds.transform

    if sample > 1:
        data = data[::sample, ::sample]
        transform = transform * rasterio.Affine.scale(sample, sample)

    # Mask nodata
    data = np.where((data == nodata) | ~np.isfinite(data), np.nan, data)

    rows, cols = data.shape
    if rows < 2 or cols < 2:
        return []

    # Create coordinate grids
    col_indices = np.arange(cols)
    row_indices = np.arange(rows)
    col_grid, row_grid = np.meshgrid(col_indices, row_indices)

    # Transform to world coordinates
    x_grid = (
        transform.a * (col_grid + 0.5) + transform.b * (row_grid + 0.5) + transform.c
    )
    y_grid = (
        transform.d * (col_grid + 0.5) + transform.e * (row_grid + 0.5) + transform.f
    )

    # Determine contour levels
    valid_data = data[np.isfinite(data)]
    if valid_data.size == 0:
        return []

    z_min = float(np.floor(valid_data.min() / interval) * interval)
    z_max = float(np.ceil(valid_data.max() / interval) * interval)
    levels = np.arange(z_min, z_max + interval, interval)

    # Generate contours using matplotlib (non-display mode)
    fig, ax = plt.subplots()
    cs = ax.contour(x_grid, y_grid, data, levels=levels)
    plt.close(fig)

    results: List[Tuple[float, List[np.ndarray]]] = []
    for level_idx, level in enumerate(cs.levels):
        polylines: List[np.ndarray] = []
        for path in cs.allsegs[level_idx]:
            if len(path) < 2:
                continue
            # Scale coordinates and add Z
            scaled = np.zeros((len(path), 3))
            scaled[:, 0] = path[:, 0] * xy_scale
            scaled[:, 1] = path[:, 1] * xy_scale
            scaled[:, 2] = level * z_scale
            polylines.append(scaled)
        if polylines:
            results.append((level * z_scale, polylines))

    return results


def export_contours_dxf(
    contours: List[Tuple[float, List[np.ndarray]]],
    output_path: str,
    layer_prefix: str = "CONTOUR",
) -> None:
    """
    Export contours to a DXF file.

    Each elevation gets its own layer named {layer_prefix}_{elevation}.
    """
    import ezdxf

    doc = ezdxf.new("R2010")
    msp = doc.modelspace()

    for elevation, polylines in contours:
        layer_name = f"{layer_prefix}_{elevation:.1f}"
        if layer_name not in doc.layers:
            doc.layers.new(name=layer_name)

        for polyline in polylines:
            points = [(p[0], p[1], p[2]) for p in polyline]
            msp.add_polyline3d(points, dxfattribs={"layer": layer_name})

    doc.saveas(output_path)


def export_parcels_dxf(
    parcels_geojson: dict,
    output_path: str,
    xy_scale: float = 1.0,
    transform_func=None,
    layer_name: str = "PARCELS",
) -> int:
    """
    Export parcel boundaries to a DXF file.

    Args:
        parcels_geojson: GeoJSON FeatureCollection with parcel polygons
        output_path: Path to output DXF file
        xy_scale: Scale factor for coordinates
        transform_func: Optional function to transform (lon, lat) -> (x, y)
        layer_name: DXF layer name

    Returns:
        Number of parcels exported
    """
    import ezdxf
    from shapely.geometry import shape

    doc = ezdxf.new("R2010")
    msp = doc.modelspace()
    doc.layers.new(name=layer_name)

    count = 0
    for feature in parcels_geojson.get("features", []):
        geom = shape(feature["geometry"])

        if geom.geom_type == "Polygon":
            polygons = [geom]
        elif geom.geom_type == "MultiPolygon":
            polygons = list(geom.geoms)
        else:
            continue

        for poly in polygons:
            # Get exterior ring
            coords = list(poly.exterior.coords)
            if transform_func:
                coords = [transform_func(c[0], c[1]) for c in coords]
            points = [(c[0] * xy_scale, c[1] * xy_scale, 0) for c in coords]
            if len(points) >= 3:
                msp.add_polyline3d(points, close=True, dxfattribs={"layer": layer_name})
                count += 1

    doc.saveas(output_path)
    return count


class DxfExporter:
    """
    Unified DXF exporter that combines multiple layers into a single file.
    """

    def __init__(self):
        import ezdxf

        self.doc = ezdxf.new("R2010")
        self.msp = self.doc.modelspace()
        self._layer_colors = {
            "CONTOURS": 8,  # Gray
            "PARCELS": 3,  # Green
            "BUILDINGS": 5,  # Blue
            "origin": 1,  # Red
            "north": 2,  # Yellow
        }

    def _ensure_layer(self, name: str, color: int = None) -> None:
        if name not in self.doc.layers:
            layer_color = color or self._layer_colors.get(name, 7)
            self.doc.layers.new(name=name, dxfattribs={"color": layer_color})

    def add_contours(
        self,
        contours: List[Tuple[float, List[np.ndarray]]],
        layer_prefix: str = "CONTOUR",
        major_interval: float = None,
    ) -> int:
        """
        Add contour lines to the DXF.

        Args:
            contours: List of (elevation, [polylines]) tuples
            layer_prefix: Prefix for layer names
            major_interval: If set, contours at this interval get a different layer

        Returns:
            Total number of contour polylines added
        """
        count = 0
        for elevation, polylines in contours:
            if major_interval and abs(elevation % major_interval) < 0.01:
                layer_name = f"{layer_prefix}_MAJOR"
                color = 7  # White for major contours
            else:
                layer_name = f"{layer_prefix}_MINOR"
                color = 8  # Gray for minor contours

            self._ensure_layer(layer_name, color)

            for polyline in polylines:
                points = [(p[0], p[1], p[2]) for p in polyline]
                self.msp.add_polyline3d(points, dxfattribs={"layer": layer_name})
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
    ) -> int:
        """
        Add polygons from a GeoJSON FeatureCollection.

        Args:
            geojson: GeoJSON FeatureCollection
            layer_name: DXF layer name
            xy_scale: Scale factor for coordinates
            transform_func: Optional function to transform (lon, lat) -> (x, y)
            z_value: Z coordinate for all points
            color: Layer color (uses default if None)

        Returns:
            Number of polygons added
        """
        from shapely.geometry import shape

        self._ensure_layer(layer_name, color)

        count = 0
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
                # Get exterior ring
                coords = list(poly.exterior.coords)
                if transform_func:
                    try:
                        coords = [transform_func(c[0], c[1]) for c in coords]
                    except Exception:
                        continue
                points = [(c[0] * xy_scale, c[1] * xy_scale, z_value) for c in coords]
                if len(points) >= 3:
                    self.msp.add_polyline3d(
                        points, close=True, dxfattribs={"layer": layer_name}
                    )
                    count += 1

        return count

    def add_cross(
        self,
        center: tuple[float, float, float],
        size: float = 50.0,
        layer_name: str = "origin",
        color: int | None = None,
    ) -> None:
        """
        Add a simple cross marker centered at the given point.

        Args:
            center: (x, y, z) in output units
            size: Full width/height of the cross
            layer_name: DXF layer name
            color: Optional layer color override
        """
        self._ensure_layer(layer_name, color)
        x, y, z = center
        half = size / 2.0
        self.msp.add_line(
            (x - half, y, z), (x + half, y, z), dxfattribs={"layer": layer_name}
        )
        self.msp.add_line(
            (x, y - half, z), (x, y + half, z), dxfattribs={"layer": layer_name}
        )

    def add_north_arrow(
        self,
        base: tuple[float, float, float],
        length: float = 75.0,
        head_length: float = 15.0,
        head_angle_deg: float = 25.0,
        layer_name: str = "north",
        color: int | None = None,
    ) -> None:
        """
        Add a one-sided north arrow pointing +Y.

        Args:
            base: (x, y, z) base point in output units
            length: Arrow shaft length
            head_length: Arrow head length
            head_angle_deg: Arrow head angle from shaft
            layer_name: DXF layer name
            color: Optional layer color override
        """
        self._ensure_layer(layer_name, color)
        x, y, z = base
        tip = (x, y + length, z)
        self.msp.add_line((x, y, z), tip, dxfattribs={"layer": layer_name})

        angle = math.radians(head_angle_deg)
        dx = head_length * math.sin(angle)
        dy = head_length * math.cos(angle)
        left = (tip[0] - dx, tip[1] - dy, z)
        right = (tip[0] + dx, tip[1] - dy, z)
        self.msp.add_line(tip, left, dxfattribs={"layer": layer_name})
        self.msp.add_line(tip, right, dxfattribs={"layer": layer_name})

    def save(self, output_path: str) -> None:
        """Save the DXF file."""
        self.doc.saveas(output_path)

