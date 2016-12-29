import unittest

"""
Implement a queue with 2 stacks.
Your queue should have an enqueue and a dequeue function and it should be "first in first out" (FIFO).
"""


class SelfImplementQueue:
    stack1 = []
    stack2 = []

    def __init__(self):
        pass

    def enqueue(self, item):
        """
        Adds a new item to the queue.

        :param item:
            The item to add to the queue.
        """
        self.stack1.append(item)

    def dequeue(self):
        """
        Remove an item from the queue.

        :param item:
            The item to remove from the queue.
        """
        # Move all values to stack2, in reverse order.
        for index in range(len(self.stack1)):
            value = self.stack1.pop()
            self.stack2.append(value)

        # Remove the first value from the stack.
        self.stack2.pop()

        # Return the values to stack1.
        for index in range(len(self.stack2)):
            value = self.stack2.pop()
            self.stack1.append(value)

    def __str__(self):
        return str(self.stack1)


class TestList(unittest.TestCase):
    def test_right(self):
        queue = SelfImplementQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()
        queue.enqueue(4)

        self.assertEqual(str(queue), '[2, 3, 4]')


if __name__ == '__main__':
    unittest.main()
