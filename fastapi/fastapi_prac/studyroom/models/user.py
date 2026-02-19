from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, unique=True, index=True)  # 로그인 ID (학번)
    password = Column(String)
    name = Column(String)

    # 관계 설정 (User <-> Reservation)
    # back_populates는 상대방 모델에 있는 변수 이름이어야 함
    reservations = relationship("Reservation", back_populates="user")

    # 리뷰와의 관계도 추가 (선택사항, 나중에 편하게 쓰려고)
    reviews = relationship("Review", back_populates="user")
