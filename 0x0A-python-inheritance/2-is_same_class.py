#!/usr/bin/python3
"""
Module.
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the class."""
    if type(obj) is a_class:
        return True
    else:
        return False
