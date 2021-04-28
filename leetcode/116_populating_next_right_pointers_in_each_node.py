"""
116. Populating Next Right Pointers in Each Node
- Medium
- Tree, DFS, BFS
- Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""


# Approach 1: BFS
# Time: O(N) | Space: O(N), 因為對於 perfect binary tree 而言，最後一層會包含 N/2 個節點
# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
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


# Approach 2: Using previously established next pointers
# 利用父層的節點來修改子層節點
# Time: O(N) | Space: O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            head = leftmost

            while head:
                # first type connection
                head.left.next = head.right

                # second type connection
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root
