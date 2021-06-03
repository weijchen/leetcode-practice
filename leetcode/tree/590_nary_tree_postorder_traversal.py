"""
590. N-ary Tree Postorder Traversal
- Easy
- BFS, DFS, Tree
- Link: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# Solution 1: Recursive
# Time: O(N) | Space: O(N)
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return ans

        self.helper(root, ans)
        return ans

    def helper(self, node, path):
        if not node:
            return

        if node.children:
            for child in node.children:
                self.helper(child, path)
        path.append(node.val)
