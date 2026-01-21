import pandas as pd
import numpy as np

def deduplication(data, column):

    if data.duplicated(column).any() == True:
        raise ValueError(f"There is a duplicate value in the 'customer_id' field")
    return data
