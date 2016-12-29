import unittest

"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
"""

n = 7
k = 3
arr = [1, 2, 3, 4, 5, 6, 7]


def rotate(k, original_array):
    return original_array[k + 1:] + original_array[:k + 1]


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(rotate(k, arr), [5, 6, 7, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
