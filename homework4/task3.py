"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.
my_precious_logger("error: file not found")
# stderr
'error: file not found'
my_precious_logger("OK")
# stdout
'OK'
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests
You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout
"""
import string
import sys


def my_precious_logger(text: str):
    """
    Writes string to stderr if first word is 'error'
    otherwise writes it to stdout
    """
    if text.split()[0].strip(string.punctuation) == 'error':
        sys.stderr.write(text)
    else:
        sys.stdout.write(text)
