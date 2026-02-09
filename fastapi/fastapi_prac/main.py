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
from database import engine, Base

# [중요] models를 임포트해야 Base가 "아, 이런 테이블을 만들어야 하는구나" 하고 인식합니다.
# (아직 파일을 안 채웠지만 곧 만들 예정이니 미리 적어둡니다)
from todo.models.todo import Todo
from todo.routers import todo_router

app = FastAPI()

# 1. 테이블 생성 (앱 실행 시 DB에 테이블이 없으면 자동 생성)
Base.metadata.create_all(bind=engine)

# 2. 라우터 등록 (이제 /todos 주소로 접속 가능해짐)
app.include_router(todo_router.router)


@app.get("/")
def health_check():
    return {"message": "Todo 서버가 정상 작동 중입니다!"}
