from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Tuple

import requests

NAIP_EXPORT_URL = "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage"


def build_naip_request(
    bbox_3857: Tuple[float, float, float, float],
    pixel_size: float,
    max_size: int,
) -> Dict[str, str]:
    xmin, ymin, xmax, ymax = bbox_3857
    width_m = max(1.0, xmax - xmin)
    height_m = max(1.0, ymax - ymin)
    width_px = max(1, int(width_m / pixel_size))
    height_px = max(1, int(height_m / pixel_size))

    scale = min(1.0, max_size / width_px, max_size / height_px)
    width_px = max(1, int(width_px * scale))
    height_px = max(1, int(height_px * scale))

    rendering_rule = json.dumps({"rasterFunction": "NaturalColor"})

    return {
        "bbox": f"{xmin},{ymin},{xmax},{ymax}",
        "bboxSR": "3857",
        "size": f"{width_px},{height_px}",
        "imageSR": "3857",
        "format": "png",
        "renderingRule": rendering_rule,
        "f": "image",
    }


def download_naip_image(
    bbox_3857: Tuple[float, float, float, float],
    out_png: Path,
    pixel_size: float = 1.0,
    max_size: int = 4000,
) -> Dict[str, float]:
    params = build_naip_request(bbox_3857, pixel_size, max_size)
    with requests.get(NAIP_EXPORT_URL, params=params, stream=True, timeout=120) as resp:
        resp.raise_for_status()
        out_png.parent.mkdir(parents=True, exist_ok=True)
        with out_png.open("wb") as f:
            for chunk in resp.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

    size = params["size"].split(",")
    width_px = int(size[0])
    height_px = int(size[1])

    return {
        "bbox_3857": bbox_3857,
        "width": width_px,
        "height": height_px,
        "pixel_size": pixel_size,
        "max_size": max_size,
    }
