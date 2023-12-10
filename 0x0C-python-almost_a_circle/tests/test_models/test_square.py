#!/usr/bin/python3
"""
Module Name: test_square

Description: This module is for testing Square class

Classes:
- TestSquareInstantiation
- TestSquareGettersSetters
- TestSquareSize
- TestSquareX
- TestSquareY
- TestSquareInitializationOrder
- TestSquareArea
- TestSquareDisplay
- TestSquareStr
- TestSquareUpdate
- TestSquareToDictionary
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys


class TestSquareInstantiation(unittest.TestCase):
    """Tests Square instantiation"""

    def test_instance_of_base(self):
        """Tests if a square object is an instance of `Base`"""

        self.assertIsInstance(Square(4), Base)

    def test_instance_of_rectangle(self):
        """Tests if a square object is an instance of `Rectangle`"""

        self.assertIsInstance(Square(4), Rectangle)

    def test_no_arguments(self):
        """Tests if an exception is raised when no arguments
        are passed to Square during instantiation"""

        with self.assertRaises(TypeError):
            Square()

    def test_single_argument(self):
        """Tests if ids are correctly assigned"""

        square1 = Square(4)
        square2 = Square(8)
        self.assertEqual(square1.id, square2.id - 1)

    def test_id_assignment_with_two_args(self):
        """Tests if ids are correctly assigned"""

        square1 = Square(8, 4)
        square2 = Square(6, 3)
        self.assertEqual(square1.id, square2.id - 1)

    def test_id_assignment_with_three_args(self):
        """Tests if ids are correctly assigned"""

        square1 = Square(8, 4, 2)
        square2 = Square(6, 3, 1)
        self.assertEqual(square1.id, square2.id - 1)

    def test_id_assignment_with_four_args(self):
        """Tests if id is correctly assigned"""

        square = Square(8, 4, 2, 6)
        self.assertEqual(square.id, 6)

    def test_excess_arguments(self):
        """Tests if an exception is raised when
        excess arguments are passed"""

        with self.assertRaises(TypeError):
            Square(8, 4, 2, 6, 14)

    def test_default_x(self):
        """Tests if x is set properly"""

        square = Square(5)
        self.assertEqual(square.x, 0)

    def test_default_y(self):
        """Tests if y is set properly"""

        square = Square(5)
        self.assertEqual(square.y, 0)

    def test_default_id(self):
        """Tests if id is not None when not passed"""

        square = Square(5)
        self.assertIsNotNone(square.id)


class TestSquareGettersSetters(unittest.TestCase):
    """Tests getters and setters"""

    def test_size_getter(self):
        """Tests if `size` is retrieved correctly"""

        square = Square(8)
        self.assertEqual(square.size, 8)

    def test_size_setter(self):
        """Tests if `size` is set correctly"""

        square = Square(8)
        square.size = 4
        self.assertEqual(square.size, 4)

    def test_width_getter(self):
        """Tests if `width` is retrieved correctly"""

        square = Square(8)
        self.assertEqual(square.width, 8)

    def test_height_getter(self):
        """Tests if `height` is retrieved correctly"""

        square = Square(8)
        self.assertEqual(square.height, 8)

    def test_x_getter(self):
        """Tests if `x` is retrieved correctly"""

        square = Square(8, 4)
        self.assertEqual(square.x, 4)

    def test_y_getter(self):
        """Tests if `y` is retrieved correctly"""

        square = Square(8, 4, 2)
        self.assertEqual(square.y, 2)


class TestSquareSize(unittest.TestCase):
    """Tests size validity"""

    def test_input_size_float(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(8.2, 4, 2, 6)

    def test_input_size_none(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 4, 2, 6)

    def test_input_size_str(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("8.2", 4, 2, 6)

    def test_input_size_complex(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(8), 4, 2, 6)

    def test_input_size_dict(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"One": 1}, 4, 2, 6)

    def test_input_size_bool(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False, 4, 2, 6)

    def test_input_size_list(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3], 4, 2, 6)

    def test_input_size_set(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 4, 2, 6)

    def test_input_size_tuple(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2), 4, 2, 6)

    def test_input_size_frozenset(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3}), 4, 2, 6)

    def test_input_size_range(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(8), 4, 2, 6)

    def test_input_size_bytes(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b"One", 4, 2, 6)

    def test_input_size_bytearray(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b"One"), 4, 2, 6)

    def test_input_size_memoryview(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b"One"), 4, 2, 6)

    def test_input_size_inf(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float("inf"), 4, 2, 6)

    def test_input_size_nan(self):
        """Tests if an exception is raised
        when input size is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float("nan"), 4, 2, 6)

    def test_invalid_size_type_setter(self):
        """Tests input size in setter"""

        square = Square(8, 4, 2, 6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.size = 8.2

    def test_size_negative(self):
        """Tests if an exception is raised if
        size is less than 0"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square = Square(-8, 4, 2, 6)

    def test_size_zero(self):
        """Tests if an exception is raised if
        size is equal to 0"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square = Square(0, 4, 2, 6)

    def test_size_negative_setter(self):
        """Tests if an exception is raised if
        size is less than 0"""

        square = Square(8, 4, 2, 6)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.size = -8

    def test_size_zero_setter(self):
        """Tests if an exception is raised if
        size is equal to 0"""

        square = Square(8, 4, 2, 6)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.size = 0


class TestSquareX(unittest.TestCase):
    """Tests x validity"""

    def test_input_x_float(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, 2.2)

    def test_input_x_none(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, None)

    def test_input_x_str(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, "2")

    def test_input_x_complex(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, complex(2))

    def test_input_x_dict(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, {"One": 1})

    def test_input_x_bool(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, False)

    def test_input_x_list(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, [1, 2, 3])

    def test_input_x_set(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, {1, 2, 3})

    def test_input_x_tuple(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, (1, 2))

    def test_input_x_frozenset(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, frozenset({1, 2, 3}))

    def test_input_x_range(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, range(8))

    def test_input_x_bytes(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, b"One")

    def test_input_x_bytearray(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, bytearray(b"One"))

    def test_input_x_memoryview(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, memoryview(b"One"))

    def test_input_x_inf(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, float("inf"))

    def test_input_x_nan(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, float("nan"))

    def test_invalid_x_type_setter(self):
        """Tests input x in setter"""

        square = Square(8, 4, 2, 6)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.x = 8.2

    def test_x_negative(self):
        """Tests if an exception is raised if
        x is less than 0"""

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(8, -2)

    def test_x_negative_setter(self):
        """Tests if an exception is raised if
        x is less than 0"""

        square = Square(8, 4, 2, 6)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.x = -8


class TestSquareY(unittest.TestCase):
    """Tests y validity"""

    def test_input_y_float(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, 6.2)

    def test_input_y_none(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, None)

    def test_input_y_str(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, "6")

    def test_input_y_complex(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, complex(6))

    def test_input_y_dict(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, {"One": 1})

    def test_input_y_bool(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, True)

    def test_input_y_list(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, [1, 2, 3])

    def test_input_y_set(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, {1, 2, 3})

    def test_input_y_tuple(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, (1, 2))

    def test_input_y_frozenset(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, frozenset({1, 2, 3}))

    def test_input_y_range(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, range(8))

    def test_input_y_bytes(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, b"One")

    def test_input_y_bytearray(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, bytearray(b"One"))

    def test_input_y_memoryview(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, memoryview(b"One"))

    def test_input_y_inf(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, float("inf"))

    def test_input_y_nan(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 4, float("nan"))

    def test_invalid_y_type_setter(self):
        """Tests input y in setter"""

        square = Square(8, 4, 2, 6)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.y = 8.2

    def test_y_negative(self):
        """Tests if an exception is raised if
        y is less than 0"""

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(8, 4, -6)

    def test_y_negative_setter(self):
        """Tests if an exception is raised if
        y is less than 0"""

        square = Square(8, 4, 2, 6)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.y = -8


class TestSquareInitializationOrder(unittest.TestCase):
    """Tests the order of exception raising when
    initializing attributes with invalid values"""

    def test_size_then_x(self):
        """Tests size first"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(8.2, 2.2)

    def test_size_then_y(self):
        """Tests size first"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(8.2, 4, 6.2)

    def test_x_then_y(self):
        """Tests x first"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, 2.2, 6.2)


class TestSquareArea(unittest.TestCase):
    """Tests a Square object's area"""

    def test_area_regular_numbers(self):
        """Tests if the `area` method works properly
        with regular numbers"""

        square = Square(4, 12, 2, 6)
        self.assertEqual(square.area(), 16)

    def test_area_large_numbers(self):
        """Tests if the `area` method works properly
        with large numbers"""

        square = Square(999999999999999999, 2, 6)
        self.assertEqual(square.area(), 999999999999999998000000000000000001)

    def test_area_after_update(self):
        """Tests if the `area` method works properly
        after updating width and height"""

        square = Square(4, 12, 2, 6)
        square.size = 3
        self.assertEqual(square.area(), 9)

    def test_area_with_arg(self):
        """Tests if an exception is raised when an argument
        is passed to `area`"""

        square = Square(4, 12, 2, 6)
        with self.assertRaises(TypeError):
            square.area(8)


class TestSquareDisplay(unittest.TestCase):
    """Tests the display method"""

    def setUp(self):
        """
        Saves sys.stdout in an attribute to restore it later
        and redirect sys.stdout to capture print output
        """

        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        """Restores sys.stdout"""

        sys.stdout = self.saved_stdout

    def test_display_basic(self):
        """Tests display with a small Square"""

        square = Square(3)
        square.display()
        self.assertEqual(sys.stdout.getvalue(), "###\n###\n###\n")

    def test_display_large_Square(self):
        """Tests display with a larger Square"""

        square = Square(5)
        square.display()
        self.assertEqual(
            sys.stdout.getvalue(), "#####\n#####\n#####\n#####\n#####\n"
            )

    def test_display_Square_single_character(self):
        """Tests display with a Square of width and height 1"""

        square = Square(1)
        square.display()
        self.assertEqual(sys.stdout.getvalue(), "#\n")

    def test_display_with_x_and_y(self):
        """Tests display with given x and y"""

        square = Square(3, 1, 1)
        expected_output = "\n ###\n ###\n ###\n"
        square.display()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_display_with_x(self):
        """Tests display with given x"""

        square = Square(3, 1)
        expected_output = " ###\n ###\n ###\n"
        square.display()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_display_with_y(self):
        """Tests display with given y"""

        square = Square(3, 0, 1)
        expected_output = "\n###\n###\n###\n"
        square.display()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_display_with_arg(self):
        """Tests the display method when passed an argument"""

        square = Square(8, 2, 6)
        with self.assertRaises(TypeError):
            square.display(1)


class TestSquareStr(unittest.TestCase):
    """Tests the __str__ method"""

    def setUp(self):
        """
        Save sys.stdout in an attribute to restore it later
        and redirect sys.stdout to capture print output
        """

        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Restore sys.stdout"""

        sys.stdout = self.saved_stdout

    def test_basic_str_output(self):
        """Tests basic usage"""

        square = Square(4, 2, 1, 1)
        expected_output = "[Square] (1) 2/1 - 4"
        self.assertEqual(str(square), expected_output)

    def test_default_values(self):
        """Tests str() with default values"""

        square = Square(4)
        expected_output = "[Square] (1) 0/0 - 4"
        self.assertEqual(str(square), expected_output)

    def test_default_values_and_x(self):
        """Tests str() with default values and given x"""

        square = Square(4, 1)
        expected_output = "[Square] (1) 1/0 - 4"
        self.assertEqual(str(square), expected_output)

    def test_large_values(self):
        """Tests str() with large values"""

        square = Square(10000, 30000, 40000, 42)
        expected_output = "[Square] (42) 30000/40000 - 10000"
        self.assertEqual(str(square), expected_output)

    def test_none_id(self):
        """Tests str() without passing id"""

        square = Square(5, 7, 8)
        expected_output = "[Square] (1) 7/8 - 5"
        self.assertEqual(str(square), expected_output)

    def test_multiple_instances(self):
        """Tests str() with multiple objects"""

        square1 = Square(1, 3, 4, 5)
        square2 = Square(6, 8, 9, 10)
        square3 = Square(11, 13, 14, 15)
        expected_output = (
            "[Square] (5) 3/4 - 1"
            "[Square] (10) 8/9 - 6"
            "[Square] (15) 13/14 - 11"
            )
        self.assertEqual(str(square1) + str(square2)
                         + str(square3), expected_output)

    def test_updated_attributes(self):
        """Tests str() after setting attributes"""

        square = Square(11, 0, 0, 9)
        square.size = 13
        square.x = 5
        square.y = 3
        self.assertEqual("[Square] (9) 5/3 - 13", str(square))

    def test_one_arg(self):
        """Tests str() with one argument"""

        square = Square(1, 3, 4, 5)
        with self.assertRaises(TypeError):
            square.__str__(3)


class TestSquareUpdate(unittest.TestCase):
    """Tests the update method"""

    def setUp(self):
        """
        Save sys.stdout in an attribute to restore it later
        and redirect sys.stdout to capture print output
        """

        Base._Base__nb_objects = 0

    def test_update_no_args(self):
        """Tests update method without arguments"""

        square = Square(10, 10, 10, 10)
        square.update()
        self.assertEqual(str(square), "[Square] (10) 10/10 - 10")

    def test_update_None_id(self):
        """Tests update method with None id"""

        square = Square(10, 10, 10, 10)
        square.update(None)
        self.assertEqual(str(square), "[Square] (1) 10/10 - 10")

    def test_update_None_id_and_other_attr(self):
        """Tests update method with None id and more args"""

        square = Square(10, 10, 10, 10)
        square.update(None, 2, 3, 4)

        self.assertEqual(str(square), "[Square] (1) 3/4 - 2")

    def test_update_id(self):
        """Tests updating id"""

        square = Square(10, 10, 10, 10)
        square.update(89)
        self.assertEqual(str(square), "[Square] (89) 10/10 - 10")

    def test_update_size(self):
        """Tests updating width"""

        square = Square(10, 10, 10, 10)
        square.update(89, 2)
        self.assertEqual(str(square), "[Square] (89) 10/10 - 2")

    def test_update_x(self):
        """Tests updating x"""

        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3)
        self.assertEqual(str(square), "[Square] (89) 3/10 - 2")

    def test_update_y(self):
        """Tests updating y"""

        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (89) 3/4 - 2")

    def test_update_excess_args(self):
        """Tests updating y"""

        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3, 4, 5)
        self.assertEqual(str(square), "[Square] (89) 3/4 - 2")

    def test_update_width_getter(self):
        """Tests if the width is updated"""

        square = Square(10, 10, 10, 10)
        square.update(89, 2)
        self.assertEqual(2, square.width)

    def test_update_height_getter(self):
        """Testing if the height is updated"""
        square = Square(10, 10, 10, 10)
        square.update(89, 2)
        self.assertEqual(2, square.height)

    def test_update_twice(self):
        """Tests updating y"""

        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3, 4)
        square.update(79, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (79) 3/4 - 2")

    def test_update_all_attributes(self):
        """Tests updating all attributes"""

        square = Square(1, 2, 3, 4)
        square.update(10, 20, 30, 40)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 40)

    def test_update_with_fewer_arguments(self):
        """Tests updating fewer attributes
        and checks if the rest is unchanged"""

        square = Square(1, 2, 3, 4)
        square.update(10, 20)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_invalid_size_type(self):
        """Tests updating size with a value that isn't an int"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(89, "2")

    def test_update_zero_size(self):
        """Tests updating size with 0"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(89, 0)

    def test_update_negative_size(self):
        """Tests updating size with a negative value"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(89, -2)

    def test_update_invalid_x_type(self):
        """Tests updating x with a value that isn't an int"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(89, 2, "4")

    def test_update_negative_x(self):
        """Tests updating x with a negative value"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(89, 2, -4)

    def test_update_invalid_y_type(self):
        """Tests updating y with a value that isn't an int"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(89, 2, 3, "5")

    def test_update_negative_y(self):
        """Tests updating y with a negative value"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(89, 2, 3, -5)

    def test_update_size_then_x(self):
        """Tests width first"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(89, "2", "4")

    def test_update_size_then_y(self):
        """Tests width first"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(89, "2", 3, "5")

    def test_update_x_then_y(self):
        """Tests x first"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(89, 2, "4", "5")

    def test_update_id_kwargs(self):
        """Tests updating id"""

        square = Square(10, 10, 10, 10)
        square.update(id=89)
        self.assertEqual(str(square), "[Square] (89) 10/10 - 10")

    def test_update_size_id_kwargs(self):
        """Tests updating size and id"""

        square = Square(10, 10, 10, 10)
        square.update(id=89, size=2)
        self.assertEqual(str(square), "[Square] (89) 10/10 - 2")

    def test_update_size_id_kwargs(self):
        """Tests updating size and id"""

        square = Square(10, 10, 10, 10)
        square.update(id=89, size=2, x=3)
        self.assertEqual(str(square), "[Square] (89) 3/10 - 2")

    def test_update_x_size_id_kwargs(self):
        """Tests updating x, size and id"""

        square = Square(10, 10, 10, 10)
        square.update(id=89, size=2, x=3, y=4)
        self.assertEqual(str(square), "[Square] (89) 3/4 - 2")

    def test_update_y_x_size_id_kwargs(self):
        """Tests updating y, x, size and id"""

        square = Square(10, 10, 10, 10)
        square.update(id=89, size=3, x=4, y=5)
        self.assertEqual(str(square), "[Square] (89) 4/5 - 3")

    def test_update_width_getter_kwargs(self):
        """Tests if the width is updated"""

        square = Square(10, 10, 10, 10)
        square.update(id=89, size=8)
        self.assertEqual(8, square.width)

    def test_update_height_getter_kwargs(self):
        """Tests if the height is updated"""
        square = Square(10, 10, 10, 10)
        square.update(id=89, size=9)
        self.assertEqual(9, square.height)

    def test_update_None_id_kwargs(self):
        """Tests update method with None id"""

        square = Square(10, 10, 10, 10)
        square.update(id=None)
        self.assertEqual(str(square), "[Square] (1) 10/10 - 10")

    def test_update_None_id_and_others_kwargs(self):
        """Tests update method with None id and other attributes"""

        square = Square(10, 10, 10, 10)
        square.update(id=None, size=3, x=4)
        self.assertEqual(str(square), "[Square] (1) 4/10 - 3")

    def test_update_twice_kwargs(self):
        """Tests updating y"""

        square = Square(10, 10, 10, 10)
        square.update(id=89, size=3, x=4, y=5)
        square.update(id=79, size=3, x=4, y=5)
        self.assertEqual(str(square), "[Square] (79) 4/5 - 3")

    def test_update_all_attributes_kwargs(self):
        """Tests updating all attributes"""

        square = Square(1, 2, 3, 4)
        square.update(id=10, size=30, x=40, y=50)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 30)
        self.assertEqual(square.x, 40)
        self.assertEqual(square.y, 50)

    def test_update_with_fewer_arguments_kwargs(self):
        """Tests updating fewer attributes
        and checks if the rest is unchanged"""

        square = Square(1, 2, 3, 4)
        square.update(id=10, size=20)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_invalid_size_type_kwargs(self):
        """Tests updating size with a value that isn't an int"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size="2")

    def test_update_zero_size_kwargs(self):
        """Tests updating size with 0"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=0)

    def test_update_negative_size_kwargs(self):
        """Tests updating size with a negative value"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=-2)

    def test_update_invalid_x_type_kwargs(self):
        """Tests updating x with a value that isn't an int"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(x="4")

    def test_update_negative_x_kwargs(self):
        """Tests updating x with a negative value"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(x=-4)

    def test_update_invalid_y_type_kwargs(self):
        """Tests updating y with a value that isn't an int"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(y="5")

    def test_update_negative_y_kwargs(self):
        """Tests updating y with a negative value"""

        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(y=-5)

    def test_update_args_kwargs(self):
        """Tests using both args and kwargs"""

        square = Square(10, 10, 10, 10)
        square.update(98, 2, x=4, y=5)
        self.assertEqual(str(square), "[Square] (98) 10/10 - 2")

    def test_update_kwargs_invalid_attr_names(self):
        """Tests passing all arguments as wrong attribute names"""

        square = Square(10, 10, 10, 10)
        square.update(w=4, z=5)
        self.assertEqual(str(square), "[Square] (10) 10/10 - 10")

    def test_update_kwargs_some_invalid_attr_names(self):
        """Tests passing some wrong attribute names as arguments"""

        square = Square(10, 10, 10, 10)
        square.update(size=3, x=4, w=4, z=5, id=98)
        self.assertEqual(str(square), "[Square] (98) 4/10 - 3")


class TestSquareToDictionary(unittest.TestCase):
    """Tests the to_dictionary() method"""

    def setUp(self):
        """
        Save sys.stdout in an attribute to restore it later
        and redirect sys.stdout to capture print output
        """

        Base._Base__nb_objects = 0

    def test_to_dictionary_usage(self):
        """Tests using to_dictionary()"""

        sq_dict = Square(10, 2, 1).to_dictionary()
        expected_output = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(sq_dict, expected_output)

    def test_updating_with_dictionary(self):
        """Tests updating attributes with a dictionary"""

        square1 = Square(10, 2, 1)
        square2 = Square(1, 1)
        sq1_dict = square1.to_dictionary()
        square2.update(**sq1_dict)
        self.assertTrue(isinstance(sq1_dict, dict))
        self.assertEqual(str(square2), "[Square] (1) 2/1 - 10")
        self.assertIsNot(square1, square2)

    def test_to_dictionary_with_arg(self):
        """Testing passing an argument to to_dictionary()"""

        square = Square(10, 2, 1)
        with self.assertRaises(TypeError):
            square.to_dictionary(5)


if __name__ == '__main__':
    unittest.main()
