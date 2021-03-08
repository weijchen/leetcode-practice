"""
144. Binary Tree Preorder Traversal
- Medium
- Stack, Tree
- Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursion Solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        retList = []
        if not root:
            return retList
        self.helper(root, retList)
        return retList

    def helper(self, root: TreeNode, _list: List):
        if not root:
            return
        _list.append(root.val)
        self.helper(root.left, _list)
        self.helper(root.right, _list)


# Iterative Solution
# Time: O(n)
# Space: O(n)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        st = [root]

        while root and len(st) is not 0:
            root = st.pop()
            l.append(root.val)
            if root.right:
                st.append(root.right)
            if root.left:
                st.append(root.left)

        return l
