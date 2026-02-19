import os
from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt  # JWT 처리를 위해 추가
from dotenv import load_dotenv

from database import get_db
from models.user import User

# UserLogin 스키마 추가 임포트
from schemas.user import UserCreate, UserResponse, UserLogin

# 환경 변수 로드 (토큰 생성용)
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

router = APIRouter(prefix="/users", tags=["users"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# --- JWT 토큰 생성 함수 추가 ---
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# 3. 회원가입 API
@router.post(
    "/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.student_id == user.student_id).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="이미 등록된 학번입니다."
        )

    hashed_password = pwd_context.hash(user.password)
    new_user = User(
        student_id=user.student_id, password=hashed_password, name=user.name
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# 4. 로그인 API (수정 완료)
@router.post("/login")
def login(user_req: UserLogin, db: Session = Depends(get_db)):
    # 1. 유저 찾기
    user = db.query(User).filter(User.student_id == user_req.student_id).first()
    if not user:
        raise HTTPException(
            status_code=401, detail="학번 또는 비밀번호가 잘못되었습니다."
        )

    # 2. 비밀번호 검증
    if not pwd_context.verify(user_req.password, user.password):
        raise HTTPException(
            status_code=401, detail="학번 또는 비밀번호가 잘못되었습니다."
        )

    # 3. 토큰 발급
    access_token = create_access_token(data={"sub": user.student_id})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_name": user.name,
    }
