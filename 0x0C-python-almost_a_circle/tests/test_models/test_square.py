import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    This is to test the file square.py.
    """
    def test_square_creation(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_square_string_representaion(self):
        """
        This ensure that the representation of the square
        is in the correct format.
        """
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_squarre_size_setter(self):
        """
        This ensures the size is set correctly.
        """
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_update_with_args(self):
        """
        This tests is the attributes have been asssigned
        the correct arguments.
        """
        square = Square(5)
        square.update(1, 10, 2, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_with_kwargs(self):
        """
        This tests to ensure the attributes have been assigned
        the correct key/values.
        """
        square = Square(5)
        square.update(id=1, size=10, x=1, y=3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 3)

    def test_update_with_args_and_kwargs(self):
        """
        This tests that the attributes have been asssigned the 
        correct arguments.
        """
        square = Square(5)
        square.update(id=1, size=10, y=3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 3)


if __name__ == "__main__":
    unittest.main()
