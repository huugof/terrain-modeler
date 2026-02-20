"""Regression tests for build pipeline output/contour validation (task 1.7)."""
from __future__ import annotations

import pytest

from va_lidar_context.config import BuildConfig
from va_lidar_context.pipeline.build import build


def _cfg(**overrides) -> BuildConfig:
    """Return a BuildConfig with safe defaults that won't reach network I/O."""
    defaults = dict(
        outputs=("buildings", "terrain"),
        contour_interval=None,
        xyz_mode="grid",
        combine_output=False,
        # center=None means the pipeline will hit a validation error before network
        center=None,
    )
    defaults.update(overrides)
    return BuildConfig(**defaults)


# ---------------------------------------------------------------------------
# Contour interval validation
# ---------------------------------------------------------------------------


def test_contours_without_interval_raises():
    cfg = _cfg(outputs=("contours",))
    with pytest.raises(ValueError, match="Contours output requires"):
        build(cfg)


def test_contours_with_interval_passes_validation():
    """With a valid interval, the contour validation itself passes.
    The build will fail later (no center/data), but not on the interval check."""
    cfg = _cfg(outputs=("contours",), contour_interval=2.0)
    with pytest.raises(Exception) as exc_info:
        build(cfg)
    # Must NOT be the interval-related ValueError
    assert "Contours output requires" not in str(exc_info.value)


def test_xyz_contour_mode_without_interval_raises():
    cfg = _cfg(outputs=("xyz",), xyz_mode="contours", contour_interval=None)
    with pytest.raises(ValueError, match="XYZ contour output requires"):
        build(cfg)


def test_xyz_grid_mode_without_interval_passes_validation():
    """xyz in grid mode does not require a contour interval."""
    cfg = _cfg(outputs=("xyz",), xyz_mode="grid", contour_interval=None)
    with pytest.raises(Exception) as exc_info:
        build(cfg)
    assert "contour" not in str(exc_info.value).lower() or "requires" not in str(exc_info.value)


def test_contour_interval_without_contours_output_raises():
    """Passing a contour interval when contours is not in outputs should raise."""
    cfg = _cfg(outputs=("terrain",), contour_interval=2.0, xyz_mode="grid")
    with pytest.raises(ValueError, match="--contours requires"):
        build(cfg)


def test_contour_interval_with_xyz_contour_mode_is_valid():
    """contour_interval + xyz contours mode (without 'contours' output) is valid."""
    cfg = _cfg(outputs=("xyz",), xyz_mode="contours", contour_interval=2.0)
    with pytest.raises(Exception) as exc_info:
        build(cfg)
    # Should NOT raise the contour interval mismatch errors
    assert "contours" not in str(exc_info.value).lower() or (
        "requires" not in str(exc_info.value)
    )


# ---------------------------------------------------------------------------
# Default outputs no longer include contours
# ---------------------------------------------------------------------------


def test_default_outputs_do_not_require_contour_interval():
    """A BuildConfig with default outputs must pass contour validation without an interval."""
    cfg = BuildConfig()  # uses DEFAULT_OUTPUTS = ("buildings", "terrain")
    with pytest.raises(Exception) as exc_info:
        build(cfg)
    assert "Contours output requires" not in str(exc_info.value)
    assert "XYZ contour output requires" not in str(exc_info.value)
