from homework3.task1 import cache


@cache(times=3)
def func(a: int, b: int) -> int:
    return (a ** b) ** 2


some = 100, 200
val_1 = func(*some)
val_2 = func(*some)
val_3 = func(*some)
val_4 = func(*some)
val_5 = func(*some)


def test_cache():
    assert (val_1 is val_2) is True
    assert (val_1 is val_2 is val_3) is True
    assert (val_1 is val_2 is val_3 is val_4) is True
    assert (val_1 is val_2 is val_3 is val_4 is val_5) is False
