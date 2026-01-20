import requests
import aiohttp
import asyncio
import os
from pprint import pprint
from dotenv import load_dotenv

# .env 파일에서 환경변수(API KEY)를 불러옵니다.
load_dotenv()

# ==========================================
# [설정] API URL 및 인증 키 준비
# ==========================================
# 기본 URL (현재 상영작)
BASE_URL = "https://api.themoviedb.org/3/movie/now_playing"
# .env 파일에 저장된 API 키를 가져옵니다. (보안)
API_KEY = os.getenv('TMDB_API_KEY')

# 공통 헤더 (신분증 역할)
HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}

# ==========================================
# [비동기 함수] 상세 정보 가져오기 (Part 2)
# ==========================================

async def fetch_url(session, url):
    """
    세션과 URL을 받아 비동기로 요청을 보내는 일꾼 함수입니다.
    """
    params = {'language': 'ko-kr'}
    
    # session.get: requests.get과 같지만 비동기로 작동합니다.
    # async with: 통신이 끝나면 연결을 안전하게 닫아줍니다.
    async with session.get(url, params=params, headers=HEADERS) as response:
        # await response.json(): 데이터가 다 들어올 때까지 기다렸다가 JSON으로 변환합니다.
        return await response.json()

async def request_all(urls):
    """
    여러 URL을 받아 동시에(병렬로) 요청을 보내는 관리자 함수입니다.
    """
    # aiohttp.ClientSession: 브라우저 창을 하나 띄운다고 생각하면 됩니다.
    async with aiohttp.ClientSession() as session:
        # tasks: 아직 실행되지 않은 '할 일 목록'을 만듭니다.
        # 리스트 컴프리헨션을 사용해 url 개수만큼 fetch_url 함수를 준비시킵니다.
        tasks = [fetch_url(session, url) for url in urls]
        
        # asyncio.gather: 준비된 모든 작업(*tasks)을 한 번에 실행합니다.
        # 모든 응답이 올 때까지 기다립니다(await).
        responses = await asyncio.gather(*tasks)
        
        print(f"✅ 비동기 요청 완료: 총 {len(responses)}개의 상세 정보를 가져왔습니다.")
        return responses

# ==========================================
# [메인 로직] 동기 -> 비동기 연결 (Part 1 + Part 2)
# ==========================================

def main():
    # --- [Step 1] 동기 방식(requests)으로 영화 목록 가져오기 ---
    print("1. 현재 상영작 목록 조회 중 (동기 방식)...")
    
    params = {
        'language': 'ko-kr',
        'page': 1  # 1페이지만 가져옵니다 (20개)
    }

    try:
        # requests를 사용해 동기적으로 요청합니다. (순차 실행)
        response = requests.get(BASE_URL, headers=HEADERS, params=params)
        
        # 상태 코드가 200(성공)이 아니면 에러를 발생시킵니다.
        response.raise_for_status()
        
        data = response.json()
        movies = data['results'] # 영화 20개의 요약 정보 리스트
        
    except Exception as e:
        print(f"목록 조회 중 에러 발생: {e}")
        return # 에러 나면 프로그램 종료

    # --- [Step 2] 영화 ID 추출하기 ---
    # 리스트 컴프리헨션: movies 리스트를 돌면서 'id' 값만 뽑아냅니다.
    movie_ids = [movie['id'] for movie in movies]
    print(f"-> 추출된 영화 ID 개수: {len(movie_ids)}개")

    # --- [Step 3] 상세 정보 URL 만들기 ---
    # ID를 이용해 상세 정보를 조회할 URL 리스트를 만듭니다.
    # 예: https://api.themoviedb.org/3/movie/12345
    url_list = [
        f"https://api.themoviedb.org/3/movie/{movie_id}"
        for movie_id in movie_ids
    ]

    # --- [Step 4] 비동기 방식(aiohttp)으로 상세 정보 긁어오기 ---
    print("2. 상세 정보 동시 요청 시작 (비동기 방식)...")
    
    # asyncio.run(): 비동기 함수(request_all)를 실행하는 스위치입니다.
    # 동기 함수인 main() 안에서 비동기 세계로 진입합니다.
    detailed_movies = asyncio.run(request_all(url_list))

    # --- [Step 5] 원하는 정보만 뽑아서 출력하기 ---
    print("3. 결과 출력")
    
    final_result = [
        {
            'title': movie['title'],                # 제목
            'vote_average': movie['vote_average'],  # 평점
            'revenue': movie.get('revenue', 0)      # 수익 (없으면 0)
        }
        for movie in detailed_movies
    ]

    pprint(final_result)

# ==========================================
# [실행 진입점]
# ==========================================
if __name__ == "__main__":
    # 이 파일이 직접 실행될 때만 main() 함수를 호출합니다.
    main()
