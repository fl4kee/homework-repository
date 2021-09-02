import pytest

from homework2.task3 import combinations_


@pytest.mark.parametrize(
    "arr1, arr2, expected",
    [
        ([1, 2], [3, 4], [[1, 3], [1, 4], [2, 3], [2, 4]]),
    ]
)
def test_combinations_(arr1, arr2, expected):
    assert combinations_(arr1, arr2) == expected
