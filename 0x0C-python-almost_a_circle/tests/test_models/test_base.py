import json
import unittest
import os
from unittest.mock import patch, mock_open
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    This class tests the Base class file.
    """

    def test_id_assigned_when_id_provided(self):
        """
        This function tests whether or not an 'id'
        has been provided as inputi to the Base constructor.
        """
        base = Base(id=100)
        self.assertEqual(base.id, 100)

    def test_id_increment_when_id_not_provided(self):
        """
        This fucntion tests that theres an 'id' input present and if there
        isn't, the id attribute of each instance is incremented from the
        previous instance.
        """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_id_type(self):
        """
        This function tests the type of date being input as 'id'.
        Making sure it's an integer.

        *requirement says do not need to test ofor type*
        """
        base = Base(id=100)
        self.assertIsInstance(base.id, int)

    def test_private_attribute_not_accessible(self):
        """
        This function tests to ensure that the private attribute
        __nb_objects is not accessible from the instance of Base class.
        """
        base = Base(id=100)
        with self.assertRaises(AttributeError):
            base.__nb_objects

    def test_to_json_string_with_list(self):
        """
        This tests if a list of dictionaries was created.
        """
        list_dictionaries = [
                {"name": "John", "age": 30},
                {"name": "Jane", "age": 28}
        ]

        json_string = Base.to_json_string(list_dictionaries)

        expected_json_string = ('[{"name": "John", "age": 30}, '
                                '{"name": "Jane", "age": 28}]')
        self.assertEqual(json_string, expected_json_string)

    def test_to_json_string_with_empty_list(self):
        """
        This is to test if the list is empty.
        """
        list_dictionaries = []
        json_string = Base.to_json_string(list_dictionaries)

        expected_json_string = "[]"
        self.assertEqual(json_string, expected_json_string)

    def test_to_json_string_with_none(self):
        """
        This tests if the list is 'None'.
        """
        json_string = Base.to_json_string(None)

        expected_json_string = "[]"
        self.assertEqual(json_string, expected_json_string)

    def test_from_json_string(self):
        """
        This tests whether the list of dictionaries is empty or None.
        """
        json_string = ""
        expected_json_string = []
        self.assertEqual(
            Base.from_json_string(json_string),
            expected_json_string
        )

        json_string = None
        expected_json_string = []
        self.assertEqual(
            Base.from_json_string(json_string),
            expected_json_string
        )

    def setUp(self):
        """
        This tests whether the file names exist.
        """
        self.rectangle_filename = "Reactangle.json"
        self.square_filename = "Square.json"
        self.invalid_filename = "Invalid.json"

    def tearDown(self):
        """
        This tests whether the file pathe exists.
        """
        if os.path.exists(self.rectangle_filename):
            os.remove(self.rectangle_filename)
        if os.path.exists(self.square_filename):
            os.remove(self.square_filename)
        if os.path.exists(self.invalid_filename):
            os.remove(self.invalid_filename)

    def test_load_from_file_rectangle(self):
        """
        This tests whether the created instances have been loaded to
        the rectangle file.
        """
        rectangle = Rectangle(10, 5)
        rectangle.save_to_file([rectangle])

        instances = Rectangle.load_from_file()

        self.assertEqual(len(instances), 1)
        self.assertEqual(instances[0].__dict__, rectangle.__dict__)

    def test_load_from_file_squarre(self):
        """
        This tests if a Square instance has been created and saved
        to a file square.
        """
        square = Square(7)
        square.save_to_file([square])

        instances = Square.load_from_file()

        self.assertEqual(len(instances), 1)
        self.assertEqual(instances[0].__dict__, square.__dict__)

    def test_load_from_file_invalid(self):
        """
        This tests if the isnatnces have been properly loaded.
        """
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 0)

    """Task 16"""
    def test_save_to_file(self):
        """
        This tests if a list of objects can be saved to a file.
        """
        class MockObject:
            """
            Define mock objects
            """
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def to_dictionary(self):
                return [{"name": self.name, "age": self.age}]

        mock1 = MockObject("John", 30)
        mock2 = MockObject("Jane", 28)
        list_objs = [mock1, mock2]

        expected_json = Base.to_json_string([
            mock1.to_dictionary(),
            mock2.to_dictionary()
        ])

        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", mock_open()) as mock_file:
                with patch.object(
                        MockObject, "to_dictionary",
                        side_effect=[
                            mock1.to_dictionary(),
                            mock2.to_dictionary()
                        ]):

                    Base.save_to_file(list_objs)
                    expected_filename = "Base.json"
                    expected_mode = "w"
                    mock_file.assert_called_once_with(
                        expected_filename,
                        expected_mode
                    )
                    actual_write_call = mock_file().write.call_args[0][0]
                    self.assertEqual(actual_write_call, expected_json)


if __name__ == "__main__":
    unittest.main()
