from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.director import DirectorRepository
from app.schemas.director import DirectorCreate


class DirectorService:
    @staticmethod
    def create_director(db: Session, director_create: DirectorCreate):
        return DirectorRepository.create_director(db, director_create)

    @staticmethod
    def get_directors(db: Session, skip: int, limit: int):
        return DirectorRepository.get_directors(db, skip, limit)
