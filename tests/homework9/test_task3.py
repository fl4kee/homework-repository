import os

import pytest

from homework9.task3 import universal_file_counter

DIR_WITH_FILES = os.path.join(os.path.dirname(__file__))
FILE1_DIR = os.path.join(os.path.dirname(__file__), 'file1.txt')
FILE2_DIR = os.path.join(os.path.dirname(__file__), 'file2.txt')


@pytest.fixture
def manage_input_file():
    with open(FILE1_DIR, 'w') as f1:
        f1.writelines(['1\n', '2\n', '3'])
    with open(FILE2_DIR, 'w') as f2:
        f2.writelines(['Hello there\n', 'I am file with string\n', 'Have a good day'])
    yield
    os.remove(FILE1_DIR)
    os.remove(FILE2_DIR)


def test_universal_file_counter(manage_input_file):
    assert universal_file_counter(DIR_WITH_FILES, 'txt') == 6
    assert universal_file_counter(DIR_WITH_FILES, 'txt', str.split) == 14
