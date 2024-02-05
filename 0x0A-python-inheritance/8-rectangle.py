#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""class definition"""


class Rectangle(BaseGeometry):
    """ class definition"""

    def __init__(self, width, height):
        """innitializer
        the reectangle innitializer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
