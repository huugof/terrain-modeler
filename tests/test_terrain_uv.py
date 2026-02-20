from __future__ import annotations

import numpy as np
import trimesh
from pyproj import Transformer
from rasterio.transform import Affine

from va_lidar_context.core.mesh import apply_scene_transform
from va_lidar_context.pipeline.build import _compute_terrain_uv, _resolve_scene_transform_center


def _sample_vertices() -> np.ndarray:
    # 2x2 grid cell centers for transform:
    #   Affine(10, 0, 1000, 0, -10, 2000)
    #   row 0 (north): y = 1995
    #   row 1 (south): y = 1985
    return np.array(
        [
            [1005.0, 1995.0, 0.0],  # northwest
            [1015.0, 1995.0, 0.0],  # northeast
            [1005.0, 1985.0, 0.0],  # southwest
            [1015.0, 1985.0, 0.0],  # southeast
        ],
        dtype=float,
    )


def test_compute_terrain_uv_keeps_obj_north_up_convention():
    vertices = _sample_vertices()
    transform = Affine(10.0, 0.0, 1000.0, 0.0, -10.0, 2000.0)
    to_3857 = Transformer.from_crs("EPSG:3857", "EPSG:3857", always_xy=True)
    bbox_3857 = (1000.0, 1020.0, 1980.0, 2000.0)  # xmin, xmax, ymin, ymax

    uv_raster = _compute_terrain_uv(
        vertices,
        xy_scale=1.0,
        to_3857_from_laz=to_3857,
        transform=transform,
        raster_width=2,
        raster_height=2,
        bbox_3857=bbox_3857,
        use_raster_uv=True,
        flip_u=False,
        flip_v=False,
    )

    uv_projected = _compute_terrain_uv(
        vertices,
        xy_scale=1.0,
        to_3857_from_laz=to_3857,
        transform=transform,
        raster_width=2,
        raster_height=2,
        bbox_3857=bbox_3857,
        use_raster_uv=False,
        flip_u=False,
        flip_v=False,
    )

    expected = np.array(
        [
            [0.25, 0.75],  # northwest (top-left of image)
            [0.75, 0.75],  # northeast
            [0.25, 0.25],  # southwest
            [0.75, 0.25],  # southeast
        ],
        dtype=float,
    )
    assert np.allclose(np.array(uv_raster), expected)
    assert np.allclose(np.array(uv_projected), expected)


def test_compute_terrain_uv_flip_flags_are_explicit_and_deterministic():
    vertices = _sample_vertices()
    transform = Affine(10.0, 0.0, 1000.0, 0.0, -10.0, 2000.0)
    to_3857 = Transformer.from_crs("EPSG:3857", "EPSG:3857", always_xy=True)
    bbox_3857 = (1000.0, 1020.0, 1980.0, 2000.0)

    base = np.array(
        _compute_terrain_uv(
            vertices,
            xy_scale=1.0,
            to_3857_from_laz=to_3857,
            transform=transform,
            raster_width=2,
            raster_height=2,
            bbox_3857=bbox_3857,
            use_raster_uv=False,
            flip_u=False,
            flip_v=False,
        )
    )
    flip_u = np.array(
        _compute_terrain_uv(
            vertices,
            xy_scale=1.0,
            to_3857_from_laz=to_3857,
            transform=transform,
            raster_width=2,
            raster_height=2,
            bbox_3857=bbox_3857,
            use_raster_uv=False,
            flip_u=True,
            flip_v=False,
        )
    )
    flip_v = np.array(
        _compute_terrain_uv(
            vertices,
            xy_scale=1.0,
            to_3857_from_laz=to_3857,
            transform=transform,
            raster_width=2,
            raster_height=2,
            bbox_3857=bbox_3857,
            use_raster_uv=False,
            flip_u=False,
            flip_v=True,
        )
    )

    assert np.allclose(flip_u[:, 0], 1.0 - base[:, 0])
    assert np.allclose(flip_u[:, 1], base[:, 1])
    assert np.allclose(flip_v[:, 0], base[:, 0])
    assert np.allclose(flip_v[:, 1], 1.0 - base[:, 1])


def _make_mesh(vertices: np.ndarray) -> trimesh.Trimesh:
    faces = np.array([[0, 1, 2], [1, 3, 2]], dtype=int)
    return trimesh.Trimesh(vertices=vertices, faces=faces, process=False)


def test_scene_rotation_changes_world_space_uv_projection():
    vertices = _sample_vertices()
    transform = Affine(10.0, 0.0, 1000.0, 0.0, -10.0, 2000.0)
    to_3857 = Transformer.from_crs("EPSG:3857", "EPSG:3857", always_xy=True)
    bbox_3857 = (1000.0, 1020.0, 1980.0, 2000.0)

    uv_before = np.array(
        _compute_terrain_uv(
            vertices,
            xy_scale=1.0,
            to_3857_from_laz=to_3857,
            transform=transform,
            raster_width=2,
            raster_height=2,
            bbox_3857=bbox_3857,
            use_raster_uv=False,
            flip_u=False,
            flip_v=False,
        )
    )

    mesh = _make_mesh(vertices.copy())
    apply_scene_transform(mesh, center_x=1010.0, center_y=1990.0, rotate_deg=30.0)
    uv_after = np.array(
        _compute_terrain_uv(
            mesh.vertices,
            xy_scale=1.0,
            to_3857_from_laz=to_3857,
            transform=transform,
            raster_width=2,
            raster_height=2,
            bbox_3857=bbox_3857,
            use_raster_uv=False,
            flip_u=False,
            flip_v=False,
        )
    )

    assert not np.allclose(uv_before, uv_after)


def test_resolve_scene_transform_center_prefers_user_center():
    terrain = _make_mesh(_sample_vertices())
    buildings = _make_mesh(_sample_vertices() + np.array([200.0, 100.0, 0.0]))

    cx, cy = _resolve_scene_transform_center(
        terrain,
        buildings,
        center_laz_x=123.0,
        center_laz_y=456.0,
        xy_scale=2.0,
    )

    assert cx == 246.0
    assert cy == 912.0


def test_resolve_scene_transform_center_falls_back_to_mesh_bounds():
    terrain = _make_mesh(_sample_vertices())
    buildings = _make_mesh(_sample_vertices() + np.array([200.0, 100.0, 0.0]))

    cx, cy = _resolve_scene_transform_center(
        terrain,
        buildings,
        center_laz_x=None,
        center_laz_y=None,
        xy_scale=1.0,
    )
    assert np.isclose(cx, 1010.0)
    assert np.isclose(cy, 1990.0)

    cx2, cy2 = _resolve_scene_transform_center(
        None,
        buildings,
        center_laz_x=None,
        center_laz_y=None,
        xy_scale=1.0,
    )
    assert np.isclose(cx2, 1210.0)
    assert np.isclose(cy2, 2090.0)

    cx3, cy3 = _resolve_scene_transform_center(
        None,
        None,
        center_laz_x=None,
        center_laz_y=None,
        xy_scale=1.0,
    )
    assert cx3 == 0.0
    assert cy3 == 0.0
