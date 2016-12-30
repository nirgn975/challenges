import unittest


def merge_sort(array):
    if len(array) < 2:
        return array

    pivot = round(len(array)/2)
    left = array[:pivot]
    right = array[pivot:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []

    while left and right:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    print(result + left + right)
    return result + left + right


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(merge_sort([5, 4, 3, 7, 2, 1, 10, 9, 6, 8]),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()