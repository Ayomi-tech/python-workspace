import pandas as pd
from read_data import import_json

champs = import_json()
greater_than_5 = []


for pages in champs:
    champions_details = champs[pages]
    
    
    champ_data= {
        'name' :champions_details['name'],
        'title' :champions_details['title'],
        'attack' : champions_details['info']['attack'],
        'defense' :champions_details['info']['defense'],
       }
    if champ_data['attack'] > 5 | champ_data['defense'] > 5:
        greater_than_5.append(champ_data)


names = pd.json_normalize(greater_than_5)
print(f" The len of the filter data is: ",len(names))
print(names.head(5))
