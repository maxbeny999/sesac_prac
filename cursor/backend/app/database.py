import os
import sys
from urllib.parse import urlparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import get_settings

# Windows: libpq가 사용자 경로(한글 등)를 읽다 UTF-8 디코딩 오류 나는 경우 방지
if sys.platform == "win32":
    os.environ.setdefault("PGPASSFILE", "")
    os.environ.setdefault("PGSERVICEFILE", "")

settings = get_settings()

# DSN 문자열 대신 개별 인자로 연결 (Windows 한글 경로 등에서 position 63 디코딩 오류 회피)
_parsed = urlparse(settings.database_url)
_dbname = (_parsed.path or "/").lstrip("/") or "tododb"
_connect_args = {
    "host": _parsed.hostname or "localhost",
    "port": _parsed.port or 5432,
    "user": _parsed.username or "postgres",
    "password": _parsed.password or "",
    "dbname": _dbname,
    "client_encoding": "UTF8",
}

engine = create_engine(
    "postgresql://",
    pool_pre_ping=True,
    connect_args=_connect_args,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
