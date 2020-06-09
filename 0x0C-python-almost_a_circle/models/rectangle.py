#!/usr/bin/python3
"Rectangle class"


from models.base import Base


class Rectangle(Base):
    "Rectangle class"

    def __init__(self, width, height, x=0, y=0, id=None):
        "Rectangle class"
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
