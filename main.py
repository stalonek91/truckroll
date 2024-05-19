import pandas as pd
import re
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='\n%(levelname)s: %(message)s\n',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

def get_column_names_to_list(df) -> list:
    logging.info('get_column_names_to_list function started')
    output_list = []

    column_names = list(df.columns)
    for element in column_names:
        no_new_line_element = element.replace('\n', ' ')
        output_list.append(no_new_line_element)

    return output_list


def get_number_of_rows(df):
    number_of_rows = len(df)
    print(f'Number of rows is: {number_of_rows}')
    return number_of_rows
    
#TODO: column needs to be specified by user
def get_column_content(df_row):
    logging.info('get_column_content function started')
    for column, value in df_row.items():
        if column == 'Nokia Ticket':
            # print(f'Column: {column} value: {value}')
            entry = value
            return entry


def remove_non_alpha(user_string):
    # logging.info('remove_non_alpha function started')
    clean_string = re.sub('[^0-9a-zA-Z]+', '', user_string)
    return clean_string



def dict_creation_from_value(value_from_column):
    logging.info('dict_creation_from_value function started')
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
        

df = pd.read_excel('truckroll.xlsx')
first_row_df = df.loc[0]
value = get_column_content(first_row_df)


first_row_df_dict = dict_creation_from_value(value)
for key, value in first_row_df_dict.items():
    print(f"Key is: {key} with value: {value}")



list_col_names = get_column_names_to_list(df)

# for element in list_col_names:
#     print(f' Element: {element}')