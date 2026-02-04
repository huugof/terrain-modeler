from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

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
DEFAULT_NAIP_FLIP_U = False
DEFAULT_NAIP_FLIP_V = False
DEFAULT_COMBINE_OUTPUT = False
DEFAULT_TREES_ENABLED = False
DEFAULT_TREES_RESOLUTION = 2.0
DEFAULT_TREES_SAMPLE = 2
DEFAULT_TREES_MIN_HEIGHT = 10.0
DEFAULT_TREES_MAX_HEIGHT = None
DEFAULT_TREES_RADIUS = 6.0


@dataclass(frozen=True)
class BuildConfig:
    tile_name: str
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
    naip_texture: bool = False
    naip_pixel_size: float = DEFAULT_NAIP_PIXEL_SIZE
    naip_max_size: int = DEFAULT_NAIP_MAX_SIZE
    naip_flip_u: bool = DEFAULT_NAIP_FLIP_U
    naip_flip_v: bool = DEFAULT_NAIP_FLIP_V
    combine_output: bool = DEFAULT_COMBINE_OUTPUT
    trees: bool = DEFAULT_TREES_ENABLED
    trees_resolution: float = DEFAULT_TREES_RESOLUTION
    trees_sample: int = DEFAULT_TREES_SAMPLE
    trees_min_height: float = DEFAULT_TREES_MIN_HEIGHT
    trees_max_height: float | None = DEFAULT_TREES_MAX_HEIGHT
    trees_radius: float = DEFAULT_TREES_RADIUS
