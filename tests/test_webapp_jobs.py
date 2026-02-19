from __future__ import annotations

import io
import threading
import time
import zipfile
from pathlib import Path

import pytest

from va_lidar_context import auth_store, webapp


@pytest.fixture()
def auth_webapp_env(tmp_path, monkeypatch):
    out_dir = tmp_path / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    db_path = tmp_path / "app.db"

    monkeypatch.setattr(webapp, "AUTH_ENABLED", True)
    monkeypatch.setattr(webapp, "DB_PATH", db_path)
    monkeypatch.setattr(webapp, "OUT_DIR", out_dir)
    monkeypatch.setattr(webapp, "_auth_started", False)
    monkeypatch.setattr(webapp, "_recent_jobs_change_version", 0)

    with webapp.JOBS_LOCK:
        webapp.JOBS.clear()

    webapp.ensure_auth_store()

    auth_store.upsert_user(db_path, "user1@example.com", is_active=True)
    auth_store.upsert_user(db_path, "user2@example.com", is_active=True)

    user1 = auth_store.find_user_by_email(db_path, "user1@example.com")
    user2 = auth_store.find_user_by_email(db_path, "user2@example.com")
    assert user1 is not None and user2 is not None

    sid1 = auth_store.create_session(db_path, int(user1["id"]), ttl_seconds=3600)
    sid2 = auth_store.create_session(db_path, int(user2["id"]), ttl_seconds=3600)

    yield {
        "out_dir": out_dir,
        "db_path": db_path,
        "user1": user1,
        "user2": user2,
        "sid1": sid1,
        "sid2": sid2,
    }

    with webapp.JOBS_LOCK:
        webapp.JOBS.clear()


def _client_for_sid(sid: str):
    client = webapp.app.test_client()
    with client.session_transaction() as sess:
        sess["sid"] = sid
        sess["csrf_token"] = "test-csrf"
    return client


def _create_job(
    *,
    job_id: str,
    owner_id: int,
    out_dir: Path,
    db_path: Path,
    files: list[str],
    status: str = "done",
    created_at: float | None = None,
    custom_name: str = "",
) -> webapp.Job:
    job_dir = out_dir / job_id
    job_dir.mkdir(parents=True, exist_ok=True)
    for name in files:
        (job_dir / name).write_text(f"dummy {name}\n")

    summary_name = custom_name or job_id
    job = webapp.Job(
        job_id=job_id,
        status=status,
        created_at=created_at if created_at is not None else time.time(),
        user_id=owner_id,
        summary={
            "name": summary_name,
            "custom_name": custom_name,
            "outputs": {"dir": str(job_dir), "files": files},
        },
    )
    with webapp.JOBS_LOCK:
        webapp.JOBS[job_id] = job

    auth_store.record_job_owner(db_path, job_id, owner_id)
    auth_store.set_job_status(db_path, job_id, status)
    return job


def test_recent_jobs_scoped_to_current_user(auth_webapp_env):
    _create_job(
        job_id="job-user1",
        owner_id=int(auth_webapp_env["user1"]["id"]),
        out_dir=auth_webapp_env["out_dir"],
        db_path=auth_webapp_env["db_path"],
        files=["terrain.obj"],
    )
    _create_job(
        job_id="job-user2",
        owner_id=int(auth_webapp_env["user2"]["id"]),
        out_dir=auth_webapp_env["out_dir"],
        db_path=auth_webapp_env["db_path"],
        files=["terrain.obj"],
    )

    client1 = _client_for_sid(auth_webapp_env["sid1"])
    resp1 = client1.get("/recent-jobs")
    assert resp1.status_code == 200
    jobs1 = resp1.get_json()["jobs"]
    assert [j["job_id"] for j in jobs1] == ["job-user1"]

    client2 = _client_for_sid(auth_webapp_env["sid2"])
    resp2 = client2.get("/recent-jobs")
    assert resp2.status_code == 200
    jobs2 = resp2.get_json()["jobs"]
    assert [j["job_id"] for j in jobs2] == ["job-user2"]


def test_recent_jobs_use_user_sequence_labels(auth_webapp_env):
    owner_id = int(auth_webapp_env["user1"]["id"])
    base = time.time()
    for idx in range(1, 7):
        _create_job(
            job_id=f"job-{idx}",
            owner_id=owner_id,
            out_dir=auth_webapp_env["out_dir"],
            db_path=auth_webapp_env["db_path"],
            files=["terrain.obj"],
            status="done",
            created_at=base + idx,
            custom_name="House" if idx == 5 else "",
        )

    client = _client_for_sid(auth_webapp_env["sid1"])
    resp = client.get("/recent-jobs")
    assert resp.status_code == 200
    payload = resp.get_json()["jobs"]
    by_job_id = {item["job_id"]: item for item in payload}
    assert by_job_id["job-4"]["name"] == "Job 4"
    assert by_job_id["job-5"]["name"] == "House"
    assert by_job_id["job-6"]["name"] == "Job 6"


def test_non_owner_cannot_access_job_routes(auth_webapp_env):
    _create_job(
        job_id="job-owned",
        owner_id=int(auth_webapp_env["user1"]["id"]),
        out_dir=auth_webapp_env["out_dir"],
        db_path=auth_webapp_env["db_path"],
        files=["terrain.obj"],
    )

    client2 = _client_for_sid(auth_webapp_env["sid2"])

    status_resp = client2.get("/jobs/job-owned", headers={"Accept": "application/json"})
    assert status_resp.status_code == 403

    artifacts_resp = client2.get("/jobs/job-owned/artifacts")
    assert artifacts_resp.status_code == 403

    download_resp = client2.get("/jobs/job-owned/download/terrain.obj")
    assert download_resp.status_code == 403


def test_download_all_and_inline_download(auth_webapp_env):
    _create_job(
        job_id="job-zip",
        owner_id=int(auth_webapp_env["user1"]["id"]),
        out_dir=auth_webapp_env["out_dir"],
        db_path=auth_webapp_env["db_path"],
        files=["terrain.obj", "buildings.obj", "terrain.mtl"],
    )

    client = _client_for_sid(auth_webapp_env["sid1"])

    zip_resp = client.get("/jobs/job-zip/download-all")
    assert zip_resp.status_code == 200
    assert zip_resp.mimetype == "application/zip"

    with zipfile.ZipFile(io.BytesIO(zip_resp.data), "r") as archive:
        names = sorted(archive.namelist())
    assert names == ["buildings.obj", "terrain.mtl", "terrain.obj"]

    attachment_resp = client.get("/jobs/job-zip/download/terrain.obj")
    assert attachment_resp.status_code == 200
    assert (
        "attachment"
        in (attachment_resp.headers.get("Content-Disposition") or "").lower()
    )

    inline_resp = client.get("/jobs/job-zip/download/terrain.obj?inline=1")
    assert inline_resp.status_code == 200
    assert (
        "attachment"
        not in (inline_resp.headers.get("Content-Disposition") or "").lower()
    )


def test_download_rejects_invalid_file_name(auth_webapp_env):
    _create_job(
        job_id="job-safe",
        owner_id=int(auth_webapp_env["user1"]["id"]),
        out_dir=auth_webapp_env["out_dir"],
        db_path=auth_webapp_env["db_path"],
        files=["terrain.obj"],
    )

    client = _client_for_sid(auth_webapp_env["sid1"])
    resp = client.get("/jobs/job-safe/download/..%5Csecret.txt")
    assert resp.status_code == 400


def test_recent_jobs_rehydrate_from_db(auth_webapp_env, monkeypatch):
    job_id = "job-restored"
    job_dir = auth_webapp_env["out_dir"] / job_id
    job_dir.mkdir(parents=True, exist_ok=True)
    (job_dir / "terrain.obj").write_text("dummy terrain\n")

    auth_store.upsert_job_snapshot(
        auth_webapp_env["db_path"],
        job_id,
        user_id=int(auth_webapp_env["user1"]["id"]),
        created_at=time.time(),
        status="done",
        summary={"name": "restored-job"},
    )
    auth_store.replace_job_artifacts(
        auth_webapp_env["db_path"],
        job_id,
        [{"name": "terrain.obj", "size": 12, "mtime": time.time()}],
    )

    with webapp.JOBS_LOCK:
        webapp.JOBS.clear()
    monkeypatch.setattr(webapp, "_auth_started", False)
    webapp.ensure_auth_store()

    with webapp.JOBS_LOCK:
        restored = webapp.JOBS.get(job_id)
        assert restored is not None
        assert restored.summary.get("name") == "restored-job"
        outputs = restored.summary.get("outputs")
        assert isinstance(outputs, dict)
        assert "terrain.obj" in outputs.get("files", [])

    client = _client_for_sid(auth_webapp_env["sid1"])
    resp = client.get("/recent-jobs")
    assert resp.status_code == 200
    jobs = resp.get_json()["jobs"]
    assert jobs and jobs[0]["job_id"] == job_id


def test_rehydrate_discovers_nested_output_dir_from_report(auth_webapp_env, monkeypatch):
    job_id = "job-nested-output"
    nested_dir = auth_webapp_env["out_dir"] / job_id / "tile-abc"
    nested_dir.mkdir(parents=True, exist_ok=True)
    (nested_dir / "terrain.obj").write_text("dummy terrain\n")
    (nested_dir / "report.json").write_text(f'{{"output_dir": "{nested_dir}"}}')

    auth_store.upsert_job_snapshot(
        auth_webapp_env["db_path"],
        job_id,
        user_id=int(auth_webapp_env["user1"]["id"]),
        created_at=time.time(),
        status="done",
        summary={"name": "nested"},
    )
    # Intentionally do not write job_artifacts rows to mimic legacy records.
    auth_store.replace_job_artifacts(auth_webapp_env["db_path"], job_id, [])

    with webapp.JOBS_LOCK:
        webapp.JOBS.clear()
    monkeypatch.setattr(webapp, "_auth_started", False)
    webapp.ensure_auth_store()

    client = _client_for_sid(auth_webapp_env["sid1"])
    artifacts_resp = client.get(f"/jobs/{job_id}/artifacts")
    assert artifacts_resp.status_code == 200
    files = artifacts_resp.get_json()["files"]
    names = [item["name"] for item in files]
    assert "terrain.obj" in names


def test_job_logs_long_poll_returns_when_log_arrives(auth_webapp_env):
    user_id = int(auth_webapp_env["user1"]["id"])
    job = _create_job(
        job_id="job-log-wait",
        owner_id=user_id,
        out_dir=auth_webapp_env["out_dir"],
        db_path=auth_webapp_env["db_path"],
        files=[],
        status="running",
    )

    def append_log() -> None:
        time.sleep(0.05)
        with job.change_cond:
            job.logs.append("INFO: hello from worker")
            webapp._notify_job_change_locked(job)

    threading.Thread(target=append_log, daemon=True).start()

    client = _client_for_sid(auth_webapp_env["sid1"])
    started = time.monotonic()
    resp = client.get("/logs/job-log-wait?offset=0&wait=1")
    elapsed = time.monotonic() - started
    assert resp.status_code == 200
    payload = resp.get_json()
    assert payload["status"] == "running"
    assert payload["logs"] == ["INFO: hello from worker"]
    assert payload["offset"] == 1
    assert elapsed >= 0.04


def test_job_logs_long_poll_times_out_without_changes(auth_webapp_env):
    user_id = int(auth_webapp_env["user1"]["id"])
    _create_job(
        job_id="job-log-timeout",
        owner_id=user_id,
        out_dir=auth_webapp_env["out_dir"],
        db_path=auth_webapp_env["db_path"],
        files=[],
        status="running",
    )

    client = _client_for_sid(auth_webapp_env["sid1"])
    started = time.monotonic()
    resp = client.get("/logs/job-log-timeout?offset=0&wait=0.1")
    elapsed = time.monotonic() - started
    assert resp.status_code == 200
    payload = resp.get_json()
    assert payload["status"] == "running"
    assert payload["logs"] == []
    assert payload["offset"] == 0
    assert elapsed >= 0.08


def test_recent_jobs_long_poll_returns_on_change(auth_webapp_env):
    owner_id = int(auth_webapp_env["user1"]["id"])
    job = _create_job(
        job_id="job-recent-wait",
        owner_id=owner_id,
        out_dir=auth_webapp_env["out_dir"],
        db_path=auth_webapp_env["db_path"],
        files=[],
        status="running",
    )

    client = _client_for_sid(auth_webapp_env["sid1"])
    initial = client.get("/recent-jobs")
    assert initial.status_code == 200
    since_version = int(initial.get_json()["version"])

    def finish_job() -> None:
        time.sleep(0.05)
        with job.change_cond:
            job.status = "done"
            webapp._notify_job_change_locked(job)
        webapp._notify_recent_jobs_change()

    threading.Thread(target=finish_job, daemon=True).start()

    started = time.monotonic()
    resp = client.get(f"/recent-jobs?since={since_version}&wait=1")
    elapsed = time.monotonic() - started
    assert resp.status_code == 200
    payload = resp.get_json()
    assert int(payload["version"]) > since_version
    jobs = payload["jobs"]
    assert jobs and jobs[0]["job_id"] == "job-recent-wait"
    assert jobs[0]["status"] == "done"
    assert elapsed >= 0.04


def test_recent_jobs_long_poll_times_out_without_change(auth_webapp_env):
    owner_id = int(auth_webapp_env["user1"]["id"])
    _create_job(
        job_id="job-recent-timeout",
        owner_id=owner_id,
        out_dir=auth_webapp_env["out_dir"],
        db_path=auth_webapp_env["db_path"],
        files=[],
        status="running",
    )

    client = _client_for_sid(auth_webapp_env["sid1"])
    initial = client.get("/recent-jobs")
    assert initial.status_code == 200
    since_version = int(initial.get_json()["version"])

    started = time.monotonic()
    resp = client.get(f"/recent-jobs?since={since_version}&wait=0.1")
    elapsed = time.monotonic() - started
    assert resp.status_code == 200
    payload = resp.get_json()
    assert int(payload["version"]) == since_version
    assert elapsed >= 0.08
