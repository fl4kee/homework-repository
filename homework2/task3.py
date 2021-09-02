import itertools

"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations_(*args: List[Any]) -> List[List]:
    """
    Accepts any number of lists
    Returns all possible combinations of elements in giving lists
    """
    return [list(i) for i in list(itertools.product(*args))]
