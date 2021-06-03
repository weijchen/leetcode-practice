"""
144. Binary Tree Preorder Traversal
- Easy
- Stack, Tree
- Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
"""


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution 1: Recursion
# Time: O(N) | Space: O(N)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        self.helper(root, ans)
        return ans

    def helper(self, node: TreeNode, path: List[TreeNode]):
        if not node:
            return
        path.append(node.val)
        self.helper(node.left, path)
        self.helper(node.right, path)


# Solution 2: Iterative
# Time: O(n) | Space: O(n)
# 需注意 left, right 順序對調
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans

        st = [root]
        while st:
            node = st.pop()
            ans.append(node.val)
            # 注意這邊順序要反過來
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)

        return ans
