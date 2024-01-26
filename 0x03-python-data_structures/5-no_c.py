#!/usr/bin/python3
"""Remove all characters c and C from a string"""


def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i not in "cC":
            new_string += i
    return (new_string)
