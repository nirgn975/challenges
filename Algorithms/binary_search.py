import unittest
import math


def binary_search(array, start, finish, to_find):
    print(array, start, finish)
    if start > finish:
        return "Not Found"

    middle = math.floor((start+finish)/2)
    if array[middle] > to_find:
        return binary_search(array, start, middle - 1, to_find)
    elif array[middle] < to_find:
        return binary_search(array, middle + 1, finish, to_find)
    else:
        return middle


class TestList(unittest.TestCase):
    def test_right(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(binary_search(array, 0, len(array), 4), 3)


if __name__ == '__main__':
    unittest.main()
