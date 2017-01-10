"""
## Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphanumeric characters, including digits, uppercase and lowercase alphabets.

## Example
"abcde" -> 0 `# no characters repeats more than once`
"aabbcde" -> 2 `# 'a' and 'b'`
"aabbcdeB" -> 2 `# 'a' and 'b'`
"indivisibility" -> 1 `# 'i'`
"Indivisibilities" -> 2 `# 'i' and 's'`
"aa11" -> 2 `# 'a' and '1'`
"""

from collections import Counter

def duplicate_count(text):
    duplicates = 0

    for key, value in Counter(list(text.lower())).iteritems():
        if value > 1:
            duplicates += 1

    return duplicates
