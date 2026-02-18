from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

DEFAULT_OUT_DIR = Path("./out")
DEFAULT_FORMAT = "obj"
DEFAULT_UNITS = "feet"
DEFAULT_RESOLUTION = 1.0
DEFAULT_PERCENTILE = 95
DEFAULT_MIN_HEIGHT = 8.0
DEFAULT_MAX_HEIGHT = 300.0
DEFAULT_FLOOR_TO_FLOOR = 10.0
DEFAULT_KEEP_RASTERS = False
DEFAULT_TERRAIN_SAMPLE = 1
DEFAULT_FILL_DTM = False
DEFAULT_FILL_MAX_DIST = 10.0
DEFAULT_FILL_SMOOTHING = 0
DEFAULT_FILL_HARD = False
DEFAULT_RANDOM_SEED = None
DEFAULT_NAIP_PIXEL_SIZE = 1.0
DEFAULT_NAIP_MAX_SIZE = 4000
DEFAULT_NAIP_TILED = False
DEFAULT_NAIP_FLIP_U = False
DEFAULT_NAIP_FLIP_V = False
DEFAULT_COMBINE_OUTPUT = False
DEFAULT_CLIP_SIZE = None
DEFAULT_FLIP_Y = False
DEFAULT_FLIP_X = False
DEFAULT_TERRAIN_FLIP_Y = False
DEFAULT_ROTATE_Z = 0.0
DEFAULT_PROJECT_ZERO = 0.0
DEFAULT_XYZ_MODE = "grid"
DEFAULT_DXF_CONTOUR_SPACING = 0.0
DEFAULT_DXF_INCLUDE_PARCELS = True
DEFAULT_DXF_INCLUDE_BUILDINGS = True
DEFAULT_ALLOW_MULTI_TILE = False
DEFAULT_PROVIDER = "va"
DEFAULT_CLEANUP_INTERMEDIATES = False
DEFAULT_OUTPUTS: Tuple[str, ...] = ("contours", "xyz")


@dataclass(frozen=True)
class BuildConfig:
    """User-configurable build inputs for the pipeline."""

    tile_name: str | None = None
    job_id: str | None = None
    center: tuple[float, float] | None = None  # (lat, lon)
    size: float | None = DEFAULT_CLIP_SIZE
    out_dir: Path = DEFAULT_OUT_DIR
    force: bool = False
    fmt: str = DEFAULT_FORMAT
    units: str = DEFAULT_UNITS
    resolution: float = DEFAULT_RESOLUTION
    percentile: int = DEFAULT_PERCENTILE
    min_height: float = DEFAULT_MIN_HEIGHT
    max_height: float = DEFAULT_MAX_HEIGHT
    floor_to_floor: float = DEFAULT_FLOOR_TO_FLOOR
    keep_rasters: bool = DEFAULT_KEEP_RASTERS
    terrain_sample: int = DEFAULT_TERRAIN_SAMPLE
    fill_dtm: bool = DEFAULT_FILL_DTM
    fill_hard: bool = DEFAULT_FILL_HARD
    fill_max_dist: float = DEFAULT_FILL_MAX_DIST
    fill_smoothing: int = DEFAULT_FILL_SMOOTHING
    random_heights_min: float | None = None
    random_heights_max: float | None = None
    random_seed: int | None = DEFAULT_RANDOM_SEED
    naip_pixel_size: float = DEFAULT_NAIP_PIXEL_SIZE
    naip_max_size: int = DEFAULT_NAIP_MAX_SIZE
    naip_tiled: bool = DEFAULT_NAIP_TILED
    naip_flip_u: bool = DEFAULT_NAIP_FLIP_U
    naip_flip_v: bool = DEFAULT_NAIP_FLIP_V
    combine_output: bool = DEFAULT_COMBINE_OUTPUT
    outputs: Tuple[str, ...] = DEFAULT_OUTPUTS
    flip_y: bool = DEFAULT_FLIP_Y
    flip_x: bool = DEFAULT_FLIP_X
    terrain_flip_y: bool = DEFAULT_TERRAIN_FLIP_Y
    rotate_z: float = DEFAULT_ROTATE_Z
    project_zero: float | None = DEFAULT_PROJECT_ZERO
    xyz_mode: str = DEFAULT_XYZ_MODE
    xyz_contour_spacing: float | None = None
    dxf_contour_spacing: float | None = None
    dxf_include_parcels: bool = DEFAULT_DXF_INCLUDE_PARCELS
    dxf_include_buildings: bool = DEFAULT_DXF_INCLUDE_BUILDINGS
    contour_interval: float | None = None
    allow_multi_tile: bool = DEFAULT_ALLOW_MULTI_TILE
    provider: str = DEFAULT_PROVIDER
    cleanup_intermediates: bool = DEFAULT_CLEANUP_INTERMEDIATES
