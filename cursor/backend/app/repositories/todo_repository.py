from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: TodoCreate) -> Todo:
        todo = Todo(
            title=data.title,
            description=data.description,
        )
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        return self.db.query(Todo).filter(Todo.id == todo_id).first()

    def get_list(self, completed: Optional[bool] = None) -> List[Todo]:
        q = self.db.query(Todo)
        if completed is not None:
            q = q.filter(Todo.completed == completed)
        return q.order_by(Todo.created_at.desc()).all()

    def update(self, todo: Todo, data: TodoUpdate) -> Todo:
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(todo, key, value)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def delete(self, todo: Todo) -> None:
        self.db.delete(todo)
        self.db.commit()
