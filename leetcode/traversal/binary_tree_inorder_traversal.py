"""
Binary Tree Inorder Traversal
- Link: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
"""


# Approach 1: Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        self.helper(root, ans)
        return ans

    def helper(self, node: TreeNode, ans: List[TreeNode]):
        if node.left:
            self.helper(node.left, ans)
        ans.append(node.val)
        if node.right:
            self.helper(node.right, ans)


# Approach 2: Iterative
class Solution:
    def inorderTraversal(self, root):
        ans = []
        if not root: return ans
        st = []
        while True:
            # for iterating left side nodes
            while root:
                st.append(root)
                root = root.left
            if not st:
                return ans
            node = st.pop()
            ans.append(node.val)
            # for iterating right side nodes
            root = node.right
