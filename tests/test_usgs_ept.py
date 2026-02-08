from __future__ import annotations

from typing import Any, Dict

import va_lidar_context.providers.usgs_ept as usgs_ept


def _feature(name: str, coords, year: int | None = None, url: str | None = None):
    return {
        "type": "Feature",
        "properties": {
            "name": name,
            "year": year,
            "url": url or f"https://usgs-lidar-public.s3.amazonaws.com/{name}/ept.json",
        },
        "geometry": {"type": "Polygon", "coordinates": [coords]},
    }


def _boundaries(*features: Dict[str, Any]) -> Dict[str, Any]:
    return {"type": "FeatureCollection", "features": list(features)}


def test_resolve_ept_bbox_full_coverage(monkeypatch, tmp_path):
    # AOI bbox (0,0)-(10,10). Boundary covers full AOI.
    full_poly = [(-1, -1), (11, -1), (11, 11), (-1, 11), (-1, -1)]
    boundaries = _boundaries(_feature("FULL_DATASET", full_poly, year=2020))

    monkeypatch.setattr(usgs_ept, "load_boundaries", lambda *args, **kwargs: boundaries)
    monkeypatch.setattr(usgs_ept, "_ept_exists", lambda *_args, **_kwargs: True)
    monkeypatch.setattr(
        usgs_ept,
        "_fetch_ept_metadata",
        lambda *_args, **_kwargs: {"srs": {"wkt": "EPSG:4326"}},
    )

    source = usgs_ept.resolve_ept_from_bbox((0, 0, 10, 10), cache_dir=tmp_path)
    assert source is not None
    assert source.metadata.get("coverage_status") == "full"
    ratio = source.metadata.get("coverage_ratio")
    assert ratio is not None
    assert ratio >= 0.99


def test_resolve_ept_bbox_partial_coverage(monkeypatch, tmp_path):
    # AOI bbox (0,0)-(10,10). Boundary covers half AOI.
    half_poly = [(0, 0), (5, 0), (5, 10), (0, 10), (0, 0)]
    boundaries = _boundaries(_feature("PARTIAL_DATASET", half_poly, year=2022))

    monkeypatch.setattr(usgs_ept, "load_boundaries", lambda *args, **kwargs: boundaries)
    monkeypatch.setattr(usgs_ept, "_ept_exists", lambda *_args, **_kwargs: True)
    monkeypatch.setattr(
        usgs_ept,
        "_fetch_ept_metadata",
        lambda *_args, **_kwargs: {"srs": {"wkt": "EPSG:4326"}},
    )

    source = usgs_ept.resolve_ept_from_bbox((0, 0, 10, 10), cache_dir=tmp_path)
    assert source is not None
    assert source.metadata.get("coverage_status") == "partial"
    ratio = source.metadata.get("coverage_ratio")
    assert ratio is not None
    assert 0.4 < ratio < 0.6


def test_resolve_ept_bbox_prefers_full_over_partial(monkeypatch, tmp_path):
    # Partial dataset is newer but should not win over full coverage.
    full_poly = [(-1, -1), (11, -1), (11, 11), (-1, 11), (-1, -1)]
    half_poly = [(0, 0), (5, 0), (5, 10), (0, 10), (0, 0)]
    boundaries = _boundaries(
        _feature("PARTIAL_NEW", half_poly, year=2024),
        _feature("FULL_OLD", full_poly, year=2020),
    )

    monkeypatch.setattr(usgs_ept, "load_boundaries", lambda *args, **kwargs: boundaries)
    monkeypatch.setattr(usgs_ept, "_ept_exists", lambda *_args, **_kwargs: True)
    monkeypatch.setattr(
        usgs_ept,
        "_fetch_ept_metadata",
        lambda *_args, **_kwargs: {"srs": {"wkt": "EPSG:4326"}},
    )

    source = usgs_ept.resolve_ept_from_bbox((0, 0, 10, 10), cache_dir=tmp_path)
    assert source is not None
    assert source.metadata.get("coverage_status") == "full"
    assert source.metadata.get("dataset") == "FULL_OLD"
