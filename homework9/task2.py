"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager
from typing import Generator


@contextmanager
def error_suppressor(exception_) -> Generator:
    try:
        yield
    except exception_:
        pass


class ErrorSuppressor():
    def __init__(self, exception_):
        self.exception = exception_

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is self.exception:
            return True
