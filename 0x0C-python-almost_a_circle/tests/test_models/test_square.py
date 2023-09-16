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


if __name__ == "__main__":
    unittest.main()
