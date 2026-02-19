from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from repositories.review_repository import ReviewRepository
from models import Reservation
from schemas.review import ReviewCreate


class ReviewService:
    def __init__(self):
        self.repository = ReviewRepository()

    def create_review(self, db: Session, review_req: ReviewCreate, user_id: int):
        # 1. 예약 정보 조회 (ORM 사용)
        reservation = (
            db.query(Reservation)
            .filter(Reservation.id == review_req.reservation_id)
            .first()
        )

        # 2. 예약이 없거나, 남의 예약인 경우 차단
        if not reservation:
            raise HTTPException(status_code=404, detail="예약 정보를 찾을 수 없습니다.")

        if reservation.user_id != user_id:
            raise HTTPException(
                status_code=403, detail="본인의 예약에만 리뷰를 작성할 수 있습니다."
            )

        # 3. (선택) 이용 완료 상태 체크
        # 실습 중에는 편의를 위해 주석 처리합니다. 필요시 주석 해제하고 DB에서 status를 변경해보세요.
        # if reservation.status != "COMPLETED":
        #     raise HTTPException(status_code=400, detail="이용이 완료된 예약만 리뷰를 작성할 수 있습니다.")

        # 4. 중복 리뷰 체크 (1:1 관계)
        if self.repository.get_review_by_reservation(db, review_req.reservation_id):
            raise HTTPException(
                status_code=409, detail="이미 리뷰를 작성한 예약입니다."
            )

        return self.repository.create_review(db, review_req, user_id)
