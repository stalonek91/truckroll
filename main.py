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

def print_list(list):

    for element in list_col_names:
        print(f' Element: {element}')


def print_dict(data):
    logging.debug('PRINTING THE DICTIONARY IN print_dict function')
    try:
        if isinstance(data, pd.Series):
            if data.empty:
                raise ValueError("Dict cannot be printed, it's and empty Series")
        elif isinstance(data, dict):
            if not data:
                raise ValueError(" DICT cannot be printed, it's empty row.")
        for key, value in data.items():
            print(f"Key is: {key} with value: {value}")
    except ValueError as e:
        print(f'An error occured in PRINT_DICT function: {e}')




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
def get_columns_content(df_row) -> list:
    list_of_dicts = []

    logging.info('get_column_content function started')
    for column, value in df_row.items():
        logging.info('Calling dict_creating function withing GET_COLUMNS_CONTENT func')
        list_of_dicts.append(dict_creation_from_value(value))

    return list_of_dicts



def remove_non_alpha(user_string):
    # logging.info('remove_non_alpha function started')
    clean_string = re.sub('[^0-9a-zA-Z]+', '', user_string)
    return clean_string

def dict_creation_from_value(value_from_column):
    logging.info('dict_creation_from_value function started')
    logging.debug(f'This is content that is being processed: {value_from_column}')
    split_values_to_dict = {}

    try:
        if value_from_column is None:
            raise ValueError ("Row is empty!")
        
        if not isinstance(value_from_column, str):
            logging.warning(f'Skipping non-string value: {value_from_column}')
            return value_from_column
        
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
    
    except ValueError as e:
        print(f'Error: {e}')
        

df = pd.read_excel('truckroll.xlsx')
first_row_df = df.loc[0]
list_of_values_dict = get_columns_content(first_row_df)

# Iterate over the list and print each dictionary
for i, item in enumerate(list_of_values_dict):
    print(f"Dictionary {i + 1}:")
    if isinstance(item, dict):
        for key, value in item.items():
            print(f"  Key: {key}, Value: {value}")
    else:
        print(f"  Value: {item}")

# value = get_columns_content(first_row_df)

# print(f' type of value is: {type(value)}')



# first_row_df_dict = dict_creation_from_value(value)
# print_dict(first_row_df_dict)
# list_col_names = get_column_names_to_list(df)

# print_list(list_col_names)
# print_dict(first_row_df)

#TODO: i want to write a function that will take 1st row as an argument, iterate over all columns, and try to use 
# get_column_content on each entry. 
# current flow: first_row_df = df.loc[0]-> pandas_series, value = get_column_content(first_row_df) ->string, first_row_df_dict = dict_creation_from_value(value) ->dict
#

