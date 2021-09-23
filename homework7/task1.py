"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any, counter=0) -> int:
    if(isinstance(tree, dict)):
        for value in tree.values():
            counter = find_occurrences(value, element, counter)
    elif isinstance(tree, (list, tuple, set)):
        for item in tree:
            counter = find_occurrences(item, element, counter)
    else:
        if tree == element:
            counter += 1
        return counter
    return counter
