from sqlalchemy.orm import Session
from todo.models.todo import Todo
from todo.schemas.todo import TodoCreateRequest
from todo.repositories.todo_repository import todo_repository


class TodoService:
    def create_todo(self, db: Session, request: TodoCreateRequest):
        # 1. 스키마(요청 데이터) -> 모델(DB 데이터) 변환
        # 사용자는 content만 보냈지만, DB에는 is_done=False가 기본으로 들어갑니다.
        new_todo = Todo(content=request.content)

        # 2. Repository에게 "저장해줘" 요청
        return todo_repository.create_todo(db, new_todo)

    def get_todos(self, db: Session):
        # 복잡한 로직 없이 바로 목록 조회 요청
        return todo_repository.get_todos(db)


todo_service = TodoService()
