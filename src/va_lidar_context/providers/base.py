from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Protocol, Tuple, Literal

BBoxWGS84 = Tuple[float, float, float, float]


@dataclass(frozen=True)
class LidarSource:
    """
    Resolved point-cloud source for a given bbox.

    source_type:
      - "laz": downloadable LAZ file(s)
      - "ept": Entwine Point Tile endpoint
    """

    source_type: Literal["laz", "ept"]
    uri: str
    bbox_wgs84: BBoxWGS84
    crs_wkt: str | None = None
    metadata: Dict[str, Any] = field(default_factory=dict)


class LidarProvider(Protocol):
    def resolve(self, bbox_wgs84: BBoxWGS84) -> LidarSource:
        """Return a LiDAR source covering the bbox."""


class FootprintsProvider(Protocol):
    def fetch_geojson(self, bbox_wgs84: BBoxWGS84) -> Dict[str, Any]:
        """Return building footprints intersecting the bbox (GeoJSON)."""


class ParcelsProvider(Protocol):
    def fetch_geojson(self, bbox_wgs84: BBoxWGS84) -> Dict[str, Any]:
        """Return parcel polygons intersecting the bbox (GeoJSON)."""
