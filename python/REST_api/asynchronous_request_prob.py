import requests
import os
from dotenv import load_dotenv
from pprint import pprint

# 비동기를 위한 라이브러리 (aiohttp는 pip install aiohttp 필요)
import aiohttp
import asyncio

load_dotenv()

# ==========================================
# [Step 1] 동기 방식: 영화 목록에서 ID 수집하기
# ==========================================

URL = "https://api.themoviedb.org/3/movie/now_playing"
API_KEY = os.getenv('TMDB_API_KEY')

params = {
    'language': 'ko-kr',
    'page': 1,
}

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# 1. 영화 ID를 담을 리스트 준비
movie_ids = []

try:
    print("1. 영화 ID 수집 시작 (동기 방식)...")
    
    # 1페이지부터 2페이지까지 (총 40개 예상)
    for page_num in range(1, 3):
        params['page'] = page_num
        response = requests.get(URL, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        results = data['results']
        
        # ID만 뽑아서 리스트에 추가 (리스트 컴프리헨션 활용)
        ids = [movie['id'] for movie in results]
        movie_ids.extend(ids)

    print(f"-> 수집된 ID 개수: {len(movie_ids)}개")

except Exception as e:
    print(f"ID 수집 중 에러 발생: {e}")


# ==========================================
# [Step 2] 비동기 방식: 상세 정보 동시에 가져오기
# ==========================================

# 2. 개별 상세 정보를 가져오는 일꾼 함수 (Coroutine)
async def fetch_detail(session, movie_id):
    detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    
    # aiohttp로 요청 보내기 (requests와 비슷하지만 await가 필요함)
    async with session.get(detail_url, headers=headers, params=params) as response:
        return await response.json()

# 3. 일꾼들을 관리하고 실행하는 메인 함수
async def main(ids):
    # 세션(통로) 하나를 열어서 공유합니다.
    async with aiohttp.ClientSession() as session:
        tasks = []
        
        # ID 개수만큼 일꾼에게 작업을 배정(예약)합니다.
        for m_id in ids:
            task = fetch_detail(session, m_id) # 작업 생성
            tasks.append(task)                 # 작업 목록에 추가
        
        # gather: "모든 작업 동시에 시작!" (끝날 때까지 기다림)
        print("2. 상세 정보 비동기 요청 시작 (동시 실행)...")
        results = await asyncio.gather(*tasks)
        
        return results

# ==========================================
# [Step 3] 실행 (동기 -> 비동기 연결)
# ==========================================

if __name__ == "__main__":
    # movie_ids가 잘 모였는지 확인하고 비동기 실행
    if movie_ids:
        # 여기가 핵심입니다! 
        # 동기 세상에서 만든 movie_ids를 들고 비동기 함수(main)를 실행합니다.
        final_results = asyncio.run(main(movie_ids))
        
        print("3. 모든 작업 완료!")
        
        # 결과 확인 (너무 기니까 첫 번째 영화 제목만 출력해봅니다)
        if final_results:
            print(f"첫 번째 영화 제목: {final_results[0]['title']}")
            print(f"마지막 영화 제목: {final_results[-1]['title']}")
            pprint(final_results) # 전체를 보고 싶으면 주석 해제