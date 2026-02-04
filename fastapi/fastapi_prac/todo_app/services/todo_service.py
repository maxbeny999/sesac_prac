from fastapi import HTTPException
from todo_app.repositories.todo_repository import todo_repository
from todo_app.schemas.todo import TodoCreate, Todo


class TodoService:
    def create_todo(self, todo_data: TodoCreate):
        # 규칙검사(비즈니스 로직)
        if not todo_data.task:
            # 에러 발생시
            raise HTTPException(status_code=422, detail="할 일을 입력해주세요")

        # 변환 (스키마 -> 엔티티)
        # 신청서(todo_data) 를 토대로 실제 저장할 객체 생성(Todo)
        new_todo = Todo(id=None, task=todo_data.task, is_done=todo_data.is_done)

        result = todo_repository.save(new_todo)
        return result

    def get_todos(self):
        return todo_repository.get_all()

    def update_status(self, todo_id: int, is_done: bool):
        # 있는지 없는지 확인은 레포지토리가 처리하게 뒀지만,
        # 더 꼼꼼하게 하려면 여기서 get으로 확인 먼저 하는 게 정석입니다.
        updated_todo = todo_repository.update_status(todo_id, is_done)
        if not updated_todo:
            raise HTTPException(status_code=404, detail="할 일을 찾을 수 없습니다.")
        return updated_todo

    # [추가] 삭제
    def delete_todo(self, todo_id: int):
        todo_repository.delete(todo_id)


todo_service = TodoService()
