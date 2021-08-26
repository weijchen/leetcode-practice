"""
101. Symmetric Tree
- Easy
- Tree, DFS, BFS
- Link: https://leetcode.com/problems/symmetric-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: Traverse + Recursion
# Time: O(N) | Space: O(N), when the tree is a skewed tree
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False

            if a.val != b.val:
                return False

            return dfs(a.left, b.right) and dfs(a.right, b.left)

        return dfs(root, root)
