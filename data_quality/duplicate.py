import pandas as pd
import numpy as np

from to_lowercase_dropna import import_file

main_data = import_file()

# def deduplication(data, column):

#     if data.duplicated(column).any() == True:
#         raise ValueError(f"There is a duplicate value in the 'customer_id' field.")

    # return data



duplicate_values = []

def deduplicatio(data, column):
    
    duplicate = data[data.duplicated(column)]
    
    if len(duplicate) >= 1:
        duplicate_values.append(duplicate)
        raise ValueError(f"There is a duplicate value in the 'customer_id' field")
        
    return duplicate

print(deduplicatio(main_data, 'Customer ID'))