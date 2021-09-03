import pytest

from homework2.task2 import major_and_minor_elem


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)), ([3, 2, 3], (3, 2))
    ]
)
def test_major_and_minor_elem(test_input, expected):
    assert major_and_minor_elem(test_input) == expected
