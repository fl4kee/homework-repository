"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def backspace_compare(first: str, second: str):
    def change_string(string):
        changed_string = []
        for letter in string:
            if letter != '#':
                changed_string.append(letter)
            elif string.index(letter) == 0:
                continue
            else:
                changed_string.pop()
            return ''.join(changed_string)
    return(change_string(first) == change_string(second))
