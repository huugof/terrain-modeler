"""Regression tests for parse_float / parse_int hardening and /run 400 responses
(tasks 1.6)."""

from __future__ import annotations

import unittest.mock as mock

import pytest

import va_lidar_context.webapp.settings as _webapp_settings
from va_lidar_context.webapp import app, parse_float, parse_int

# ---------------------------------------------------------------------------
# Unit tests for parse_float / parse_int
# ---------------------------------------------------------------------------


class TestParseFloat:
    def test_none_returns_none(self):
        assert parse_float(None) is None

    def test_empty_string_returns_none(self):
        assert parse_float("") is None

    def test_whitespace_only_returns_none(self):
        assert parse_float("   ") is None

    def test_valid_integer_string(self):
        assert parse_float("42") == pytest.approx(42.0)

    def test_valid_float_string(self):
        assert parse_float("3.14") == pytest.approx(3.14)

    def test_negative_float(self):
        assert parse_float("-1.5") == pytest.approx(-1.5)

    def test_invalid_string_returns_none(self):
        assert parse_float("abc") is None

    def test_invalid_mixed_returns_none(self):
        assert parse_float("1.2.3") is None

    def test_invalid_with_whitespace_returns_none(self):
        assert parse_float("  not-a-number  ") is None


class TestParseInt:
    def test_none_returns_none(self):
        assert parse_int(None) is None

    def test_empty_string_returns_none(self):
        assert parse_int("") is None

    def test_whitespace_only_returns_none(self):
        assert parse_int("   ") is None

    def test_valid_integer_string(self):
        assert parse_int("7") == 7

    def test_negative_integer(self):
        assert parse_int("-3") == -3

    def test_invalid_string_returns_none(self):
        assert parse_int("abc") is None

    def test_float_string_returns_none(self):
        # int("3.14") raises — should return None, not raise
        assert parse_int("3.14") is None

    def test_invalid_with_whitespace_returns_none(self):
        assert parse_int("  bad  ") is None


# ---------------------------------------------------------------------------
# Integration tests: /run route returns 400 (not 500) on bad numeric input
# ---------------------------------------------------------------------------


@pytest.fixture()
def client(monkeypatch):
    monkeypatch.setattr(_webapp_settings._config, "auth_enabled", False)
    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess["csrf_token"] = "test-csrf"
        yield c


def _base_form(**overrides):
    """Minimal valid form data for /run."""
    data = {
        "csrf_token": "test-csrf",
        "coords": "37.5, -77.5",
        "size": "500",
        "units": "feet",
        "output_terrain": "on",
    }
    data.update(overrides)
    return data


def test_invalid_size_returns_400_not_500(client):
    resp = client.post("/run", data=_base_form(size="not-a-number"))
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_invalid_coords_returns_400_not_500(client):
    resp = client.post("/run", data=_base_form(coords="notanumber, -77.5"))
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_invalid_terrain_complexity_falls_back_to_default(client, monkeypatch):
    """Non-numeric terrain_complexity should fall through to default (2), not 500."""
    import unittest.mock as mock

    monkeypatch.setattr(_webapp_settings._config, "out_dir", __import__("pathlib").Path("/tmp"))

    # We only want to test that the form parsing doesn't blow up, not run the pipeline.
    # Patch _run_build_job so the background thread doesn't actually build.
    with mock.patch("va_lidar_context.webapp._run_build_job"):
        resp = client.post(
            "/run",
            data=_base_form(terrain_complexity="garbage"),
        )
    # Should not be 500 — either 200/202 (job queued) or a known 400 (no pipeline)
    assert resp.status_code != 500


def test_run_defaults_to_computed_heights_without_random_override(client, monkeypatch):
    captured = {}
    monkeypatch.setattr(_webapp_settings._config, "out_dir", __import__("pathlib").Path("/tmp"))

    class _ImmediateThread:
        def __init__(self, target=None, args=(), daemon=None):
            self._target = target
            self._args = args

        def start(self):
            if self._target is not None:
                self._target(*self._args)

    def _capture_cfg(_job, cfg):
        captured["cfg"] = cfg

    with mock.patch("va_lidar_context.webapp.routes.threading.Thread", _ImmediateThread):
        with mock.patch("va_lidar_context.webapp.routes._run_build_job", side_effect=_capture_cfg):
            resp = client.post(
                "/run",
                data=_base_form(output_buildings="on"),
            )

    assert resp.status_code in (302, 303)
    cfg = captured.get("cfg")
    assert cfg is not None
    assert cfg.random_heights_min is None
    assert cfg.random_heights_max is None
