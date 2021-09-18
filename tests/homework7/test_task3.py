import pytest

from homework7.task3 import tic_tac_toe_checker

board = [['-', '-', 'o'],
         ['-', 'x', 'o'],
         ['x', 'o', 'x']]

board2 = [['-', '-', 'o'],
          ['-', 'o', 'o'],
          ['x', 'x', 'x']]

board3 = [['-', '-', 'o'],
          ['-', 'o', 'o'],
          ['o', 'x', 'x']]

board4 = [['x', 'x', 'o'],
          ['o', 'o', 'x'],
          ['x', 'o', 'x']]


@pytest.mark.parametrize('input_board, expected', [(board, 'unfinished'),
                                                   (board2, 'x wins'),
                                                   (board3, 'o wins'),
                                                   (board4, 'draw')])
def test_tic_tac_toe_checker(input_board, expected):
    assert tic_tac_toe_checker(input_board) == expected
