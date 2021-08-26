"""
104. Maximum Depth of Binary Tree
- Easy
- Tree, DFS, Recursion
- Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: DFS (iterative)
# Time: O(N) | Space: O(N)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return ans
        st = [(root, 1)]

        while st:
            node, depth = st.pop()
            if node.left:
                st.append((node.left, depth + 1))
            if node.right:
                st.append((node.right, depth + 1))

            if not node.left and not node.right:
                ans = max(ans, depth)

        return ans
