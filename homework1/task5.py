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
    try:
        if not (1 < k < len(nums)):
            raise Exception
        max_ = sum(nums[0:k])
        for i in range(1, len(nums)):
            if sum(nums[i:i + k]) > max_:
                max_ = sum(nums[i:i + k])
        return max_
    except Exception as e:
        print(e)
        return 0
