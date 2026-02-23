import os
import sys

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# .env 로드 시 UTF-8 사용. 실패하면 Windows에서는 CP949 시도 (UnicodeDecodeError 방지)
try:
    load_dotenv(".env", encoding="utf-8")
except UnicodeDecodeError:
    if sys.platform == "win32":
        load_dotenv(".env", encoding="cp949")
    else:
        raise


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@localhost:5432/tododb"

    class Config:
        extra = "ignore"


def get_settings() -> Settings:
    return Settings()
