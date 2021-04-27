"""
103. Binary Tree Zigzag Level Order Traversal
- Medium
- Stack, Tree, BFS
- Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Approach 1: BFS
# Time: O(N) | Space: O(N), for saving nextL
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        self.helper([root], ans)
        return ans

    def helper(self, curL, ans, fromRight=False):
        while len(curL) > 0:
            nextL = []
            nextLVal = []

            for node in curL:
                nextLVal.append(node.val)

                if node.left:
                    nextL.append(node.left)
                if node.right:
                    nextL.append(node.right)
            if fromRight:
                nextLVal = nextLVal[::-1]
            fromRight = not fromRight    # toggle
            ans.append(nextLVal)
            curL = nextL
