from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.review import ReviewCreate, ReviewResponse
from app.services.review import ReviewService

router = APIRouter(prefix="/reviews", tags=["reviews"])


# 1.리뷰 등록 (Post /reviews/)
@router.post("/", status_code=201, response_model=ReviewResponse)
def create_review(review_create: ReviewCreate, db: Session = Depends(get_db)):
    return ReviewService.create_review(db, review_create)


# 2. 특정 영화의 리뷰 조회 (GET /review/movie/{movie_id})


@router.get("/movie/{movie_id}", response_model=List[ReviewResponse])
def get_reviews_by_movie(
    movie_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    return ReviewService.get_reviews_by_movie_id(db, movie_id, skip, limit)
