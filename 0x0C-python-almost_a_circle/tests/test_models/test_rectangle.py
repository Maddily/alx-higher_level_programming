#!/usr/bin/python3
"""
Module Name: test_rectangle

Description: This module is for testing Rectangle class.

Classes:
- TestRectangleInstantiation
- TestRectangleGettersSetters
- TestRectangleWidth
- TestRectangleHeight
- TestRectangleX
- TestRectangleY
- TestRectangleInitializationOrder
- TestRectangleArea
- TestRectangleDisplay
- TestRectangleStr
- TestRectangleUpdate
- TestRectangleToDictionary
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangleInstantiation(unittest.TestCase):
    """
    Tests Rectangle instantiation.
    """

    def test_instance_of_base(self):
        """Tests if a rectangle object is an instance of `Base`"""

        self.assertIsInstance(Rectangle(8, 4), Base)

    def test_no_arguments(self):
        """Tests if an exception is raised when no arguments
        are passed to Rectangle during instantiation"""

        with self.assertRaises(TypeError):
            Rectangle()

    def test_single_argument(self):
        """Tests if an exception is raised when only
         a single argument is passed to Rectangle
         during instantiation"""

        with self.assertRaises(TypeError):
            Rectangle(8)

    def test_id_assignment_with_two_args(self):
        """Tests if ids are correctly assigned"""

        rectangle1 = Rectangle(8, 4)
        rectangle2 = Rectangle(6, 3)
        self.assertEqual(rectangle1.id, rectangle2.id - 1)

    def test_id_assignment_with_three_args(self):
        """Tests if ids are correctly assigned"""

        rectangle1 = Rectangle(8, 4, 2)
        rectangle2 = Rectangle(6, 3, 1)
        self.assertEqual(rectangle1.id, rectangle2.id - 1)

    def test_id_assignment_with_four_args(self):
        """Tests if ids are correctly assigned"""

        rectangle1 = Rectangle(8, 4, 2, 6)
        rectangle2 = Rectangle(6, 3, 1, 5)
        self.assertEqual(rectangle1.id, rectangle2.id - 1)

    def test_excess_arguments(self):
        """Tests if an exception is raised when
        excess arguments are passed"""

        with self.assertRaises(TypeError):
            Rectangle(8, 4, 2, 6, 14, 28)

    def test_default_x(self):
        """Tests if x is set properly"""

        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.x, 0)

    def test_default_y(self):
        """Tests if y is set properly"""

        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.y, 0)

    def test_default_id(self):
        """Tests if id is not None when not passed"""

        rectangle = Rectangle(5, 10)
        self.assertIsNotNone(rectangle.id)


class TestRectangleGettersSetters(unittest.TestCase):
    """Tests getters and setters"""

    def test_width_getter(self):
        """Tests if `width` is retrieved correctly"""

        rectangle = Rectangle(8, 4, 2, 6)
        self.assertEqual(rectangle.width, 8)

    def test_height_getter(self):
        """Tests if `height` is retrieved correctly"""

        rectangle = Rectangle(8, 4, 2, 6)
        self.assertEqual(rectangle.height, 4)

    def test_x_getter(self):
        """Tests if `x` is retrieved correctly"""

        rectangle = Rectangle(8, 4, 2, 6)
        self.assertEqual(rectangle.x, 2)

    def test_y_getter(self):
        """Tests if `y` is retrieved correctly"""

        rectangle = Rectangle(8, 4, 2, 6)
        self.assertEqual(rectangle.y, 6)

    def test_width_setter(self):
        """Tests if `width` is set correctly"""

        rectangle = Rectangle(8, 4, 2, 6)
        rectangle.width = 12
        self.assertEqual(rectangle.width, 12)

    def test_height_setter(self):
        """Tests if `height` is set correctly"""

        rectangle = Rectangle(8, 4, 2, 6)
        rectangle.height = 8
        self.assertEqual(rectangle.height, 8)

    def test_x_setter(self):
        """Tests if `x` is set correctly"""

        rectangle = Rectangle(8, 4, 2, 6)
        rectangle.x = 4
        self.assertEqual(rectangle.x, 4)

    def test_y_setter(self):
        """Tests if `y` is set correctly"""

        rectangle = Rectangle(8, 4, 2, 6)
        rectangle.y = 9
        self.assertEqual(rectangle.y, 9)

    def test_getter_with_private_width(self):
        """Tests if an exception is raised when
        width is accessed as private"""

        with self.assertRaises(AttributeError):
            print(Rectangle(8, 4).__width)

    def test_getter_with_private_height(self):
        """Tests if an exception is raised when
        height is accessed as private"""

        with self.assertRaises(AttributeError):
            print(Rectangle(8, 4).__height)

    def test_getter_with_private_x(self):
        """Tests if an exception is raised when
        x is accessed as private"""

        with self.assertRaises(AttributeError):
            print(Rectangle(8, 4).__x)

    def test_getter_with_private_y(self):
        """Tests if an exception is raised when
        y is accessed as private"""

        with self.assertRaises(AttributeError):
            print(Rectangle(8, 4).__y)


class TestRectangleWidth(unittest.TestCase):
    """Tests width validity"""

    def test_input_width_float(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(8.2, 4, 2, 6)

    def test_input_width_none(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4, 2, 6)

    def test_input_width_str(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("8.2", 4, 2, 6)

    def test_input_width_complex(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(8), 4, 2, 6)

    def test_input_width_dict(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"One": 1}, 4, 2, 6)

    def test_input_width_bool(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 4, 2, 6)

    def test_input_width_list(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 4, 2, 6)

    def test_input_width_set(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 4, 2, 6)

    def test_input_width_tuple(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 4, 2, 6)

    def test_input_width_frozenset(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 4, 2, 6)

    def test_input_width_range(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(8), 4, 2, 6)

    def test_input_width_bytes(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b"One", 4, 2, 6)

    def test_input_width_bytearray(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b"One"), 4, 2, 6)

    def test_input_width_memoryview(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b"One"), 4, 2, 6)

    def test_input_width_inf(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("inf"), 4, 2, 6)

    def test_input_width_nan(self):
        """Tests if an exception is raised
        when input width is not an integer"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("nan"), 4, 2, 6)

    def test_invalid_width_type_setter(self):
        """Tests input width in setter"""

        rectangle = Rectangle(8, 4, 2, 6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.width = 8.2

    def test_width_negative(self):
        """Tests if an exception is raised if
        width is less than 0"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-8, 4, 2, 6)

    def test_width_zero(self):
        """Tests if an exception is raised if
        width is equal to 0"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4, 2, 6)

    def test_width_negative_setter(self):
        """Tests if an exception is raised if
        width is less than 0"""

        rectangle = Rectangle(8, 4, 2, 6)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.width = -8

    def test_width_zero_setter(self):
        """Tests if an exception is raised if
        width is equal to 0"""

        rectangle = Rectangle(8, 4, 2, 6)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.width = 0


class TestRectangleHeight(unittest.TestCase):
    """Tests height validity"""

    def test_input_height_float(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, 4.2, 2, 6)

    def test_input_height_none(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, None, 2, 6)

    def test_input_height_str(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, "4", 2, 6)

    def test_input_height_complex(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, complex(4), 2, 6)

    def test_input_height_dict(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, {"One": 1}, 2, 6)

    def test_input_height_bool(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, True, 2, 6)

    def test_input_height_list(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, [1, 2, 3], 2, 6)

    def test_input_height_set(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, {1, 2, 3}, 2, 6)

    def test_input_height_tuple(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, (1, 2), 2, 6)

    def test_input_height_frozenset(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, frozenset({1, 2, 3}), 2, 6)

    def test_input_height_range(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, range(8), 2, 6)

    def test_input_height_bytes(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, b"One", 2, 6)

    def test_input_height_bytearray(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, bytearray(b"One"), 2, 6)

    def test_input_height_memoryview(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, memoryview(b"One"), 2, 6)

    def test_input_height_inf(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, float("inf"), 2, 6)

    def test_input_height_nan(self):
        """Tests if an exception is raised
        when input height is not an integer"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, float("nan"), 2, 6)

    def test_invalid_height_type_setter(self):
        """Tests input height in setter"""

        rectangle = Rectangle(8, 4, 2, 6)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.height = 8.2

    def test_height_negative(self):
        """Tests if an exception is raised if
        height is less than 0"""

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle = Rectangle(8, -4, 2, 6)

    def test_height_zero(self):
        """Tests if an exception is raised if
        height is equal to 0"""

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle = Rectangle(8, 0, 2, 6)

    def test_height_negative_setter(self):
        """Tests if an exception is raised if
        height is less than 0"""

        rectangle = Rectangle(8, 4, 2, 6)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.height = -8

    def test_height_zero_setter(self):
        """Tests if an exception is raised if
        height is equal to 0"""

        rectangle = Rectangle(8, 4, 2, 6)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.height = 0


class TestRectangleX(unittest.TestCase):
    """Tests x validity"""

    def test_input_x_float(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, 2.2, 6)

    def test_input_x_none(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, None, 6)

    def test_input_x_str(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, "2", 6)

    def test_input_x_complex(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, complex(2), 6)

    def test_input_x_dict(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, {"One": 1}, 6)

    def test_input_x_bool(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, False, 6)

    def test_input_x_list(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, [1, 2, 3], 6)

    def test_input_x_set(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, {1, 2, 3}, 6)

    def test_input_x_tuple(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, (1, 2), 6)

    def test_input_x_frozenset(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, frozenset({1, 2, 3}), 6)

    def test_input_x_range(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, range(8), 6)

    def test_input_x_bytes(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, b"One", 6)

    def test_input_x_bytearray(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, bytearray(b"One"), 6)

    def test_input_x_memoryview(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, memoryview(b"One"), 6)

    def test_input_x_inf(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, float("inf"), 6)

    def test_input_x_nan(self):
        """Tests if an exception is raised
        when input x is not an integer"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, float("nan"), 6)

    def test_invalid_x_type_setter(self):
        """Tests input x in setter"""

        rectangle = Rectangle(8, 4, 2, 6)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.x = 8.2

    def test_x_negative(self):
        """Tests if an exception is raised if
        x is less than 0"""

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(8, 4, -2, 6)

    def test_x_negative_setter(self):
        """Tests if an exception is raised if
        x is less than 0"""

        rectangle = Rectangle(8, 4, 2, 6)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rectangle.x = -8


class TestRectangleY(unittest.TestCase):
    """Tests y validity"""

    def test_input_y_float(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, 6.2)

    def test_input_y_none(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, None)

    def test_input_y_str(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, "6")

    def test_input_y_complex(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, complex(6))

    def test_input_y_dict(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, {"One": 1})

    def test_input_y_bool(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, True)

    def test_input_y_list(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, [1, 2, 3])

    def test_input_y_set(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, {1, 2, 3})

    def test_input_y_tuple(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, (1, 2))

    def test_input_y_frozenset(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, frozenset({1, 2, 3}))

    def test_input_y_range(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, range(8))

    def test_input_y_bytes(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, b"One")

    def test_input_y_bytearray(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, bytearray(b"One"))

    def test_input_y_memoryview(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, memoryview(b"One"))

    def test_input_y_inf(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, float("inf"))

    def test_input_y_nan(self):
        """Tests if an exception is raised
        when input y is not an integer"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 4, 2, float("nan"))

    def test_invalid_y_type_setter(self):
        """Tests input y in setter"""

        rectangle = Rectangle(8, 4, 2, 6)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle.y = 8.2

    def test_y_negative(self):
        """Tests if an exception is raised if
        y is less than 0"""

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(8, 4, 2, -6)

    def test_y_negative_setter(self):
        """Tests if an exception is raised if
        y is less than 0"""

        rectangle = Rectangle(8, 4, 2, 6)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rectangle.y = -8


class TestRectangleInitializationOrder(unittest.TestCase):
    """Tests the order of exception raising when
    initializing attributes with invalid values"""

    def test_width_then_height(self):
        """Tests width first"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(8.2, 4.2)

    def test_width_then_x(self):
        """Tests width first"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(8.2, 4, 2.2)

    def test_width_then_y(self):
        """Tests width first"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(8.2, 4, 2, 6.2)

    def test_height_then_x(self):
        """Tests height first"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, 4.2, 2.2)

    def test_height_then_y(self):
        """Tests height first"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, 4.2, 2, 6.2)

    def test_x_then_y(self):
        """Tests x first"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 4, 2.2, 6.2)


class TestRectangleArea(unittest.TestCase):
    """Tests a rectangle object's area"""

    def test_area_regular_numbers(self):
        """Tests if the `area` method works properly
        with regular numbers"""

        rectangle = Rectangle(4, 12, 2, 6)
        self.assertEqual(rectangle.area(), 48)

    def test_area_large_numbers(self):
        """Tests if the `area` method works properly
        with large numbers"""

        rectangle = Rectangle(999999999999999, 999999999999999999, 2, 6)
        self.assertEqual(rectangle.area(), 999999999999998999000000000000001)

    def test_area_after_update(self):
        """Tests if the `area` method works properly
        after updating width and height"""

        rectangle = Rectangle(4, 12, 2, 6)
        rectangle.width = 3
        rectangle.height = 6
        self.assertEqual(rectangle.area(), 18)

    def test_area_with_arg(self):
        """Tests if an exception is raised when an argument
        is passed to `area`"""

        rectangle = Rectangle(4, 12, 2, 6)
        with self.assertRaises(TypeError):
            rectangle.area(8)


class TestRectangleDisplay(unittest.TestCase):
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
        """Tests display with a small rectangle"""

        rectangle = Rectangle(3, 2)
        rectangle.display()
        self.assertEqual(sys.stdout.getvalue(), "###\n###\n")

    def test_display_large_rectangle(self):
        """Tests display with a larger rectangle"""

        rectangle = Rectangle(5, 4)
        rectangle.display()
        self.assertEqual(sys.stdout.getvalue(), "#####\n#####\n#####\n#####\n")

    def test_display_rectangle_single_character(self):
        """Tests display with a rectangle of width and height 1"""

        rectangle = Rectangle(1, 1)
        rectangle.display()
        self.assertEqual(sys.stdout.getvalue(), "#\n")

    def test_display_with_x_and_y(self):
        """Tests display with given x and y"""

        rectangle = Rectangle(3, 2, 1, 1)
        expected_output = "\n ###\n ###\n"
        rectangle.display()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_display_with_x(self):
        """Tests display with given x"""

        rectangle = Rectangle(3, 2, 1)
        expected_output = " ###\n ###\n"
        rectangle.display()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_display_with_y(self):
        """Tests display with given y"""

        rectangle = Rectangle(3, 2, 0, 1)
        expected_output = "\n###\n###\n"
        rectangle.display()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_display_with_arg(self):
        """Tests the display method when passed an argument"""

        rectangle = Rectangle(8, 4, 2, 6)
        with self.assertRaises(TypeError):
            rectangle.display(1)


class TestRectangleStr(unittest.TestCase):
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

        rectangle = Rectangle(4, 5, 2, 1, 1)
        expected_output = "[Rectangle] (1) 2/1 - 4/5"
        self.assertEqual(str(rectangle), expected_output)

    def test_default_values(self):
        """Tests str() with default values"""

        rectangle = Rectangle(4, 5)
        expected_output = "[Rectangle] (1) 0/0 - 4/5"
        self.assertEqual(str(rectangle), expected_output)

    def test_default_values_and_x(self):
        """Tests str() with default values and given x"""

        rectangle = Rectangle(4, 5, 1)
        expected_output = "[Rectangle] (1) 1/0 - 4/5"
        self.assertEqual(str(rectangle), expected_output)

    def test_large_values(self):
        """Tests str() with large values"""

        rectangle = Rectangle(10000, 20000, 30000, 40000, 42)
        expected_output = "[Rectangle] (42) 30000/40000 - 10000/20000"
        self.assertEqual(str(rectangle), expected_output)

    def test_none_id(self):
        """Tests str() without passing id"""

        rectangle = Rectangle(5, 6, 7, 8)
        expected_output = "[Rectangle] (1) 7/8 - 5/6"
        self.assertEqual(str(rectangle), expected_output)

    def test_multiple_instances(self):
        """Tests str() with multiple objects"""

        rectangle1 = Rectangle(1, 2, 3, 4, 5)
        rectangle2 = Rectangle(6, 7, 8, 9, 10)
        rectangle3 = Rectangle(11, 12, 13, 14, 15)
        expected_output = (
            "[Rectangle] (5) 3/4 - 1/2"
            "[Rectangle] (10) 8/9 - 6/7"
            "[Rectangle] (15) 13/14 - 11/12"
            )
        self.assertEqual(str(rectangle1) + str(rectangle2)
                         + str(rectangle3), expected_output)

    def test_updated_attributes(self):
        """Tests str() after setting attributes"""

        rectangle = Rectangle(11, 12, 0, 0, 9)
        rectangle.width = 13
        rectangle.height = 7
        rectangle.x = 5
        rectangle.y = 3
        self.assertEqual("[Rectangle] (9) 5/3 - 13/7", str(rectangle))

    def test_one_arg(self):
        """Tests str() with one argument"""

        rectangle = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rectangle.__str__(3)


class TestRectangleUpdate(unittest.TestCase):
    """Tests the update method"""

    def setUp(self):
        """
        Save sys.stdout in an attribute to restore it later
        and redirect sys.stdout to capture print output
        """

        Base._Base__nb_objects = 0

    def test_update_no_args(self):
        """Tests update method without arguments"""

        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update()
        self.assertEqual(str(rectangle), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_None_id(self):
        """Tests update method with None id"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(None)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_None_id_and_other_attr(self):
        """Tests update method with None id and more args"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(None, 2, 3, 4)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 4/10 - 2/3")

    def test_update_id(self):
        """Tests updating id"""

        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_width(self):
        """Tests updating width"""

        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89, 2)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_height(self):
        """Tests updating height"""

        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89, 2, 3)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_x(self):
        """Tests updating x"""

        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89, 2, 3, 4)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_y(self):
        """Tests updating y"""

        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_excess_args(self):
        """Tests updating y"""

        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_twice(self):
        """Tests updating y"""

        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89, 2, 3, 4, 5)
        rectangle.update(79, 2, 3, 4, 5)
        self.assertEqual(str(rectangle), "[Rectangle] (79) 4/5 - 2/3")

    def test_update_all_attributes(self):
        """Tests updating all attributes"""

        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(10, 20, 30, 40, 50)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 20)
        self.assertEqual(rectangle.height, 30)
        self.assertEqual(rectangle.x, 40)
        self.assertEqual(rectangle.y, 50)

    def test_update_with_fewer_arguments(self):
        """Tests updating fewer attributes
        and checks if the rest is unchanged"""

        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(10, 20)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 20)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_update_invalid_width_type(self):
        """Tests updating width with a value that isn't an int"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(89, "2")

    def test_update_zero_width(self):
        """Tests updating width with 0"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.update(89, 0)

    def test_update_negative_width(self):
        """Tests updating width with a negative value"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.update(89, -2)

    def test_update_invalid_height_type(self):
        """Tests updating height with a value that isn't an int"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(89, 2, "3")

    def test_update_zero_height(self):
        """Tests updating height with 0"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.update(89, 2, 0)

    def test_update_negative_height(self):
        """Tests updating height with a negative value"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.update(89, 2, -3)

    def test_update_invalid_x_type(self):
        """Tests updating x with a value that isn't an int"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.update(89, 2, 3, "4")

    def test_update_negative_x(self):
        """Tests updating x with a negative value"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rectangle.update(89, 2, 3, -4)

    def test_update_invalid_y_type(self):
        """Tests updating y with a value that isn't an int"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle.update(89, 2, 3, 4, "5")

    def test_update_negative_y(self):
        """Tests updating y with a negative value"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rectangle.update(89, 2, 3, 4, -5)

    def test_update_width_then_height(self):
        """Tests width first"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(89, "2", "3")

    def test_update_width_then_x(self):
        """Tests width first"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(89, "2", 3, "4")

    def test_update_width_then_y(self):
        """Tests width first"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(89, "2", 3, 4, "5")

    def test_update_height_then_x(self):
        """Tests height first"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(89, 2, "3", "4")

    def test_update_height_then_y(self):
        """Tests height first"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(89, 2, "3", 4, "5")

    def test_update_x_then_y(self):
        """Tests x first"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.update(89, 2, 3, "4", "5")

    def test_update_id_kwargs(self):
        """Tests updating id"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=89)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_width_id_kwargs(self):
        """Tests updating width and id"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=89, width=2)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_width_height_id_kwargs(self):
        """Tests updating width, height and id"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=89, width=2, height=3)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_x_width_height_id_kwargs(self):
        """Tests updating x, width, height and id"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=89, width=2, height=3, x=4)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_y_x_width_height_id_kwargs(self):
        """Tests updating y, x, width, height and id"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_None_id_kwargs(self):
        """Tests update method with None id"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=None)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_None_id_and_others_kwargs(self):
        """Tests update method with None id and other attributes"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=None, width=2, height=3, x=4)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 4/10 - 2/3")

    def test_update_twice_kwargs(self):
        """Tests updating y"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=89, width=2, height=3, x=4, y=5)
        rectangle.update(id=79, width=2, height=3, x=4, y=5)
        self.assertEqual(str(rectangle), "[Rectangle] (79) 4/5 - 2/3")

    def test_update_all_attributes_kwargs(self):
        """Tests updating all attributes"""

        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(id=10, width=20, height=30, x=40, y=50)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 20)
        self.assertEqual(rectangle.height, 30)
        self.assertEqual(rectangle.x, 40)
        self.assertEqual(rectangle.y, 50)

    def test_update_with_fewer_arguments_kwargs(self):
        """Tests updating fewer attributes
        and checks if the rest is unchanged"""

        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(id=10, width=20)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 20)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_update_invalid_width_type_kwargs(self):
        """Tests updating width with a value that isn't an int"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(width="2")

    def test_update_zero_width_kwargs(self):
        """Tests updating width with 0"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.update(width=0)

    def test_update_negative_width_kwargs(self):
        """Tests updating width with a negative value"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.update(width=-2)

    def test_update_invalid_height_type_kwargs(self):
        """Tests updating height with a value that isn't an int"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(height="3")

    def test_update_zero_height_kwargs(self):
        """Tests updating height with 0"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.update(height=0)

    def test_update_negative_height_kwargs(self):
        """Tests updating height with a negative value"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.update(height=-3)

    def test_update_invalid_x_type_kwargs(self):
        """Tests updating x with a value that isn't an int"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.update(x="4")

    def test_update_negative_x_kwargs(self):
        """Tests updating x with a negative value"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rectangle.update(x=-4)

    def test_update_invalid_y_type_kwargs(self):
        """Tests updating y with a value that isn't an int"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle.update(y="5")

    def test_update_negative_y_kwargs(self):
        """Tests updating y with a negative value"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rectangle.update(y=-5)

    def test_update_args_kwargs(self):
        """Tests using both args and kwargs"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(98, 2, 3, x=4, y=5)
        self.assertEqual(str(rectangle), "[Rectangle] (98) 10/10 - 2/3")

    def test_update_kwargs_invalid_attr_names(self):
        """Tests passing all arguments as wrong attribute names"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(w=4, z=5)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_kwargs_some_invalid_attr_names(self):
        """Tests passing some wrong attribute names as arguments"""

        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(height=3, x=4, w=4, z=5, id=98, width=2)
        self.assertEqual(str(rectangle), "[Rectangle] (98) 4/10 - 2/3")


class TestRectangleToDictionary(unittest.TestCase):
    """Tests the to_dictionary() method"""

    def setUp(self):
        """
        Save sys.stdout in an attribute to restore it later
        and redirect sys.stdout to capture print output
        """

        Base._Base__nb_objects = 0

    def test_to_dictionary_usage(self):
        """Tests using to_dictionary()"""

        rect_dict = Rectangle(10, 2, 1, 9).to_dictionary()
        expected_output = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(rect_dict, expected_output)

    def test_updating_with_dictionary(self):
        """Tests updating attributes with a dictionary"""

        rectangle1 = Rectangle(10, 2, 1, 9)
        rectangle2 = Rectangle(1, 1)
        rect1_dict = rectangle1.to_dictionary()
        rectangle2.update(**rect1_dict)
        self.assertTrue(isinstance(rect1_dict, dict))
        self.assertEqual(str(rectangle2), "[Rectangle] (1) 1/9 - 10/2")
        self.assertIsNot(rectangle1, rectangle2)

    def test_to_dictionary_with_arg(self):
        """Testing passing an argument to to_dictionary()"""

        rectangle = Rectangle(10, 2, 1, 9)
        with self.assertRaises(TypeError):
            rectangle.to_dictionary(5)


if __name__ == '__main__':
    unittest.main()
