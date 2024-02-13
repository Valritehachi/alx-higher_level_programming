#!/usr/bin/python3
"""Defines class method for the square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent square method function."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer of the square instance
        Args:
            size (int): The side length of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The identifier for the square.
        """

        super().__init__(size, size, x, y,id)

    @property
    def size(self):
        """getter property of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter property of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update property of the square."""
        if args and len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(min(len(args), len(attrs))):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in ['id', 'size', 'x', 'y']:
                    setattr(self, key, value)
    def to_dictionary(self):
        """dictionary property of the square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
    def display(self):
        """display property of the square."""
        spaces = [' '] * self.x
        hashes = ['#'] * self.width
        row = spaces + hashes
        row_str = "".join(row)
        for i in range(self.y):
            print( )
        for i in range(self.height):
            print(" " *self.x + "#" *self.width)

    def __str__(self):
        """string property of the square."""
        lines = []
        lines.append("[Square]")
        id = self.id
        lines.append(f"({id})")
        lines.append(f"{self.x}/{self.y}")
        lines.append("-")
        lines.append(f"{self.width}")

        return " ".join(lines)


