import unittest

"""
Given a list_of_ints, find the highest_product you can get from three of the integers.
The input list_of_ints will always have at least three integers.
"""


def highest_product(list_of_ints):
    sorted_list = sorted(list_of_ints)
    return sorted_list[-1] * sorted_list[-2] * sorted_list[-3]


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(highest_product([1, 7, 3, 4]), 84)


if __name__ == '__main__':
    unittest.main()
