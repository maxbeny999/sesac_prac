from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional


# 1. 예약 신청서 (Request)
class ReservationCreate(BaseModel):
    study_room_id: int
    date: date
    start_time: int

    # 시간 검증: 9시~18시 사이인지 체크
    @field_validator("start_time")
    def validate_time(cls, v):
        if not (9 <= v < 18):
            raise ValueError("운영 시간은 09:00 ~ 18:00 입니다.")
        return v


# 2. 예약 조회 영수증 (Response)
class ReservationResponse(BaseModel):
    id: int
    study_room_id: int
    user_id: int  # 누가 예약했는지
    date: date
    start_time: int
    end_time: int
    status: str

    # 관계된 데이터도 포함 가능 (나중에 심화 과정)
    # study_room_name: str

    model_config = {"from_attributes": True}
