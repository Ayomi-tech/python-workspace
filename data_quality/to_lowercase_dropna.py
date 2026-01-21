import pandas as pd

def to_lowercase_dropna(data):
    
    data.columns = [col.lower().replace(" ","_") for col in data.columns]
    data = data.dropna() #inplace=True
    
    return data
