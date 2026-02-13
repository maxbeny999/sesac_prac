from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)  # 고유번호
    title = Column(String, index=True)  # 영화 제목
    year = Column(Integer)  # 개봉 연도
    description = Column(Text)  # 줄거리

    # 감독 id 외래키로 추가
    director_id = Column(Integer, ForeignKey("directors.id"))

    director = relationship("Director", back_populates="movies")

    # 연결된 리뷰 불러오기
    reviews = relationship("Review", back_populates="movie")
