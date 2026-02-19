from sqlalchemy.orm import Session
from models import Review
from schemas.review import ReviewCreate


class ReviewRepository:
    # 리뷰 생성
    def create_review(self, db: Session, review_req: ReviewCreate, user_id: int):
        new_review = Review(
            user_id=user_id,
            reservation_id=review_req.reservation_id,
            rating=review_req.rating,
            comment=review_req.comment,
        )
        db.add(new_review)
        db.commit()
        db.refresh(new_review)
        return new_review

    # 특정 예약에 달린 리뷰 조회 (중복 확인용)
    def get_review_by_reservation(self, db: Session, reservation_id: int):
        return db.query(Review).filter(Review.reservation_id == reservation_id).first()
