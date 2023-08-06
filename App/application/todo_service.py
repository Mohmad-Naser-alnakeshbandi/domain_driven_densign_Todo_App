# App/application/todo_service.py
from App.domain.todo import Todo
from App.infrastructure.todo_repository import TodoRepository


class TodoService:
    def __init__(self, todo_repo: TodoRepository):
        self.todo_repo = todo_repo

    def add_todo(self, content: str, status:str):
        todo = Todo(id=None, content=content, created_at=None, status= status)
        self.todo_repo.add_todo(todo)

    def get_all_todos(self):
        return self.todo_repo.get_all_todos()

    def update_a_todo_status(self, todo_id: int, todo_statuss: str):
        self.todo_repo.update_a_todo_status(todo_id, todo_statuss)

    def delete_a_todo(self, todo_id: int):
        return self.todo_repo.delete_a_todo(todo_id)
