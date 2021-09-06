# Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
# Calculation time should not take more than a minute. Use functional
# capabilities of multiprocessing module.
# You are not allowed to modify slow_calculate function.

import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def calc_with_mp(value: int) -> int:
    range_value = range(value)
    p = Pool(60)
    result = p.map(slow_calculate, range_value)
    p.close()
    p.join()
    return sum(result)


