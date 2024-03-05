#!/usr/bin/python3

"""
A function that replaces or add key/value in a dictionary
"""


def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for keys in a_dictionary:
            if keys == key:
                a_dictionary[keys] = value
    return a_dictionary
