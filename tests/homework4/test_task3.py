import pytest

from homework4.task3 import my_precious_logger


@pytest.mark.parametrize('test_data, expected',
                         [({'string': 'error: something went wrong'}, {'is_error': True}),
                          ({'string': 'No error'}, {'is_error': False})])
def test_my_precious_logger(capsys, test_data, expected):
    my_precious_logger(test_data['string'])
    has_error = bool(capsys.readouterr().err)
    assert has_error is expected['is_error']
