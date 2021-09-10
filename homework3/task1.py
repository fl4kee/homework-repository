# @cache(times=3)
# def some_function():
#     pass
# Would give out cached value up to times number only. Example:

import functools
from typing import Callable


def cache(times: int) -> Callable:

    def cache_decorator(func: Callable) -> Callable:
        """
        Accepts a functions
        Returns cashed function
        """
        cache_dict: dict[tuple, str] = {}

        @functools.wraps(func)
        def wrapper(*args):
            if args in cache_dict and cache_dict[args][1] <= times:
                result = cache_dict[args][0]
                cache_dict[args][1] += 1
            else:
                result = func(*args)
                count = 1
                cache_dict[args] = [result, count]
            return result
        return wrapper
    return cache_decorator
