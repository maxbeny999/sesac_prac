from pydantic import BaseModel


class MovieCreate(BaseModel):
    title: str
    year: int
    director: str
    description: str | None = None
