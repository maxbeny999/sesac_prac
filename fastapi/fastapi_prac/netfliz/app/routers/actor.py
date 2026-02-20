from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.actor import ActorCreate, ActorResponse
from app.services.actor import ActorService

router = APIRouter(prefix="/actors", tags=["actors"])


@router.post("/", status_code=201, response_model=ActorResponse)
def create_actor(actor_create: ActorCreate, db: Session = Depends(get_db)):
    return ActorService.create_actor(db, actor_create)


@router.get("/", response_model=List[ActorResponse])
def get_actors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return ActorService.get_actors(db, skip, limit)
