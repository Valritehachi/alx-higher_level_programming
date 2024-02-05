#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
""" class definition"""


class Square(Rectangle):

    def __init__(self, size):
        """innitializer"""
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """string"""
        return f"[Square] {self.__size}/{self.__size}"
