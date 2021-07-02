"""
1448. Count Good Nodes in Binary Tree
- Medium
- Tree, DFS, BFS, Binary Tree
- Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: DFS
# Time: O(N) | Space: O(N)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        st = [(root, root.val)]
        count = 1
        while st:
            node, val = st.pop()
            if node.left:
                if node.left.val >= val:
                    count += 1
                st.append((node.left, max(node.left.val, val)))
            if node.right:
                if node.right.val >= val:
                    count += 1
                st.append((node.right, max(node.right.val, val)))

        return count
