from sqlalchemy.orm import Session, joinedload
from app.models.movie import Movie
from app.schemas.movie import MovieCreate


class MovieRepository:
    @staticmethod
    def create_movie(db: Session, movie_create: MovieCreate):
        new_movie = Movie(
            title=movie_create.title,
            year=movie_create.year,
            description=movie_create.description,
            director_id=movie_create.director_id,
        )
        db.add(new_movie)  # 장바구니에 담기
        db.commit()  # 결제 버튼 누르기 (실제 저장)
        db.refresh(new_movie)  # 영수증 받기 (DB가 만들어준 ID값 등을 받아옴)
        return new_movie

    @staticmethod
    def get_movies(db: Session, skip: int, limit: int):
        # [수정] .options(joinedload(Movie.reviews)) 추가
        # 뜻: "영화 가져올 때, reviews 테이블도 JOIN 해서 같이 가져와!"
        return (
            db.query(Movie)
            .options(joinedload(Movie.reviews), joinedload(Movie.director))
            .offset(skip)
            .limit(limit)
            .all()
        )

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
