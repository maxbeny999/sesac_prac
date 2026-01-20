import requests
import pprint

URL = "https://api.upbit.com/v1/candles/seconds"

response = requests.get(URL, params={'market' : 'KRW-BTC'})

pprint(response.json())