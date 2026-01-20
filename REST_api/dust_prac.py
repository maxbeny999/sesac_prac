import requests
import os
from pprint import pprint
from dotenv import load_dotenv
from urllib.parse import unquote

load_dotenv()
# 1. 시도별 실시간 측정 정보 조회에 대한 요청을 보내야 한다.
    # -> URL이 필요하다.
URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
API_KEY = unquote(os.getenv('DUST_API_KEY'))

params = {
    'serviceKey' : API_KEY,
    'sidoName' : '서울',
    'returnType' : 'json',
    'ver': 1.0,
    'numOfRows' : 100
}

response = requests.get(URL, params=params)

data = response.json()

dust_info = data['response']['body']['items']

# 2. 초미세먼지 농도는 어떤 key를 가지고 있냐?
    # 문서를 뒤지니, pm25Value더라.

# pprint(dust_info)
min_pm25Value = float('inf')
min_pm25Value_stationName = None

for info in dust_info:
    pm25Value = info['pm25Value']
    pm25Flag = info['pm25Flag']
    stationName = info['stationName']

    # pm25Value는 info에서 가져올 수 있는데,
    # 경우에 따라서 '-'로 표현되는 경우가 있다.
    # 이것을 처리해 주어야 한다.
    # 그냥 넘길껍니다.
    # if pm25Value == '-':
    #     continue

    if pm25Flag: # 기본값이 None이었거든요,
        # flag가 통신장애 / 장비점검 / 자료이상 등등에 따라 처리하는 로직이 들어갈겁니다.
        continue
    
    pm25Value = int(pm25Value)
    if min_pm25Value > pm25Value:
        min_pm25Value = pm25Value
        min_pm25Value_stationName = stationName
    # print(min_pm25Value)
print(min_pm25Value_stationName)
print(min_pm25Value)