from column_to_int import convert_to_int
from duplicate import deduplicatio
from import_data import import_file
from to_lowercase_dropna import to_lowercase_dropna


def main():

    main_data = import_file()

    new_data = to_lowercase_dropna(main_data)

    duplicate_value = deduplicatio(new_data, 'Customer ID')

    # int_value = convert_to_int(new_data)

    print(duplicate_value)
