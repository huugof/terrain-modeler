from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Optional, Tuple

import numpy as np
import trimesh
from shapely.affinity import scale as scale_geom
from shapely.validation import make_valid

from .heights import FootprintHeight


def extrude_footprints(
    footprints: Iterable[FootprintHeight],
    xy_scale: float = 1.0,
    z_scale: float = 1.0,
) -> Optional[trimesh.Trimesh]:
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
    mesh.export(path)


def combine_meshes(meshes: List[trimesh.Trimesh]) -> Optional[trimesh.Trimesh]:
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
        f.write("usemtl terrain\n")
        for face in t_faces:
            v1, v2, v3 = face
            f.write(f"f {v1 + 1}/{v1 + 1} {v2 + 1}/{v2 + 1} {v3 + 1}/{v3 + 1}\n")
        if len(b_faces):
            f.write("o buildings\n")
            f.write("usemtl buildings\n")
            for face in b_faces:
                v1, v2, v3 = face
                f.write(f"f {v1 + 1 + t_count} {v2 + 1 + t_count} {v3 + 1 + t_count}\n")

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


def tree_mesh_from_canopy(
    canopy_height_path: str,
    dtm_path: str,
    xy_scale: float,
    z_scale: float,
    sample: int,
    min_height: float,
    radius: float,
    max_height: Optional[float] = None,
) -> Optional[trimesh.Trimesh]:
    try:
        import numpy as np
        import rasterio
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("numpy and rasterio are required for tree mesh") from exc

    if sample < 1:
        raise ValueError("sample must be >= 1")

    with rasterio.open(canopy_height_path) as chm_ds, rasterio.open(dtm_path) as dtm_ds:
        chm = chm_ds.read(1)
        dtm = dtm_ds.read(1)
        nodata = chm_ds.nodata if chm_ds.nodata is not None else -9999
        transform = chm_ds.transform

    if sample > 1:
        chm = chm[::sample, ::sample]
        dtm = dtm[::sample, ::sample]
        transform = transform * rasterio.Affine.scale(sample, sample)

    rows, cols = chm.shape
    if rows == 0 or cols == 0:
        return None

    meshes: List[trimesh.Trimesh] = []
    for r in range(rows):
        for c in range(cols):
            h = float(chm[r, c])
            if not np.isfinite(h) or h == nodata:
                continue
            if h < min_height:
                continue
            if max_height is not None and h > max_height:
                h = max_height
            base = float(dtm[r, c])
            if not np.isfinite(base) or base == nodata:
                continue
            x = transform.a * (c + 0.5) + transform.b * (r + 0.5) + transform.c
            y = transform.d * (c + 0.5) + transform.e * (r + 0.5) + transform.f
            try:
                cone = trimesh.creation.cone(
                    radius=radius * xy_scale, height=h * z_scale, sections=6
                )
            except Exception:
                continue
            cone.apply_translation((x * xy_scale, y * xy_scale, base * z_scale))
            meshes.append(cone)

    if not meshes:
        return None
    return trimesh.util.concatenate(meshes)
