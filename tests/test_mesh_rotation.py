import math

import numpy as np

from va_lidar_context.core.mesh import DxfExporter, export_terrain_xyz
from va_lidar_context.core.raster import RasterMeta, write_raster


def _round_point(pt, ndigits=6):
    return tuple(round(v, ndigits) for v in pt)


def test_export_terrain_xyz_rotation(tmp_path):
    raster_path = tmp_path / "raster.tif"
    data = np.ones((2, 2), dtype=np.float32)
    meta = RasterMeta(
        transform=(1.0, 0.0, 100.0, 0.0, 1.0, 200.0),
        width=2,
        height=2,
        crs_wkt="EPSG:3857",
        nodata=-9999.0,
    )
    write_raster(raster_path, data, meta)

    base_path = tmp_path / "base.xyz"
    export_terrain_xyz(
        str(raster_path),
        str(base_path),
        xy_scale=1.0,
        z_scale=1.0,
        sample=1,
        origin=(0.0, 0.0),
        rotate_deg=0.0,
    )

    out_path = tmp_path / "out.xyz"
    export_terrain_xyz(
        str(raster_path),
        str(out_path),
        xy_scale=1.0,
        z_scale=1.0,
        sample=1,
        origin=(0.0, 0.0),
        rotate_deg=90.0,
    )

    points = []
    with open(out_path, "r") as f:
        for line in f:
            x, y, z = (float(v) for v in line.split())
            points.append((x, y, z))

    base_points = []
    with open(base_path, "r") as f:
        for line in f:
            x, y, z = (float(v) for v in line.split())
            base_points.append((x, y, z))

    base_radii = sorted(round(math.hypot(x, y), 6) for x, y, _ in base_points)
    rot_radii = sorted(round(math.hypot(x, y), 6) for x, y, _ in points)
    assert base_radii == rot_radii

    base_zs = sorted(round(z, 6) for _, _, z in base_points)
    rot_zs = sorted(round(z, 6) for _, _, z in points)
    assert base_zs == rot_zs


def test_dxf_polygon_rotation():
    dxf = DxfExporter()
    square = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [1.0, 0.0],
                            [1.0, 1.0],
                            [0.0, 1.0],
                            [0.0, 0.0],
                            [1.0, 0.0],
                        ]
                    ],
                },
            }
        ],
    }

    count = dxf.add_polygons_from_geojson(
        square,
        layer_name="TEST",
        xy_scale=1.0,
        origin=(0.0, 0.0),
        rotate_deg=90.0,
    )
    assert count == 1

    polylines = list(dxf.msp.query("POLYLINE"))
    assert len(polylines) == 1
    vertices = [
        (v.dxf.location.x, v.dxf.location.y, v.dxf.location.z)
        for v in polylines[0].vertices
    ]

    expected = {
        (0.0, 1.0, 0.0),
        (-1.0, 1.0, 0.0),
        (-1.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
    }
    assert {_round_point(p) for p in vertices} == expected
