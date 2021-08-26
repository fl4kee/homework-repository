from homework1.task2 import check_fibonacci

def test_check_fibonacci_positive():
  assert check_fibonacci([1, 1, 2, 3, 5, 8, 13])

def test_check_fibonacci_negative():
  assert not check_fibonacci([1, -1, 24, 3, 12, 8, -13])

