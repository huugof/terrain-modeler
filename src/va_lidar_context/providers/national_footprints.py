from __future__ import annotations

from typing import Any, Dict, Tuple

from ..constants import MAX_RECORD_COUNT, MSBFP2_QUERY
from .arcgis import paged_query_geojson


def fetch_footprints_geojson(
    bbox: Tuple[float, float, float, float],
    *,
    max_records: int = MAX_RECORD_COUNT,
) -> Dict[str, Any]:
    """
    Fetch Microsoft US Building Footprints from the Esri-hosted FeatureServer.

    Args:
        bbox: (xmin, ymin, xmax, ymax) in WGS84 (EPSG:4326)
        max_records: pagination size (server max record count)

    Returns:
        GeoJSON FeatureCollection with building polygons
    """
    return paged_query_geojson(
        MSBFP2_QUERY,
        bbox,
        out_fields="OBJECTID",
        max_record_count=max_records,
    )
