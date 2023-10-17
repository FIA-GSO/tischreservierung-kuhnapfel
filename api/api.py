import sqlite3
from . import db
from typing import List
from datetime import datetime


def dict_factory(cursor: sqlite3.Cursor) -> List[dict]:
    return [
        dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()
    ]


def get_open_tables(start: datetime, end: datetime) -> List[dict]:
    database = db.get_db()
    cur = database.cursor()
    cur.execute("SELECT * FROM tische WHERE tischnummer NOT IN (SELECT DISTINCT reservierungen.tischnummer FROM reservierungen WHERE datetime(strftime('%s', zeitpunkt) + 3600, 'unixepoch') >= datetime(?) AND datetime(zeitpunkt) < datetime(?) AND storniert = 'False')", (start, end))

    return dict_factory(cur)