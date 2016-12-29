import unittest

"""
Suppose we could access yesterday's stock prices as a list, where:

* The indices are the time in minutes past trade opening time, which was 9:30am local time.
* The values are the price in dollars of Apple stock at that time.

So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.
Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

For example:
```
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
```

No "shorting"—you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).
"""


def get_max_profit(stock_prices_yesterday):
    dict_list = []

    for index, start_value in enumerate(stock_prices_yesterday):
        temp_list = []
        for value in stock_prices_yesterday[index:]:
            temp_list.append((start_value - value) * -1)
        dict_list.append(max(temp_list))

    return max(dict_list)


class TestList(unittest.TestCase):
    def test_right(self):
        self.assertEqual(get_max_profit([10, 7, 5, 8, 11, 9]), 6)
        self.assertEqual(get_max_profit([2, 11, 5, 12, 0]), 10)
        self.assertEqual(get_max_profit([2, 11, 20, 12, 0]), 18)


if __name__ == '__main__':
    unittest.main()
