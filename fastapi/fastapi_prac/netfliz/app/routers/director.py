from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.director import DirectorCreate, DirectorResponse
from app.services.director import DirectorService

router = APIRouter(prefix="/directors", tags=["directors"])


@router.post("/", status_code=201, response_model=DirectorResponse)
def create_director(director_create: DirectorCreate, db: Session = Depends(get_db)):
    return DirectorService.create_director(db, director_create)


@router.get("/", response_model=List[DirectorResponse])
def get_directors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return DirectorService.get_directors(db, skip, limit)
