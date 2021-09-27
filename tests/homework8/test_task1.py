import os

import pytest

from homework8.task1 import KeyValueStorage

FILE_DIR = os.path.join(os.path.dirname(__file__), 'data.txt')


@pytest.fixture
def manage_correct_input_file():
    with open(FILE_DIR, 'w') as text_file:
        text_file.writelines(['name=kek\n', 'last_name=top\n', 'power=9001\n',
                              'song=shadilay\n', '__doc__=built_in\n'])
    yield
    os.remove(FILE_DIR)


@pytest.fixture
def manage_incorrect_input_file():
    with open(FILE_DIR, 'w') as text_file:
        text_file.writelines(['.=wrong_key\n'])
    yield
    os.remove(FILE_DIR)


def test_keyvaluestorage_incorrect_inp(manage_correct_input_file):
    storage = KeyValueStorage(FILE_DIR)
    assert storage.name == 'kek'
    assert storage['last_name'] == 'top'
    assert storage.power == 9001
    assert storage['song'] == 'shadilay'
    assert storage.__doc__ == 'Class for saving attributes from a file'


def test_keyvaluestorage_correct_inp(manage_incorrect_input_file):
    with pytest.raises(ValueError, match="Key should be alphanumeric and can contain '_': ."):
        KeyValueStorage(FILE_DIR)
