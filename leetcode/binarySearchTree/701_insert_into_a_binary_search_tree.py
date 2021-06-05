"""
701. Insert Into a Binary Search Tree
- Medium
- Tree
- Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: Recursive
# Time: O(N) | Space: O(H), the height of BST
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        self.helper(root, val)

        return root

    def helper(self, node, val):
        if node.val < val:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self.helper(node.right, val)
        if node.val > val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self.helper(node.left, val)


# Solution 1: Recursive (with better coding)
# Time: O(N) | Space: O(H), the height of BST
class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root
