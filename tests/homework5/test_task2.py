import functools

from homework5.task2 import print_result


def test_print_result(capsys):
    @print_result
    def custom_sum(*args):
        """This function can sum any objects which have __add___"""
        return functools.reduce(lambda x, y: x + y, args)

    assert custom_sum([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
    assert custom_sum(1, 2, 3, 4) == 10
    assert capsys.readouterr().out
    assert custom_sum.__doc__ == 'This function can sum any objects which have __add___'
    assert custom_sum.__name__ == 'custom_sum'

    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10
    assert not capsys.readouterr().out
