"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if nums and k and 0 < k < len(nums):
        start_index = k-1
        arr = [nums[i-start_index:i + 1] for i in range(start_index,
                                                        len(nums))]
        arr_sum = [sum(arr[i]) for i in range(len(arr))]
        return max(arr_sum)
    return 0
