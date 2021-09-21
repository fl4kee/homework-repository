import time

from homework3.task2 import calc_with_mp


def test_calc_with_mp():
    start_time = time.time()
    calc_with_mp(25)
    end_time = time.time() - start_time
    print(end_time)
    assert (end_time <= 10) is True
