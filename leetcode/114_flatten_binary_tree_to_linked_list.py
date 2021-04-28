"""
113. Flatten Binary Tree to Linked List
- Medium
- Tree, DFS
- Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""


# Approach 1: Recursion
# Time: O(N) | Space: O(H), where H is the height of the tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flattenTree(self, node: TreeNode) -> None:
        # null case
        if not node:
            return None

        # leaf case
        if not node.left and not node.right:
            return node

        # recursively flatten the left subtree
        leftTail = self.flattenTree(node.left)
        rightTail = self.flattenTree(node.right)

        # connect leftTree and rightTree with leftTail
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None

        return rightTail if rightTail else leftTail

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenTree(root)


# Approach 2
