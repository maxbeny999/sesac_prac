from pydantic import BaseModel


class MovieCreate(BaseModel):
    title: str
    year: int
    director: str
    description: str | None = None


#  2. 응답용(출력용) 스키마.
class MovieResponse(MovieCreate):
    id: int

    # [핵심] DB 객체를 Pydantic이 읽을 수 있게 해주는 설정
    class Config:
        from_attributes = True
