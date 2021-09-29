"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager
from typing import Generator, Type


@contextmanager
def error_suppressor(exception_: Type[Exception]) -> Generator:
    try:
        yield
    except exception_:
        pass


class ErrorSuppressor:
    def __init__(self, exception_: Type[Exception]) -> None:
        self.exception = exception_

    def __enter__(self) -> None:
        pass

    def __exit__(self, exc_type: type, exc_value: str, traceback: str) -> bool:
        if issubclass(exc_type, self.exception):
            return True
        return False
