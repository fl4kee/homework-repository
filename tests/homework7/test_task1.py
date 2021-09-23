import pytest

from homework7.task1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


@pytest.mark.parametrize('tree, element_to_search, expected', [(example_tree, 'RED', 6),
                                                               (example_tree, 'BLUE', 2),
                                                               (example_tree, 'ORANGE', 0)])
def test_find_occurrences(tree, element_to_search, expected):
    assert find_occurrences(tree, element_to_search) == expected
