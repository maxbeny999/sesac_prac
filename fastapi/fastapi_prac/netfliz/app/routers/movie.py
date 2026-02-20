from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.movie import MovieCreate, MovieResponse
from app.services.movie import MovieService  # 서비스만 import


router = APIRouter(prefix="/movies", tags=["movies"])


@router.post("/", status_code=201, response_model=MovieResponse)
def create_movie(movie_create: MovieCreate, db: Session = Depends(get_db)):
    return MovieService.create_movie(db, movie_create)


@router.get("/", response_model=List[MovieResponse])
def get_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return MovieService.get_movies(db, skip, limit)


@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    return MovieService.get_movie(db, movie_id)


@router.put("/{movie_id}", response_model=MovieResponse)
def update_movie(
    movie_id: int, movie_update: MovieCreate, db: Session = Depends(get_db)
):
    return MovieService.update_movie(db, movie_id, movie_update)


@router.delete("/{movie_id}", status_code=204)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    MovieService.delete_movie(db, movie_id)
    return None


@router.post("/{movie_id}/actors/{actor_id}", response_model=MovieResponse)
def cast_actor_to_movie(movie_id: int, actor_id: int, db: Session = Depends(get_db)):
    return MovieService.cast_actor(db, movie_id, actor_id)
