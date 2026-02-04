# # main.py
# from fastapi import FastAPI
# from todo_app.routes.todo_router import router as todo_router

# app = FastAPI()

# # 라우터 등록
# app.include_router(todo_router)


# @app.get("/")
# def read_root():
#     return {"message": "Todo List Started"}


# ----------------------------------------------------


# main.py (수정)

from fastapi import FastAPI
from contextlib import asynccontextmanager
from todo_app.connection import create_db_and_tables  # <-- 가져오기
from todo_app.routers.todo_router import router as todo_router
from fastapi.middleware.cors import CORSMiddleware


# [추가] 수명주기(Lifespan) 설정: 서버 켜질 때 딱 한 번 실행됨
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()  # 테이블 생성!
    yield


# lifespan 등록
app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST 등)
    allow_headers=["*"],  # 모든 헤더 허용
)

app.include_router(todo_router)


@app.get("/")
def read_root():
    return {"message": "Hello, Todo List with DB!"}
