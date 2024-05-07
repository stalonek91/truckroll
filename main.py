import pandas as pd
import re

df = pd.read_excel('truckroll.xlsx')
# print(df.columns)

x = df.loc[0]


def get_number_of_rows(df):
    number_of_rows = len(df)
    print(f'Number of rows is: {number_of_rows}')
    return number_of_rows
    

def get_ticket_id(df_row):
    for column, value in df_row.items():
        if column == 'Details':
            # print(f'Column: {column} value: {value}')
            entry = value
            return entry


value = get_ticket_id(x)

def remove_non_alpha(user_string):

    clean_string = re.sub('[^0-9a-zA-Z]+', '', user_string)
    return clean_string



def dict_creation_from_value(value_from_column):
    split_values_to_dict = {}
    lines = value_from_column.split('\n')

    for line in lines:
        parts = line.split(':', 1)

        if len(parts) == 2:
            key = parts[0].split()
            value = parts[1]
            key = str(key[1:]) #Removing special 1st character

            key = remove_non_alpha(key)



            if key == 'Salesforce':
                try:
                    value = int(value)
                except ValueError:
                    pass

            split_values_to_dict[key] = value

    return split_values_to_dict
        



x = dict_creation_from_value(value)
for key, value in x.items():
    print(f"Key is: {key} with value: {value}")


