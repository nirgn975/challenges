"""
Given root of tree with arbitrary number of children nodes transform data from tree to list. Where data from neighbour nodes in tree located in neighbour position in list.

Example:
```
       1
      / \
     2   3  -> [1,2,3,4,5,6,7]
    /|\   \
   4 5 6   7
```
"""

class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

def tree_to_list(tree_root):
    list = []
    result_list = []
    list.append(tree_root)

    while list:
        t = list.pop(0)
        result_list.append(t.data)
        while t.child_nodes:
            list.append(t.child_nodes.pop(0))

    return result_list
