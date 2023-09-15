import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    This class is to test the file Rectangle.py.
    """

    def setUp(self):
        """
        This function tests whether the instance Rectangle
        has been created.
        """
        self.rectangle = Rectangle(10, 20, 5, 5, 1)

    def test_constructor(self):
        """
        This function verifies if the attributes are correctly.
        """
        self.assertEqual(self.rectangle.width, 10)
        self.assertEqual(self.rectangle.height, 20)
        self.assertEqual(self.rectangle.x, 5)
        self.assertEqual(self.rectangle.y, 5)
        self.assertEqual(self.rectangle.id, 1)

    def test_getters_and_setters(self):
        """
        This function ensures the values are retrieved correctly.
        """
        self.assertEqual(self.rectangle.width, 10)
        self.rectangle.width = 15
        self.assertEqual(self.rectangle.width, 15)

        self.assertEqual(self.rectangle.height, 20)
        self.rectangle.height = 25
        self.assertEqual(self.rectangle.height, 25)

        self.assertEqual(self.rectangle.x, 5)
        self.rectangle.x = 10
        self.assertEqual(self.rectangle.x, 10)

        self.assertEqual(self.rectangle.y, 5)
        self.rectangle.y = 10
        self.assertEqual(self.rectangle.y, 10)

    def test_base_class_inheritance(self):
        """
        This ensures that the class correctly inherits the 'id' attribute
        from the Base class.
        """
        with self.assertRaises(AttributeError):
            print(self.rectangle.__width)
        with self.assertRaises(AttributeError):
            print(self.rectangle.__height)
        with self.assertRaises(AttributeError):
            print(self.rectangle.__x)
        with self.assertRaises(AttributeError):
            print(self.rectangle.__y)

    def test_invalid_values(self):
        """
        This tests whether the values given are invalid.
        """
        rectangle = Rectangle(5, 10, 2, 3)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_invalid_width(self):
        """
        This tests whether the width given is invalid.
        """
        with self.assertRaises(TypeError):
            Rectangle("invalid input", 10, 2, 3)

    def test_invalid_height(self):
        """
        This tests whether the height given is invalid.
        """
        with self.assertRaises(TypeError):
            Rectangle(5, "invalid input", 2, 3)

    def test_invalid_x(self):
        """
        This tests whether the x given is invalid.
        """
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid input", 3)

    def test_invalid_y(self):
        """
        This tests whether the y given is invalid.
        """
        with self.assertRaises(TypeError):
            Rectangle("5, 10, 2, invalid input")

    def test_negative_width(self):
        """
        This tests if the wisth given is negative.
        """
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 2, 3)

    def test_negative_width(self):
        """
        This tests if the width given is negative.
        """
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 2, 3)

    def test_negative_height(self):
        """
        This tests if the height given is negative.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, -10, 2, 3)

    def test_negative_x(self):
        """
        This tests if the x given is negative.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3)

    def test_negative_y(self):
        """
        This tests if the y given is negative.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3)

    def test_area(self):
        """
        This tests that area of a rectangle is calculated correctly.
        """
        self.assertEqual(self.rectangle.area(), 200)

    def test_display(self):
        """
        This will test if the rectangle will be printed and displayed
        correctly.
        """
        rectangle = Rectangle(2, 3, 4, 5)

        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        rectangle.display()
        output = sys.stdout.getvalue()
        sys.stdout = saved_stdout
        expected_output = "\n\n\n\n\n    ##\n    ##\n    ##\n"
        self.assertEqual(output, expected_output)

    def test_string_representation(self):
        """
        This tests that the representation of the rectangle is in the correct
        format.
        """
        expected_string = "[Rectangle] (1) 5/5 - 10/20"
        self.assertEqual(str(self.rectangle), expected_string)


if __name__ == "__main__":
    unittest.main()
