import unittest


def bubble_sort(array):
    for i in range(len(array)):
        print(array)
        for j in range(len(array)-1, i, -1):
            if array[j] < array[j-1]:
                array[j - 1], array[j] = array[j], array[j - 1]

    return array


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(bubble_sort([5, 4, 3, 7, 2, 1, 10, 9, 6, 8]),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()