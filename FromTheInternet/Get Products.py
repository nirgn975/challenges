import unittest

"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:
```
[1, 7, 3, 4]
```

your function would return:
```
[84, 12, 28, 21]
```

by calculating:
```
[7*3*4, 1*3*4, 1*7*4, 1*7*3]
```

**Do not use division in your solution.**
"""


def get_products_of_all_ints_except_at_index(products_list):
    results_list = []

    for value in products_list:
        current_product = 1
        for item in products_list:
            if not value == item:
                current_product *= item
        results_list.append(current_product)

    return results_list


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(get_products_of_all_ints_except_at_index([1, 7, 3, 4]), [84, 12, 28, 21])


if __name__ == '__main__':
    unittest.main()
