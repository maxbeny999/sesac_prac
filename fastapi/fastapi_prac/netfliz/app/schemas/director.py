from pydantic import BaseModel


class DirectorCreate(BaseModel):
    name: str


class DirectorResponse(DirectorCreate):
    id: int

    class Config:
        from_attributes = True
