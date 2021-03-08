"""
226. Invert Binary Tree
- Easy
- Tree
- Link: https://leetcode.com/problems/invert-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time: O(n) -> each node in the tree is visited only once
# Space: O(n) -> recursion will call h times (where h is the height of the tree). and h belongs to n
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        self.helper(root)
        return root
    
    def helper(self, root: TreeNode):
        if not root.left and not root.right:
            return None
        else:
            root.left, root.right = root.right, root.left
            if root.left:
                self.helper(root.left)
            if root.right:
                self.helper(root.right)
            