#!/usr/bin/python3
"""Module containing the Base class"""
import json
import csv


class Base:
    """class base for object management."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identifier for the instance. If not provided,
                      a unique identifier will be assigned.
        """
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
        """setter method for id attribute"""
        self.validate_type('id', value)
        self.validate_xy('id', value)

        self.__id = value

    def to_json_string(list_dictionaries):
        """dictionary for the json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file for class method"""
        my_list = []
        if list_objs is not None:
            my_list = list_objs
        file_name = f"{cls.__name__}.json"

        dicts = []
        for obj in my_list:
            dicts.append(obj.to_dictionary())

        with open(file_name, "w") as file:
            file.write(cls.to_json_string(dicts))

    def from_json_string(json_string):
        """json string for class method"""
        if json_string is None or len(json_string) == 0:
            return []
        list_data = json.loads(json_string)
        return list_data

    @classmethod
    def create(cls, **dictionary):
        """create class method for the dictionary"""
        args = (2, 2, 2)
        obj = cls(*args)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """load class method for the dictionary"""
        file_name = f"{cls.__name__}.json"

        objs = []
        with open(file_name, "r") as file:
            items = cls.from_json_string(file.read())
            for item in items:
                objs.append(cls.create(**item))
        return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file for the class method"""
        my_list = []
        if list_objs is not None:
            my_list = list_objs
        file_name = f"{cls.__name__}.csv"

        dicts = []
        for obj in my_list:
            dicts.append(obj.to_dictionary())

        headers = list(dicts[0].keys())
        with open(file_name, "w", newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=dicts[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(dicts)

    @classmethod
    def load_from_file_csv(cls):
        """load from file class method"""
        file_name = f"{cls.__name__}.csv"

        objs = []
        with open(file_name, "r", newline='') as file:
            csv_reader = csv.DictReader(file)
            for item in csv_reader:
                for field in list(item.keys()):
                    item[field] = int(item[field])
                objs.append(cls.create(**item))
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module."""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
