import pytest

from homework9.task2 import ErrorSuppressor, error_suppressor


class CustomValueExc(ValueError):
    pass


def test_error_suppressor_func():
    try:
        with error_suppressor(ValueError):
            raise CustomValueExc
    except ValueError:
        assert False, "raised an exception"


def test_error_raised_in_error_suppressor_func():
    with pytest.raises(ValueError):
        with error_suppressor(TypeError):
            raise ValueError


def test_error_suppressor_class():
    try:
        with ErrorSuppressor(ValueError):
            raise CustomValueExc
    except ValueError:
        assert False, "raised an exception"


def test_error_raised_in_error_suppressor_class():
    with pytest.raises(ValueError):
        with ErrorSuppressor(TypeError):
            raise ValueError
