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

    def update(self, *args, **kwargs):
        """Update"""
        if args and len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(min(len(args), len(attrs))):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in ['id', 'size', 'x', 'y']:
                    setattr(self, key, value)
    def to_dictionary(self):
        """dictionary"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
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


