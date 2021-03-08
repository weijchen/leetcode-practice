"""
543. Diameter of Binary Tree
- Easy
- Tree
- Link: https://leetcode.com/problems/diameter-of-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        retArr = [0]
        self.helper(root, retArr)
        return max(retArr)

    def helper(self, root: TreeNode, _arr: List):
        if not root.left and not root.right:
            return 0
        else:
            left_l = self.helper(root.left, _arr) + 1 if root.left else 0
            right_l = self.helper(root.right, _arr) + 1 if root.right else 0
            _arr.append(left_l + right_l)

            return max(left_l, right_l)
