from sqlalchemy.orm import Session
from app.models.director import Director
from app.schemas.director import DirectorCreate


class DirectorRepository:
    @staticmethod
    def create_director(db: Session, director_create: DirectorCreate):
        new_director = Director(name=director_create.name)
        db.add(new_director)
        db.commit()
        db.refresh(new_director)
        return new_director

    @staticmethod
    def get_director_by_id(db: Session, director_id: int):
        return db.query(Director).filter(Director == director_id).first()

    @staticmethod
    def get_directors(db: Session, skip: int, limit: int):
        return db.query(Director).offset(skip).limit(limit).all()
