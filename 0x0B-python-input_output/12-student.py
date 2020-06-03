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

    def to_json(self, attrs=None):
        """JSON"""
        if type(attrs) == list and all(isinstance(dt, str) for dt in attrs):
            dic = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    dic[k] = v
            return dic
        else:
            return self.__dict__
