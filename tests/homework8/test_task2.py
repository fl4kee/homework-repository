import os
from collections.abc import Iterable

from homework8.task2 import TableData

FILE_DIR = os.path.join(os.path.dirname(__file__), 'example.sqlite')


def test_tabledata():
    presidents = TableData(db_name=FILE_DIR, table_name='presidents')
    assert isinstance(presidents, Iterable)
    assert len(presidents) == 3
    assert presidents['Yeltsin'] == ('Yeltsin', 999, 'Russia')
    presidents_list = []
    for president in presidents:
        presidents_list.append(president['name'])
    assert presidents_list == ['Yeltsin', 'Trump', 'Big Man Tyrone']
