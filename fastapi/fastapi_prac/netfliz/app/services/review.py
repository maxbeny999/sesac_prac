from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.review import ReviewRepository
from app.repositories.movie import MovieRepository
from app.schemas.review import ReviewCreate


class ReviewService:
    @staticmethod
    def create_review(db: Session, review_create: ReviewCreate):
        # 영화가 존재하는지 부터 확인(MovieRepo) 활용
        movie = MovieRepository.get_movie_by_id(db, review_create.movie_id)

        if movie is None:
            raise HTTPException(
                status_code=404, detail="리뷰를 작성할 영화가 존재하지 않습니다"
            )

        # 영화가 존재하면 리뷰 저장 진행
        return ReviewRepository.create_review(db, review_create)

    @staticmethod
    def get_reviews_by_movie_id(db: Session, movie_id: int, skip: int, limit: int):
        # 여기선 영화 존재여부를 확인 안 해도 빈 리스트가 나가니까 패스
        return ReviewRepository.get_review_by_movie_id(db, movie_id, skip, limit)
