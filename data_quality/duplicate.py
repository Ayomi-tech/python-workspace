from import_data import read_file
from to_lowercase_dropna import to_lowercase_dropna
import pandas as pd


# def deduplication(data, column):

#     if data.duplicated(column).any() == True:
#         raise ValueError(f"There is a duplicate value in the 'customer_id' field.")

    # return data

duplicate_values = []


def deduplicatio(data, column)-> pd.DataFrame:

    duplicate = data[data.duplicated(column)]

    if len(duplicate) >= 1:
        duplicate_values.append(duplicate)
        raise ValueError(f"There is a duplicate value in the {column} field")

    return duplicate

main_data = to_lowercase_dropna(read_file())

print(deduplicatio(main_data, 'customer_id'))
