"""Bring the database schema up to date on startup.

``db/schema.sql`` and every file in ``db/migrations/`` are written to be
idempotent (``CREATE ... IF NOT EXISTS`` / ``ADD COLUMN IF NOT EXISTS``), so we
can safely replay all of them every time the API (or the seed script) starts.
This removes the "did you run ``make migrate``?" foot-gun.
"""

from pathlib import Path

import psycopg

from .database import DATABASE_URL

_DB_DIR = Path(__file__).resolve().parents[2] / "db"


def ensure_schema() -> None:
    files = [_DB_DIR / "schema.sql"]
    migrations = _DB_DIR / "migrations"
    if migrations.is_dir():
        files += sorted(migrations.glob("*.sql"))

    try:
        with psycopg.connect(DATABASE_URL, autocommit=True) as conn:
            for path in files:
                sql = path.read_text(encoding="utf-8").strip()
                if sql:
                    conn.execute(sql)
    except Exception as exc:  # noqa: BLE001 - never block startup on this
        print(f"[db_bootstrap] schema sync skipped: {exc}")
