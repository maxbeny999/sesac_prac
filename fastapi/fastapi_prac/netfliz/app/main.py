from fastapi import FastAPI
from app.database import engine, Base
from app.routers import movie
from app.models import movie as movie_model  # DB 테이블 설계도
from app.routers import movie as movie_router_file  # API 라우터
from app.models import review as review_model
from app.routers import review as review_router_file
from app.models import director as director_model
from app.routers import director as director_router_file

# Base가 무비모델을 읽어서 db에 테이블을 설치
Base.metadata.create_all(bind=engine)

# FastAPI 앱 생성 (가게 오픈)
app = FastAPI()

# 라우터 등록
# movie_router_file 안에 있는 'router' 변수를 가져옵니다.
app.include_router(movie_router_file.router)
app.include_router(review_router_file.router)
app.include_router(director_router_file.router)


# 데코레이터(@): 요청이 들어오면 이 함수가 처리한다고 '인터폰' 연결
@app.get("/")
def read_root():

    return {"message": "Netfliz"}
