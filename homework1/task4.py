"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l)
    there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
import time
from typing import List

start = time.perf_counter()


def sum_two_arrs(arr1, arr2):
    sum_ = []
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            sum.append(arr1[i] + arr2[j])
    return sum_


def count_zeroes(arr1, arr2):
    count = sum_two_arrs(arr1, arr2)
    return count.count(0)


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    sum1 = sum_two_arrs(a, b)
    sum2 = sum_two_arrs(c, d)
    return count_zeroes(sum1, sum2)


# if __name__ == '__main__':

    # finish = time.perf_counter()
    # print(f'Finished in {round(finish - start, 2)} second(s)')
