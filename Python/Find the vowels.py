"""
We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

So given a string "super", we should return a list of [2, 4].

```
Some examples:
Mmmm  => []
Super => [2,4]
Apple => [1,5]
YoMama -> [1,2,4,6]
```

**NOTE**: Vowels in this context refers to English Language Vowels - a e i o u y

**NOTE**: this is indexed from [1..n] (not zero indexed!)
"""

def vowel_indices(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels_count = []

    # Go through the letters word.
    for index, letter in enumerate(word):
        # Check if the letter is in vowels list of vowels uppercase list.
        if letter in vowels or letter in [x.upper() for x in vowels]:
            # Save the index of the letter.
            vowels_count.append(index + 1)

    return vowels_count
