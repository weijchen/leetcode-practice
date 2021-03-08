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


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.helper(root, root)
    
    def helper(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        
        return p.val == q.val and self.helper(p.left, q.right) and self.helper(p.right, q.left)
