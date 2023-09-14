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


if __name__ == "__main__":
    unittest.main()
