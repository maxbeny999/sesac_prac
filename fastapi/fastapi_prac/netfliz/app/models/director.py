from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # 감독 이름

    # 관계 설정 감독 1명 : 영화 N개
    # 영화에서 'director 라는 변수로 감독 찾게 연결
    movies = relationship("Movie", back_populates="director")
