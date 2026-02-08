from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Dict

import requests

ROCKYWEB_HEALTH_URL = (
    "https://rockyweb.usgs.gov/vdelivery/Datasets/Staged/Elevation/LPC/"
)


def check_rockyweb(
    cache_path: Path,
    *,
    ttl_seconds: int = 900,
    timeout: int = 10,
    logger=None,
) -> Dict[str, Any]:
    """Check rockyweb availability and cache the result."""
    now = time.time()
    if cache_path.exists():
        try:
            payload = json.loads(cache_path.read_text())
            if now - float(payload.get("checked_at", 0)) < ttl_seconds:
                return payload
        except Exception:
            pass

    status = None
    ok = False
    error = None
    try:
        resp = requests.head(ROCKYWEB_HEALTH_URL, timeout=timeout, allow_redirects=True)
        status = resp.status_code
        ok = status not in (204,) and status < 500
    except requests.RequestException as exc:
        error = str(exc)
        ok = False

    payload = {
        "ok": ok,
        "status": status,
        "error": error,
        "checked_at": now,
        "url": ROCKYWEB_HEALTH_URL,
    }
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(payload, indent=2, sort_keys=True))
    if logger:
        if ok:
            logger.info(f"rockyweb health OK (status={status})")
        else:
            logger.warning(f"rockyweb health FAILED (status={status}, error={error})")
    return payload
