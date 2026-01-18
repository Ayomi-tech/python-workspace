import requests
import pandas as pd

url = "https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/champion.json"

def data_extraction():

    response = requests.get(url)

    if response.status_code != 200:
        response.raise_for_status

    champion = response.json()
    champions = champion['data']

    return champions