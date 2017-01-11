"""
The input is a string `str` of digits. Cut the string into chunks of size `sz` (ignore the last chunk if its size is less than `sz`).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse it; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If
    * `sz` is `<= 0` or if `str` is `empty` return ""
    * `sz` is greater `(>)` than the length of str it is impossible to take a chunk of size `sz` hence return "".

Examples:
```
revrot("123456987654", 6) --> "234561876549"
revrot("123456987653", 6) --> "234561356789"
revrot("66443875", 4) --> "44668753"
revrot("66443875", 8) --> "64438756"
revrot("664438769", 8) --> "67834466"
revrot("123456779", 8) --> "23456771"
revrot("", 8) --> ""
revrot("123456779", 0) --> ""
```
"""

def revrot(strng, sz):
    if not len(strng) or sz <= 0 or len(strng) < sz:
        return ''

    new_strng = ''
    for strng_list in map(None, *([iter(strng)] * sz)):
        if not None in strng_list:
            new_strng += reverse_or_rotate(''.join(strng_list), sz)

    return new_strng


def reverse_or_rotate(string, limit):
    sum = 0
    for index, value in enumerate(string):
        sum += pow(int(value), 2)

    if sum % 2 == 0:
        return string[::-1]

    return string[1:limit] + string[0]
        
