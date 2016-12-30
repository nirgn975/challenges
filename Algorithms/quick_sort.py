import unittest


def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = array.pop(0)
    left = []
    right = []

    for i in array:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    array = quick_sort(left) + [pivot] + quick_sort(right)
    print(array)
    return array


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(quick_sort([5, 4, 3, 7, 2, 1, 10, 9, 6, 8]),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()