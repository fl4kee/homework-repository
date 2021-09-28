"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6
"""
import os
from pathlib import Path
from typing import Callable, Optional, Union


def universal_file_counter(
    dir_path: Union[str, Path], file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    count: int = 0
    for file in os.listdir(dir_path):
        if file.endswith('.txt'):
            with open(os.path.join(dir_path, file), 'r') as f:
                for line in f:
                    if tokenizer is None:
                        count += 1
                    else:
                        count += len(tokenizer(line))

    return count
