"""
700. Search in a Binary Search Tree
- Easy
- Tree
- Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: DFS
# Time: O(N) | Space: O(H), the height of the BST
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        st = [root]

        while st:
            node = st.pop()
            if node.val == val:
                return node

            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        return None
