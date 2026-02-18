from __future__ import annotations

import time

from va_lidar_context import auth_store


def test_user_and_session_lifecycle(tmp_path):
    db_path = tmp_path / "auth.db"
    auth_store.init_db(db_path, "admin@example.com")

    admin = auth_store.find_user_by_email(db_path, "admin@example.com")
    assert admin is not None
    assert admin["is_admin"] is True
    assert admin["is_active"] is True

    auth_store.upsert_user(db_path, "user@example.com", is_admin=False, is_active=True)
    user = auth_store.find_user_by_email(db_path, "user@example.com")
    assert user is not None

    sid = auth_store.create_session(db_path, user["id"], ttl_seconds=60)
    session_user = auth_store.get_user_by_session(db_path, sid)
    assert session_user is not None
    assert session_user["email"] == "user@example.com"

    auth_store.revoke_session(db_path, sid)
    assert auth_store.get_user_by_session(db_path, sid) is None


def test_rate_limit_and_active_jobs(tmp_path):
    db_path = tmp_path / "auth.db"
    auth_store.init_db(db_path)
    auth_store.upsert_user(db_path, "user@example.com", is_active=True)
    user = auth_store.find_user_by_email(db_path, "user@example.com")
    assert user is not None
    user_id = user["id"]

    now = time.time()
    auth_store.add_build_request(db_path, user_id)
    assert auth_store.count_build_requests_since(db_path, user_id, now - 3600) >= 1

    auth_store.set_active_job(db_path, "job1", user_id, "queued")
    assert auth_store.count_active_jobs(db_path, user_id) == 1
    auth_store.finish_active_job(db_path, "job1", "done")
    assert auth_store.count_active_jobs(db_path, user_id) == 0


def test_nonce_consume_replay(tmp_path):
    db_path = tmp_path / "auth.db"
    auth_store.init_db(db_path)
    assert auth_store.consume_nonce(db_path, "abc", max_age_seconds=10) is True
    assert auth_store.consume_nonce(db_path, "abc", max_age_seconds=10) is False
