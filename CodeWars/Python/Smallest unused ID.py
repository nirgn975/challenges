"""
Hey awesome programmer!

You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!

Therefore you need a method, which returns the smallest unused ID for your next new data item...

Note: The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs, but you don't have to find or remove them!

Go on and code some pure awesomeness!
"""

def next_id(arr):
    # sort the list
    sorted_arr = sorted(arr)

    # remove duplicates form the list
    sorted_arr = list(set(sorted_arr))

    # delete negative numbers from the list
    new_sorted_arr = []
    for i in range(len(sorted_arr)):
        if (sorted_arr[i] >= 0):
            new_sorted_arr.append(sorted_arr[i])

    # return the smallet unused ID
    for y in range(len(new_sorted_arr)):
        if (new_sorted_arr[y] != y):
            return y
    return len(new_sorted_arr)
