from import_data import read_file
import pandas as pd


def to_lowercase_dropna(data: pd.DataFrame) -> pd.DataFrame:

    data.columns = [col.lower().replace(" ", "_") for col in data.columns]
    data = data.dropna()

    return data

print(to_lowercase_dropna(read_file()))
