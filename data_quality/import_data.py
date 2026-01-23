import pandas as pd


def import_file():
    data = pd.read_csv("data_quality.csv")

    return data
