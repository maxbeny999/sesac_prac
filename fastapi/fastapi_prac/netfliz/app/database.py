import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. 환경변수 로드
# .env 파일에 숨겨둔 비밀번호들을 꺼내옵니다.
load_dotenv()

# 2. DB 접속 주소 만들기
# DB와 연결하기 위한 주소를 만듭니다. (PostgreSQL용)
SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# 3. 엔진(Engine) 생성 = [발전소]
# 실제 DB와의 '물리적인 연결 통로'를 엽니다.
# 가장 밑바닥에서 DB와 소통하는 핵심 부품입니다.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 4. 세션 공장(SessionLocal) 생성 = [콘센트]
# 엔진(발전소)에서 전기를 끌어와서, 우리가 쓸 수 있는 '콘센트(Session)'를 만들어주는 공장입니다.
# 요청이 들어올 때마다 이 공장에서 '세션(전화기)'을 하나씩 찍어냅니다.
# - autocommit=False: 자동 저장을 끕니다. (우리가 직접 commit() 명령을 내려야 저장됨 -> 실수 방지)
# - autoflush=False: 데이터 변경사항을 즉시 DB에 반영하지 않고, 필요할 때 반영합니다. (성능 최적화)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Base 클래스 = [조상님]
# 앞으로 만들 모든 모델(테이블)들의 '공통 조상'입니다.
# "class Movie(Base):" 처럼 상속받으면, 파이썬이 "아, 너는 DB 테이블이구나" 하고 알아챕니다.
Base = declarative_base()
