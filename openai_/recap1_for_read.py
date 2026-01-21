import requests
from pprint import pprint
import os
from dotenv import load_dotenv
from openai import OpenAI

# [1] 환경 설정 로드
# .env 파일에서 비밀번호(API KEY)를 꺼내와서 os 환경변수에 등록합니다.
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
URL = "https://api.openai.com/v1/chat/completions"
model = "gpt-4o-mini"

# [2] 클라이언트 생성 (통신 담당자)
# 이 객체가 열쇠(API Key)를 들고 OpenAI 서버와 대화를 주고받습니다.
client = OpenAI(api_key=OPENAI_API_KEY)


# [3] 기억 저장소 초기화 (전역 변수)
# 함수 밖에서 선언했으므로 프로그램이 꺼질 때까지 내용이 유지됩니다.
# 첫 번째 칸에 AI의 성격(페르소나)을 정의해 둡니다.
history = [
    {"role": "system", "content": "당신은 사용자와의 대화내용을 기억하는 비서입니다."}
]


# [4] 함수 정의 (설계도 등록 단계)
# 이 시점에서는 코드가 실행되는 것이 아니라, '이런 기능이 있다'고 파이썬이 기억만 하고 넘어갑니다.
# 외부에서 던져준 데이터(user_text)를 내부에서는 'user_input'이라는 이름표로 받습니다.
def chat_with_memory(user_input):
    
    # [9] 사용자 질문 기록 (함수 진입 후 첫 번째 할 일)
    # 방금 들어온 질문을 공용 노트(history)에 적어둡니다.
    history.append({"role": "user", "content": user_input})
    
    # [10] API 서버로 요청 전송
    # 질문 하나만 보내는 게 아니라, 지금까지 쌓인 'history' 전체를 보냅니다.
    # stream=True 옵션을 켜서 답변을 한 번에 받지 않고 조각조각 받겠다고 선언합니다.
    response = client.chat.completions.create(
        model=model,
        messages=history,
        stream=True
    )
    
    # [11] 빈 문자열 준비
    # 날아오는 글자 조각들을 하나로 합칠 빈 그릇입니다.
    full_response = ""

    # [12] 스트리밍 데이터 처리 (반복문)
    # 서버에서 물방울(chunk)이 뚝뚝 떨어질 때마다 받아서 처리합니다.
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            # flush=True: 버퍼에 담아두지 말고 즉시 화면에 출력 (타자기 효과)
            # end="": 줄바꿈 방지 (옆으로 이어 붙이기)
            print(content, end="", flush=True)
            
            # 화면 출력과 별개로, 기억을 위해 변수에도 차곡차곡 모아둡니다.
            full_response += content

    # [13] AI 답변 기록 (가장 중요한 부분!)
    # 완성된 문장을 공용 노트(history)에 적어둡니다.
    # 이걸 안 하면 다음 턴에서 AI가 자기가 무슨 말을 했는지 까먹습니다.
    history.append({"role": "assistant", "content": full_response})
    
    # [14] 함수 종료 및 복귀
    # 완성된 답변을 들고 호출했던 위치(Main Loop)로 돌아갑니다.
    return full_response


# [5] 프로그램 진입점 (Main Execution)
# 파이썬 파일을 직접 실행했을 때만 여기서부터 코드가 시작됩니다.
if __name__ == "__main__":
    
    # [6] 무한 루프 시작 (대화 사이클)
    while True:
        # [7] 사용자 입력 대기 (Blocking)
        # 사용자가 엔터를 칠 때까지 프로그램이 여기서 멈춰 기다립니다.
        # 입력된 값은 'user_text'라는 변수에 담깁니다.
        user_text = input("User: ")
        
        # 종료 조건 확인
        if user_text.lower() in ["quit", "exit"]:
            break
        
        # [8] AI 말하기 준비
        # "AI: "를 먼저 찍고, 커서를 그 옆에 대기시킵니다 (end="").
        print("AI: ", end="")
        
        # [8-1] 함수 호출 (점프!)
        # user_text(재료)를 들고 위쪽의 [4]번 chat_with_memory 공장으로 이동합니다.
        # 함수가 일을 다 마치고 돌아올 때까지 여기서 기다립니다.
        chat_with_memory(user_text)
        
        # [15] 줄바꿈 처리
        # 함수가 끝나고 돌아오면 커서가 문장 맨 끝에 붙어있으므로,
        # 보기 좋게 엔터(줄바꿈)를 한 번 쳐줍니다.
        print() 
        
        # [16] 다시 [6]번으로 돌아가서 입력을 기다립니다.