import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# 1. .env 파일 로드 (환경변수 읽어오기)
load_dotenv()

# 2. 환경변수에서 DB 주소 가져오기
DATABASE_URL = os.getenv("DATABASE_URL")

# (혹시나 DATABASE_URL을 못 읽어왔을 때를 대비한 안전장치)
if not DATABASE_URL:
    raise ValueError(
        "❌ .env 파일에서 'DATABASE_URL'을 찾을 수 없습니다! 설정을 확인해주세요."
    )

# 3. 엔진 생성
engine = create_engine(DATABASE_URL)

# 4. 세션 생성기
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. 모델들의 부모 클래스
Base = declarative_base()


# 의존성 주입(Dependency Injection)을 위한 함수
# (나중에 라우터에서 db 세션을 빌려 쓸 때 사용합니다)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
