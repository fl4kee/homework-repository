"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l)
    there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def sum_two_arrs(arr1: List[int], arr2: List[int]) -> List[int]:
    sum_ = []
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            sum_.append(arr1[i] + arr2[j])
    return sum_


def count_zeroes(arr1: List[int], arr2: List[int]) -> int:
    count = sum_two_arrs(arr1, arr2)
    return count.count(0)


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    sum1 = sum_two_arrs(a, b)
    sum2 = sum_two_arrs(c, d)
    return count_zeroes(sum1, sum2)
