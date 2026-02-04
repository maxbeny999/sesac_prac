
from fastapi import FastAPI
from contextlib import asynccontextmanager
from connection import create_db_and_tables
from products.router import router as product_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(product_router)

@app.get("/")
def root():
    return {"message": "Product API System"}