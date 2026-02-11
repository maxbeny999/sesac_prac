from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)  # 댓글 내용
    rating = Column(Integer)  # (평점1~5점)

    # 영화의 id 를 줘 어떤 영화의 것인지 구분.
    movie_id = Column(Integer, ForeignKey("movies.id"))

    # 관계설정. python 안에서 'review.movie' 하면 바로 영화 객체를 불러오기
    movie = relationship("Movie", back_populates="reviews")

