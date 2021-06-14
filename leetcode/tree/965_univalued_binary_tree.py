# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: Recursive
# Time: O(N) | Space: O(N), when the tree is a skewed tree
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        if root.left:
            if root.val != root.left.val:
                return False

        if root.right:
            if root.val != root.right.val:
                return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)


# Solution 2: DFS (Recursive)
# Time: O(N) | Space: O(N)
class Solution(object):
    def isUnivalTree(self, root):
        vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(set(vals)) == 1
