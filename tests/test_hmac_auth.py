from __future__ import annotations

import json
import time

from va_lidar_context.hmac_auth import (
    canonical_payload,
    parse_key_map,
    sign_payload,
    validate_timestamp,
    verify_signature,
)


def test_parse_key_map():
    payload = parse_key_map(json.dumps({"k1": "secret1", "k2": "secret2"}))
    assert payload["k1"] == "secret1"
    assert payload["k2"] == "secret2"


def test_sign_and_verify():
    body = b'{"status":"done"}'
    payload = canonical_payload("POST", "/internal/worker/jobs/abc/complete", 100, "n1", body)
    sig = sign_payload("top-secret", payload)
    assert verify_signature("top-secret", payload, sig) is True
    assert verify_signature("wrong", payload, sig) is False


def test_validate_timestamp():
    now = time.time()
    assert validate_timestamp(int(now), 300, now=now)
    assert not validate_timestamp(int(now - 1000), 300, now=now)
