"""
104. Maximum Depth of Binary Tree
- Easy
- Tree, DFS, Recursion
- Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS solution
# Time: O(n)
# Space: O(log(N)) -> the average height of a tree would be log(N), but worst case is O(N) when the tree is heavily unbalanced
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        maxL = 1
        st = [(root, 1)]

        while st:
            curr_n, curr_l = st.pop()

            if curr_n.left:
                if curr_l+1 > maxL:
                    maxL = curr_l + 1
                st.append((curr_n.left, curr_l+1))

            if curr_n.right:
                if curr_l+1 > maxL:
                    maxL = curr_l + 1
                st.append((curr_n.right, curr_l+1))

        return maxL
