# App/infrastructure/todo_repository.py
import sqlite3
from typing import List

from App.domain.todo import Todo


class TodoRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def add_todo(self, todo: Todo):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO todos (content, status) VALUES (?,?)", (todo.content, todo.status))
            conn.commit()

    def get_all_todos(self) -> List[Todo]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, content, created_at, status FROM todos")
            rows = cursor.fetchall()
            return [Todo(*row) for row in rows]

    def update_a_todo_status(self, todo_id: int, todo_status: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE todos SET status=? WHERE id=?", (todo_status, todo_id))
            conn.commit()

    def delete_a_todo(self, todo_id: int):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
            conn.commit()
