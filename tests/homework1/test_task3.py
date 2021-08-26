import os
from homework1.task3 import find_maximum_and_minimum

dir = os.getcwd() + '\\tests\\homework1\\test_file.txt'


def test_find_maximum_and_minimum_positive():
    print(dir)
    assert find_maximum_and_minimum(dir) == (-123, 981)
