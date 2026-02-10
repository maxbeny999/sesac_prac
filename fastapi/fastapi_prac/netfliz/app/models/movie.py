from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)  # 고유번호
    title = Column(String, index=True)  # 영화 제목
    year = Column(Integer)  # 개봉 연도
    director = Column(String)  # 감독
    description = Column(Text)  # 줄거리
