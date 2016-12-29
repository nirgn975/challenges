"""
Welcome, Warrior! In this kata, you will get a message and you will need to get the frequency of each and every character!

Explanation (Python)

Your function will be called `char_freq` and you will get passed a string, you will then return a dictionary with as keys the characters, and as values how many times that character is in the string. You can assume you will be given valid input.

Example
```
char_freq("I like cats") # Returns {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1}
```
"""

def char_freq(message):
    d = {}
    for word in message:
        if word in d:        # check if the word is already in the dictionary
            d[word] += 1
        else:                # add it if it's not in the dictionary
            d[word] = 1
    return d
