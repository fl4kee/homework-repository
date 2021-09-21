"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from itertools import chain
from typing import List


def rows_generator(field):
    board_size = len(field[0])
    for row in range(board_size):
        yield field[row]


def cols_generator(field):
    board_size = len(field[0])
    for i in range(board_size):
        col = []
        for j in range(board_size):
            col.append(field[j][i])
        yield col


def get_diag(field):
    board_size = len(field[0])
    diag = []
    for i in range(board_size):
        diag.append(field[i][i])
    return diag


def get_side_diag(field):
    board_size = len(field[0])
    side_diag = []
    for i in range(board_size):
        side_diag.append(field[i][board_size - i - 1])
    return side_diag


def win_condition(field, player):
    # Checks if winner is in some row
    for row in rows_generator(field):
        if all(box == player for box in row):
            return True
    # Checks if winner is in some column
    for col in cols_generator(field):
        if all(box == player for box in col):
            return True
    # Checks if winner is in diagonal
    if all(box == player for box in get_diag(field)):
        return True
    # Checks if winner is in side diagonal
    elif all(box == player for box in get_side_diag(field)):
        return True
    return False


def tic_tac_toe_checker(field: List[List]) -> str:
    if win_condition(field, 'x'):
        return 'x wins'
    elif win_condition(field, 'o'):
        return 'o wins'
    elif {'-'}.issubset(chain.from_iterable(field)):
        return 'unfinished'
    else:
        return 'draw'
