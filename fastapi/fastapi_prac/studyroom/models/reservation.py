from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    UniqueConstraint,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)

    # FK (Foreign Key) 설정
    user_id = Column(Integer, ForeignKey("users.id"))
    study_room_id = Column(Integer, ForeignKey("study_rooms.id"))

    date = Column(Date, nullable=False)  # 예약 날짜
    start_time = Column(Integer, nullable=False)  # 시작 시간 (9, 10...)
    end_time = Column(Integer, nullable=False)  # 종료 시간 (10, 11...)
    status = Column(String, default="CONFIRMED")  # CONFIRMED, CANCELLED, COMPLETED

    created_at = Column(DateTime, default=func.now())  # 예약 생성 시간

    # 관계 설정
    user = relationship("User", back_populates="reservations")
    study_room = relationship("StudyRoom", back_populates="reservations")

    # 1:1 관계 (Reservation <-> Review)
    review = relationship("Review", back_populates="reservation", uselist=False)

    # 🚫 중요: DB 레벨에서 중복 예약 원천 차단
    # (같은 방, 같은 날짜, 같은 시작 시간에는 데이터가 1개만 들어가야 함)
    __table_args__ = (
        UniqueConstraint(
            "study_room_id", "date", "start_time", name="uix_room_date_time"
        ),
    )
