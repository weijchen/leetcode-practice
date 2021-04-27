"""
106. Construct Binary Tree from Inorder and Postorder Traversal
- Medium
- Array, Tree, DFS
- Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""


# Approach 1: Recursion + Array
# Time: O(N^2) | Space: O()
# 缺點：變更原始輸入、平方的時間複雜度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        rootVal = postorder.pop()
        root = TreeNode(rootVal)
        indexInInorder = inorder.index(rootVal)

        # 這邊要注意先後順序
        root.right = self.buildTree(inorder[indexInInorder+1:], postorder)
        root.left = self.buildTree(inorder[:indexInInorder], postorder)

        return root


# Approach 2: Recursion + Map
# Time: O(N) | Space: O(N)
class Solution:
    def buildTree(self, inorder, postorder):
        map_inorder = {}
        for i, val in enumerate(inorder):
            map_inorder[val] = i

        def recur(low, high):
            if low > high:
                return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x
        return recur(0, len(inorder)-1)
