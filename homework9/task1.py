"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from contextlib import ExitStack
from functools import wraps
from pathlib import Path
from typing import Callable, Iterator, List, Union


def sorted_gen(gen: Callable) -> Callable:
    @wraps(gen)
    def inner(*args):
        return iter(sorted((gen(*args))))
    return inner


@sorted_gen
def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    with ExitStack() as stack:
        files = [stack.enter_context(open(fname)) for fname in file_list]
        for file in files:
            for line in file:
                yield int(line)
