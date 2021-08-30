import pytest

from homework1.task4 import check_sum_of_four, count_zeroes, sum_two_arrs


@pytest.mark.parametrize("arr1, arr2, arr3, arr4, expected", [
    ([1, -8, 3], [3, 5, -10], [-5, -9, 20], [-15, 6, 7], 1),
    ([1, -8, 3], [3, 5, -10], [-5, -9, 20], [-15, 8, 8], 3),
    ([], [], [], [], 0)
])
def test_check_sum_of_four(arr1, arr2, arr3, arr4, expected):
    assert check_sum_of_four(arr1, arr2, arr3, arr4) == expected


@pytest.mark.parametrize("arr1, arr2, expected", [
    ([1, 2, 3], [1, 2, 3], [2, 3, 4, 3, 4, 5, 4, 5, 6]),
    ([], [], [])
])
def test_sum_two_arrs(arr1, arr2, expected):
    assert sum_two_arrs(arr1, arr2) == expected


@pytest.mark.parametrize("arr1, arr2, expected", [
    ([1, 2, 3], [1, 2, 3], 0),
    ([], [], 0),
    ([1, 3, -4], [-2, 1, -3], 1)
])
def test_count_zeroes(arr1, arr2, expected):
    assert count_zeroes(arr1, arr2) == expected
