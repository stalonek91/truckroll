import pandas as pd
import re
import logging
import json

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

def print_list(elements):
    logging.info('Entering print_list function')
    for element in elements:
        print(f'Element: {element}')

def print_dict(data):
    logging.info('Entering print_dict function')
    try:
        if isinstance(data, pd.Series):
            if data.empty:
                raise ValueError("Dict cannot be printed, it's an empty Series")
        elif isinstance(data, dict):
            if not data:
                raise ValueError("Dict cannot be printed, it's an empty dictionary.")
        for key, value in data.items():
            print(f"Key is: {key} with value: {value}")
    except ValueError as e:
        logging.error(f'An error occurred in print_dict function: {e}')

def get_column_names_to_list(df) -> list:
    logging.info('Entering get_column_names_to_list function')
    return [element.replace('\n', ' ') for element in df.columns]

def get_number_of_rows(df):
    number_of_rows = len(df)
    logging.info(f'Number of rows: {number_of_rows}')
    return number_of_rows

def get_columns_content(df_row) -> list:
    logging.info('Entering get_columns_content function')
    return [dict_creation_from_value(value, column) for column, value in df_row.items()]

def remove_non_alpha(user_string):
    return re.sub('[^0-9a-zA-Z]+', '', user_string)

def dict_creation_from_value(value_from_column, user_key):
    logging.info('Entering dict_creation_from_value function')
    split_values_to_dict = {}

    try:
        if value_from_column is None:
            raise ValueError("Row is empty!")
        
        if not isinstance(value_from_column, str):
            logging.warning(f'Skipping non-string value: {value_from_column}')
            return {user_key: value_from_column}
        
        lines = value_from_column.split('\n')
        for line in lines:
            parts = line.split(':', 1)
            if len(parts) == 2:
                value = parts[1].strip()  # Ensure value is stripped of whitespace
                key = str(parts[0].split()[1])  # Remove first special character
                key = remove_non_alpha(key)

                if key == 'Salesforce':
                    try:
                        value = int(value)
                    except ValueError:
                        pass

                split_values_to_dict[key] = value
            else:
                split_values_to_dict[user_key] = line.strip()

        return split_values_to_dict
    
    except ValueError as e:
        logging.error(f'Error: {e}')
        return {user_key: value_from_column}

def create_json_file(final_dict, file_path='truckroll.json'):
    logging.info('Creating json file in create_json_file function')
    with open(file_path, 'w') as json_file:
        json.dump(final_dict, json_file, indent=4)

def create_final_dict_for_json(column_names, list_of_values_dict) -> dict:
    logging.info('Entering create_final_dict_for_json function')
    formatted_columns = [remove_non_alpha(column) for column in column_names]
    final_output_dict = {formatted_columns[i]: list_of_values_dict[i] for i in range(len(formatted_columns))}

    if final_output_dict:
        logging.debug('Final dict successfully created in create_final_dict_for_json function')
    else:
        logging.error('Final dict is empty! Something went wrong in create_final_dict_for_json function')
    
    return final_output_dict

# Main execution
df = pd.read_excel('truckroll.xlsx')
first_row_df = df.loc[0]
list_of_values_dict = get_columns_content(first_row_df)
print_list(list_of_values_dict)
column_names = df.columns

# Create the final dictionary and write to JSON file
create_json_file(create_final_dict_for_json(column_names, list_of_values_dict))
