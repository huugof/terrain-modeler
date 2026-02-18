from __future__ import annotations

import io
import json
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import requests
from PIL import Image

NAIP_EXPORT_URL = "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage"


def build_naip_request(
    bbox_3857: Tuple[float, float, float, float],
    pixel_size: float,
    max_size: int,
) -> Dict[str, str]:
    """Build NAIP ImageServer exportImage params for a bbox."""
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


def build_naip_request_with_size(
    bbox_3857: Tuple[float, float, float, float],
    width_px: int,
    height_px: int,
) -> Dict[str, str]:
    """Build NAIP params with an explicit pixel size."""
    xmin, ymin, xmax, ymax = bbox_3857
    rendering_rule = json.dumps({"rasterFunction": "NaturalColor"})
    width_px = max(1, int(width_px))
    height_px = max(1, int(height_px))
    return {
        "bbox": f"{xmin},{ymin},{xmax},{ymax}",
        "bboxSR": "3857",
        "size": f"{width_px},{height_px}",
        "imageSR": "3857",
        "format": "png",
        "renderingRule": rendering_rule,
        "f": "image",
    }


def _fetch_naip_png(params: Dict[str, str]) -> bytes:
    with requests.get(NAIP_EXPORT_URL, params=params, timeout=180) as resp:
        resp.raise_for_status()
        content_type = resp.headers.get("Content-Type", "").lower()
        if "image" not in content_type:
            text = resp.text[:800]
            raise RuntimeError(
                "NAIP exportImage returned non-image response: "
                f"{content_type or 'unknown'} {text}"
            )
        return resp.content


def _validate_png(path: Path) -> None:
    if not path.exists():
        raise RuntimeError("PNG download failed: file missing")
    size = path.stat().st_size
    if size < 16:
        raise RuntimeError("PNG download failed: file too small")
    with path.open("rb") as f:
        header = f.read(8)
        if header != b"\x89PNG\r\n\x1a\n":
            raise RuntimeError("PNG download failed: invalid header")
        try:
            f.seek(-12, 2)
        except OSError as exc:
            raise RuntimeError("PNG download failed: truncated file") from exc
        tail = f.read(12)
        if len(tail) != 12 or tail[4:8] != b"IEND":
            raise RuntimeError("PNG download failed: missing IEND chunk")
    try:
        with Image.open(path) as img:
            img.verify()
    except Exception as exc:
        raise RuntimeError(f"PNG download failed: unreadable ({exc})") from exc


def _normalize_mode(tile: Image.Image, mode: str) -> Image.Image:
    if tile.mode == mode:
        return tile
    if mode == "RGBA" and tile.mode == "RGB":
        return tile.convert("RGBA")
    return tile.convert(mode)


def download_naip_image(
    bbox_3857: Tuple[float, float, float, float],
    out_png: Path,
    pixel_size: float = 1.0,
    max_size: int = 4000,
) -> Dict[str, float]:
    """Download a NAIP image for the bbox and save to PNG."""
    params = build_naip_request(bbox_3857, pixel_size, max_size)
    last_err = None
    for _ in range(2):
        try:
            with requests.get(
                NAIP_EXPORT_URL, params=params, stream=True, timeout=180
            ) as resp:
                resp.raise_for_status()
                content_type = resp.headers.get("Content-Type", "").lower()
                if "image" not in content_type:
                    text = resp.text[:800]
                    raise RuntimeError(
                        "NAIP exportImage returned non-image response: "
                        f"{content_type or 'unknown'} {text}"
                    )
                out_png.parent.mkdir(parents=True, exist_ok=True)
                with out_png.open("wb") as f:
                    for chunk in resp.iter_content(chunk_size=1024 * 1024):
                        if chunk:
                            f.write(chunk)

            _validate_png(out_png)
            last_err = None
            break
        except Exception as exc:
            last_err = exc
    if last_err is not None:
        raise last_err

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


def download_naip_image_tiled(
    bbox_3857: Tuple[float, float, float, float],
    out_png: Path,
    pixel_size: float = 0.3,
    tile_max_size: int = 4000,
) -> Dict[str, float]:
    """Download a NAIP image by tiling requests to avoid size limits."""
    xmin, ymin, xmax, ymax = bbox_3857
    width_m = max(1.0, xmax - xmin)
    height_m = max(1.0, ymax - ymin)
    total_width_px = max(1, int(np.ceil(width_m / pixel_size)))
    total_height_px = max(1, int(np.ceil(height_m / pixel_size)))

    max_size = tile_max_size
    attempts = 0
    while True:
        tiles_x = max(1, int(np.ceil(total_width_px / max_size)))
        tiles_y = max(1, int(np.ceil(total_height_px / max_size)))
        tile_width_px = int(np.ceil(total_width_px / tiles_x))
        tile_height_px = int(np.ceil(total_height_px / tiles_y))

        mosaic: Image.Image | None = None
        mosaic_mode = "RGB"

        try:
            for ty in range(tiles_y):
                y0_px = ty * tile_height_px
                y1_px = min(total_height_px, (ty + 1) * tile_height_px)
                y_max = ymax - (y0_px * pixel_size)
                y_min = ymax - (y1_px * pixel_size)
                tile_h = max(1, y1_px - y0_px)
                for tx in range(tiles_x):
                    x0_px = tx * tile_width_px
                    x1_px = min(total_width_px, (tx + 1) * tile_width_px)
                    x_min = xmin + (x0_px * pixel_size)
                    x_max = xmin + (x1_px * pixel_size)
                    tile_w = max(1, x1_px - x0_px)

                    params = build_naip_request_with_size(
                        (x_min, y_min, x_max, y_max),
                        tile_w,
                        tile_h,
                    )

                    tile = None
                    last_err = None
                    for _ in range(3):
                        try:
                            data = _fetch_naip_png(params)
                            with Image.open(io.BytesIO(data)) as img:
                                img.load()
                                tile = img.copy()
                            last_err = None
                            break
                        except Exception as exc:
                            last_err = exc
                    if last_err is not None or tile is None:
                        raise RuntimeError(
                            f"NAIP tile decode failed at {tx + 1}/{tiles_x}, {ty + 1}/{tiles_y}: {last_err}"
                        )
                    if mosaic is None:
                        mosaic_mode = "RGBA" if "A" in tile.mode else "RGB"
                        mosaic = Image.new(
                            mosaic_mode, (total_width_px, total_height_px)
                        )
                    tile = _normalize_mode(tile, mosaic_mode)
                    if tile.size != (tile_w, tile_h):
                        tile = tile.crop((0, 0, tile_w, tile_h))
                    mosaic.paste(tile, (x0_px, y0_px))
        except Exception:
            attempts += 1
            if attempts >= 3:
                raise
            # If a single tile fails, force subdivision even if size is small.
            if tiles_x == 1 and tiles_y == 1:
                max_size = max(256, min(total_width_px, total_height_px) // 2)
                continue
            if max_size <= 1000:
                raise
            max_size = max(1000, max_size // 2)
            continue

        out_png.parent.mkdir(parents=True, exist_ok=True)
        if mosaic is None:
            raise RuntimeError("NAIP tiled download produced no image tiles")
        mosaic.save(out_png, format="PNG")

        _validate_png(out_png)

        return {
            "bbox_3857": bbox_3857,
            "width": total_width_px,
            "height": total_height_px,
            "pixel_size": pixel_size,
            "max_size": max_size,
            "tiled": True,
            "tiles_x": tiles_x,
            "tiles_y": tiles_y,
        }
