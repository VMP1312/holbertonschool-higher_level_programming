#!/usr/bin/python3
"""
Module.
"""


def read_lines(filename="", nb_lines=0):
    """Returns the number of lines"""
    cnt = 0
    with open(filename, 'r') as fl:
        for line in fl:
            cnt += 1
        if nb_lines <= 0 or cnt <= nb_lines:
            print(line, end="")
