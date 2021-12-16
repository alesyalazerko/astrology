import os
import requests
import json

KEY = os.environ.get('API_KEY')
HOST = os.environ.get('API_HOST')

sign =''
day = ''

def fetchAstroData(sign: str, day: str, api_key: str, api_host: str) -> dict or None:
    url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"

    querystring = {"sign": f'{str(input("enter your zodiac sign"))}', "day": f'{str(input("enter the day: yesterday, today or tomorrow"))}'}

    headers = {
        'x-rapidapi-host': "api_host",
        'x-rapidapi-key': "api_key"
    }

    response = requests.request("POST", url, headers=headers, params=querystring)
    json_r = json.loads(response.text)

    if response.status_code == 200:
        return json_r
    else:
        return None

fetch = fetchAstroData(sign, day, KEY, HOST)
with open('astro.json', 'w') as f:
    f.write(json.dumps(fetch, indent=4))
