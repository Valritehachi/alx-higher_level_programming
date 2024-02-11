#!/usr/bin/python3
import json

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

    def to_json_string(list_dictionaries):
        """dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        my_list = []
        if list_objs is not None:
            my_list = list_objs
        file_name = f"{cls.__name__}.json"

        dicts = []
        for obj in my_list:
            dicts.append( obj.to_dictionary() )

        with open(file_name, "w") as file:
            file.write( cls.to_json_string(dicts) )

    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        list_data = json.loads(json_string)
        return list_data
        
