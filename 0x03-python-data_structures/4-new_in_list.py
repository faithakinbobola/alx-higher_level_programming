#!/usr/bin/python3
"""Replace ina copy"""


def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0:
        return (copy)
    elif idx > len(my_list) - 1:
        return (copy)
    else:
        copy[idx] = element
    return (copy)
