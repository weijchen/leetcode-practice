"""
145. Binary Tree Postorder Traversal
- Easy
- Stack, Tree
- Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: Recursive
# Time: O(N) | Space: O(N)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        self.helper(root, ans)
        return ans

    def helper(self, node: TreeNode, ans: List[TreeNode]):
        if node.left:
            self.helper(node.left, ans)
        if node.right:
            self.helper(node.right, ans)
        ans.append(node.val)


# Solution 2: Iterative
# Time: O(N) | Space: O(N)
# 先製作反向的 postorder，最後輸出做 reverse
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans

        st = [root]
        while st:
            node = st.pop()
            ans.append(node.val)
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)

        return ans[::-1]
