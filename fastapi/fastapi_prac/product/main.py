from fastapi import FastAPI
from contextlib import asynccontextmanager
from connection import create_db_and_tables

# Models를 임포트해야 테이블이 생성됩니다 (init 파일 활용)
from products import models
from products.router import category_router, product_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(category_router.router)
app.include_router(product_router.router)


@app.get("/")
def root():
    return {"message": "Product API System"}
