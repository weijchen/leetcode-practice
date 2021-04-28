"""
117. Populating Next Right Pointers in Each Node II
- Medium
- Tree, DFS
- Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""


# Approach 1: BFS
# Time: O(N) | Space: O(N), since for perfect binary tree, the number of node in last layer will be N/2
# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
# self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.connectTree([root])
        return root

    def connectTree(self, curL: List['Node']):
        while len(curL) > 0:
            nextL = []

            for idx, n in enumerate(curL):
                if idx+1 < len(curL):
                    n.next = curL[idx+1]
                else:
                    n.next = None

                if n.left:
                    nextL.append(n.left)
                if n.right:
                    nextL.append(n.right)
            curL = nextL
