#!/usr/bin/python3

"""
A function that rerutns a list with values multiplied by a number
"""

def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
