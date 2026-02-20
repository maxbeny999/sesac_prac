from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.movie import MovieRepository
from app.schemas.movie import MovieCreate
from app.repositories.actor import ActorRepository


class MovieService:
    @staticmethod
    def create_movie(db: Session, movie_create: MovieCreate):
        # 나중에 여기에 "중복 제목 방지 로직" 등이 들어갑니다.
        return MovieRepository.create_movie(db, movie_create)

    @staticmethod
    def get_movies(db: Session, skip: int, limit: int):
        return MovieRepository.get_movies(db, skip, limit)

    @staticmethod
    def get_movie(db: Session, movie_id: int):
        movie = MovieRepository.get_movie_by_id(db, movie_id)
        if movie is None:
            raise HTTPException(status_code=404, detail="영화를 찾을 수 없습니다.")
        return movie

    @staticmethod
    def update_movie(db: Session, movie_id: int, movie_update: MovieCreate):
        # 1. 있는지 확인 (Service가 Repo를 호출)
        movie = MovieRepository.get_movie_by_id(db, movie_id)

        # 2. 없으면 에러 (Service의 역할)
        if movie is None:
            raise HTTPException(
                status_code=404, detail="수정할 영화를 찾을 수 없습니다."
            )

        # 3. 있으면 업데이트 진행
        return MovieRepository.update_movie(db, movie, movie_update)

    @staticmethod
    def delete_movie(db: Session, movie_id: int):
        movie = MovieRepository.get_movie_by_id(db, movie_id)
        if movie is None:
            raise HTTPException(
                status_code=404, detail="삭제할 영화를 찾을 수 없습니다."
            )

        MovieRepository.delete_movie(db, movie)

    @staticmethod
    def cast_actor(db: Session, movie_id: int, actor_id: int):
        # 1. 영화와 배우가 실제로 존재하는지 확인
        movie = MovieRepository.get_movie_by_id(db, movie_id)
        actor = ActorRepository.get_actor_by_id(db, actor_id)

        if not movie:
            raise HTTPException(status_code=404, detail="영화를 찾을 수 없습니다.")
        if not actor:
            raise HTTPException(status_code=404, detail="배우를 찾을 수 없습니다.")

        # 2. 존재하면 연결 진행
        return MovieRepository.add_actor_to_movie(db, movie, actor)
