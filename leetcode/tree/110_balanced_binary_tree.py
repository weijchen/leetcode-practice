"""
110. Balanced Binary Tree
- Easy
- Tree, DFS, Recursion
- Link: https://leetcode.com/problems/balanced-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: Bottom-up
# Time: O(N) | Space: O(N)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            # 要同時檢查左右子樹是否為 balanced
            if abs(left_height - right_height) > 1 or left_height == -1 or right_height == -1:
                return -1
            return max(left_height, right_height) + 1

        return height(root) != -1


# Solution 2: Top-down
# Time: O(NlogN) | Space:O(N)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
