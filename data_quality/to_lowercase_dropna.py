import pandas as pd
from import_data import import_file

main_data = import_file()


def to_lowercase_dropna(data):
    
    data.columns = [col.lower().replace(" ","_") for col in data.columns]

    data = data.dropna() #inplace=True
    
    return data

print(to_lowercase_dropna(main_data))
