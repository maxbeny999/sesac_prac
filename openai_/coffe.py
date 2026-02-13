import os
import sys
from enum import Enum
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field
from collections import defaultdict

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# [네트워크 이슈 방지] 프록시 설정 초기화
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""

if not api_key:
    print(" 오류: .env 파일에 OPENAI_API_KEY가 없습니다.")
    sys.exit(1)

client = OpenAI(api_key=api_key)
MODEL_NAME = "gpt-4o-2024-08-06"


#  Pydantic 모델 정의
class Temperature(str, Enum):
    ICE = "ICE"
    HOT = "HOT"


class Size(str, Enum):
    TALL = "Tall"
    GRANDE = "Grande"
    VENTI = "Venti"


class OrderItem(BaseModel):
    menu: str = Field(description="수식어와 인삿말을 제거한 메뉴의 표준 이름")
    temperature: Temperature = Field(description="음료의 온도 (기본: ICE)")
    size: Size = Field(description="컵 사이즈 (기본: Tall, R/Regular는 Tall로 취급)")
    quantity: int = Field(description="주문 수량")


class OrderResponse(BaseModel):
    orders: List[OrderItem]


#  비즈니스 로직
def summarize_orders(order_response: OrderResponse) -> str:
    order_summary = defaultdict(int)

    for item in order_response.orders:
        key = (item.menu, item.temperature.value, item.size.value)
        order_summary[key] += item.quantity

    if not order_summary:
        return ">>  주문 내용을 찾지 못했습니다."

    result_text = "\n **[최종 주문 집계]** \n" + "-" * 30 + "\n"
    total_cups = 0

    # 가나다 순 정렬
    for (menu, temp, size), count in sorted(order_summary.items()):
        result_text += f"- {menu} ({temp}/{size}) : {count}잔\n"
        total_cups += count

    result_text += "-" * 30 + f"\n Total: {total_cups}잔\n"
    return result_text


#  AI 분석 실행
def analyze_chat_log(chat_text: str) -> str:
    print("\n AI가 슬랙 대화 내용을 분석 중입니다...", end="", flush=True)

    system_prompt = """
    너는 카페 주문 집계 매니저다. 
    제공된 슬랙 채팅 로그에서 잡담(인삿말, 이름, 시간)을 제외하고 '주문 메뉴'만 정확히 추출하라.

    [처리 규칙]
    1. 메뉴명 정제: '자몽에이드', '아보카도바나나', '딥앤초코 파르페' 등 메뉴 이름만 남길 것.
    2. 사이즈 매핑: 'R', 'Regular', '레귤러' -> Tall
    3. 기본값: 온도는 ICE, 사이즈는 Tall (명시된 경우만 변경)
    4. 예외 처리: '{ 아이스 : 로얄밀크티 }' 같은 이상한 포맷도 내용을 파악해 추출할 것.
    """

    try:
        completion = client.beta.chat.completions.parse(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": chat_text},
            ],
            response_format=OrderResponse,
        )

        # 분석 완료 후 줄바꿈
        print(" 완료!\n")

        parsed_data = completion.choices[0].message.parsed
        return (
            summarize_orders(parsed_data) if parsed_data else "Error: 데이터 변환 실패"
        )

    except Exception as e:
        return f"\n 에러 발생: {str(e)}"


# --- 메인 실행부 (터미널 입력 모드) ---
if __name__ == "__main__":
    print("\n [AI 주문 집계기] 실행됨")
    print(" 대화 내용을 입력하세요")
    print(" 입력을 마치려면 줄바꿈 후 '끝' 이라고 입력하고 엔터를 치세요.\n")
    print("-" * 50)

    lines = []
    while True:
        try:
            line = input()
            # 사용자가 '끝' 이라고 입력하면 입력을 종료하고 분석 시작
            if line.strip() == "끝":
                break
            lines.append(line)
        except EOFError:
            break

    full_text = "\n".join(lines)

    if full_text.strip():
        result = analyze_chat_log(full_text)
        print(result)
    else:
        print(" 입력된 내용이 없습니다. 프로그램을 종료합니다.")
