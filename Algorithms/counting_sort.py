import unittest


def counting_sort(array, k):
    c = [0] * k
    result = [0] * len(array)
    print('Original Array: ', array)

    for value in array:
        c[value-1] += 1

    print('-----')
    print('c after counting: ', c)
    print('-----')

    for i in range(1, k):
        c[i] += c[i-1]

    print('c after previous elements: ', c)
    print('-----')
    for i in range(len(array), 0, -1):
        value = array[i-1]
        index = c[value - 1] - 1
        result[index] = value
        print('result: ', result)

    return result


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(counting_sort([5, 4, 3, 7, 2, 1, 10, 9, 6, 8], 10),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()