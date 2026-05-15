from __future__ import annotations

import shutil
from pathlib import Path

import numpy as np
import rasterio
from rasterio.fill import fillnodata
from rasterio.mask import mask as rio_mask
from rasterio.warp import Resampling, reproject

from ..util import run_subprocess


def fill_nodata_raster(
    in_path: Path,
    out_path: Path,
    max_distance: float = 10.0,
    smoothing_iterations: int = 0,
    hard_fill: bool = False,
) -> Path:
    """Fill nodata holes in a raster using GDAL or rasterio."""
    cmd = shutil.which("gdal_fillnodata.py") or shutil.which("gdal_fillnodata")
    src_path = in_path
    if cmd:
        args = [
            cmd,
            "-md",
            str(max_distance),
            "-si",
            str(smoothing_iterations),
            "-of",
            "GTiff",
            str(in_path),
            str(out_path),
        ]
        run_subprocess(args, check=True, capture_output=True)
        if not hard_fill:
            return out_path
        src_path = out_path

    with rasterio.open(src_path) as src:
        profile = src.profile
        data = src.read(1, masked=True)
        nodata = src.nodata if src.nodata is not None else -9999

    mask = (~data.mask).astype("uint8")
    filled = fillnodata(
        data.filled(nodata),
        mask=mask,
        max_search_distance=max_distance,
        smoothing_iterations=smoothing_iterations,
    )

    profile.update(dtype="float32", nodata=nodata)
    with rasterio.open(out_path, "w", **profile) as dst:
        dst.write(filled.astype("float32"), 1)

    if hard_fill:
        with rasterio.open(out_path) as src:
            arr = src.read(1, masked=True)
            nodata = src.nodata if src.nodata is not None else -9999
            if np.any(arr.mask):
                max_dist = max(arr.shape) * 2
                mask = (~arr.mask).astype("uint8")
                filled2 = fillnodata(
                    arr.filled(nodata),
                    mask=mask,
                    max_search_distance=max_dist,
                    smoothing_iterations=0,
                )
                profile = src.profile
                with rasterio.open(out_path, "w", **profile) as dst:
                    dst.write(filled2.astype("float32"), 1)

    return out_path


def clip_raster(
    in_path: Path,
    out_path: Path,
    polygon,
) -> Path:
    """Clip a raster to a polygon and write the output."""
    with rasterio.open(in_path) as src:
        nodata = src.nodata if src.nodata is not None else -9999
        try:
            out_image, out_transform = rio_mask(
                src,
                [polygon],
                crop=True,
                all_touched=False,
                nodata=nodata,
            )
        except ValueError as exc:
            raise ValueError("Clip polygon does not overlap raster bounds") from exc
        profile = src.profile
        profile.update(
            height=out_image.shape[1],
            width=out_image.shape[2],
            transform=out_transform,
            nodata=nodata,
        )
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with rasterio.open(out_path, "w", **profile) as dst:
            dst.write(out_image)
    return out_path
