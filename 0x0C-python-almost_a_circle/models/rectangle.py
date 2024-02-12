#!/usr/bin/python3
"""shape representation"""

from models.base import Base

class Rectangle(Base):
    """class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """innitializer"""
        self.validate_type('width', width)
        self.validate_value('width', width)
        self.validate_type('height', height)
        self.validate_value('height', height)
        self.validate_type('x', x)
        self.validate_type('y', y)
        self.validate_xy('x', x)
        self.validate_xy('y', y)

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def validate_type(self, name, value):
        """validate type"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

    def validate_value(self, name, value):
        """validate value"""
        if value <= 0:
            raise ValueError(f"{name} must be > 0")
    def validate_xy(self, name, value):
        """validate value"""
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        self.validate_type('width', value)
        self.validate_value('width', value)

        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        self.validate_type('height', value)
        self.validate_value('height', value)

        self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x
    @x.setter
    def x(self, value):
        """setter"""
        self.validate_type('x', value)
        self.validate_xy('x', value)

        self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        self.validate_type('y', value)
        self.validate_xy('y', value)

        self.__y = value

    def area(self):
        """area"""
        area = self.__height * self.__width
        return area

    def display(self):
        """display"""
        spaces = [' '] * self.__x
        hashes = ['#'] * self.__width
        row = spaces + hashes
        row_str = "".join(row)
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(row_str)
    
    def __str__(self):
        """str"""
        lines = []
        lines.append("[Rectangle]")
        id = self.id
        lines.append(f"({id})")
        lines.append(f"{self.__x}/{self.__y}")
        lines.append("-")
        lines.append(f"{self.__width}/{self.__height}")

        return " ".join(lines)

    def update (self, *args, **kwargs):
        """innitializer"""
        if args and len(args) > 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(min(len(args), len(attrs))):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in ['id', 'width', 'height', 'x', 'y']:
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictionary"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height, 'x': self.__x, 'y': self.__y}
