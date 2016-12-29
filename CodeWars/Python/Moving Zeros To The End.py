"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

```
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
```
"""

def move_zeros(array):
    original_array = array[:]
    num_items_moved = 0

    for index, item in enumerate(original_array):
        try:
            if int(item) == 0 and not (item is False):
                value = int(array.pop(index - num_items_moved))
                array.append(value)
                num_items_moved += 1
        except Exception as exception:
            continue

    return array
