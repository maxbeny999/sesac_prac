from fastapi import FastAPI
from database import engine, Base
from routers import user_router, reservation_router, review_router
from models import User, StudyRoom, Reservation, Review

# DB 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router.router)
app.include_router(reservation_router.router)
app.include_router(review_router.router)


@app.get("/")
def read_root():
    return {"message": "Hello, StudyRoom!"}
