"""
94. Binary Tree Inorder Traversal
- Medium
- Hash Table, Stack, Tree
- Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursion solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        retList = []
        if not root:
            return retList
        self.helperFunc(root, retList)
        return retList

    def helperFunc(self, root: TreeNode, _list) -> List[int]:
        if not root:
            return
        self.helperFunc(root.left, _list)
        _list.append(root.val)
        self.helperFunc(root.right, _list)

# Iterative solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
      retList = []
      st = []
      if not root:
        return

      while st or root:
        while root:
          st.append(root)
          root = root.left
        root = st.pop()
        retList.append(root.val)
        root = root.right
        
      return retList
        


