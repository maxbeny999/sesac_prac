# mysite4/main.py

from fastapi import FastAPI
from database import engine, Base
from mysite4.models.post import Post

# [추가 1] 라우터 가져오기
from mysite4.routes.post_router import router as post_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

# [추가 2] 라우터 등록하기
app.include_router(post_router)
