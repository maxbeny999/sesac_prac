from sqlalchemy.orm import Session
from app.models.review import Review
from app.schemas.review import ReviewCreate

class ReviewRepository:

    @staticmethod
    def create_review(db: Session, review_create: ReviewCreate):
        new_review = Review(
            content=review_create.content,
            rating=review_create.rating,
            movie_id=review_create.movie_id
        )
        db.add(new_review)
        db.commit()
        db.refresh(new_review)
        return new_review
    
    @staticmethod
    def get_review_by_movie_id(db: Session, movie_id: int, skip: int = 0, limit: int =10):
        return db.query(Review).filter(Review.movie_id == movie_id).offset(skip).limit(limit).all()
    