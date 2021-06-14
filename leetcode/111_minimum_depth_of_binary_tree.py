"""
111. Minimum Depth of Binary Tree
- Easy
- Tree, DFS, BFS
- Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: BFS
# Time: O(N) -> when balanced tree, we need to traverse till the bottom level, thus we visit N/2 nodes
# Space: O(N) -> all nodes were visited
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.bfs(root)

    def bfs(self, root: TreeNode):
        curr_l = [(root, 1)]
        next_l = []

        while curr_l:
            next_l = []
            for _ in curr_l:
                curr_n, curr_depth = _[0], _[1]
                if not curr_n.left and not curr_n.right:
                    return curr_depth
                if curr_n.left:
                    next_l.append((curr_n.left, curr_depth+1))
                if curr_n.right:
                    next_l.append((curr_n.right, curr_depth+1))
            curr_l = next_l


# Solution 2: DFS
# Time: O(N) | Space: O(N)
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        ans = float('inf')
        st = [(root, 1)]
        while st:
            node, depth = st.pop()

            if node.left:
                st.append((node.left, depth + 1))
            if node.right:
                st.append((node.right, depth + 1))

            if not node.left and not node.right:
                ans = min(ans, depth)

        return ans
