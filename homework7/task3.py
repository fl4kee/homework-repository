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


def win_check(line: List[List]) -> str:
    line_set = set(line)
    if len(line_set) == 1 and '-' not in line_set:
        return f'{list(line_set)[0]} wins'
    return ''


def win_by_row(field: List[List]) -> str:
    for row in field:
        win = win_check(row)
        if win:
            break
    return win


def win_by_col(field: List[List]) -> str:
    board_size = len(field[0])
    for i in range(board_size):
        col = []
        for j in range(board_size):
            col.append(field[j][i])
        win = win_check(col)
        if win:
            break
    return win


def win_by_diag(field: List[List]) -> str:
    board_size = len(field[0])
    diag = []
    for i in range(board_size):
        diag.append(field[i][i])
    return win_check(diag)


def win_by_side_diag(field: List[List]) -> str:
    board_size = len(field[0])
    side_diag = []
    for i in range(board_size):
        side_diag.append(field[i][board_size - i - 1])
    return win_check(side_diag)


def tic_tac_toe_checker(field: List[List]) -> str:
    result = win_by_row(field) or \
        win_by_col(field) or \
        win_by_diag(field) or \
        win_by_side_diag(field)
    if not result and {'-'}.issubset(chain.from_iterable(field)):
        return 'unfinished'
    else:
        return result or 'draw'
