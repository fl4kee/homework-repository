import pytest

from homework3.task4 import is_armstrong


@pytest.mark.parametrize(
    "test_input,expected",
    [(9, True), (10, False), (1, True), (153, True)],
)
def test_is_armstrong(test_input, expected):
    assert is_armstrong(test_input) == expected
