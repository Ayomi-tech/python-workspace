import pandas as pd
import numpy as np

def import_file():
    data = pd.read_csv("data_quality.csv")

    return data
