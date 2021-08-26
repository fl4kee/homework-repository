from homework1.task3 import find_maximum_and_minimum


def test_find_maximum_and_minimum_positive():
    assert find_maximum_and_minimum('C:\\Users\\flake\\projects\
                                    \\homework-repository \\tests\
                                    \\homework1\\test_file.txt') == (-123, 981)
