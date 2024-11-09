import sqlite3
from typing import Any


class DBManager:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def execute(
        self,
        query: str,
        meny: bool = True,
        insert_data: list[Any] = None,
    ) -> list[tuple[Any]]:
        with sqlite3.connect(self.db_path) as con:
            cursor = con.cursor()
            if meny:
                return_data: sqlite3.Cursor = cursor.executemany(query, insert_data)
            else:
                return_data: sqlite3.Cursor = cursor.execute(query)
            return return_data.fetchall()


db_manager = DBManager("my_db.db")
