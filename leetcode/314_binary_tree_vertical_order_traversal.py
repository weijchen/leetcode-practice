"""
314. Binary Tree Vertical Order Traversal
- Medium
- Hash Table, Tree, DFS, BFS, Binary Tree
- Link: https://leetcode.com/problems/binary-tree-vertical-order-traversal/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: BFS
# Time: O(N) | Space: O(H)
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            if node is not None:

                d[col].append(node.val)

                queue.append((node.left, col-1))
                queue.append((node.right, col+1))

        return [d[x] for x in sorted(d.keys())]
