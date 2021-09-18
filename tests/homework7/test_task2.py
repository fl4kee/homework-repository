import pytest

from homework7.task2 import backspace_compare


@pytest.mark.parametrize('string1, string2, expected', [('ab#c', 'ad#c', True),
                                                        ('a##c', '#a#c', True),
                                                        ('a#c', 'b', False)])
def test_backspace_compare(string1, string2, expected):
    assert backspace_compare(string1, string2) == expected
