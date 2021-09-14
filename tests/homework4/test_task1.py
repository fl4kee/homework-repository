import os

import pytest

from homework4.task1 import read_magic_number

FILE_DIR = os.getcwd() + "/tests/homework4/data.txt"


@pytest.fixture
def manage_correct_input_file():
    with open(FILE_DIR, 'w') as text_file:
        text_file.writelines(['1\n', 'Hello there\n', 'Bye\n'])
    yield
    os.remove(FILE_DIR)


@pytest.fixture
def manage_incorrect_input_file():
    with open(FILE_DIR, 'w') as text_file:
        text_file.writelines(['I am not a number\n', 'Hello there\n', 'Bye\n'])
    yield
    os.remove(FILE_DIR)


def test_read_magic_number_positive_case(manage_correct_input_file):
    assert read_magic_number(FILE_DIR) is True


def test_read_magic_number_negative_case(manage_incorrect_input_file):
    assert read_magic_number(FILE_DIR) is False


def test_read_magic_number_error():
    with pytest.raises(ValueError, match="Something went wrong"):
        read_magic_number('not file')
