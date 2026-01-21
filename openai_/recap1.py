import requests
from pprint import pprint
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
URL = "https://api.openai.com/v1/chat/completions"
model = "gpt-4o-mini"

client = OpenAI(api_key=OPENAI_API_KEY)

history = [
    {"role": "system", "content": "당신은 사용자와의 대화내용을 기억하는 비서입니다."}
]

def chat_with_memory(user_input):
    # 1. 사용자 질문을 기록에 추가
    history.append({"role": "user", "content": user_input})
    
    # 2. 전체 기록을 API에 전송
    response = client.chat.completions.create(
        model=model,
        messages=history,
        stream=True
    )
    
    # 3. 모델의 답변을 기록에 추가 (이것이 맥락 유지의 핵심)
    
    full_response = ""

    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True) # flush 옵션을 통해 출력 버퍼를 즉시 비워 스트리밍 답변이 지연 없이 실시간으로 표시되도록 한다.
            full_response += content

    history.append({"role": "assistant", "content": full_response})
    
    return full_response

if __name__ == "__main__":
    while True:
        user_text = input("User: ")
        if user_text.lower() in ["quit", "exit"]:
            break
        print("AI: ", end="")
        chat_with_memory(user_text)
        print()