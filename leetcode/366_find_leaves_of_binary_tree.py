"""
366. Find Leaves of Binary Tree
- Medium
- Tree, DFS, Binary Tree
- Link: https://leetcode.com/problems/find-leaves-of-binary-tree/
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
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        ret = collections.defaultdict(list)

        def order(node):
            if not node:
                return 0
            height_l = order(node.left)
            height_r = order(node.right)
            height = max(height_l, height_r) + 1
            ret[height].append(node.val)
            return height

        order(root)
        return [val for val in ret.values()]
