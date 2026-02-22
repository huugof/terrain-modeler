"""Form parsing, defaults, provider helpers, and parcel/data-source payloads."""

from __future__ import annotations

from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

from ..config import (
    DEFAULT_DXF_CONTOUR_SPACING,
    DEFAULT_DXF_INCLUDE_BUILDINGS,
    DEFAULT_DXF_INCLUDE_PARCELS,
    DEFAULT_MAX_HEIGHT,
    DEFAULT_MIN_HEIGHT,
    DEFAULT_OUTPUTS,
    DEFAULT_RESOLUTION,
    DEFAULT_UNITS,
    DEFAULT_XYZ_MODE,
)
from ..constants import (
    DEFAULT_PREVIEW_CENTER,
    MSBFP2_LAYER,
    USGS_LIDAR_INDEX_LAYER,
    VGIN_FOOTPRINTS_LAYER,
    VGIN_LIDAR_LAYER,
)
from ..parcels.registry import load_sources
from . import settings as _settings

# ---------------------------------------------------------------------------
# Low-level parsers
# ---------------------------------------------------------------------------


def parse_float(value: str | None) -> Optional[float]:
    if value is None:
        return None
    value = value.strip()
    if value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def parse_int(value: str | None) -> Optional[int]:
    if value is None:
        return None
    value = value.strip()
    if value == "":
        return None
    try:
        return int(value)
    except ValueError:
        return None


def parse_bool(value: str | None) -> bool:
    return value is not None


# ---------------------------------------------------------------------------
# Provider helpers
# ---------------------------------------------------------------------------

VA_BOUNDS = {"lat_min": 36.5, "lat_max": 39.5, "lon_min": -83.0, "lon_max": -75.0}


def is_in_virginia(lon: float, lat: float) -> bool:
    return (
        VA_BOUNDS["lon_min"] <= lon <= VA_BOUNDS["lon_max"]
        and VA_BOUNDS["lat_min"] <= lat <= VA_BOUNDS["lat_max"]
    )


def resolve_provider(lat: float | None, lon: float | None) -> str:
    if lat is None or lon is None:
        from ..config import DEFAULT_PROVIDER

        return DEFAULT_PROVIDER
    return "va" if is_in_virginia(lon, lat) else "national"


def provider_label(provider: str) -> str:
    return "VGIN (Virginia)" if provider == "va" else "USGS 3DEP (National)"


# ---------------------------------------------------------------------------
# Status display helpers
# ---------------------------------------------------------------------------


def status_label(status: str) -> str:
    mapping = {
        "queued": "Queued",
        "running": "Running",
        "done": "Completed",
        "error": "Failed",
    }
    return mapping.get(status, status.title())


def status_class(status: str) -> str:
    if status in ("queued", "running"):
        return "status-running"
    if status == "done":
        return "status-done"
    if status == "error":
        return "status-error"
    return "status-unknown"


# ---------------------------------------------------------------------------
# Image quality
# ---------------------------------------------------------------------------

ALLOWED_IMAGE_QUALITY = frozenset({"standard", "high", "ultra"})


def resolve_image_quality(value: str | None) -> tuple[float, int, bool]:
    quality = (value or "").strip().lower()
    if quality == "high":
        return (0.5, 8000, False)
    if quality == "ultra":
        return (0.3, 12000, False)
    return (1.0, 4000, False)


# ---------------------------------------------------------------------------
# Coverage cache
# ---------------------------------------------------------------------------


def coverage_cache_key(lon: float, lat: float) -> str:
    return f"{round(lon, 4)},{round(lat, 4)}"


# ---------------------------------------------------------------------------
# Form defaults / prefill
# ---------------------------------------------------------------------------


def snapshot_defaults() -> Dict[str, Any]:
    outputs = set(DEFAULT_OUTPUTS)
    return {
        "out": str(_settings._config.out_dir),
        "units": "feet",
        "provider": "national",
        "provider_label": "USGS 3DEP (National)",
        "center1": DEFAULT_PREVIEW_CENTER[0],
        "center2": DEFAULT_PREVIEW_CENTER[1],
        "job_name": "",
        "clip_size": 3000.0,
        "resolution": DEFAULT_RESOLUTION,
        "terrain_complexity": 5,
        "rotate_z": 0.0,
        "xyz_mode": DEFAULT_XYZ_MODE,
        "xyz_contour_spacing": 0.0,
        "dxf_contour_spacing": DEFAULT_DXF_CONTOUR_SPACING,
        "dxf_include_parcels": DEFAULT_DXF_INCLUDE_PARCELS,
        "dxf_include_buildings": DEFAULT_DXF_INCLUDE_BUILDINGS,
        "output_terrain": "terrain" in outputs,
        "output_buildings": "buildings" in outputs,
        "output_contours": "contours" in outputs,
        "output_naip": True,
        "output_xyz": "xyz" in outputs,
        "min_height": DEFAULT_MIN_HEIGHT,
        "max_height": DEFAULT_MAX_HEIGHT,
        "random_min_height": _settings._config.default_random_min_height,
        "random_max_height": _settings._config.default_random_max_height,
        "contour_interval": 2.0,
        "image_quality": "standard",
    }


def extract_form_defaults(
    *,
    coords: str,
    clip_size: float,
    units: str,
    terrain_complexity: int,
    rotate_z: float,
    contour_interval: Optional[float],
    dxf_contour_spacing: Optional[float],
    dxf_include_parcels: bool,
    dxf_include_buildings: bool,
    xyz_mode: str,
    image_quality: str,
    random_min_height: Optional[float],
    random_max_height: Optional[float],
    output_terrain: bool,
    output_buildings: bool,
    output_contours: bool,
    output_naip: bool,
    output_xyz: bool,
    custom_name: str,
) -> Dict[str, Any]:
    return {
        "center1": coords.split(",")[0].strip() if "," in coords else coords,
        "center2": coords.split(",")[1].strip() if "," in coords else "",
        "job_name": custom_name,
        "clip_size": clip_size,
        "units": units,
        "terrain_complexity": terrain_complexity,
        "rotate_z": rotate_z,
        "contour_interval": contour_interval if contour_interval is not None else 2.0,
        "dxf_contour_spacing": (
            dxf_contour_spacing if dxf_contour_spacing is not None else DEFAULT_DXF_CONTOUR_SPACING
        ),
        "dxf_include_parcels": dxf_include_parcels,
        "dxf_include_buildings": dxf_include_buildings,
        "xyz_mode": xyz_mode,
        "image_quality": image_quality,
        "random_min_height": random_min_height,
        "random_max_height": random_max_height,
        "output_terrain": output_terrain,
        "output_buildings": output_buildings,
        "output_contours": output_contours,
        "output_naip": output_naip,
        "output_xyz": output_xyz,
    }


def merge_prefill_defaults(
    defaults: Dict[str, Any], saved: Optional[Dict[str, Any]]
) -> Dict[str, Any]:
    if not isinstance(saved, dict):
        return defaults
    allowed = {
        "center1",
        "center2",
        "job_name",
        "clip_size",
        "units",
        "terrain_complexity",
        "rotate_z",
        "contour_interval",
        "dxf_contour_spacing",
        "dxf_include_parcels",
        "dxf_include_buildings",
        "xyz_mode",
        "image_quality",
        "random_min_height",
        "random_max_height",
        "output_terrain",
        "output_buildings",
        "output_contours",
        "output_naip",
        "output_xyz",
    }
    for key in allowed:
        if key in saved:
            defaults[key] = saved[key]
    return defaults


# ---------------------------------------------------------------------------
# Parcel / data-source payloads
# ---------------------------------------------------------------------------


def parcel_sources_payload() -> List[Dict[str, Any]]:
    sources = []
    for source in load_sources():
        payload: Dict[str, Any] = {
            "id": source.id,
            "name": source.name,
            "url": source.query_url,
        }
        if source.coverage is not None:
            payload["coverage"] = {
                "xmin": source.coverage[0],
                "ymin": source.coverage[1],
                "xmax": source.coverage[2],
                "ymax": source.coverage[3],
            }
        if source.exclude:
            payload["exclude"] = [
                {"xmin": b[0], "ymin": b[1], "xmax": b[2], "ymax": b[3]} for b in source.exclude
            ]
        sources.append(payload)
    return sources


def _domain_key(url: str) -> str:
    return urlparse(url).netloc.lower()


def _base_service_url(url: str) -> str:
    parsed = urlparse(url)
    root = f"{parsed.scheme}://{parsed.netloc}"
    marker = "/arcgis/rest/services"
    idx = parsed.path.find(marker)
    if idx != -1:
        return root + marker
    return root


def data_sources_payload(parcel_sources: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    static_sources = [
        {"name": "VGIN LiDAR", "url": VGIN_LIDAR_LAYER},
        {"name": "VGIN Footprints", "url": VGIN_FOOTPRINTS_LAYER},
        {"name": "USGS 3DEP LiDAR", "url": USGS_LIDAR_INDEX_LAYER},
        {"name": "Microsoft Footprints", "url": MSBFP2_LAYER},
        {
            "name": "NAIP Imagery",
            "url": "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer",
        },
    ]

    entries = list(static_sources)
    for source in parcel_sources:
        if source.get("url"):
            entries.append({"name": source["name"], "url": source["url"]})

    provider_labels = {
        "vginmaps.vdem.virginia.gov": "VGIN",
    }

    grouped: Dict[str, Dict[str, Any]] = {}
    order: List[str] = []
    for entry in entries:
        domain = _domain_key(entry["url"])
        if domain not in grouped:
            grouped[domain] = {
                "name": entry["name"],
                "url": entry["url"],
                "details": [],
            }
            order.append(domain)
        grouped[domain]["details"].append(entry["name"])

    sources = []
    for domain in order:
        group = grouped[domain]
        if len(group["details"]) > 1:
            name = provider_labels.get(domain, domain)
            url = _base_service_url(group["url"])
        else:
            name = group["name"]
            url = group["url"]
        sources.append(
            {
                "name": name,
                "url": url,
                "details": group["details"],
            }
        )
    return sources
