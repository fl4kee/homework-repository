"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    """
    Accepts a functions
    Returns cashed function
    """
    cache: dict[tuple, str] = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            result = cache[args]
        else:
            result = func(*args)
            cache[args] = result
        return result
    return wrapper
