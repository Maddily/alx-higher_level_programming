#!/usr/bin/python3
"""
Module Name: test_base

This module is for testing base module.

Classes:
- TestBase
- TestBaseToJsonString
- TestBaseSaveToFile
- TestBaseFromJsonString
- TestBaseCreate
- TestBaseLoadFromFile
- TestBaseSaveToFileCsv
- TestBaseLoadFromFileCsv
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """
    Tests base module.
    """

    def setUp(self):
        """Resets __nb_objects before each method"""
        Base._Base__nb_objects = 0

    def test_nb_objects_incrementing(self):
        """Tests if __nb_objects is incremented
        when no id is passed"""

        object_without_id = Base()
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_id_incrementing(self):
        """Tests if id is incremented when no
        id is passed"""

        object1 = Base()
        object2 = Base()

        self.assertEqual(object1.id, object2.id - 1)

    def test_id_assignment(self):
        """Tests if id is assigned correctly"""

        object_with_id = Base(14)

        self.assertEqual(object_with_id.id, 14)

    def test_zero_id(self):
        """Tests if id is assigned correctly
        when 0 is passed"""

        object_with_id = Base(0)

        self.assertEqual(object_with_id.id, 0)

    def test_nb_objects_not_incrementing(self):
        """Tests if __nb_objects is not incremented
        when an id is passed."""

        object_with_id = Base(14)

        self.assertEqual(Base._Base__nb_objects, 0)

    def test_multiple_instances(self):
        """Tests if the id for each instance
        is unique if multiple instances are created."""

        objects = [Base() for _ in range(100)]
        objects_ids = {obj.id for obj in objects}

        self.assertEqual(len(objects_ids), len(objects))

    def test_incremental_ids(self):
        """Creates instances without providing an id and
        verifies that the ids are assigned incrementally."""

        object1 = Base()
        object2 = Base()
        object3 = Base()

        self.assertEqual(object1.id, object3.id - 2)

    def test_none_id(self):
        """Creates instances with id as None and
        verifies that the ids are assigned incrementally"""

        object1 = Base(None)
        object2 = Base(None)
        object3 = Base(None)

        self.assertEqual(object1.id, object3.id - 2)

    def test_none_and_provided_ids(self):
        """Tests if ids are set correctly with and without
        providing ids"""

        object1 = Base()
        object2 = Base()
        object3 = Base()
        object4 = Base(14)
        object5 = Base()

        self.assertEqual(object1.id, object5.id - 3)

    def test_nb_objects_private(self):
        '""'
        with self.assertRaises(AttributeError):
            print(Base(14).__nb_objects)

    def test_id_str(self):
        """Tests an id that isn't an integer"""

        self.assertEqual("O", Base("O").id)

    def test_id_float(self):
        """Tests an id that isn't an integer"""

        self.assertEqual(2.2, Base(2.2).id)

    def test_id_complex(self):
        """Tests an id that isn't an integer"""

        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_id_dict(self):
        """Tests an id that isn't an integer"""

        self.assertEqual({"One": 1}, Base({"One": 1}).id)

    def test_id_bool(self):
        """Tests an id that isn't an integer"""

        self.assertEqual(True, Base(True).id)

    def test_id_list(self):
        """Tests an id that isn't an integer"""

        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_id_tuple(self):
        """Tests an id that isn't an integer"""

        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_id_set(self):
        """Tests an id that isn't an integer"""

        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_id_frozenset(self):
        """Tests an id that isn't an integer"""

        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_id_range(self):
        """Tests an id that isn't an integer"""

        self.assertEqual(range(5), Base(range(5)).id)

    def test_id_bytes(self):
        """Tests an id that isn't an integer"""

        self.assertEqual(b'One', Base(b'One').id)

    def test_id_bytearray(self):
        """Tests an id that isn't an integer"""

        self.assertEqual(bytearray(b'One'), Base(bytearray(b'One')).id)

    def test_id_memoryview(self):
        """Tests an id that isn't an integer"""

        self.assertEqual(memoryview(b'One'), Base(memoryview(b'One')).id)

    def test_id_inf(self):
        """Tests an id that isn't an integer"""

        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_id_nan(self):
        """Tests an id that isn't an integer"""

        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        """Tests an id that isn't an integer"""

        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Tests the to_json_string() method"""

    def test_none_list(self):
        """Tests the to_json_string method with a None list"""

        self.assertEqual(Base().to_json_string(None), "[]")

    def test_empty_list(self):
        """Tests the to_json_string method with an empty list"""

        self.assertEqual(Base().to_json_string([]), "[]")

    def test_to_json_string_rectangle_type(self):
        """Tests the type of what's returned by
        the to_json_string method"""

        rectangle = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(
            type(Base.to_json_string([rectangle.to_dictionary()])), str
            )

    def test_to_json_string_square_type(self):
        """Tests the type of what's returned by
        the to_json_string method"""

        square = Square(10, 20, 30, 40)
        self.assertEqual(
            type(Base.to_json_string([square.to_dictionary()])), str
            )

    def test_to_json_string_rectangle_one_dict(self):
        """Tests the length of what's returned by
        the to_json_string method"""

        rectangle = Rectangle(10, 2, 3, 4, 5)
        self.assertTrue(
            len(Base.to_json_string([rectangle.to_dictionary()])) == 53
            )

    def test_to_json_string_rectangle_two_dict(self):
        """Tests the length of what's returned by
        the to_json_string method"""

        rectangle1 = Rectangle(1, 2, 3, 10, 4)
        rectangle2 = Rectangle(10, 2, 3, 4, 5)
        list = [rectangle1.to_dictionary(), rectangle2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list)) == 106)

    def test_to_json_string_square_one_dict(self):
        """Tests the length of what's returned by
        the to_json_string method"""

        square = Square(10, 2, 3, 4)
        self.assertTrue(
            len(Base.to_json_string([square.to_dictionary()])) == 39
            )

    def test_to_json_string_square_two_dict(self):
        """Tests the length of what's returned by
        the to_json_string method"""

        square1 = Square(1, 2, 3, 10)
        square2 = Square(10, 2, 3, 4)
        list = [square1.to_dictionary(), square2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list)) == 78)

    def test_to_json_string_without_args(self):
        """Test not passing arguments to to_json_string()"""

        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_excess_args(self):
        """Test passing extra arguments to to_json_string()"""

        with self.assertRaises(TypeError):
            Base.to_json_string([], 4)


class TestBaseSaveToFile(unittest.TestCase):
    """Tests save_to_file()"""

    @classmethod
    def tearDownClass(cls):
        """Deletes files created in this class."""

        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_rectangle(self):
        """Tests save_to_file() with one rectangle object"""

        rectangle = Rectangle(10, 2, 3, 4, 5)
        Rectangle.save_to_file([rectangle])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        """Tests save_to_file() with two rectangle objects"""

        rectangle1 = Rectangle(10, 2, 3, 4, 5)
        rectangle2 = Rectangle(1, 2, 3, 4, 10)
        Rectangle.save_to_file([rectangle1, rectangle2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 106)

    def test_save_to_file_square(self):
        """Tests save_to_file() with one square object"""

        square = Square(10, 2, 3, 4)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_two_squares(self):
        """Tests save_to_file() with two square objects"""

        square1 = Square(10, 2, 3, 4)
        square2 = Square(1, 2, 3, 10)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 78)

    def test_save_to_file_super_class_name(self):
        """Tests calling save_to_file() from Base"""

        square = Square(10, 2, 3, 4)
        Base.save_to_file([square])
        with open("Base.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_overwrite(self):
        """Tests overwriting the created file when
        save_to_file() is called twice"""

        square = Square(10, 2, 3, 4)
        Square.save_to_file([square])
        square = Square(1, 2, 3, 10)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_None(self):
        """Tests save_to_file() when passing None"""

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_empty_list(self):
        """Tests save_to_file() when passing an empty list"""

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_with_no_args(self):
        """Tests save_to_file() with no arguments"""

        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_excess_arg(self):
        """Tests save_to_file() with excess arguments"""

        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 4)


class TestBaseFromJsonString(unittest.TestCase):
    """Tests the from_json_string() method"""

    def test_none_list(self):
        """Tests the from_json_string method with a None list"""

        self.assertEqual(Base().from_json_string(None), [])

    def test_empty_list(self):
        """Tests the from_json_string method with an empty list"""

        self.assertEqual(Base().from_json_string("[]"), [])

    def test_from_json_string_type(self):
        """Tests the type of what's returned by
        the from_json_string method"""

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_rectangle_one_dict(self):
        """Tests the usage of from_json_string"""

        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_rectangle_two_dict(self):
        """Tests the usage of from_json_string"""

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_square_one_dict(self):
        """Tests the usage of from_json_string"""

        list_input = [{'id': 89, 'size': 10, 'x': 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_square_two_dict(self):
        """Tests the usage of from_json_string"""

        list_input = [
            {'id': 89, 'size': 10, 'x': 4},
            {'id': 98, 'size': 10, 'x': 12}
            ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_without_args(self):
        """Test not passing arguments to from_json_string()"""

        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_excess_args(self):
        """Test passing extra arguments to from_json_string()"""

        with self.assertRaises(TypeError):
            Base.from_json_string("[]", 4)


class TestBaseCreate(unittest.TestCase):
    """Tests create method"""

    def setUp(self):
        """Resets __nb_objects before each method"""

        Base._Base__nb_objects = 0

    def test_create_rectangle_str(self):
        """Tests calling str() on the new rectangle"""

        rectangle1 = Rectangle(3, 5, 1)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertEqual(str(rectangle2), "[Rectangle] (1) 1/0 - 3/5")

    def test_create_rectangle_same_str(self):
        """Tests the equality of string representation of two
        rectangles"""

        rectangle1 = Rectangle(3, 5, 1)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertEqual(str(rectangle1), str(rectangle2))

    def test_create_rectangle_is_same(self):
        """Tests if two rectangles aren't the same"""

        rectangle1 = Rectangle(3, 5, 1)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertIsNot(rectangle1, rectangle2)

    def test_create_rectangle_are_equal(self):
        """Tests if two rectangles aren't equal"""

        rectangle1 = Rectangle(3, 5, 1)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertNotEqual(rectangle1, rectangle2)

    def test_create_square_str(self):
        """Tests calling str() on the new square"""

        square1 = Square(3, 1)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertEqual(str(square2), "[Square] (1) 1/0 - 3")

    def test_create_square_same_str(self):
        """Tests the equality of string representation of two
        squares"""

        square1 = Square(3, 5, 1)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertEqual(str(square1), str(square2))

    def test_create_square_is_same(self):
        """Tests if two squares aren't the same"""

        square1 = Square(3, 5, 1)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertIsNot(square1, square2)

    def test_create_square_are_equal(self):
        """Tests if two squares aren't equal"""

        square1 = Square(3, 5, 1)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertNotEqual(square1, square2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Tests load_from_file method"""

    @classmethod
    def tearDownClass(cls):
        """Deletes files created in this class."""

        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def setUp(self):
        """Resets __nb_objects before each method"""

        Base._Base__nb_objects = 0

    def test_load_from_file_rectangle_type(self):
        """Tests the type of the return value"""

        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(2, 4)
        list_rectangles_input = [rectangle1, rectangle2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(type(list_rectangles_output), list)

    def test_load_from_file_rectangle_equal(self):
        """Tests the equality of two lists containing rectangle instances"""

        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(2, 4)
        list_rectangles_input = [rectangle1, rectangle2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertNotEqual(list_rectangles_input, list_rectangles_output)

    def test_load_from_file_rectangle_instance1_str(self):
        """Tests the equality of two str representation
        of the same rectangle after saving to and loading from a file"""

        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(2, 4)
        list_rectangles_input = [rectangle1, rectangle2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rectangle1), str(list_rectangles_output[0]))

    def test_load_from_file_rectangle_instance2_str(self):
        """Tests the equality of two str representation
        of the same rectangle after saving to and loading from a file"""

        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(2, 4)
        list_rectangles_input = [rectangle1, rectangle2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rectangle2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_instance_type(self):
        """Tests the type of instances in a list"""

        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(2, 4)
        list_rectangles_input = [rectangle1, rectangle2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(
            all(
                type(instance) is Rectangle
                for instance in list_rectangles_output
            )
        )

    def test_load_from_file_square_instance1_str(self):
        """Tests the equality of two str representation
        of the same square after saving to and loading from a file"""

        square1 = Square(10, 7, 2)
        square2 = Square(2)
        list_squares_input = [square1, square2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(square1), str(list_squares_output[0]))

    def test_load_from_file_square_instance2_str(self):
        """Tests the equality of two str representation
        of the same square after saving to and loading from a file"""

        square1 = Square(10, 7, 2)
        square2 = Square(2)
        list_squares_input = [square1, square2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(square2), str(list_squares_output[1]))

    def test_load_from_file_square_instance_type(self):
        """Tests the type of instances in a list"""

        square1 = Square(10, 7, 2)
        square2 = Square(2)
        list_squares_input = [square1, square2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertTrue(
            all(
                type(instance) is Square for instance in list_squares_output
            )
        )

    def test_load_from_file_non_existing(self):
        """Tests loading from a non-existing file"""

        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output, [])

    def test_load_from_file_with_args(self):
        """Tests calling load_from_file with arguments"""

        with self.assertRaises(TypeError):
            Base.load_from_file([], 4)


class TestBaseSaveToFileCsv(unittest.TestCase):
    """Tests save_to_file_csv()"""

    @classmethod
    def tearDownClass(cls):
        """Deletes files created in this class."""

        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_rectangle(self):
        """Tests save_to_file_csv() with one rectangle object"""

        rectangle = Rectangle(10, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([rectangle])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue(file.read(), "5,10,2,3,4")

    def test_save_to_file_csv_two_rectangles(self):
        """Tests save_to_file_csv() with two rectangle objects"""

        rectangle1 = Rectangle(10, 2, 3, 4, 5)
        rectangle2 = Rectangle(1, 2, 3, 4, 10)
        Rectangle.save_to_file_csv([rectangle1, rectangle2])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue(file.read(), "5,10,2,3,4\n10,1,2,3,4")

    def test_save_to_file_csv_square(self):
        """Tests save_to_file_csv() with one square object"""

        square = Square(10, 2, 3, 4)
        Square.save_to_file_csv([square])
        with open("Square.csv", "r") as file:
            self.assertTrue(file.read(), "4,10,2,3")

    def test_save_to_file_csv_two_squares(self):
        """Tests save_to_file_csv() with two square objects"""

        square1 = Square(10, 2, 3, 4)
        square2 = Square(1, 2, 3, 10)
        Square.save_to_file_csv([square1, square2])
        with open("Square.csv", "r") as file:
            self.assertTrue(file.read(), "4,10,2,3\n10,1,2,3")

    def test_save_to_file_csv_overwrite(self):
        """Tests overwriting the created file when
        save_to_file_csv() is called twice"""

        square = Square(10, 2, 3, 4)
        Square.save_to_file_csv([square])
        square = Square(1, 2, 3, 10)
        Square.save_to_file_csv([square])
        with open("Square.csv", "r") as file:
            self.assertTrue(file.read(), "10,1,2,3")

    def test_save_to_file_csv_None(self):
        """Tests save_to_file_csv() when passing None"""

        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_csv_empty_list(self):
        """Tests save_to_file_csv() when passing an empty list"""

        Square.save_to_file_csv([])
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_csv_with_no_args(self):
        """Tests save_to_file_csv() with no arguments"""

        with self.assertRaises(TypeError):
            Square.save_to_file_csv()

    def test_save_to_file_csv_excess_arg(self):
        """Tests save_to_file_csv() with excess arguments"""

        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([], 4)


class TestBaseLoadFromFileCsv(unittest.TestCase):
    """Tests load_from_file method"""

    @classmethod
    def tearDownClass(cls):
        """Deletes files created in this class."""

        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def setUp(self):
        """Resets __nb_objects before each method"""

        Base._Base__nb_objects = 0

    def test_load_from_file_csv_rectangle_type(self):
        """Tests the type of the return value"""

        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(2, 4)
        list_rectangles_input = [rectangle1, rectangle2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(type(list_rectangles_output), list)

    def test_load_from_file_csv_rectangle_equal(self):
        """Tests the equality of two lists containing rectangle instances"""

        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(2, 4)
        list_rectangles_input = [rectangle1, rectangle2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertNotEqual(list_rectangles_input, list_rectangles_output)

    def test_load_from_file_csv_rectangle_instance1_str(self):
        """Tests the equality of two str representation
        of the same rectangle after saving to and loading from a file"""

        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(2, 4)
        list_rectangles_input = [rectangle1, rectangle2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rectangle1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_rectangle_instance2_str(self):
        """Tests the equality of two str representation
        of the same rectangle after saving to and loading from a file"""

        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(2, 4)
        list_rectangles_input = [rectangle1, rectangle2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rectangle2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_instance_type(self):
        """Tests the type of instances in a list"""

        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(2, 4)
        list_rectangles_input = [rectangle1, rectangle2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertTrue(
            all(
                type(instance) is Rectangle
                for instance in list_rectangles_output
            )
        )

    def test_load_from_file_csv_square_instance1_str(self):
        """Tests the equality of two str representation
        of the same square after saving to and loading from a file"""

        square1 = Square(10, 7, 2)
        square2 = Square(2)
        list_squares_input = [square1, square2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(square1), str(list_squares_output[0]))

    def test_load_from_file_csv_square_instance2_str(self):
        """Tests the equality of two str representation
        of the same square after saving to and loading from a file"""

        square1 = Square(10, 7, 2)
        square2 = Square(2)
        list_squares_input = [square1, square2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(square2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_instance_type(self):
        """Tests the type of instances in a list"""

        square1 = Square(10, 7, 2)
        square2 = Square(2)
        list_squares_input = [square1, square2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertTrue(
            all(
                type(instance) is Square for instance in list_squares_output
            )
        )

    def test_load_from_file_csv_non_existing(self):
        """Tests loading from a non-existing file"""

        list_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_output, [])

    def test_load_from_file_csv_with_args(self):
        """Tests calling load_from_file with arguments"""

        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 4)


if __name__ == '__main__':
    unittest.main()
