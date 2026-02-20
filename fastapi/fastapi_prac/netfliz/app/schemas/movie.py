from typing import List
from pydantic import BaseModel
from app.schemas.review import ReviewResponse
from app.schemas.director import DirectorResponse
from app.schemas.actor import ActorResponse


class MovieCreate(BaseModel):
    title: str
    year: int
    director_id: int
    description: str | None = None


#  2. 응답용(출력용) 스키마.
class MovieResponse(MovieCreate):
    id: int
    reviews: List[ReviewResponse] = []  # <--- [NEW] 영화 정보 안에 리뷰 리스트 포함!

    director: DirectorResponse | None = None
    actors: List[ActorResponse] = []

    class Config:
        from_attributes = True
