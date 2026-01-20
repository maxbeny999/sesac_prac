import asyncio
import time

# 1. [async def] 요리법 정의
async def make_burger():
    print("🍔 버거 굽기 시작 (3초 소요)")
    await asyncio.sleep(3) # 3초 동안 딴짓 가능
    print("🍔 버거 완성!")
    return "버거"

async def fry_potato():
    print("🍟 감자 튀기기 시작 (2초 소요)")
    await asyncio.sleep(2)
    print("🍟 감자 완성!")
    return "감튀"

async def pour_coke():
    print("🥤 콜라 따르기 (1초 소요)")
    await asyncio.sleep(1)
    print("🥤 콜라 완성!")
    return "콜라"

async def main():
    print("=== 📢 주방 오픈! (이벤트 루프 시작) ===")
    start_time = time.time()

    # 2. [create_task] 설거지 담당 알바생 부르기
    # "설거지(배경음악 재생 등)"는 요리와 상관없이 뒤에서 알아서 하라고 시킴
    # await를 안 썼으므로 기다리지 않고 바로 다음 줄로 넘어감!
    background_task = asyncio.create_task(play_music())

    # 3. [gather] 세트 메뉴 동시에 만들기
    # 버거, 감자, 콜라를 동시에 주문 넣고 다 나올 때까지 기다림(await)
    print("👨‍🍳 세트 메뉴 조리 시작!")
    result = await asyncio.gather(
        make_burger(),
        fry_potato(),
        pour_coke()
    )
    
    end_time = time.time()
    print(f"=== ✅ 서빙 완료: {result} ===")
    print(f"총 걸린 시간: {end_time - start_time:.2f}초 (다 따로 했으면 6초 걸렸음!)")

# 번외: 배경 작업용 함수
async def play_music():
    print("🎵 (백그라운드) 노동요 재생 중...")
    await asyncio.sleep(5)
    print("🎵 노래 끝")

# 4. [run] 매니저가 가게 문을 엶
if __name__ == "__main__":
    asyncio.run(main())