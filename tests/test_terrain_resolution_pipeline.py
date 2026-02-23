from __future__ import annotations

from pathlib import Path

from va_lidar_context.config import BuildConfig
from va_lidar_context.pipeline import build as build_module


def _touch(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("x")


def _mock_raster_ops(
    monkeypatch, dtm_resolutions: list[float], clip_calls: list[tuple[str, str]]
) -> None:
    def _fake_make_dtm(_laz_path: Path, out_path: Path, resolution: float) -> Path:
        dtm_resolutions.append(float(resolution))
        _touch(out_path)
        return out_path

    def _fake_clip(in_path: Path, out_path: Path, _poly) -> Path:
        clip_calls.append((in_path.name, out_path.name))
        _touch(out_path)
        return out_path

    monkeypatch.setattr(build_module, "make_dtm", _fake_make_dtm)
    monkeypatch.setattr(build_module, "make_dtm_unclassified", _fake_make_dtm)
    monkeypatch.setattr(build_module, "clip_raster", _fake_clip)
    monkeypatch.setattr(build_module, "raster_has_data", lambda _path: True)


def test_stage_rasters_legacy_mode_uses_single_clipped_raster(tmp_path, monkeypatch):
    dtm_resolutions: list[float] = []
    clip_calls: list[tuple[str, str]] = []
    _mock_raster_ops(monkeypatch, dtm_resolutions, clip_calls)

    cfg = BuildConfig(
        resolution=1.0,
        terrain_resolution=None,
        fill_dtm=False,
        force=True,
    )

    dtm_use_path, terrain_source_path, contour_source_path = build_module._stage_rasters(
        cfg,
        laz_processing_path=tmp_path / "tile.laz",
        clip_poly=object(),
        dtm_path=tmp_path / "dtm.tif",
        dtm_filled_path=tmp_path / "dtm_filled.tif",
        dtm_clip_path=tmp_path / "dtm_clip.tif",
        terrain_dtm_path=tmp_path / "dtm_terrain.tif",
        terrain_dtm_filled_path=tmp_path / "dtm_terrain_filled.tif",
        terrain_dtm_clip_path=tmp_path / "dtm_terrain_clip.tif",
        contour_clip_path=tmp_path / "dtm_contour_clip.tif",
        dsm_path=tmp_path / "dsm.tif",
        ndsm_path=tmp_path / "ndsm.tif",
        export_buildings=False,
        override_heights=False,
    )

    assert dtm_resolutions == [1.0]
    assert clip_calls == [("dtm.tif", "dtm_clip.tif")]
    assert dtm_use_path.name == "dtm.tif"
    assert terrain_source_path.name == "dtm_clip.tif"
    assert contour_source_path.name == "dtm_clip.tif"


def test_stage_rasters_upstream_mode_uses_coarse_terrain_and_fine_contours(tmp_path, monkeypatch):
    dtm_resolutions: list[float] = []
    clip_calls: list[tuple[str, str]] = []
    _mock_raster_ops(monkeypatch, dtm_resolutions, clip_calls)

    cfg = BuildConfig(
        resolution=1.0,
        terrain_resolution=4.0,
        fill_dtm=False,
        force=True,
    )

    dtm_use_path, terrain_source_path, contour_source_path = build_module._stage_rasters(
        cfg,
        laz_processing_path=tmp_path / "tile.laz",
        clip_poly=object(),
        dtm_path=tmp_path / "dtm.tif",
        dtm_filled_path=tmp_path / "dtm_filled.tif",
        dtm_clip_path=tmp_path / "dtm_clip.tif",
        terrain_dtm_path=tmp_path / "dtm_terrain.tif",
        terrain_dtm_filled_path=tmp_path / "dtm_terrain_filled.tif",
        terrain_dtm_clip_path=tmp_path / "dtm_terrain_clip.tif",
        contour_clip_path=tmp_path / "dtm_contour_clip.tif",
        dsm_path=tmp_path / "dsm.tif",
        ndsm_path=tmp_path / "ndsm.tif",
        export_buildings=False,
        override_heights=False,
    )

    assert dtm_resolutions == [1.0, 4.0]
    assert clip_calls == [
        ("dtm.tif", "dtm_contour_clip.tif"),
        ("dtm_terrain.tif", "dtm_terrain_clip.tif"),
    ]
    assert dtm_use_path.name == "dtm.tif"
    assert contour_source_path.name == "dtm_contour_clip.tif"
    assert terrain_source_path.name == "dtm_terrain_clip.tif"
