"""
863. All Nodes Distance K in Binary Tree
- Medium
- Tree, DFS, BFS, Binary Tree
- Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: Annotate Parent
# Time: O(N) | Space: O(N), when the tree is a skewed-tree
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        # transform the tree structure into a graph-like structure
        queue = collections.deque([(target, 0)])
        # to prevent traverse back to the parent node
        seen = {target}
        while queue:
            if queue[0][1] == k:
                return [_[0].val for _ in queue]
            node, level = queue.popleft()
            for nei in node.left, node.right, node.par:
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, level+1))
        return []
