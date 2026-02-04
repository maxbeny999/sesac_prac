# from pydantic import BaseModel


# # 기본 todo
# class Todo:
#     def __init__(self, id, task, is_done):
#         self.id = id
#         self.task = task
#         self.is_done = is_done


# # todoCreate (사용자가 보낼 데이터)
# class TodoCreate(BaseModel):
#     task: str
#     is_done: bool = False

# # todoResponse (사용자에게 보여줄 데이터)
# class TodoResponse(BaseModel):
#     id: int
#     task: str
#     is_done: bool

from sqlmodel import SQLModel, Field
from typing import Optional


# DB 테이블 겸 저장용 객체 엔티티
class Todo(SQLModel, table=True):
    # 프라임 키 True 이 번호가 고유id
    id: Optional[int] = Field(default=None, primary_key=True)
    task: str
    is_done: bool = False


# 입력용
class TodoCreate(SQLModel):
    task: str
    is_done: bool = False


# 응답용
class TodoResponse(SQLModel):
    id: int
    task: str
    is_done: bool
