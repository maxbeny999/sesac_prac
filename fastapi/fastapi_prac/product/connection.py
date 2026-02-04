# connection.py
from sqlmodel import SQLModel, create_engine

# DB 이름 확인!
DATABASE_URL = "postgresql+psycopg://postgres:1234@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
