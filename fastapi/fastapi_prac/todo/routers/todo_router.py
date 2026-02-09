from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from todo.schemas.todo import TodoCreateRequest, TodoResponse
from todo.services.todo_service import todo_service

# prefix="/todos": 이 라우터 안의 모든 URL 앞에 /todos가 자동으로 붙습니다.
router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TodoResponse)
def create_todo_handler(
    request: TodoCreateRequest,
    db: Session = Depends(get_db),  # FastAPI가 DB 세션을 주입해줍니다.
):
    # 사용자의 요청(request)과 DB 세션(db)을 서비스에 넘깁니다.
    return todo_service.create_todo(db, request)


@router.get("", response_model=list[TodoResponse])
def get_todos_handler(db: Session = Depends(get_db)):
    return todo_service.get_todos(db)
