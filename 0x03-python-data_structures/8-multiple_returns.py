#!/usr/bin/python3
"""Function that returns a tuple with the length of a string and its first character"""


def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None
    else:
        return ((len(sentence), sentence[0]))

    
