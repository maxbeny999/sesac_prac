from fastapi import APIRouter, status, Body

from todo_app.schemas.todo import TodoCreate, TodoResponse
from todo_app.services.todo_service import todo_service

# 메인주소
router = APIRouter(prefix="/todos")


# 할일 등록 POST
# status_code=201: "생성 성공" 이라는 뜻을 가진 표준 코드
# response_model: 응답이 나갈 때 TodoResponse 모양으로 포장
@router.post("", status_code=status.HTTP_201_CREATED, response_model=TodoResponse)
def create_todo(todo_data: TodoCreate):
    return todo_service.create_todo(todo_data)


# 목록 조회 GET
# response_model=list[TodoResponse]: 데이터가 여러개니까 리스트로 다시 감싸줌
@router.get("", response_model=list[TodoResponse])
def get_todos():
    return todo_service.get_todos()


# [추가] 체크박스 토글 (PATCH)
# 주소 예시: /todos/3 (Body에 {"is_done": true} 실어서 보냄)
@router.patch("/{todo_id}", response_model=TodoResponse)
def update_todo_status(todo_id: int, is_done: bool = Body(embed=True)):
    return todo_service.update_status(todo_id, is_done)


# [추가] 삭제 (DELETE)
# 주소 예시: /todos/3
@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    todo_service.delete_todo(todo_id)
