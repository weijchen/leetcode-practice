"""
102. Binary Tree Level Order Traversal
- Medium
- Tree, BFS
- Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: BFS (Iterative)
# Time: O(N) | Space: O(N), for saving nextL
# Definition for a binary tree node.
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        curLevel = [root]

        while curLevel:
            nextLevel = []
            curLevelVal = []
            for node in curLevel:
                curLevelVal.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            curLevel = nextLevel
            ans.append(curLevelVal)

        return ans
