#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""class definition"""


class Rectangle(BaseGeometry):
    """ shape definition"""

    def __init__(self, width, height):
           """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height

    def area(self):
        """area definition"""
        return(self.__width * self.__height)

    def __str__(self):
        """string definition"""
        return f"[Rectangle] {self.__width}/{self.__height}"
