from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # [M:N] 관계 배우도 자기가 출현한 역할을 조회 가능하게 해야함.
    # secondary="movie_actor" 라고 테이블의 이름을 문자로 적음
    movies = relationship("Movie", secondary="movie_actor", back_populates="actors")
