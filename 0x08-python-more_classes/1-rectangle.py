#!/usr/bin/python3
"""
Prints a rectangle
"""


class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width"""
        return self.__width

    @property
    def height(self):
        """Height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Width setter"""
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        if(value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Height setter"""
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        if(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
