import requests_mock

from homework4.task2 import count_dots_on_i


def test_count_dots_on_i():
    with requests_mock.Mocker() as m:
        m.get('http://test.com', text='Supposed to count i\'s in this text')
        assert count_dots_on_i('http://test.com') == 3
