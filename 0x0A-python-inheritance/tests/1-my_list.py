import unittest


class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)


class TestMyList(unittest.TestCase):
    def test_print_sorted(self):
        """
        This test case will test the print_sorted method of the MyList class.

        This test checks if the print_sorted method correctly sorts and
        prints the elements of MyList instance.

        It redirects the standard output to capture the printed result
        and compares it to the expected sorted list.
        """
        my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        my_list.print_sorted()

        self.assertEqual(my_list, "[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]\n")


if __name__ == '__main__':
    unittest.main()