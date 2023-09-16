import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    This is to test the file square.py.
    """
    def test_square_creation(self):
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_square_string_representaion(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")


if __name__ == "__main__":
    unittest.main()
