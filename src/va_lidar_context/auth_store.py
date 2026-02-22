from __future__ import annotations

import json
import secrets
import sqlite3
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from .util import ensure_dir

_ALLOWED_DDL_TABLES = frozenset(
    {
        "users",
        "sessions",
        "jobs",
        "build_requests",
        "active_jobs",
        "used_nonces",
        "job_artifacts",
    }
)
_ALLOWED_DDL_COLUMNS = frozenset(
    {
        "started_at",
        "exit_code",
        "error",
        "summary_json",
        "updated_at",
    }
)


def _validate_ddl_name(name: str, allowed: frozenset) -> None:
    if name not in allowed:
        raise ValueError(f"Disallowed DDL identifier: {name!r}")


def _connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA busy_timeout=5000")
    except sqlite3.DatabaseError:
        pass
    return conn


def _table_columns(conn: sqlite3.Connection, table_name: str) -> set[str]:
    _validate_ddl_name(table_name, _ALLOWED_DDL_TABLES)
    rows = conn.execute(f"PRAGMA table_info({table_name})").fetchall()
    return {str(row["name"]) for row in rows}


def _ensure_column(conn: sqlite3.Connection, table_name: str, column_name: str, ddl: str) -> None:
    _validate_ddl_name(table_name, _ALLOWED_DDL_TABLES)
    _validate_ddl_name(column_name, _ALLOWED_DDL_COLUMNS)
    columns = _table_columns(conn, table_name)
    if column_name in columns:
        return
    conn.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {ddl}")


def init_db(db_path: Path, admin_email: str | None = None) -> None:
    ensure_dir(db_path.parent)
    with _connect(db_path) as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              email TEXT NOT NULL UNIQUE,
              is_admin INTEGER NOT NULL DEFAULT 0,
              is_active INTEGER NOT NULL DEFAULT 1,
              created_at REAL NOT NULL,
              updated_at REAL NOT NULL
            );

            CREATE TABLE IF NOT EXISTS sessions (
              id TEXT PRIMARY KEY,
              user_id INTEGER NOT NULL,
              issued_at REAL NOT NULL,
              expires_at REAL NOT NULL,
              revoked_at REAL,
              FOREIGN KEY (user_id) REFERENCES users(id)
            );
            CREATE INDEX IF NOT EXISTS idx_sessions_user_id ON sessions(user_id);

            CREATE TABLE IF NOT EXISTS jobs (
              job_id TEXT PRIMARY KEY,
              user_id INTEGER,
              created_at REAL NOT NULL,
              status TEXT NOT NULL DEFAULT 'queued',
              finished_at REAL,
              FOREIGN KEY (user_id) REFERENCES users(id)
            );
            CREATE INDEX IF NOT EXISTS idx_jobs_user_id ON jobs(user_id);

            CREATE TABLE IF NOT EXISTS build_requests (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              user_id INTEGER NOT NULL,
              created_at REAL NOT NULL,
              FOREIGN KEY (user_id) REFERENCES users(id)
            );
            CREATE INDEX IF NOT EXISTS idx_build_requests_user_created
            ON build_requests(user_id, created_at);

            CREATE TABLE IF NOT EXISTS active_jobs (
              job_id TEXT PRIMARY KEY,
              user_id INTEGER NOT NULL,
              status TEXT NOT NULL,
              started_at REAL NOT NULL,
              finished_at REAL,
              FOREIGN KEY (user_id) REFERENCES users(id)
            );
            CREATE INDEX IF NOT EXISTS idx_active_jobs_user_status
            ON active_jobs(user_id, status);

            CREATE TABLE IF NOT EXISTS used_nonces (
              nonce TEXT PRIMARY KEY,
              created_at REAL NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_used_nonces_created
            ON used_nonces(created_at);

            CREATE TABLE IF NOT EXISTS job_artifacts (
              job_id TEXT NOT NULL,
              name TEXT NOT NULL,
              size INTEGER NOT NULL DEFAULT 0,
              mtime REAL NOT NULL DEFAULT 0,
              PRIMARY KEY (job_id, name),
              FOREIGN KEY (job_id) REFERENCES jobs(job_id)
            );
            CREATE INDEX IF NOT EXISTS idx_job_artifacts_job_id
            ON job_artifacts(job_id);
            """
        )
        _ensure_column(conn, "jobs", "started_at", "REAL")
        _ensure_column(conn, "jobs", "exit_code", "INTEGER")
        _ensure_column(conn, "jobs", "error", "TEXT")
        _ensure_column(conn, "jobs", "summary_json", "TEXT NOT NULL DEFAULT '{}'")
        _ensure_column(conn, "jobs", "updated_at", "REAL")

        conn.execute(
            "UPDATE jobs SET summary_json = '{}' WHERE summary_json IS NULL OR summary_json = ''"
        )
        conn.execute("UPDATE jobs SET updated_at = COALESCE(updated_at, finished_at, created_at)")
        conn.commit()

    if admin_email:
        upsert_user(db_path, admin_email.strip().lower(), is_admin=True, is_active=True)


def upsert_user(db_path: Path, email: str, is_admin: bool = False, is_active: bool = True) -> None:
    now = time.time()
    with _connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO users(email, is_admin, is_active, created_at, updated_at)
            VALUES(?, ?, ?, ?, ?)
            ON CONFLICT(email) DO UPDATE SET
              is_admin=excluded.is_admin,
              is_active=excluded.is_active,
              updated_at=excluded.updated_at
            """,
            (email.lower(), int(is_admin), int(is_active), now, now),
        )
        conn.commit()


def _row_to_user(row) -> Dict[str, Any]:
    return {
        "id": int(row["id"]),
        "email": str(row["email"]),
        "is_admin": bool(row["is_admin"]),
        "is_active": bool(row["is_active"]),
    }


def find_user_by_email(db_path: Path, email: str) -> Optional[Dict[str, Any]]:
    with _connect(db_path) as conn:
        row = conn.execute(
            "SELECT id, email, is_admin, is_active FROM users WHERE email = ?",
            (email.lower(),),
        ).fetchone()
    if row is None:
        return None
    return _row_to_user(row)


def get_user_by_id(db_path: Path, user_id: int) -> Optional[Dict[str, Any]]:
    with _connect(db_path) as conn:
        row = conn.execute(
            "SELECT id, email, is_admin, is_active FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()
    if row is None:
        return None
    return _row_to_user(row)


def list_users(db_path: Path) -> List[Dict[str, Any]]:
    with _connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT id, email, is_admin, is_active, created_at, updated_at
            FROM users
            ORDER BY email ASC
            """
        ).fetchall()
    return [
        {
            "id": int(row["id"]),
            "email": str(row["email"]),
            "is_admin": bool(row["is_admin"]),
            "is_active": bool(row["is_active"]),
            "created_at": float(row["created_at"]),
            "updated_at": float(row["updated_at"]),
        }
        for row in rows
    ]


def create_session(db_path: Path, user_id: int, ttl_seconds: int) -> str:
    sid = secrets.token_urlsafe(32)
    now = time.time()
    expires_at = now + ttl_seconds
    with _connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO sessions(id, user_id, issued_at, expires_at, revoked_at)
            VALUES(?, ?, ?, ?, NULL)
            """,
            (sid, user_id, now, expires_at),
        )
        conn.commit()
    return sid


def revoke_session(db_path: Path, sid: str) -> None:
    with _connect(db_path) as conn:
        conn.execute(
            "UPDATE sessions SET revoked_at = ? WHERE id = ?",
            (time.time(), sid),
        )
        conn.commit()


def get_user_by_session(db_path: Path, sid: str) -> Optional[Dict[str, Any]]:
    now = time.time()
    with _connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT u.id, u.email, u.is_admin, u.is_active
            FROM sessions s
            JOIN users u ON u.id = s.user_id
            WHERE s.id = ?
              AND s.revoked_at IS NULL
              AND s.expires_at > ?
            """,
            (sid, now),
        ).fetchone()
    if row is None:
        return None
    return _row_to_user(row)


def record_job_owner(db_path: Path, job_id: str, user_id: int | None) -> None:
    now = time.time()
    with _connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO jobs(job_id, user_id, created_at, status, summary_json, updated_at)
            VALUES(?, ?, ?, 'queued', '{}', ?)
            ON CONFLICT(job_id) DO UPDATE SET
              user_id = COALESCE(excluded.user_id, jobs.user_id),
              status = excluded.status,
              updated_at = excluded.updated_at
            """,
            (job_id, user_id, now, now),
        )
        conn.commit()


def set_job_status(db_path: Path, job_id: str, status: str) -> None:
    now = time.time()
    finished_at = now if status in ("done", "error") else None
    with _connect(db_path) as conn:
        conn.execute(
            """
            UPDATE jobs
            SET status = ?, finished_at = COALESCE(?, finished_at), updated_at = ?
            WHERE job_id = ?
            """,
            (status, finished_at, now, job_id),
        )
        conn.commit()


def get_job_owner_id(db_path: Path, job_id: str) -> Optional[int]:
    with _connect(db_path) as conn:
        row = conn.execute(
            "SELECT user_id FROM jobs WHERE job_id = ?",
            (job_id,),
        ).fetchone()
    if row is None:
        return None
    value = row["user_id"]
    return int(value) if value is not None else None


def delete_job(db_path: Path, job_id: str) -> None:
    with _connect(db_path) as conn:
        conn.execute("DELETE FROM job_artifacts WHERE job_id = ?", (job_id,))
        conn.execute("DELETE FROM active_jobs WHERE job_id = ?", (job_id,))
        conn.execute("DELETE FROM jobs WHERE job_id = ?", (job_id,))
        conn.commit()


def upsert_job_snapshot(
    db_path: Path,
    job_id: str,
    *,
    user_id: int | None,
    created_at: float,
    status: str,
    started_at: float | None = None,
    finished_at: float | None = None,
    exit_code: int | None = None,
    error: str | None = None,
    summary: Dict[str, Any] | None = None,
) -> None:
    now = time.time()
    summary_payload = summary if isinstance(summary, dict) else {}
    summary_json = json.dumps(summary_payload, separators=(",", ":"), sort_keys=True)
    with _connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO jobs(
              job_id,
              user_id,
              created_at,
              status,
              started_at,
              finished_at,
              exit_code,
              error,
              summary_json,
              updated_at
            )
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(job_id) DO UPDATE SET
              user_id = COALESCE(excluded.user_id, jobs.user_id),
              status = excluded.status,
              started_at = COALESCE(excluded.started_at, jobs.started_at),
              finished_at = COALESCE(excluded.finished_at, jobs.finished_at),
              exit_code = COALESCE(excluded.exit_code, jobs.exit_code),
              error = COALESCE(excluded.error, jobs.error),
              summary_json = excluded.summary_json,
              updated_at = excluded.updated_at
            """,
            (
                job_id,
                user_id,
                created_at,
                status,
                started_at,
                finished_at,
                exit_code,
                error,
                summary_json,
                now,
            ),
        )
        conn.commit()


def replace_job_artifacts(db_path: Path, job_id: str, artifacts: List[Dict[str, Any]]) -> None:
    cleaned: List[tuple[str, int, float]] = []
    seen: set[str] = set()
    for item in artifacts:
        raw_name = str(item.get("name") or "").strip()
        if not raw_name or raw_name in seen:
            continue
        if "/" in raw_name or "\\" in raw_name:
            continue
        seen.add(raw_name)
        try:
            size = max(int(item.get("size") or 0), 0)
        except Exception:
            size = 0
        try:
            mtime = float(item.get("mtime") or 0.0)
        except Exception:
            mtime = 0.0
        cleaned.append((raw_name, size, mtime))

    with _connect(db_path) as conn:
        conn.execute("DELETE FROM job_artifacts WHERE job_id = ?", (job_id,))
        if cleaned:
            conn.executemany(
                """
                INSERT INTO job_artifacts(job_id, name, size, mtime)
                VALUES(?, ?, ?, ?)
                """,
                [(job_id, name, size, mtime) for (name, size, mtime) in cleaned],
            )
        conn.commit()


def list_recent_jobs(
    db_path: Path, limit: int = 200, user_id: int | None = None
) -> List[Dict[str, Any]]:
    safe_limit = max(1, min(int(limit), 5000))
    where_clause = ""
    params: List[Any] = []
    if user_id is not None:
        where_clause = "WHERE user_id = ?"
        params.append(int(user_id))
    params.append(safe_limit)

    with _connect(db_path) as conn:
        rows = conn.execute(
            f"""
            SELECT
              job_id,
              user_id,
              created_at,
              status,
              started_at,
              finished_at,
              exit_code,
              error,
              summary_json,
              updated_at
            FROM jobs
            {where_clause}
            ORDER BY created_at DESC
            LIMIT ?
            """,
            tuple(params),
        ).fetchall()

        items: List[Dict[str, Any]] = []
        job_ids: List[str] = []
        for row in rows:
            raw_summary = row["summary_json"]
            summary: Dict[str, Any] = {}
            if isinstance(raw_summary, str) and raw_summary.strip():
                try:
                    parsed = json.loads(raw_summary)
                    if isinstance(parsed, dict):
                        summary = parsed
                except Exception:
                    summary = {}
            job_id = str(row["job_id"])
            job_ids.append(job_id)
            value = row["user_id"]
            items.append(
                {
                    "job_id": job_id,
                    "user_id": int(value) if value is not None else None,
                    "created_at": float(row["created_at"]),
                    "status": str(row["status"]),
                    "started_at": (
                        float(row["started_at"]) if row["started_at"] is not None else None
                    ),
                    "finished_at": (
                        float(row["finished_at"]) if row["finished_at"] is not None else None
                    ),
                    "exit_code": (int(row["exit_code"]) if row["exit_code"] is not None else None),
                    "error": str(row["error"]) if row["error"] is not None else None,
                    "summary": summary,
                    "artifacts": [],
                }
            )

        if not items:
            return items

        placeholders = ", ".join(["?"] * len(job_ids))
        artifact_rows = conn.execute(
            f"""
            SELECT job_id, name, size, mtime
            FROM job_artifacts
            WHERE job_id IN ({placeholders})
            ORDER BY name ASC
            """,
            tuple(job_ids),
        ).fetchall()

    artifacts_by_job: Dict[str, List[Dict[str, Any]]] = {}
    for row in artifact_rows:
        job_id = str(row["job_id"])
        artifacts_by_job.setdefault(job_id, []).append(
            {
                "name": str(row["name"]),
                "size": int(row["size"]),
                "mtime": float(row["mtime"]),
            }
        )

    for item in items:
        item["artifacts"] = artifacts_by_job.get(item["job_id"], [])
    return items


def add_build_request(db_path: Path, user_id: int) -> None:
    with _connect(db_path) as conn:
        conn.execute(
            "INSERT INTO build_requests(user_id, created_at) VALUES(?, ?)",
            (user_id, time.time()),
        )
        conn.commit()


def count_build_requests_since(db_path: Path, user_id: int, since_ts: float) -> int:
    with _connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT COUNT(*) AS count
            FROM build_requests
            WHERE user_id = ? AND created_at >= ?
            """,
            (user_id, since_ts),
        ).fetchone()
    return int(row["count"]) if row else 0


def set_active_job(db_path: Path, job_id: str, user_id: int, status: str = "queued") -> None:
    now = time.time()
    with _connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO active_jobs(job_id, user_id, status, started_at, finished_at)
            VALUES(?, ?, ?, ?, NULL)
            ON CONFLICT(job_id) DO UPDATE SET
              user_id = excluded.user_id,
              status = excluded.status
            """,
            (job_id, user_id, status, now),
        )
        conn.commit()


def finish_active_job(db_path: Path, job_id: str, status: str) -> None:
    now = time.time()
    with _connect(db_path) as conn:
        conn.execute(
            """
            UPDATE active_jobs
            SET status = ?, finished_at = ?
            WHERE job_id = ?
            """,
            (status, now, job_id),
        )
        conn.commit()


def count_active_jobs(db_path: Path, user_id: int) -> int:
    with _connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT COUNT(*) AS count
            FROM active_jobs
            WHERE user_id = ? AND status IN ('queued', 'running')
            """,
            (user_id,),
        ).fetchone()
    return int(row["count"]) if row else 0


def consume_nonce(db_path: Path, nonce: str, max_age_seconds: int) -> bool:
    now = time.time()
    cutoff = now - max_age_seconds
    with _connect(db_path) as conn:
        conn.execute("DELETE FROM used_nonces WHERE created_at < ?", (cutoff,))
        try:
            conn.execute(
                "INSERT INTO used_nonces(nonce, created_at) VALUES(?, ?)",
                (nonce, now),
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
