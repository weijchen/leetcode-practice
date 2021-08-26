"""
94. Binary Tree Inorder Traversal
- Easy
- Hash Table, Stack, Tree
- Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: Recursion
# Time: O(N) | Space: O(N) -> the height of skewed tree
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        self.helper(root, ans)
        return ans

    def helper(self, node: TreeNode, path: List[TreeNode]):
        if not node:
            return
        self.helper(node.left, path)
        self.helper(node.right, path)
        path.append(node.val)


# Solution 2: Iterative
# Time: O(N) | Space: O(N)
# 解題：先將能遍歷到的左節點都記錄下來，再處理父節點及右節點
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans

        st = []
        while st or root:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            ans.append(root.val)
            root = root.right
        return ans
