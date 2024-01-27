#!/usr/bin/python3
"""Print a list of integers in reverse"""


def print_reversed_list_integer(my_list=[]):
    if type(my_list) is list:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
