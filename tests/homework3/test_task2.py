import time

from homework3.task2 import calc_with_mp


def test_calc_with_mp():
    start_time = time.time()
    calc_with_mp(500)
    end_time = start_time - time.time()
    assert (end_time <= 60) is True
