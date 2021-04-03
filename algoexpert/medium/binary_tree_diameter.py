"""
Binary Tree Diameter
- Medium
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter


# Solution 1:
# Time: O(h) | Space: O(1)
def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    curDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    curHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(curDiameter, curHeight)
