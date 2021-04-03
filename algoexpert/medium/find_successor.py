"""
Find Successor
- Medium
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# Solution 1: inorder traversal, then use array to find target
# Time: O(n) | Space: O(n)
def findSuccessor(tree, node):
    # Write your code here.
    ret = []
    retVal = None
    inorderHelper(tree, ret)
    for idx, ele in enumerate(ret):
        if ele.value == node.value and idx+1 < len(ret):
            retVal = ret[idx+1]
            break

    return retVal


def inorderHelper(node, arr):
    if node is None:
        return
    inorderHelper(node.left, arr)
    arr.append(node)
    inorderHelper(node.right, arr)
