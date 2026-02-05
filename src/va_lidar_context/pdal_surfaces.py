from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import numpy as np
import rasterio
from rasterio.fill import fillnodata
from rasterio.mask import mask as rio_mask
from rasterio.warp import Resampling, reproject


def run_pdal_pipeline(pipeline: dict) -> None:
    proc = subprocess.run(
        ["pdal", "pipeline", "--stdin"],
        input=json.dumps(pipeline).encode("utf-8"),
        check=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8"))


def merge_lazs(
    laz_paths: list[Path],
    merged_path: Path,
    target_srs: str | None = None,
) -> Path:
    if not laz_paths:
        raise ValueError("No LAZ files provided for merge")
    if len(laz_paths) == 1:
        return laz_paths[0]

    pipeline = []
    merge_inputs = []
    for idx, laz_path in enumerate(laz_paths):
        reader_tag = f"r{idx}"
        pipeline.append(
            {"type": "readers.las", "filename": str(laz_path), "tag": reader_tag}
        )
        if target_srs:
            reproj_tag = f"rp{idx}"
            pipeline.append(
                {
                    "type": "filters.reprojection",
                    "out_srs": target_srs,
                    "inputs": [reader_tag],
                    "tag": reproj_tag,
                }
            )
            merge_inputs.append(reproj_tag)
        else:
            merge_inputs.append(reader_tag)

    pipeline.append({"type": "filters.merge", "inputs": merge_inputs})
    pipeline.append({"type": "writers.las", "filename": str(merged_path)})
    run_pdal_pipeline({"pipeline": pipeline})
    return merged_path


def make_dtm(laz_path: Path, dtm_path: Path, resolution: float) -> Path:
    pipeline = {
        "pipeline": [
            str(laz_path),
            {"type": "filters.range", "limits": "Classification[2:2]"},
            {
                "type": "writers.gdal",
                "filename": str(dtm_path),
                "resolution": resolution,
                "output_type": "min",
                "gdaldriver": "GTiff",
                "nodata": -9999,
            },
        ]
    }
    run_pdal_pipeline(pipeline)
    return dtm_path


def make_dsm(laz_path: Path, dsm_path: Path, resolution: float) -> Path:
    pipeline = {
        "pipeline": [
            str(laz_path),
            {"type": "filters.range", "limits": "Classification![2:2]"},
            {
                "type": "writers.gdal",
                "filename": str(dsm_path),
                "resolution": resolution,
                "output_type": "max",
                "gdaldriver": "GTiff",
                "nodata": -9999,
            },
        ]
    }
    run_pdal_pipeline(pipeline)
    return dsm_path


def make_canopy_dsm(laz_path: Path, canopy_path: Path, resolution: float) -> Path:
    pipeline = {
        "pipeline": [
            str(laz_path),
            {"type": "filters.range", "limits": "Classification[1:1]"},
            {
                "type": "writers.gdal",
                "filename": str(canopy_path),
                "resolution": resolution,
                "output_type": "max",
                "gdaldriver": "GTiff",
                "nodata": -9999,
            },
        ]
    }
    run_pdal_pipeline(pipeline)
    return canopy_path


def make_ndsm(dsm_path: Path, dtm_path: Path, ndsm_path: Path) -> Path:
    with rasterio.open(dsm_path) as dsm_ds, rasterio.open(dtm_path) as dtm_ds:
        dsm = dsm_ds.read(1)
        dtm = dtm_ds.read(1)
        nodata = dsm_ds.nodata if dsm_ds.nodata is not None else -9999

        if dsm.shape != dtm.shape or dsm_ds.transform != dtm_ds.transform:
            dtm_resampled = np.full(
                dsm.shape,
                dtm_ds.nodata if dtm_ds.nodata is not None else -9999,
                dtype=dtm.dtype,
            )
            reproject(
                source=dtm,
                destination=dtm_resampled,
                src_transform=dtm_ds.transform,
                src_crs=dtm_ds.crs,
                dst_transform=dsm_ds.transform,
                dst_crs=dsm_ds.crs,
                resampling=Resampling.bilinear,
                src_nodata=dtm_ds.nodata,
                dst_nodata=dtm_ds.nodata,
            )
            dtm = dtm_resampled

        dtm_nodata = dtm_ds.nodata if dtm_ds.nodata is not None else -9999
        mask = (dsm == nodata) | (dtm == dtm_nodata)
        ndsm = dsm - dtm
        ndsm = ndsm.astype("float32")
        ndsm[mask] = nodata

        profile = dsm_ds.profile
        profile.update(dtype="float32", nodata=nodata)
        with rasterio.open(ndsm_path, "w", **profile) as dst:
            dst.write(ndsm, 1)

    return ndsm_path


def make_chm(canopy_path: Path, dtm_path: Path, chm_path: Path) -> Path:
    return make_ndsm(canopy_path, dtm_path, chm_path)


def fill_nodata_raster(
    in_path: Path,
    out_path: Path,
    max_distance: float = 10.0,
    smoothing_iterations: int = 0,
    hard_fill: bool = False,
) -> Path:
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
        subprocess.run(args, check=True, capture_output=True)
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
