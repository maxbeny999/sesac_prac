from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from repositories.reservation_repository import ReservationRepository
from schemas.reservation import ReservationCreate


class ReservationService:
    def __init__(self):
        # Repository를 부하직원으로 둡니다.
        self.repository = ReservationRepository()

    # 예약 신청 처리 (메인 로직)
    def create_reservation(
        self, db: Session, reservation_req: ReservationCreate, user_id: int
    ):
        # 규칙 1: 이미 예약된 시간인지 확인 (창고지기에게 물어봄)
        if self.repository.is_reserved(
            db,
            reservation_req.study_room_id,
            reservation_req.date,
            reservation_req.start_time,
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="이미 예약된 시간입니다."
            )

        # 규칙 2: (나중에 추가 가능) 하루 최대 2시간 제한 등...

        # 검증 통과하면 저장!
        return self.repository.create_reservation(db, reservation_req, user_id)

    # 내 예약 조회 처리
    def get_my_reservations(self, db: Session, user_id: int):
        return self.repository.get_reservations_by_user(db, user_id)
