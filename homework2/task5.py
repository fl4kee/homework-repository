"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'o') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""
from typing import List


def custom_range(iterable: List, start: str, end=None, step=1) -> List:
    """
    Accepts unique iterable, start index, end index and step
    behaves like built-in range function
    """
    elements_list = []
    if end is None:
        end = start
        start = iterable[0]
    current_index = iterable.index(start)
    end_index = iterable.index(end)
    if step >= 1 and current_index < end_index:
        while current_index < end_index:
            elements_list.append(iterable[current_index])
            current_index += step
    elif step < 0 and end_index < current_index:
        while current_index > end_index:
            elements_list.append(iterable[current_index])
            current_index += step
    return elements_list
