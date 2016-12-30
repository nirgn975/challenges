import unittest


def selection_sort(array):
    for i in range(len(array)):
        print(array)
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array


def selection_sort2(array):
    for i in range(len(array)):
        min_value = min(array[i:])
        min_index = array[i:].index(min_value)
        array[i + min_index], array[i] = array[i], min_value

    return array


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(selection_sort([5, 4, 3, 7, 2, 1, 10, 9, 6, 8]),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(selection_sort2([5, 4, 3, 7, 2, 1, 10, 9, 6, 8]),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()