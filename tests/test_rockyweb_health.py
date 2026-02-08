from __future__ import annotations

from va_lidar_context.providers import rockyweb_health


def test_rockyweb_204_is_unavailable(monkeypatch, tmp_path):
    class Resp:
        status_code = 204

    monkeypatch.setattr(
        rockyweb_health.requests,
        "head",
        lambda *args, **kwargs: Resp(),
    )

    payload = rockyweb_health.check_rockyweb(tmp_path / "health.json", ttl_seconds=0)
    assert payload["ok"] is False
    assert payload["status"] == 204


def test_rockyweb_200_is_ok(monkeypatch, tmp_path):
    class Resp:
        status_code = 200

    monkeypatch.setattr(
        rockyweb_health.requests,
        "head",
        lambda *args, **kwargs: Resp(),
    )

    payload = rockyweb_health.check_rockyweb(tmp_path / "health.json", ttl_seconds=0)
    assert payload["ok"] is True
    assert payload["status"] == 200
