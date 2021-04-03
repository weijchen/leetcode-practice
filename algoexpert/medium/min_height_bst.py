"""
Min Height BST
- Medium
"""


def minHeightBst(array):
    return helper(array, None, 0, len(array) - 1)


# 解題思路 -> 遇到 array 的切中點操作時，可多利用 start, end indexes
# O(nlogn) time | O(n) space -> insert a node takes logN time, and we insert N nodes
def helper(array, bst, startIdx, endIdx):
    if startIdx > endIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    helper(array, bst, startIdx, midIdx-1)
    helper(array, bst, midIdx+1, endIdx)
    return bst

# O(n) time | O(n) space -> use customized insert for every insertion
def helper(array, bst, startIdx, endIdx):
    if startIdx > endIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    newBstNode = BST(array[midIdx])
    if bst is None:
      bst = newBstNode
    else:
      if array[midIdx] < bst.value:
        bst.left = newBstNode
        bst = bst.left
      else:
        bst.right = newBstNode
        bst = bst.right
    helper(array, bst, startIdx, midIdx-1)
    helper(array, bst, midIdx+1, endIdx)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
