"""
Write down the function, which reads input line-by-line,
and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as file:
        min_ = max_ = None
        for line in file:
            if min_ is None and max_ is None:
                min_ = max_ = int(line)
            if int(line) > max_:
                max_ = int(line)
            if int(line) < min_:
                min_ = int(line)
        if min_ is not None and max_ is not None:
            return (min_, max_)
        return (0, 0)
