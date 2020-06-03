#!/usr/bin/python3
"""
Module.
"""


def add_attribute(obj, key, value):
    """Class."""
    if hasattr(obj, "__slots__") and not hasattr(obj, key):
        raise TypeError("can't add new attribute")
    elif not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    elif hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, key, value)
