from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

# M:N 다대다 관계를 위한 중간 테이블
# 클래스가 아닌 순수 Table 객체
# 몇번 영화에 몇번 배우가 나온다. 라는 출석부 역할
movie_actor = Table(
    "movie_actor",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id"), primary_key=True),
    Column("actor_id", Integer, ForeignKey("actors.id"), primary_key=True),
)


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

    actors = relationship("Actor", secondary=movie_actor, back_populates="movies")
