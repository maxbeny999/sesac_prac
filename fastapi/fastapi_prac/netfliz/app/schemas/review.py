from pydantic import BaseModel


# 입력용 (작성하는 신청서 양식)
class ReviewCreate(BaseModel):
    content: str  # 리뷰내용
    rating: int  # 평점 1~5
    movie_id: int  # 어떤 영화에 단 리뷰인지 확인


# 출력용 (우리가 보여줄 양식)
class ReviewResponse(ReviewCreate):
    id: int  # db가 발급해준 리뷰 번호

    class Config:
        from_attributes = True  # ORM 활성화
