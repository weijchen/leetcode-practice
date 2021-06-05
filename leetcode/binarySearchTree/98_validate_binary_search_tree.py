"""
98. Validate Binary Search Tree
- Medium
- Tree, DFS, Recursion
- Link: https://leetcode.com/problems/validate-binary-search-tree/
- 思路：Recursive 要回傳的是錯誤的 case，以及最終的 termination point case
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: Recursive
# Time: O(N) | Space: O(H)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node, lo=float('-inf'), hi=float('inf')):
            if not node:
                return True

            if node.val <= lo or node.val >= hi:
                return False

            return (helper(node.left, lo, node.val) and helper(node.right, node.val, hi))

        return helper(root)


# Solution 2: Iterative
# Time: O(N) | Space: O(H)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        st = [(root, -math.inf, math.inf)]

        while st:
            node, lo, hi = st.pop()
            if node.val <= lo or node.val >= hi:
                return False
            if node.left:
                st.append((node.left, lo, node.val))
            if node.right:
                st.append((node.right, node.val, hi))

        return True
