#!/usr/bin/python3
"""
Module.
"""


def read_lines(filename="", nb_lines=0):
    """Returns the number of lines"""
    numl = len(open(filename).readlines())
    with open(filename, 'r') as fl:
        if nb_lines > 0 and nb_lines < numl:
            for line in range(nb_lines):
                print(fl.readline(), end="")
        else:
            print(fl.read(), end="")
