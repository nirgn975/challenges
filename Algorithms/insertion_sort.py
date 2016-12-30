import unittest


def insertion_sort(array):
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        print(array)

    return array


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(insertion_sort([5, 4, 3, 7, 2, 1, 10, 9, 6, 8]),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()