#!/usr/bin/python3
"""Create class."""


class Rectangle:
    """Define class."""

    def __init__(self, width=0, height=0):
        """Initialize shape."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """set width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not type(int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """set height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not type(int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of shape."""
        return self.width * self.height

    def perimeter(self):
        """perimeter of shape."""
        if self.width == 0 or self.height == 0:
            return 0
            return (self.width + self.height) * 2

    def __str__(self):
        """show the shape."""
        if self.width == 0 or self.height == 0:
            return ""
        return ((("#" * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        """show shape using eval."""
        return "Rectangle({}, {})".format(self.width, self.height)
    def __del__(self):
        """Print bye rectangle."""
        print("Bye rectangle...")
