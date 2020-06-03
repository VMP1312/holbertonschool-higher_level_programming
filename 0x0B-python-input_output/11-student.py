#!/usr/bin/python3
"""
Module.
"""


class Student:
    """Class."""

    def __init__(self, first_name, last_name, age):
        """Initialize."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """JSON"""
        return self.__dict__
