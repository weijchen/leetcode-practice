"""
230. Kth Smallest Element in a BST
- Medium
- Tree, BST
- Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
- 思路: BST 的重要性質 -> in-order traversal 會產生排序過的元素列表
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: Inorder traversal
# Time: O(N) | Space: O(H), the height of BST
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        path = []

        def inorder(node):
            if not node:
                return
            if node.left:
                inorder(node.left)
            path.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)

        return path[k-1]
