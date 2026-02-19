from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas.reservation import ReservationCreate, ReservationResponse
from services.reservation_service import ReservationService
from models import User
from dependencies import get_current_user  # 방금 만든 검문소!

router = APIRouter(prefix="/reservations", tags=["reservations"])

# 셰프(Service) 준비
reservation_service = ReservationService()


# 1. 예약하기
@router.post(
    "/", response_model=ReservationResponse, status_code=status.HTTP_201_CREATED
)
def create_reservation(
    reservation_req: ReservationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),  # 로그인 필수!
):
    # 서비스(셰프)에게 주문 전달
    return reservation_service.create_reservation(db, reservation_req, current_user.id)


# 2. 내 예약 목록 보기
@router.get("/me", response_model=List[ReservationResponse])
def read_my_reservations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),  # 로그인 필수!
):
    return reservation_service.get_my_reservations(db, current_user.id)
