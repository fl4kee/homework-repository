"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    element_counter = 0

    def read_elements(dictionary):
        nonlocal element_counter
        if isinstance(dictionary, dict):
            for value in dictionary.values():
                if isinstance(value, (list, tuple, set)):
                    for list_element in value:
                        read_elements(list_element)
                else:
                    read_elements(value)
        else:
            if dictionary == element:
                element_counter += 1
    read_elements(tree)
    return element_counter
