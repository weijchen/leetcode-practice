"""
Binary Tree Postorder Traversal
- Link: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
"""


# Approach 1: Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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


# Approach 2: Iterative
# 透過模擬 reverse postorder 來達成（利用 stack）
# 1. root 2. root.right 3. root.left
# Time: O(N) | Space: O(N)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        st = [root]

        # revPost -> root, (root.right, root.left), 這兩個要反過來 insert 因為 stack 為先進後出
        while len(st) > 0:
            n = st.pop(-1)
            ans.append(n.val)
            if n.left:
                st.append(n.left)
            if n.right:
                st.append(n.right)
        return ans[::-1]
