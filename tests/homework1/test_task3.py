import os

from homework1.task3 import find_maximum_and_minimum

FILE_DIR = os.getcwd() + "/tests/homework1/test_file.txt"


def test_find_maximum_and_minimum_positive():
    assert find_maximum_and_minimum(FILE_DIR) == (-123, 981)
