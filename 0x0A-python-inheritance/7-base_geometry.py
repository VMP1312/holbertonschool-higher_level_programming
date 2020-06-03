#!/usr/bin/python3
"""
Module.
"""


class BaseGeometry:
    """Class."""

    def area(self):
        """ Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validator"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
