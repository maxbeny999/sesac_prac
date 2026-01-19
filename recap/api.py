import requests
from pprint import pprint

def get_movie_by_path(path):

    URL = f"https://api.themoviedb.org/3/{path}"
    API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYWI4Yzk4OTNlNzI1YjJlMTY3MTg3Y2VmNjZiYWUzZCIsIm5iZiI6MTYyNzYwODIyMC4xMzUsInN1YiI6IjYxMDM1NDljNGU1MmVkMDA3NTg3ZDhjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7oh38inWROms2MMFyhEFbbTs8qt3a1tOu_9m-56aQn8"

    params = {
        'language' : 'ko-kr',
    }

    headers = {
        "Authorization" : f"Bearer {API_KEY}"
    }
    try:
        response = requests.get(URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data
        
    except Exception as e:
        print(e)


