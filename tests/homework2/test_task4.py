from homework2.task4 import cache


def test_cache():
    def func(a: int, b: int) -> int:
        return (a ** b) ** 2
    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
