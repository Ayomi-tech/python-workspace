import json
import pandas as pd

def import_json():

    with open("champion.json", 'r') as file:
        champion = json.load(file)

        champions = champion['data']

        return champions

