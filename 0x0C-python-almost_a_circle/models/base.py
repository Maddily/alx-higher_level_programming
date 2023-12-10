#!/usr/bin/python3
"""
Module Name: base

Description: This module defines a class `Base`.
"""
import json
import csv
import turtle


class Base:
    """
    The base of all other classes in this project.
    It manages the `id` attribute in all other classes
    and helps avoid duplicating the same code.

    Class Attributes:
    - __nb_objects: The number of instances.

    Static Methods:
    - to_json_string()-> str: Returns the JSON string
    representation of `list_dictionaries`
    - from_json_string()-> list: Returns the Python list
    representation of json_string
    - draw: Opens a window and draws all the Rectangles
    and Squares from the given lists

    Class Methods:
    - save_to_file(): Writes the JSON string representation
    of list_objs to a file.
    - load_from_file()-> list: Deserializes objects from a JSON file
    and returns a list of objects
    - create(): Returns an instance with all attributes already set
    - save_to_file_csv(): Writes the CSV string representation
    of list_objs to a file
    - load_from_file_csv()-> list: Deserializes objects from a CSV file
    and returns a list of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        id: The identifier for an instance/object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Parameters:
        - list_dictionaries: A list of dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the Python list representation of json_string.

        Parameters:
        - json_string: A JSON string representation of a list of dictionaries.
        """

        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Parameters:
        - list_objs: A list of objects whose classes inherit from `Base`.
        (For example: `Rectangle` or `Square` objects)
        """

        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                file.write(
                    cls.to_json_string(
                        [obj.to_dictionary() for obj in list_objs]
                    )
                )

    @classmethod
    def load_from_file(cls):
        """Deserializes objects from a JSON file
        and returns a list of objects"""

        try:
            with open(f"{cls.__name__}.json") as file:
                dictionaries = cls.from_json_string(file.read())
                return [cls.create(**d) for d in dictionaries]
        except IOError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Parameters:
        - dictionary: Contains pairs of attributes and values
        """

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(2, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the CSV string representation of list_objs to a file.

        Parameters:
        - list_objs: A list of objects whose classes inherit from `Base`.
        (For example: `Rectangle` or `Square` objects)
        """

        with open(f"{cls.__name__}.csv", "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attribute_names = ['width', 'height', 'x', 'y', 'id']
                elif cls.__name__ == "Square":
                    attribute_names = ['size', 'x', 'y', 'id']

                writer = csv.DictWriter(file, fieldnames=attribute_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes objects from a CSV file
        and returns a list of objects"""

        try:
            with open(f"{cls.__name__}.csv", newline="") as file:
                if cls.__name__ == "Rectangle":
                    attribute_names = ['width', 'height', 'x', 'y', 'id']
                elif cls.__name__ == "Square":
                    attribute_names = ['size', 'x', 'y', 'id']

                reader = csv.DictReader(file, fieldnames=attribute_names)
                dictionaries = [
                     dict([attr, int(val)] for attr, val in row.items())
                     for row in reader
                ]
                return [cls.create(**d) for d in dictionaries]

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles
        and Squares from the given lists

        Parameters:
        - list_rectangles: A list of rectangle instances
        - list_squares: A list of square instances
        """

        lulu = turtle.Turtle()
        lulu.shape("turtle")
        lulu.color("#9ba699")
        lulu.pensize(2)
        lulu.pencolor("#2e1616")
        lulu.speed(3)

        wd = turtle.Screen()
        wd.bgcolor("#f6eebf")
        wd.title("Lulu")

        RECTANGLE_FILL_COLOR = ("#5f7b73")
        SQUARE_FILL_COLOR = ("#ec5e5e")

        for rectangle in list_rectangles:
            lulu.up()
            lulu.goto(rectangle.x, rectangle.y)
            lulu.down()
            lulu.begin_fill()
            lulu.fillcolor(RECTANGLE_FILL_COLOR)
            for _ in range(2):
                lulu.forward(rectangle.width)
                lulu.left(90)
                lulu.forward(rectangle.height)
                lulu.left(90)
            lulu.end_fill()

        for square in list_squares:
            lulu.up()
            lulu.goto(square.x, square.y)
            lulu.down()
            lulu.begin_fill()
            lulu.fillcolor(SQUARE_FILL_COLOR)
            for _ in range(4):
                lulu.forward(square.size)
                lulu.left(90)
            lulu.end_fill()

        lulu.hideturtle()
        wd.exitonclick()
