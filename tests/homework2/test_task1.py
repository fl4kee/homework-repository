import os

import pytest

import homework2.task1 as t1

DATA_DIR = os.getcwd() + "/tests/homework2/data.txt"
DATA_SMALL_DIR = os.getcwd() + "/tests/homework2/small_data.txt"


@pytest.mark.parametrize(
    "test_input,expected",
    [('abcdefg', True), ('aabbccdd', False)]
)
def test_is_diverse(test_input, expected):
    assert t1.is_diverse(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [('a', True), ('ß', True), ('.', False), (' ', False)]
)
def test_is_character(test_input, expected):
    assert t1.is_character(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [(' ', False), ('a', True), ('.', True), ('ß', True)]
)
def test_is_symbol(test_input, expected):
    assert t1.is_symbol(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [(' ', False), ('a', False), ('.', True), ('ß', False)]
)
def test_is_punctuation(test_input, expected):
    assert t1.is_punctuation(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [('a', False), ('.', False), ('ß', True)]
)
def test_is_non_ascii(test_input, expected):
    assert t1.is_non_ascii(test_input) == expected


@pytest.mark.parametrize(
    "test_file, condition, expected",
    [
        (DATA_DIR, t1.is_non_ascii, {'Ü': 42, '»': 43, '«': 43, '—': 81,
                                     'ß': 708, 'ü': 804, 'ä': 866, 'ö': 357,
                                     '›': 1, '‹': 1, 'Ä': 15, 'Ö': 3, 'é': 6,
                                     'î': 1, '’': 1}),
        (DATA_SMALL_DIR, t1.is_non_ascii, {'ß': 2, 'ü': 3, '—': 1})
    ]
)
def test_get_symbols_on_condition(test_file, condition, expected):
    assert t1.get_symbols_on_condition(test_file, condition) == expected


@pytest.mark.parametrize(
    "test_file, expected",
    [
        (DATA_DIR, ['Nichtkämpfern', 'verständlich', 'kalyptischen', 'Mobilmachung',
                    'Umschreibung', '»unsichtbare', 'Zwickmühlen', 'Verdichtung',
                    'unsichtbare', 'anschuldigt']),
        (DATA_SMALL_DIR, ['ausführen', 'hinter', 'gefaßt', 'machen', 'Titel',
                          'nicht', 'Pfade', 'sich', 'chen', 'über'])
    ]
)
def test_get_longest_diverse_words(test_file, expected):
    assert t1.get_longest_diverse_words(test_file) == expected


@pytest.mark.parametrize(
    "test_file, expected",
    [(DATA_DIR, '›'), (DATA_SMALL_DIR, 'W')]
)
def test_get_rarest_char(test_file, expected):
    assert t1.get_rarest_char(test_file) == expected


@pytest.mark.parametrize(
    "test_file, expected",
    [(DATA_DIR, 5305), (DATA_SMALL_DIR, 7)]
)
def test_count_punctuation_chars(test_file, expected):
    assert t1.count_punctuation_chars(test_file) == expected


@pytest.mark.parametrize(
    "test_file, expected",
    [(DATA_DIR, 2972), (DATA_SMALL_DIR, 6)]
)
def test_count_non_ascii_chars(test_file, expected):
    assert t1.count_non_ascii_chars(test_file) == expected


@pytest.mark.parametrize(
    "test_file, expected",
    [(DATA_DIR, 'ä'), (DATA_SMALL_DIR, 'ü')]
)
def test_get_most_common_non_ascii_char(test_file, expected):
    assert t1.get_most_common_non_ascii_char(test_file) == expected
