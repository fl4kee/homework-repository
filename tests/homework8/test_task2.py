import os
from collections.abc import Iterable

from homework8.task2 import TableData

FILE_DIR = os.path.join(os.path.dirname(__file__), 'example.sqlite')


def test_tabledata():
    presidents = TableData(db_name=FILE_DIR, table_name='presidents')
    assert isinstance(presidents, Iterable)
    assert len(presidents) == 3
    assert presidents['Yeltsin'] == ('Yeltsin', 999, 'Russia')
    assert presidents.__next__() == ('Yeltsin', 999, 'Russia')
    assert presidents.__next__() == ('Trump', 1337, 'US')
    assert presidents.__next__() == ('Big Man Tyrone', 101, 'Kekistan')
