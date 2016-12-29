"""
Your task is to return the sum of Triangular Numbers up-to-and-including the `nth` Triangular Number.

Triangular Number: "any of the series of numbers (1, 3, 6, 10, 15, etc.) obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc."

```
[01]
02 [03]
04 05 [06]
07 08 09 [10]
11 12 13 14 [15]
16 17 18 19 20 [21]
```

e.g. If `4` is given: `1 + 3 + 6 + 10 = 20`.

Triangular Numbers cannot be negative so return 0 if a negative number is given.
"""

def sum_triangular_numbers(n):
    if n < 0:
        return 0

    sum = sum_triangular_numbers(n-1)
    return sum + (n * (n + 1)) / 2
