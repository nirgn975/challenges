"""
`late_clock` function receive an array with 4 digits and should return the latest time that can be built with those digits. The time should be in HH:MM format.

Examples:
```
[1, 9, 8, 3] => 19:38
[9, 1, 2, 5] => 21:59
```
You can suppose the input is correct and you can build from it a correct 24-hour time.
"""

from itertools import permutations

def late_clock(digits):
    mx = max(t for t in [''.join(p) for p in permutations(''.join(str(d) for d in digits))] if t[:2] < '24' and t[2:] < '60')
    return '{}:{}'.format(mx[:2], mx[2:])
