# There are multiple bugs in this code. Find them all and write tests for faulty cases.
from typing import Dict, List


class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """
    def __init__(self, functions):
        self.functions = functions

    def apply(self, data: List) -> List:
        return [
            item for item in data
            if all(i(item) for i in self.functions)
        ]


def make_filter(**keywords: Dict) -> Filter:
    """
        Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, filter_value in keywords.items():
        def keyword_filter_func(value):
            if key in value:
                return value[key] == filter_value
            else:
                return []
        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)
