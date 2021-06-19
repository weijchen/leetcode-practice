"""
501. Find Mode in Binary Search Tree
- Easy
- Tree
- Link: https://leetcode.com/problems/find-mode-in-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: InOrder Traversal + OrderedDict
# Time: O(N) | Space: O(N)
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = dict()

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            if node.val not in ans:
                ans[node.val] = 1
            else:
                ans[node.val] += 1
            traverse(node.right)

        traverse(root)
        maxVal = max(list(ans.values()))

        mod = []
        for k, v in ans.items():
            if v == maxVal:
                mod.append(k)
        return mod
