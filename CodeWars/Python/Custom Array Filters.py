"""
Dave has a lot of data he is required to apply filters to, which are simple enough, but he wants a shorter way of doing so.

He wants the following functions to work as expected:
```
even # list([1,2,3,4,5]).even() should return [2,4]
odd # list([1,2,3,4,5]).odd() should return [1,3,5]
under # list([1,2,3,4,5]).under(4) should return [1,2,3]
over # list([1,2,3,4,5]).over(4) should return [5]
in_range # list([1,2,3,4,5]).in_range(1, 3) should return [1,2,3]
```

They should also work when used together, for example:
```
list(list([1,2,3,4,5,6,7,8,9,10]).even()).under(5) # should return [2,4]
```

And finally the filters should only accept integer values from an array, for example:
```
list(["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11]).even() // should return [300, 122]
```
"""

# Built-in namespace
import __builtin__

# Extended subclass
class mylist(list):
    def even(self):
        return [i for i in self if str(i).isdigit() and i % 2 == 0]

    def odd(self):
        return [i for i in self if str(i).isdigit() and i % 2 == 1]

    def under(self, num):
        return [i for i in self if str(i).isdigit() and i < num]

    def over(self, num):
        return [i for i in self if str(i).isdigit() and i > num]

    def in_range(self, start, end):
        return [i for i in self if str(i).isdigit() and i >= start and i <= end]

# Substitute the original list with the subclass on the built-in namespace
__builtin__.list = mylist
