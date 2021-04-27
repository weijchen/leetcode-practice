"""
Binary Tree Preorder Traversal
- Link: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
"""


# Approach 1: Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        self.helper(root, ans)
        return ans

    def helper(self, node: TreeNode, ans: List[TreeNode]):
        ans.append(node.val)
        if node.left:
            self.helper(node.left, ans)
        if node.right:
            self.helper(node.right, ans)
