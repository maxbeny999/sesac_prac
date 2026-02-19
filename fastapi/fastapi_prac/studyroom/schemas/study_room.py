from pydantic import BaseModel, Field
from typing import Optional


class StudyRoomBase(BaseModel):
    name: str
    floor: int
    capacity: int
    has_whiteboard: bool = False
    has_projector: bool = False
    description: Optional[str] = None


# 스터디룸 생성 (관리자용 - 나중을 위해 만들어둠)
class StudyRoomCreate(StudyRoomBase):
    pass


# 스터디룸 조회 응답
class StudyRoomResponse(StudyRoomBase):
    id: int

    model_config = {"from_attributes": True}
