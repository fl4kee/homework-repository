from homework1.task5 import find_maximal_subarray_sum


def test_find_maximal_subarray_sum_positive():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16
    assert find_maximal_subarray_sum([], 3) == 0
    assert find_maximal_subarray_sum([1, 2, 3], -1) == 0
    assert find_maximal_subarray_sum([], 0) == 0
    assert find_maximal_subarray_sum([1, 5, 2, 3], None) == 0


def test_maximal_subarray_sum_negative():
    assert not find_maximal_subarray_sum([1, 2, 3, 4, 5, 6, 7], 6) == 6
    assert not find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 8) == 21
