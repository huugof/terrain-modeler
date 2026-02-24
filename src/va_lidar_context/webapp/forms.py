"""Form parsing, defaults, provider helpers, and parcel/data-source payloads."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, Optional, Tuple
from urllib.parse import urlparse

from ..config import (
    DEFAULT_DXF_CONTOUR_SPACING,
    DEFAULT_DXF_INCLUDE_BUILDINGS,
    DEFAULT_DXF_INCLUDE_PARCELS,
    DEFAULT_MAX_HEIGHT,
    DEFAULT_MIN_HEIGHT,
    DEFAULT_OUTPUTS,
    DEFAULT_RESOLUTION,
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

JOB_NAME_MAX_LENGTH = 120
JOB_NAME_LENGTH_ERROR = f"Name must be {JOB_NAME_MAX_LENGTH} characters or fewer."
DEFAULT_IMAGE_QUALITY = "standard"
_OUTPUT_CHECKBOXES: Tuple[Tuple[str, str], ...] = (
    ("output_terrain", "terrain"),
    ("output_buildings", "buildings"),
    ("output_contours", "contours"),
    ("output_naip", "naip"),
    ("output_xyz", "xyz"),
)


@dataclass(frozen=True)
class ParsedRunForm:
    custom_name: str
    lat: float
    lon: float
    clip_size: float
    units: str
    provider: str
    terrain_complexity: int
    min_height: float
    max_height: float
    random_min_height: float | None
    random_max_height: float | None
    image_quality: str
    outputs: tuple[str, ...]
    xyz_mode: str
    contour_interval: float | None
    xyz_contour_spacing: float | None
    dxf_contour_spacing: float | None
    dxf_include_parcels: bool
    dxf_include_buildings: bool
    rotate_z: float

    @property
    def center(self) -> tuple[float, float]:
        return (self.lat, self.lon)

    @property
    def contours_enabled(self) -> bool:
        return "contours" in self.outputs

    @property
    def xyz_enabled(self) -> bool:
        return "xyz" in self.outputs


def normalize_job_name(value: str | None) -> str:
    return str(value or "").strip()


def validate_job_name_length(name: str) -> Optional[str]:
    if len(name) > JOB_NAME_MAX_LENGTH:
        return JOB_NAME_LENGTH_ERROR
    return None


def parse_float(value: str | None) -> Optional[float]:
    if value is None:
        return None
    value = value.strip()
    if value == "":
        return None
    try:
        parsed = float(value)
    except ValueError:
        return None
    if not math.isfinite(parsed):
        return None
    return parsed


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


def parse_center_coords(value: str | None) -> tuple[Optional[float], Optional[float]]:
    parts = [p for p in re.split(r"[ ,]+", str(value or "").strip()) if p]
    lat = parse_float(parts[0]) if len(parts) > 0 else None
    lon = parse_float(parts[1]) if len(parts) > 1 else None
    return lat, lon


def normalize_units(value: str | None) -> str:
    raw = (value or "").strip().lower()
    return raw if raw in ("feet", "meters") else "feet"


def normalize_xyz_mode(value: str | None) -> str:
    raw = (value or "").strip().lower()
    return raw if raw in ("contours", "grid") else DEFAULT_XYZ_MODE


def normalize_image_quality(value: str | None) -> str:
    quality = (value or "").strip().lower()
    return quality if quality in ALLOWED_IMAGE_QUALITY else DEFAULT_IMAGE_QUALITY


def parse_selected_outputs(form: Mapping[str, Any]) -> tuple[str, ...]:
    outputs: list[str] = []
    for field, output_name in _OUTPUT_CHECKBOXES:
        if parse_bool(form.get(field)):
            outputs.append(output_name)
    return tuple(outputs)


def parse_run_form(
    form: Mapping[str, Any], *, max_clip_size: float
) -> tuple[Optional[ParsedRunForm], Optional[str]]:
    custom_name = normalize_job_name(form.get("job_name"))
    name_error = validate_job_name_length(custom_name)
    if name_error:
        return None, name_error

    units = normalize_units(form.get("units"))
    lat, lon = parse_center_coords(form.get("coords"))
    if lat is None or lon is None:
        return None, "Provide coordinates as lat, lon."

    clip_size = parse_float(form.get("size"))
    if clip_size is None:
        return None, "Provide a clip size."
    if clip_size <= 0:
        return None, "Clip size must be greater than 0."
    if clip_size > max_clip_size:
        return None, f"Clip size exceeds max ({max_clip_size:g})."

    terrain_complexity = parse_int(form.get("terrain_complexity"))
    if terrain_complexity is None:
        terrain_complexity = 2
    terrain_complexity = max(0, min(10, terrain_complexity))

    min_height = parse_float(form.get("min_height"))
    if min_height is None:
        min_height = DEFAULT_MIN_HEIGHT
    max_height = parse_float(form.get("max_height"))
    if max_height is None:
        max_height = DEFAULT_MAX_HEIGHT

    random_min = parse_float(form.get("random_min_height"))
    random_max = parse_float(form.get("random_max_height"))
    if (random_min is None) != (random_max is None):
        return None, "Provide both random min/max heights or leave both empty."
    if random_min is not None and random_max is not None and random_min >= random_max:
        return None, "Random min height must be less than random max height."

    outputs = parse_selected_outputs(form)
    if not outputs:
        return None, "Select at least one output."

    xyz_mode = normalize_xyz_mode(form.get("xyz_mode"))
    contours_enabled = "contours" in outputs
    xyz_enabled = "xyz" in outputs
    contour_interval = (
        (parse_float(form.get("contour_interval")) or 2.0)
        if (contours_enabled or (xyz_enabled and xyz_mode == "contours"))
        else None
    )
    xyz_contour_spacing = parse_float(form.get("xyz_contour_spacing"))
    if xyz_mode != "contours":
        xyz_contour_spacing = None
    if xyz_contour_spacing is not None and xyz_contour_spacing <= 0:
        xyz_contour_spacing = None

    dxf_contour_spacing = parse_float(form.get("dxf_contour_spacing")) if contours_enabled else None
    if dxf_contour_spacing is not None and dxf_contour_spacing <= 0:
        dxf_contour_spacing = None
    dxf_include_parcels = parse_bool(form.get("dxf_include_parcels")) if contours_enabled else False
    dxf_include_buildings = (
        parse_bool(form.get("dxf_include_buildings")) if contours_enabled else False
    )

    rotate_z = parse_float(form.get("rotate_z"))
    if rotate_z is None:
        rotate_z = 0.0

    return (
        ParsedRunForm(
            custom_name=custom_name,
            lat=lat,
            lon=lon,
            clip_size=clip_size,
            units=units,
            provider=resolve_provider(lat, lon),
            terrain_complexity=terrain_complexity,
            min_height=min_height,
            max_height=max_height,
            random_min_height=random_min,
            random_max_height=random_max,
            image_quality=normalize_image_quality(form.get("image_quality")),
            outputs=outputs,
            xyz_mode=xyz_mode,
            contour_interval=contour_interval,
            xyz_contour_spacing=xyz_contour_spacing,
            dxf_contour_spacing=dxf_contour_spacing,
            dxf_include_parcels=dxf_include_parcels,
            dxf_include_buildings=dxf_include_buildings,
            rotate_z=rotate_z,
        ),
        None,
    )


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
        "canceled": "Canceled",
        "error": "Failed",
    }
    return mapping.get(status, status.title())


def status_class(status: str) -> str:
    if status in ("queued", "running"):
        return "status-running"
    if status == "done":
        return "status-done"
    if status == "canceled":
        return "status-error"
    if status == "error":
        return "status-error"
    return "status-unknown"


# ---------------------------------------------------------------------------
# Image quality
# ---------------------------------------------------------------------------

ALLOWED_IMAGE_QUALITY = frozenset({"standard", "high", "ultra"})


def resolve_image_quality(value: str | None) -> tuple[float, int, bool]:
    quality = normalize_image_quality(value)
    if quality == "high":
        return (0.5, 8000, False)
    if quality == "ultra":
        return (0.3, 12000, False)
    return (1.0, 4000, False)


# ---------------------------------------------------------------------------
# Coverage cache
# ---------------------------------------------------------------------------


def coverage_cache_key(
    lon: float,
    lat: float,
    *,
    size: float | None = None,
    units: str | None = None,
) -> str:
    if size is None or units not in ("feet", "meters"):
        return f"{round(lon, 4)},{round(lat, 4)}"
    return f"{round(lon, 4)},{round(lat, 4)},{round(size, 2)},{units}"


# ---------------------------------------------------------------------------
# Form defaults / prefill
# ---------------------------------------------------------------------------


def snapshot_defaults() -> Dict[str, Any]:
    outputs = set(DEFAULT_OUTPUTS)
    outputs.discard("buildings")
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
        "output_buildings": False,
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
