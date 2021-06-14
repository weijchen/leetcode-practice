"""
100. Same Tree
- Easy
- Tree, DFS
- Link: https://leetcode.com/problems/same-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: InOrder traversal + Position args
# Time: O(N) | Space: O(N)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ret1, ret2 = [], []
        self.helper(p, ret1, -1)
        self.helper(q, ret2, -1)

        return ret1 == ret2

    def helper(self, p: TreeNode, _list: List, pos: int):
        if not p:
            return
        self.helper(p.left, _list, 1)
        _list.append((p.val, pos))
        self.helper(p.right, _list, 0)


# Solution 2: DFS (recursive)
# Time: O(N) | Space: O(1)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def dfs(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False
            return dfs(a.left, b.left) and dfs(a.right, b.right)
        
        return dfs(p, q)
