"""
572. Subtree of Another Tree
- Easy
- Tree
- Link: https://leetcode.com/problems/subtree-of-another-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: DFS
# Time: O(N * S), where S is the length of subRoot | Space: O(N)
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        st = [root]

        while st:
            node = st.pop(0)
            if node.val == subRoot.val:
                if self.checkIsSameTree(node, subRoot):
                    return True
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        return False

    def checkIsSameTree(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return self.checkIsSameTree(a.left, b.left) and self.checkIsSameTree(a.right, b.right)
