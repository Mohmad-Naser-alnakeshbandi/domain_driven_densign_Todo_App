# App/models/todo.py
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Todo:
    id: int
    content: str
    created_at: datetime
    status: str
