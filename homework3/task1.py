# @cache(times=3)
# def some_function():
#     pass
# Would give out cached value up to times number only. Example:

import functools
from typing import Callable


def cache(times):

    def cache_decorator(func: Callable) -> Callable:
        """
        Accepts a functions
        Returns cashed function
        """
        cache: dict[tuple, str] = {}

        @functools.wraps(func)
        def wrapper(*args):
            if args in cache and cache[args][1] <= times:
                result = cache[args][0]
                cache[args][1] += 1
            else:
                result = func(*args)
                count = 1
                cache[args] = [result, count]
            return result
        return wrapper
    return cache_decorator
