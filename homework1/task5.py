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
    # Array's length greater than 1, subarray's length greater than 1 but less then array's length
    if array_len > 1 and 1 < subarray_len <= array_len:
        # Initial max value
        max_sum = sum(nums[0:subarray_len - 1])
        # i - start index
        for i in range(0, array_len - subarray_len + 1):
            # j - subarray's length
            for j in range(2, subarray_len + 1):
                subarray_sum = sum(nums[i:i + j])
                max_sum = subarray_sum if subarray_sum > max_sum else max_sum
        return max_sum
    return 0
