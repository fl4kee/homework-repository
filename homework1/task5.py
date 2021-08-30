"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], subarray_len = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], subarray_len: int) -> int:
    array_len = len(nums)
    # Длина массива должна быть больше 1, длина подмассива больше 1 и не превышает длинну массива
    if all([array_len > 1, 1 < subarray_len <= array_len]):
        # Изначальное максимальное значение
        max_sum = sum(nums[0:2])
        # i - нижняя граница подмассива
        for i in range(0, array_len - subarray_len + 1):
            # j - длина подмассива
            for j in range(2, subarray_len + 1):
                subarray_sum = sum(nums[i:i + j])
                max_sum = subarray_sum if subarray_sum > max_sum else max_sum
        return max_sum
    return 0
