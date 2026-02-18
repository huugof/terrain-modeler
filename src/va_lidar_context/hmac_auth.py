from __future__ import annotations

import hashlib
import hmac
import json
import time
from typing import Dict, Optional


def parse_key_map(raw: str) -> Dict[str, str]:
    payload = json.loads(raw)
    if not isinstance(payload, dict):
        raise ValueError("HMAC key payload must be a JSON object.")
    keys: Dict[str, str] = {}
    for key_id, secret in payload.items():
        if not isinstance(key_id, str) or not isinstance(secret, str):
            continue
        key_id = key_id.strip()
        secret = secret.strip()
        if key_id and secret:
            keys[key_id] = secret
    return keys


def canonical_payload(
    method: str,
    path: str,
    timestamp: int,
    nonce: str,
    body: bytes,
) -> bytes:
    digest = hashlib.sha256(body).hexdigest()
    base = "\n".join(
        [
            method.upper(),
            path,
            str(timestamp),
            nonce,
            digest,
        ]
    )
    return base.encode("utf-8")


def sign_payload(secret: str, payload: bytes) -> str:
    return hmac.new(secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()


def verify_signature(secret: str, payload: bytes, signature: str) -> bool:
    expected = sign_payload(secret, payload)
    return hmac.compare_digest(expected, signature)


def validate_timestamp(timestamp: int, max_skew_seconds: int, now: float | None = None) -> bool:
    ref = now if now is not None else time.time()
    return abs(ref - timestamp) <= max_skew_seconds


def choose_secret(key_map: Dict[str, str], key_id: str) -> Optional[str]:
    return key_map.get(key_id)
