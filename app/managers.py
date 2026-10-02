import sqlite3

from app.models import Actor


# add manager here
class ActorManager:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create(self, first_name, last_name):
        self.cursor.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?, ?)"
            , (first_name, last_name)
        )
        self.connection.commit()

    def all(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        self.connection.commit()
        return [Actor(*row) for row in rows]

    def update(self, pk, new_first_name, new_last_name):
        self.cursor.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?"
            , (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    def delete(self, pk):
        self.cursor.execute(f"DELETE FROM "
                            f"{self.table_name} WHERE id = ?", (pk,))
        self.connection.commit()
