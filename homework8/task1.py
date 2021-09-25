# We have a file that works as key-value storage, each line is represented
# as key and value separated by = symbol, example:
# name=kek last_name=top song=shadilay power=9001
# Values can be strings or integer numbers. If a value can be treated both
# as a number and a string, it is treated as number.
# Write a wrapper class for this key value storage that works like this:
# storage = KeyValueStorage('path_to_file.txt') that has its keys and values
# accessible as collection items and as attributes.
# Example: storage['name'] # will be string 'kek' storage.song_name # will be
# 'shadilay' storage.power # will be integer 9001
# In case of attribute clash existing built-in attributes take precedence.
# In case when value cannot be assigned to an attribute (for example when there's
# a line 1=something) ValueError should be raised.
# File size is expected to be small, you are permitted to read it entirely into memory.
import re


class KeyValueStorage:
    """Class for saving attributes from a file"""
    def __init__(self, path):
        self.set_attributes(path)

    def set_attributes(self, path):
        built_in_attrs = self.__dir__()
        with open(path) as f:
            for line in f:
                key, value = line.strip('\n').split('=')
                if value.isdigit():
                    value = int(value)
                if key in built_in_attrs:
                    continue
                if not (re.search(r'^[a-zA-Z0-9_]*$', key)):
                    raise ValueError(f"Key should be alphanumeric and can contain '_': {key}")
                setattr(self, key, value)

    def __getitem__(self, name):
        return getattr(self, name)
