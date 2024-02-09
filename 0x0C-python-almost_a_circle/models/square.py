#!/usr/bin/python3
"""Defines class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer"""

        super().__init__(size, size, x, y,id)

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def display(self):
        """display"""
        spaces = [' '] * self.x
        hashes = ['#'] * self.width
        row = spaces + hashes
        row_str = "".join(row)
        for i in range(self.y):
            print( )
        for i in range(self.height):
            print(" " *self.x + "#" *self.width)

    def __str__(self):
        """str"""
        lines = []
        lines.append("[Square]")
        id = self.id
        lines.append(f"({id})")
        lines.append(f"{self.x}/{self.y}")
        lines.append("-")
        lines.append(f"{self.width}")

        return " ".join(lines)


