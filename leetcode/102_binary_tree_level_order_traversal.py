"""
102. Binary Tree Level Order Traversal
- Medium
- Tree, BFS
- Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Approach 1: BFS (Iterative)
# Time: O(N) | Space: O(N), for saving nextL
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        self.bfs([root], ans)
        return ans

    def bfs(self, curL: List[TreeNode], ans: List[int]):
        while len(curL) > 0:
            nextL = []
            nextLVal = []
            for n in curL:
                nextLVal.append(n.val)
                if n.left:
                    nextL.append(n.left)
                if n.right:
                    nextL.append(n.right)
            ans.append(nextLVal)
            curL = nextL
