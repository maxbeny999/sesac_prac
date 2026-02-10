from fastapi import APIRouter

# [주의] 이 부분은 아까 만든 스키마 파일명에 맞게 고쳐야 합니다.
from app.schemas.movie import MovieCreate

# 1. 라우터 설정 (영화 전용)
# prefix: 이 라우터의 URL 앞에 무조건 /movies가 붙음
# tags: 스웨거 문서에 'Movies'라는 이름으로 분류됨
router = APIRouter(prefix="/movies", tags=["movies"])


# 2. 영화 등록 API
@router.post("/", status_code=201)
def create_movie(movie: MovieCreate):
    """
    영화를 등록하는 API입니다.
    """
    return {"message": "영화 등록 성공 (Netfliz)", "data": movie}
