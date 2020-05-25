#!/usr/bin/python3
"""
Prints a rectangle
Use '#' to draw.
Return: None
"""


class Rectangle():
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width is not 0 or self.height is not 0:
            return (self.width + self.height) * 2
        return 0

    def __str__(self):
        string = ""
        if self.height is 0 or self.width is 0:
            return string
        for row in range(self.height):
            for clm in range(self.width):
                string += '#'
            string += '\n'
        return string[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        rectangle1 = rect_1.area()
        rectangle2 = rect_2.area()
        if rectangle1 >= rectangle2:
            return rect_1
        else:
            return rect_2
