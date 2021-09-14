import pytest

from homework4.task3 import my_precious_logger

test_data = [({'string': 'error: error occured'}, {'stderr': 'error: error occured',
                                                   'stdout': ''}),
             ({'string': 'No error'}, {'stderr': '',
                                       'stdout': 'No error'})]


@pytest.mark.parametrize('test_data, expected', test_data)
def test_my_precious_logger(capsys, test_data, expected):
    my_precious_logger(test_data['string'])
    out, err = capsys.readouterr()
    assert out == expected['stdout']
    assert err == expected['stderr']
