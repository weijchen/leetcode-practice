"""
938. Range Sum of BST
- Easy
- Tree, DFS, BST, Binary Tree
- Link: https://leetcode.com/problems/range-sum-of-bst/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: Inorder traversal
# Time: O(N) | Space: O(H), the number of recursive calls
class Solution:
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            if node.val >= low and node.val <= high:
                self.sum += node.val
            traverse(node.right)

        traverse(root)
        return self.sum
