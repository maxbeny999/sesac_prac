from sqlalchemy.orm import Session
from app.models.actor import Actor
from app.schemas.actor import ActorCreate


class ActorRepository:
    @staticmethod
    def create_actor(db: Session, actor_create: ActorCreate):
        new_actor = Actor(name=actor_create.name)
        db.add(new_actor)
        db.commit()
        db.refresh(new_actor)
        return new_actor

    @staticmethod
    def get_actors(db: Session, skip: int, limit: int):
        return db.query(Actor).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_actor_by_id(db: Session, actor_id: int):
        return db.query(Actor).filter(Actor.id == actor_id).first()