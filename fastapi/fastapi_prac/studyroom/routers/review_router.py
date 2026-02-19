from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.review import ReviewCreate, ReviewResponse
from services.review_service import ReviewService
from models import User
from dependencies import get_current_user

router = APIRouter(prefix="/reviews", tags=["reviews"])

# 셰프(Service) 준비
review_service = ReviewService()


@router.post("/", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
def create_review(
    review_req: ReviewCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),  # 로그인 필수
):
    return review_service.create_review(db, review_req, current_user.id)
