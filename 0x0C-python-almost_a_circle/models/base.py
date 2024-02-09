#!/usr/bin/python3
class Base:
    """class base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """innitializer"""
        if id is not None:
            self._id = id
        else:
            Base.__nb_objects += 1
            self._id = Base.__nb_objects

    @property
    def id(self):
        """Getter method for the 'id' attribute."""
        return self._id

    @id.setter
    def id(self, value):
        """setter"""
        self.validate_type('id', value)
        self.validate_xy('id', value)

        self.__id = value

