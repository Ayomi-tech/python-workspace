from column_to_int import convert_to_int
# from duplicate import deduplicatio
from import_data import read_file
from to_lowercase_dropna import to_lowercase_dropna


def main():

    main_data = read_file()

    new_data = to_lowercase_dropna(main_data)

    duplicate_value = deduplicatio(new_data, 'Customer ID')
    
    mismatched_value = convert_to_int(main_data)

    print(mismatched_value)
