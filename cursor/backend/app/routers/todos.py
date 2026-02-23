from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdate
from app.services.todo_service import TodoService

router = APIRouter(prefix="/todos", tags=["todos"])


def get_todo_service(db: Session = Depends(get_db)) -> TodoService:
    return TodoService(db)


@router.get("", response_model=List[TodoResponse])
def list_todos(
    completed: Optional[bool] = None,
    service: TodoService = Depends(get_todo_service),
):
    todos = service.get_todos(completed=completed)
    return todos


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: int,
    service: TodoService = Depends(get_todo_service),
):
    todo = service.get_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.post("", response_model=TodoResponse, status_code=201)
def create_todo(
    data: TodoCreate,
    service: TodoService = Depends(get_todo_service),
):
    return service.create_todo(data)


@router.patch("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    data: TodoUpdate,
    service: TodoService = Depends(get_todo_service),
):
    todo = service.update_todo(todo_id, data)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.delete("/{todo_id}", status_code=204)
def delete_todo(
    todo_id: int,
    service: TodoService = Depends(get_todo_service),
):
    if not service.delete_todo(todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
