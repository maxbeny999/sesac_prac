from typing import List
from pydantic import BaseModel


class ActorCreate(BaseModel):
    name: str


class ActorResponse(ActorCreate):
    id: int

    class Config:
        from_attributes = True
