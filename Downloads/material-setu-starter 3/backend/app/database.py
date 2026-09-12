import os

import psycopg
from psycopg.rows import dict_row

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://material_setu:material_setu_dev@127.0.0.1:5433/material_setu",
)


def get_connection():
    return psycopg.connect(
        DATABASE_URL,
        row_factory=dict_row,
    )
