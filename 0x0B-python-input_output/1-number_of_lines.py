#!/usr/bin/python3
"""
Module.
"""


def number_of_lines(filename=""):
    """Returns the number of lines"""
    cnt = 0
    with open(filename, 'r') as fl:
        for line in fl:
            cnt += 1
    return cnt
