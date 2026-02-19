from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)

    # 어떤 예약에 대한 리뷰인지 (1:1 관계)
    reservation_id = Column(Integer, ForeignKey("reservations.id"), unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # 작성자 편의상 추가

    rating = Column(Integer)  # 1~5점
    comment = Column(Text)
    created_at = Column(DateTime, default=func.now())

    # 관계 설정
    reservation = relationship("Reservation", back_populates="review")
    user = relationship("User", back_populates="reviews")
