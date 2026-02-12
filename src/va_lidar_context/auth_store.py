from __future__ import annotations

import secrets
import sqlite3
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from .util import ensure_dir


def _connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


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
            """
        )
        conn.commit()

    if admin_email:
        upsert_user(db_path, admin_email.strip().lower(), is_admin=True, is_active=True)


def upsert_user(
    db_path: Path, email: str, is_admin: bool = False, is_active: bool = True
) -> None:
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


def find_user_by_email(db_path: Path, email: str) -> Optional[Dict[str, Any]]:
    with _connect(db_path) as conn:
        row = conn.execute(
            "SELECT id, email, is_admin, is_active FROM users WHERE email = ?",
            (email.lower(),),
        ).fetchone()
    if row is None:
        return None
    return {
        "id": int(row["id"]),
        "email": str(row["email"]),
        "is_admin": bool(row["is_admin"]),
        "is_active": bool(row["is_active"]),
    }


def get_user_by_id(db_path: Path, user_id: int) -> Optional[Dict[str, Any]]:
    with _connect(db_path) as conn:
        row = conn.execute(
            "SELECT id, email, is_admin, is_active FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()
    if row is None:
        return None
    return {
        "id": int(row["id"]),
        "email": str(row["email"]),
        "is_admin": bool(row["is_admin"]),
        "is_active": bool(row["is_active"]),
    }


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
    return {
        "id": int(row["id"]),
        "email": str(row["email"]),
        "is_admin": bool(row["is_admin"]),
        "is_active": bool(row["is_active"]),
    }


def record_job_owner(db_path: Path, job_id: str, user_id: int | None) -> None:
    with _connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO jobs(job_id, user_id, created_at, status)
            VALUES(?, ?, ?, 'queued')
            ON CONFLICT(job_id) DO UPDATE SET
              user_id = COALESCE(excluded.user_id, jobs.user_id),
              status = excluded.status
            """,
            (job_id, user_id, time.time()),
        )
        conn.commit()


def set_job_status(db_path: Path, job_id: str, status: str) -> None:
    now = time.time()
    finished_at = now if status in ("done", "error") else None
    with _connect(db_path) as conn:
        conn.execute(
            """
            UPDATE jobs
            SET status = ?, finished_at = COALESCE(?, finished_at)
            WHERE job_id = ?
            """,
            (status, finished_at, job_id),
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
