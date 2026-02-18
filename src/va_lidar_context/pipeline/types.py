from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Literal, Tuple

from ..config import BuildConfig

BBoxWGS84 = Tuple[float, float, float, float]
OutputKind = Literal["buildings", "terrain", "contours", "parcels", "naip"]


@dataclass(frozen=True)
class ClipSpec:
    """Defines a square clip area around a WGS84 center point."""

    center_latlon: tuple[float, float]
    size: float
    units: str


@dataclass(frozen=True)
class LidarSource:
    """Resolved point-cloud source for a given bbox."""

    source_type: Literal["laz"]
    uri: str
    bbox_wgs84: BBoxWGS84
    crs_wkt: str | None = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class BuildArtifacts:
    """Paths to main outputs and intermediates for a build run."""

    output_dir: Path
    tile_json: Path
    laz_path: Path
    footprints_path: Path
    dtm_path: Path
    dsm_path: Path
    ndsm_path: Path
    terrain_obj: Path
    buildings_obj: Path
    report_path: Path


BuildRequest = BuildConfig
