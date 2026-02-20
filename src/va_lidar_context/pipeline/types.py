from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Literal, Tuple

BBoxWGS84 = Tuple[float, float, float, float]
OutputKind = Literal["buildings", "terrain", "contours", "parcels", "naip"]


@dataclass(frozen=True)
class LidarSource:
    """Resolved point-cloud source for a given bbox."""

    source_type: Literal["laz", "ept"]
    uri: str
    bbox_wgs84: BBoxWGS84
    crs_wkt: str | None = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class BuildResult:
    """Return value from build_pipeline() carrying exit code and output location."""

    exit_code: int
    output_dir: Path | None = None
