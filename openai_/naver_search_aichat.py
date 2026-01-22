import os
import requests
from dotenv import load_dotenv
from pprint import pprint
from openai import OpenAI
import json

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
client = OpenAI(api_key=OPENAI_API_KEY)

model = 'gpt-4o-mini'

def naver_search_news(keyword):
    """
    naver 뉴스 검색 결과를 보여드립니다.
    """

    url = "https://openapi.naver.com/v1/search/news"
    headers = {
        "X-Naver-Client-Id" : CLIENT_ID,
        "X-Naver-Client-Secret" : CLIENT_SECRET
    }
    params = {
        "query": keyword,
        "display": 5,
        "sort": "sim"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        result_text = ""

        if not data['items']:
            return "검색 결과가 없습니다."


        for item in data['items']:
            title = item['title'].replace('<b>','').replace('</b>','').replace('&quot;','"')
            link = item['link']
            result_text += f"- 제목: {title}  링크: {link}"

        return result_text 
    else:
        return f"검색 실패. 에러 코드: {response.status_code}"
    
tools = [
    {
        "type": "function",
        "function": {  
            "name": "naver_search_news",
            "description": "최신 뉴스나 특정 주제에 대한 기사 검색이 필요할 때 사용합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "검색할 키워드",
                    }
                },
                "required": ["keyword"]
            }
        }
    }
]

def run_conversation(user_query):
    messages = [{"role": "user", "content": user_query}]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        print(f"네이버 검색을 실시합니다 {len(tool_calls)}회")

        messages.append(response_message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            if function_name == "naver_search_news":
                keyword = function_args.get("keyword")
                print(f"검색어 추출 {keyword}")
                
                function_response = naver_search_news(keyword)

                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name" : function_name,
                    "content" : function_response
                })

                second_response = client.chat.completions.create(
                    model=model,
                    messages=messages
                )
                return second_response.choices[0].message.content
            
            else:
                return response_message.content
                
if __name__ == "__main__":
    query = f"{input()}"
    pprint(f"유저: {query}")

    answer = run_conversation(query)

    pprint(f"챗봇: {answer}")