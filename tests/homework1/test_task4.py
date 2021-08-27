from homework1.task4 import check_sum_of_four


def test_check_sum_of_four():
    assert check_sum_of_four([1, -8, 3],
                             [3, 5, -10],
                             [-5, -9, 20],
                             [-15, 6, 7]) == 1
    assert check_sum_of_four([1, -8, 3],
                             [3, 5, -10],
                             [-5, -9, 20],
                             [-15, 8, 8]) == 3
    assert check_sum_of_four([], [], [], []) == 0
