"""
250. Count Univalue Subtrees
- Medium
- Tree
- Link: https://leetcode.com/problems/count-univalue-subtrees/
"""


# Approach 1: Bottom-up traversal
# Time: O(N) | Space: O(H), where H is the height of tree, and # of recursion call
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.ans = 0
        if not root:
            return self.ans
        self.helper(root)
        return self.ans

    def helper(self, node: TreeNode):
        if self.isLeaf(node):
            self.ans += 1
            return True

        # 依序檢查左右子樹
        isUni = True
        if node.left:
            isUni = self.helper(
                node.left) and isUni and node.val == node.left.val
        if node.right:
            isUni = self.helper(
                node.right) and isUni and node.val == node.right.val

        self.ans += isUni
        return isUni

    def isLeaf(self, node: TreeNode) -> bool:
        return not node.left and not node.right
