from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import relationship
from database import Base


class StudyRoom(Base):
    __tablename__ = "study_rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)  # 예: "4층 스터디룸 A"
    floor = Column(Integer)  # 층수 (필터링용)
    capacity = Column(Integer)  # 수용 인원
    has_whiteboard = Column(Boolean, default=False)
    has_projector = Column(Boolean, default=False)
    description = Column(Text, nullable=True)

    # 관계 설정 (StudyRoom <-> Reservation)
    reservations = relationship("Reservation", back_populates="study_room")
