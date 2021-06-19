"""
99. Recover Binary Search Tree
- Medium
- Tree, DFS
- Link: https://leetcode.com/problems/recover-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Swap almost-sorted array
# Time: O(N) | Space: O(N)
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, second = -1, -1

        # Cool algorithm for tree traversal
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        # Important algorithm for almost-sorted array swapping
        def find_two_swapped(nums):
            n = len(nums)
            x = y = -1
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    # first swap occurence
                    if x == -1:
                        x = nums[i]
                    # second swap occurence
                    else:
                        break
            return x, y

        def recover(r, count):
            if r:
                if r.val == x or r.val == y:
                    r.val = x if r.val == y else y
                    count -= 1
                    if count == 0:
                        return
                recover(r.left, count)
                recover(r.right, count)

        path = inorder(root)
        x, y = find_two_swapped(path)
        recover(root, 2)
