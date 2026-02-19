from sqlalchemy.orm import Session, joinedload
from models import Reservation
from schemas.reservation import ReservationCreate


class ReservationRepository:
    # 1. 예약 생성 (DB 저장만 담당)
    def create_reservation(
        self, db: Session, reservation: ReservationCreate, user_id: int
    ):
        new_reservation = Reservation(
            user_id=user_id,
            study_room_id=reservation.study_room_id,
            date=reservation.date,
            start_time=reservation.start_time,
            end_time=reservation.start_time + 1,  # 1시간 단위
            status="CONFIRMED",
        )
        db.add(new_reservation)
        db.commit()
        db.refresh(new_reservation)
        return new_reservation

    # 2. 내 예약 목록 조회
    def get_reservations_by_user(self, db: Session, user_id: int):
        return (
            db.query(Reservation)
            .filter(Reservation.user_id == user_id)
            .order_by(Reservation.date.desc(), Reservation.start_time.desc())
            .all()
        )

    # 3. 중복 예약 체크 (이미 예약된 방&시간인지?)
    def is_reserved(
        self, db: Session, study_room_id: int, date, start_time: int
    ) -> bool:
        # 같은 방, 같은 날짜, 같은 시간에 'CONFIRMED' 상태인 예약이 있는지 확인
        existing = (
            db.query(Reservation)
            .filter(
                Reservation.study_room_id == study_room_id,
                Reservation.date == date,
                Reservation.start_time == start_time,
                Reservation.status == "CONFIRMED",
            )
            .first()
        )

        return existing is not None  # 있으면 True(중복), 없으면 False

    def get_reservations_by_user(self, db: Session, user_id: int):
        return (
            db.query(Reservation)
            .options(joinedload(Reservation.study_room))  # JOIN으로 한방에 가져오기!
            .filter(Reservation.user_id == user_id)
            .order_by(Reservation.date.desc())
            .all()
        )
