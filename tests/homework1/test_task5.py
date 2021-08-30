import pytest

from homework1.task5 import find_maximal_subarray_sum


@pytest.mark.parametrize("test_array, subarray_len, expected", [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
    ([111, 3, -1, -3, 5, 3, 6, 7], 3, 114),
    ([111, 3, -1, -3, 5, 3, 6, 7], 5, 115),
    ([111, 3, -1, -3, 5, 3], 6, 118),
    ([111, 3, -1, -3, 5, 3], 7, 0),
    ([], 3, 0),
    ([1, 2, 3], -1, 0),
    ([], 0, 0),

])
def test_find_maximal_subarray_sum_positive(test_array, subarray_len, expected):
    assert find_maximal_subarray_sum(test_array, subarray_len) == expected
