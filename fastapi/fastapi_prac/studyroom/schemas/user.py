from pydantic import BaseModel, EmailStr, Field


# 1. 공통 속성 (Base)
class UserBase(BaseModel):
    student_id: str = Field(..., description="학번 (로그인 ID)")
    name: str = Field(..., min_length=2, max_length=10, description="사용자 실명")


# 2. 회원가입용 (비밀번호 필요)
class UserCreate(UserBase):
    password: str = Field(..., min_length=4, description="비밀번호")


# 3. 로그인용
class UserLogin(BaseModel):
    student_id: str
    password: str


# 4. 응답용 (비밀번호 제외!)
class UserResponse(UserBase):
    id: int

    # 중요: ORM 객체(SQLAlchemy)를 Pydantic으로 변환 허용
    model_config = {"from_attributes": True}
