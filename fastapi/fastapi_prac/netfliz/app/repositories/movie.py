from sqlalchemy.orm import Session
from app.models.movie import Movie
from app.schemas.movie import MovieCreate


class MovieRepository:
    @staticmethod
    def create_movie(db: Session, movie_create: MovieCreate):
        new_movie = Movie(
            title=movie_create.title,
            year=movie_create.year,
            director=movie_create.director,
            description=movie_create.description,
        )
        db.add(new_movie)  # 장바구니에 담기
        db.commit()  # 결제 버튼 누르기 (실제 저장)
        db.refresh(new_movie)  # 영수증 받기 (DB가 만들어준 ID값 등을 받아옴)
        return new_movie

    @staticmethod
    def get_movies(db: Session):
        return db.query(Movie).all()

    @staticmethod
    def get_movie_by_id(db: Session, movie_id: int):
        return db.query(Movie).filter(Movie.id == movie_id).first()

    @staticmethod
    def update_movie(db: Session, movie: Movie, movie_update: MovieCreate):
        movie.title = movie_update.title
        movie.year = movie_update.year
        movie.director = movie_update.director
        movie.description = movie_update.description
        db.commit()
        db.refresh(movie)
        return movie

    @staticmethod
    def delete_movie(db: Session, movie: Movie):
        db.delete(movie)
        db.commit()
