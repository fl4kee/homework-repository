import string

import pytest

from homework2.task5 import custom_range


@pytest.mark.parametrize(
    "iterable, end, expected",
    [
        (string.ascii_lowercase, 'g', ['a', 'b', 'c', 'd', 'e', 'f']),
    ]
)
def test_custom_range_with_two_args(iterable, end, expected):
    assert custom_range(iterable, end) == expected


@pytest.mark.parametrize(
    "iterable, start, end, expected",
    [
        (string.ascii_lowercase, 'g', 'o', ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']),
    ]
)
def test_custom_range_with_three_args(iterable, start, end, expected):
    assert custom_range(iterable, start, end) == expected


@pytest.mark.parametrize(
    "iterable, start, end, step, expected",
    [
        (string.ascii_lowercase, 'p', 'g', -2, ['p', 'n', 'l', 'j', 'h']),
    ]
)
def test_custom_range_with_four_args(iterable, start, end, step, expected):
    assert custom_range(iterable, start, end, step) == expected
