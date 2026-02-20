from sqlalchemy.orm import Session
from app.repositories.actor import ActorRepository
from app.schemas.actor import ActorCreate

class ActorService:
    @staticmethod
    def create_actor(db: Session, actor_create: ActorCreate):
        return ActorRepository.create_actor(db, actor_create)
    
    @staticmethod
    def get_actors(db: Session, skip: int, limit: int):
        return ActorRepository.get_actors(db, skip, limit)