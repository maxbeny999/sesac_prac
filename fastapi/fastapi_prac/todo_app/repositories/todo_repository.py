# from todo_app.schemas.todo import Todo


# class TodoRepository:
#     def __init__(self):
#         # db 대용
#         self.todos = []
#         # id 관리용
#         self.todo_id = 0

#     def save(self, todo: Todo):
#         # id 1씩 증가
#         self.todo_id += 1
#         # 데이터에 id 부여
#         todo.id = self.todo_id
#         # 리스트에 저장
#         self.todos.append(todo)

#     def get_all(self):
#         return self.todos


# todo_repository = TodoRepository()

# -----------------------------------------------

from sqlmodel import Session, select
from todo_app.connection import engine
from todo_app.schemas.todo import Todo


class TodoRepository:
    def save(self, todo: Todo):
        # DB 열고 세션 넣고 저장 새로고침
        with Session(engine) as session:
            session.add(todo)
            session.commit()
            session.refresh(todo)  # DB가 만든 id 받아오기
            return todo

    def get_all(self):
        with Session(engine) as session:
            # Select * From Todo 와 같은 뜻
            statement = select(Todo).order_by(Todo.id)
            results = session.exec(statement).all()
            return results

        # [추가] 상태 변경 (체크/체크해제)

    def update_status(self, todo_id: int, is_done: bool):
        with Session(engine) as session:
            todo = session.get(Todo, todo_id)
            if todo:
                todo.is_done = is_done
                session.add(todo)
                session.commit()
                session.refresh(todo)
            return todo

    # [추가] 삭제 기능
    def delete(self, todo_id: int):
        with Session(engine) as session:
            todo = session.get(Todo, todo_id)
            if todo:
                session.delete(todo)
                session.commit()


todo_repository = TodoRepository()
