"""
107. Binary Tree Level Order Traversal II
- Medium
- Tree, BFS
- Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""


# Approach 1: BFS + reversed
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        self.helper([root], ans)
        return ans[::-1]

    def helper(self, node: TreeNode, ans: List[int]):
        curL = node

        while curL:
            nextL = []
            nextLVal = []

            for node in curL:
                nextLVal.append(node.val)
                if node.left:
                    nextL.append(node.left)
                if node.right:
                    nextL.append(node.right)

            ans.append(nextLVal)
            curL = nextL
