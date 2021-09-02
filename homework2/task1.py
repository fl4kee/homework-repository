"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from collections import Counter
from typing import Callable, Dict, List


def is_diverse(word: str) -> bool:
    """Checks if word consists of unique symbols"""
    return len(set(word)) == len(word)


def is_character(symbol: str) -> bool:
    """Checks if symbol is a character"""
    return symbol.isalpha()


def is_symbol(symbol: str) -> bool:
    """Checks if symbol is not whitespace"""
    return symbol not in string.whitespace


def is_punctuation(symbol: str) -> bool:
    """Checks if symbol is punctuation"""
    return symbol in string.punctuation


def is_non_ascii(symbol: str) -> bool:
    """Checks if symbol is non ascii character"""
    return not symbol.isascii()


def get_symbols_on_condition(file_path: str, condition: Callable) -> Dict[str, int]:
    """
    Accepts file as a first argument, condition function as a second
    returns all symbols in files filtered by passed condition
    """
    with open(file_path, 'r') as file:
        symbols: Dict[str, int] = Counter()
        for line in file:
            # replace backlash characters with actual symbols
            decoded_line = line.encode('utf-8').decode('unicode-escape')
            for symbol in decoded_line:
                if condition(symbol):
                    symbols[symbol] += 1
        return symbols


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    returns 10 longest diverse words
    """
    unique_words = {}
    with open(file_path) as file:
        for line in file:
            decoded_line = line.encode('utf-8').decode('unicode-escape').strip(string.whitespace)
            # array of words in one line
            words = decoded_line.split(' ')
            for word in words:
                strip_word = word.strip(string.punctuation)
                # if word is diverse and not in unique_words adding it to unique_words
                strip_word_len = len(strip_word)
                if strip_word_len > 0 and is_diverse(strip_word)\
                   and strip_word not in unique_words:
                    unique_words[strip_word] = strip_word_len
    # return first 10 unique words sorted by descending order
    return sorted(unique_words, key=lambda x: unique_words[x], reverse=True)[:10]


def get_rarest_char(file_path: str) -> str:
    """returns rarest character in text"""
    symbols = get_symbols_on_condition(file_path, is_symbol)
    if symbols:
        return sorted(symbols, key=lambda x: symbols[x])[0]
    return ''


def count_punctuation_chars(file_path: str) -> int:
    """returns number of punctuation symbols in text"""
    symbols = get_symbols_on_condition(file_path, is_punctuation)
    return sum(symbols.values())


def count_non_ascii_chars(file_path: str) -> int:
    """returns number of non-ascii symbols in text"""
    symbols = get_symbols_on_condition(file_path, is_non_ascii)
    return sum(symbols.values())


def get_most_common_non_ascii_char(file_path: str) -> str:
    """returns most common non ascii character in text"""
    symbols = get_symbols_on_condition(file_path, is_non_ascii)
    if symbols:
        return sorted(symbols, key=lambda x: symbols[x])[-1]
    return ''
