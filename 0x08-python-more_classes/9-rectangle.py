#!/usr/bin/python3
"""
Prints a rectangle
Use '#' to draw.
Return: None
"""


class Rectangle():
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Widht setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Height Setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        if self.width is not 0 or self.height is not 0:
            return (self.width + self.height) * 2
        return 0

    def __str__(self):
        """Prints the square"""
        string = ""
        if self.height is 0 or self.width is 0:
            return string
        for row in range(self.height):
            for clm in range(self.width):
                string += '#'
            string += '\n'
        return string[:-1]

    def __repr__(self):
        """Makes a representation"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Check a deleted instante"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Checks if a rectangle is bigger or equal to another one"""
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

    @classmethod
    def square(cls, size=0):
        """Class method."""
        return cls(size, size)
