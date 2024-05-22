import pytest
from main import print_list


def test_printing_list(capsys):
    test_data = [{'Date': '2024-04-23'}, {'MRBTSID': '  178319', 'Name': '  LPX3479BA', 'Market': '  PHOENIX'}]
    expected_output = "Element: {'Date': '2024-04-23'}\nElement: {'MRBTSID': '  178319', 'Name': '  LPX3479BA', 'Market': '  PHOENIX'}\n"

    print_list(test_data)

    output = capsys.readouterr()
    assert output.out == expected_output