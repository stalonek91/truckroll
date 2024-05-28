import pytest
import pandas as pd
from main import print_list, print_dict

@pytest.fixture
def get_list_data():
    list_test_data = [{'Date': '2024-04-23'}, {'MRBTSID': '  178319', 'Name': '  LPX3479BA', 'Market': '  PHOENIX'}]
    return list_test_data

@pytest.fixture
def get_dict_data():
    dict_test_data = {'MRBTSID': '  178319', 'Name': '  LPX3479BA', 'Market': '  PHOENIX'}
    return dict_test_data


def test_printing_list(capsys, get_list_data):
    
    expected_output = "Element: {'Date': '2024-04-23'}\nElement: {'MRBTSID': '  178319', 'Name': '  LPX3479BA', 'Market': '  PHOENIX'}\n"

    print_list(get_list_data)

    output = capsys.readouterr()
    assert output.out == expected_output



def test_printing__non_empty_dict(capsys, get_dict_data):
    expected_dict_output = "Key is: MRBTSID with value:   178319\nKey is: Name with value:   LPX3479BA\nKey is: Market with value:   PHOENIX\n"

    print_dict(get_dict_data)

    dict_output = capsys.readouterr()
    assert dict_output.out == expected_dict_output

def test_printing_empty_dict():
    empty_dict = {}

    with pytest.raises(ValueError):
        print_dict(empty_dict)