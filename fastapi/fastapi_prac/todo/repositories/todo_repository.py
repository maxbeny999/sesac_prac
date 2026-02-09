from sqlalchemy.orm import Session
from sqlalchemy import select
from todo.models.todo import Todo


class TodoRepository:
    def create_todo(self, db: Session, todo: Todo) -> Todo:
        """
        Todo 객체를 받아서 DB에 저장하고,
        ID가 생성된 최신 상태의 객체를 반환합니다.
        """
        db.add(todo)  # 1. 무대에 올리기 (Staging)
        db.commit()  # 2. 저장 확정 (Commit)
        db.refresh(todo)  # 3. 새로고침 (DB가 만들어준 ID값 받아오기)
        return todo

    def get_todos(self, db: Session) -> list[Todo]:
        """
        DB에 있는 모든 Todo 목록을 가져옵니다.
        """
        stmt = select(Todo)  # 1. "Todo 테이블 전체 선택해줘" 주문서 작성
        return db.scalars(stmt).all()  # 2. 실행해서 알맹이(Scalar)만 리스트로 반환


todo_repository = TodoRepository()
