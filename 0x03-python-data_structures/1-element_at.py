#!/usr/bin/python3
"""Secure access to an element in a list"""


def element_at(my_list, idx):
    if idx > 0:
        return (my_list[idx])
    
    elif idx < 0:
        return (None)
    
    elif idx > len(my_list - 1):
        return (None)
