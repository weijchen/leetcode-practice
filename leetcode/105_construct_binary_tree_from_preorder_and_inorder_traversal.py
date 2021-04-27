"""
105. Construct Binary Tree from Preorder and Inorder Traversal
- Medium
- Array, Tree, DFS
- Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


# Approach 1: Recursion + Array
# Time: O(N^2) | Space: O()
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        rootVal = preorder.pop(0)
        root = TreeNode(rootVal)
        indexInInorder = inorder.index(rootVal)

        # 這邊要注意先後順序
        root.left = self.buildTree(preorder, inorder[:indexInInorder])
        root.right = self.buildTree(preorder, inorder[indexInInorder+1:])
        return root


# Approach 2: Recursion + Map
# Time: O(N) | Space: O(N)
class Solution:
    def buildTree(self, preorder, inorder):
        id_map = {ele: idx for idx, ele in enumerate(inorder)}

        def recur(low, high):
            if low > high:
                return None
            node = TreeNode(preorder.pop(0))
            mid = id_map[node.val]
            node.left = recur(low, mid-1)
            node.right = recur(mid+1, high)
            return node

        return recur(0, len(inorder)-1)
