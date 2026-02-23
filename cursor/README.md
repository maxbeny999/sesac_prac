# Todo 사이트

FastAPI + PostgreSQL + React(Vite) 기반 Todo CRUD 사이트입니다.

## 구조

- **backend/** — FastAPI, SQLAlchemy ORM, Pydantic, 3계층(라우터·서비스·레포지토리)
- **frontend/** — React + Vite, REST API 연동

## 사전 요구사항

- Python 3.10+
- Node.js 18+
- PostgreSQL (로컬 또는 Docker)

## 백엔드 실행

```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

PostgreSQL에 `tododb` 데이터베이스를 생성한 뒤:

```bash
cp .env.example .env
# .env에서 DATABASE_URL 수정
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API 문서: http://localhost:8000/docs

## 프론트엔드 실행

```bash
cd frontend
npm install
cp .env.example .env
# .env에 VITE_API_URL=http://localhost:8000 (기본값)
npm run dev
```

브라우저: http://localhost:5173

## API 엔드포인트

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | /todos | 목록 (쿼리: completed=true/false) |
| GET | /todos/{id} | 단건 조회 |
| POST | /todos | 생성 |
| PATCH | /todos/{id} | 수정 |
| DELETE | /todos/{id} | 삭제 |

## 환경 변수

- **backend/.env**: `DATABASE_URL=postgresql://user:pass@localhost:5432/tododb`
- **frontend/.env**: `VITE_API_URL=http://localhost:8000`

## Windows에서 `UnicodeDecodeError` (position 63) 발생 시

1. **백엔드 실행 시 UTF-8 모드 사용**  
   ```bash
   set PYTHONUTF8=1
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
2. **DATABASE_URL**은 영문·숫자만 사용 (비밀번호에 한글/특수문자 사용 자제).
3. PostgreSQL 서버 인코딩 확인: DB에서 `SHOW server_encoding;` → `UTF8` 권장.
