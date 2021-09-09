import pytest

from homework4.task3 import my_precious_logger

test_data = [({'string': 'error: error occured'}, {'message': 'error: error occured'}),
             ({'string': 'No error'}, {'message': ''})]


@pytest.mark.parametrize('test_data, expected', test_data)
def test_my_precious_logger(capsys, test_data, expected):
    my_precious_logger(test_data['string'])
    assert capsys.readouterr().err == expected['message']
