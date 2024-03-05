#!/usr/bin/python3

"""
A function that computes the square value
"""

def square_matrix_map(matrix=[]):
    return list(map((lambda row: list(map((lambda x: x * x), row))), matrix))
