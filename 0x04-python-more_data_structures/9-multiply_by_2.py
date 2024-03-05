#!/usr/bin/python3

"""
A function that returns a new dictionary multiplied by 2
"""


def multiply_by_2(a_dictionary):
    return {key: val * 2 for key, val in a_dictionary.items()}
