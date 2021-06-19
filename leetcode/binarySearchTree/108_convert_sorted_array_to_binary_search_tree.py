"""
108. Convert Sorted Array to Binary Search Tree
- Easy
- Tree, DFS
- Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: Array
# Time: O(N) | Space: O(H), where H is the height of the tree -> O(logN)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l, r = 0, len(nums) - 1

        def inorder(l, r):
            if l > r:
                return
            mid = (r - l) // 2 + l
            midVal = nums[mid]
            root = TreeNode(midVal)
            root.left = inorder(l, mid-1)
            root.right = inorder(mid+1, r)
            return root

        return inorder(l, r)
