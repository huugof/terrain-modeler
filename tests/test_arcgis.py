from __future__ import annotations

from typing import Any, Dict

import va_lidar_context.providers.arcgis as arcgis


def test_paged_query_geojson_paginates(monkeypatch):
    calls = []

    class Resp:
        def __init__(self, payload: Dict[str, Any]):
            self._payload = payload

        def raise_for_status(self):
            return None

        def json(self):
            return self._payload

    def fake_get(url, params, timeout=60):
        calls.append(params["resultOffset"])
        if params["resultOffset"] == 0:
            return Resp({"features": [{"id": 1}, {"id": 2}]})
        return Resp({"features": []})

    monkeypatch.setattr(arcgis.requests, "get", fake_get)

    result = arcgis.paged_query_geojson(
        "https://example.com/query",
        (-1.0, -1.0, 1.0, 1.0),
        out_fields="OBJECTID",
        max_record_count=2,
    )

    assert [f["id"] for f in result["features"]] == [1, 2]
    assert calls == [0, 2]
