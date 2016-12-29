import unittest
import os

"""
This function takes the name of a directory
and prints out the paths files within that
directory as well as any files contained in
contained directories.

This function is similar to os.walk. Please don't
use os.walk in your answer. We are interested in your
ability to work with nested structures.
"""


def print_directory_contents(sPath):
    result = []

    for item in os.listdir(sPath):
        if os.path.isdir(sPath + '/' + item):
            result += print_directory_contents(sPath + '/' + item)
        else:
            result.append(item)
    return result


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(print_directory_contents('/home/nirgn/Downloads'),['file0.txt', 'file2.txt', 'file1.txt'])


if __name__ == '__main__':
    unittest.main()
