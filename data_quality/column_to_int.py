import pandas as pd

from to_lowercase_dropna import import_file

main_data = import_file()


def convert_to_int(data, column_name):

    '''
    Convert column to int and return the defined error
    message if there's a mismatched data
    '''

    try:
        data[column_name] = pd.to_numeric(data[column_name])
        print(f"The field '{column_name}' is converted successfully to: {data[column_name].dtypes}")

    except ValueError:
        raise ValueError(f"Mismatched data type: '{column_name}' Column contains values that cannot be converted to integer.")

    return data

print(convert_to_int(main_data, 'PricE'))
