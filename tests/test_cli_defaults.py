"""Regression tests for CLI default output behavior (task 1.5)."""
from __future__ import annotations

import pytest

from va_lidar_context.cli import parse_outputs
from va_lidar_context.config import DEFAULT_OUTPUTS


def test_default_outputs_are_buildings_terrain():
    """DEFAULT_OUTPUTS must not include contours or xyz so a default run never
    raises 'Contours output requires --contours INTERVAL'."""
    assert "contours" not in DEFAULT_OUTPUTS
    assert "xyz" not in DEFAULT_OUTPUTS
    assert "buildings" in DEFAULT_OUTPUTS
    assert "terrain" in DEFAULT_OUTPUTS


def test_parse_outputs_none_returns_defaults():
    """Passing None (i.e. --outputs omitted) returns DEFAULT_OUTPUTS."""
    result = parse_outputs(None)
    assert result == DEFAULT_OUTPUTS


def test_parse_outputs_none_does_not_include_contours():
    """Default outputs must not require a contour interval."""
    result = parse_outputs(None)
    assert "contours" not in result


def test_parse_outputs_explicit_contours_is_allowed():
    """Explicitly requesting contours still works; caller is responsible for interval."""
    result = parse_outputs("buildings,contours")
    assert "contours" in result


def test_parse_outputs_unknown_raises():
    with pytest.raises(ValueError, match="Unknown outputs"):
        parse_outputs("buildings,bogus")


def test_parse_outputs_deduplicates():
    result = parse_outputs("terrain,terrain,buildings")
    assert list(result).count("terrain") == 1
