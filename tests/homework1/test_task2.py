import pytest

from homework1.task2 import check_fibonacci


@pytest.mark.parametrize(
    "test_input,expected",
    [([1, 1, 2, 3, 5, 8, 13], True), ([1, -1, 24, 3, 12, 8, -13], False)],
)
def test_check_fibonacci(test_input, expected):
    assert check_fibonacci(test_input) == expected
