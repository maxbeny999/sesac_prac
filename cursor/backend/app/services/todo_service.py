from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.todo import Todo
from app.repositories.todo_repository import TodoRepository
from app.schemas.todo import TodoCreate, TodoUpdate


class TodoService:
    def __init__(self, db: Session):
        self.repository = TodoRepository(db)

    def create_todo(self, data: TodoCreate) -> Todo:
        return self.repository.create(data)

    def get_todo(self, todo_id: int) -> Optional[Todo]:
        return self.repository.get_by_id(todo_id)

    def get_todos(self, completed: Optional[bool] = None) -> List[Todo]:
        return self.repository.get_list(completed=completed)

    def update_todo(self, todo_id: int, data: TodoUpdate) -> Optional[Todo]:
        todo = self.repository.get_by_id(todo_id)
        if todo is None:
            return None
        return self.repository.update(todo, data)

    def delete_todo(self, todo_id: int) -> bool:
        todo = self.repository.get_by_id(todo_id)
        if todo is None:
            return False
        self.repository.delete(todo)
        return True
