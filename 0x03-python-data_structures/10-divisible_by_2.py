#!/usr/bin/python3
"""function that finds all multiple of 2 in a list"""


def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    result_list = []
    for i in my_list:
        if i % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return (result_list)
