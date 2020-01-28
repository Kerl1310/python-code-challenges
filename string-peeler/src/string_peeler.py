import sys


def peel_string(text):
    '''
    Remove first and last letters from a string.
    '''
    if len(text) > 2:
        return text[1:(len(text) - 1)]
    return None


if len(sys.argv) > 1:
    print(peel_string(sys.argv[1]))
