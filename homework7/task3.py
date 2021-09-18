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


def tic_tac_toe_checker(field: List[List]) -> str:
    def win_condition(player):
        return field[0][0] == field[0][1] == field[0][2] == player or \
            field[1][0] == field[1][1] == field[1][2] == player or \
            field[2][0] == field[2][1] == field[2][2] == player or \
            field[0][0] == field[1][0] == field[2][0] == player or \
            field[0][1] == field[1][1] == field[2][1] == player or \
            field[0][2] == field[1][2] == field[2][2] == player or \
            field[0][0] == field[1][1] == field[2][2] == player or \
            field[0][2] == field[1][1] == field[2][0] == player

    if win_condition('x'):
        return 'x wins'
    elif win_condition('o'):
        return 'o wins'
    elif {'-'}.issubset(chain.from_iterable(field)):
        return 'unfinished'
    else:
        return 'draw'
