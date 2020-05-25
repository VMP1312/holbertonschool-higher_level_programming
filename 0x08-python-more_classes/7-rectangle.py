#!/usr/bin/python3
"""
Prints a rectangle
"""


class Rectangle:
    """Class Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        print_symbol = "#"

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

    def area(self):
        """Area"""
        return self.height * self.width

    def perimeter(self):
        """Perimeter"""
        if self.width is 0 or self.height is 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """String"""
        string = ""
        if self.height is 0 or self.width is 0:
            return ""
        for row in range(self.height):
            for clm in range(self.width):
                string += str(self.print_symbol)
            string += '\n'
        return string[0:-1]

    def __repr__(self):
        """Representation"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Check delete"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")