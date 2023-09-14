import unittest
from models.base import Base


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


if __name__ == "__main__":
    unittest.main()