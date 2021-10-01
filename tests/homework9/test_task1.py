import os
from collections.abc import Iterator

import pytest

from homework9.task1 import merge_sorted_files

FILE1_DIR = os.path.join(os.path.dirname(__file__), 'file1.txt')
FILE2_DIR = os.path.join(os.path.dirname(__file__), 'file2.txt')
FILE3_DIR = os.path.join(os.path.dirname(__file__), 'file3.txt')


@pytest.fixture
def manage_input_files():
    with open(FILE1_DIR, 'w') as text_file1:
        text_file1.writelines(['1\n', '11\n', '15'])
    with open(FILE2_DIR, 'w') as text_file2:
        text_file2.writelines(['2\n', '4\n', '6'])
    with open(FILE3_DIR, 'w') as text_file3:
        text_file3.writelines(['8\n', '10\n', '12'])
    yield
    os.remove(FILE1_DIR)
    os.remove(FILE2_DIR)
    os.remove(FILE3_DIR)


def test_merge_sorted_files(manage_input_files):
    res = merge_sorted_files([FILE1_DIR, FILE2_DIR, FILE3_DIR])
    assert isinstance(res, Iterator)
    assert list(res) == [1, 2, 4, 6, 8, 10, 11, 12, 15]
