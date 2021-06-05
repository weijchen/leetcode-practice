"""
530. Minimum Absolute Difference in BST
- Easy
- Tree
- Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: DFS
# Time: O(N) | Space: O(H)
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = math.inf

        st = [(root, -math.inf, math.inf)]

        while st:
            node, minVal, maxVal = st.pop()
            ans = min(ans, min(abs(node.val-minVal), abs(node.val-maxVal)))
            if node.left:
                st.append((node.left, node.val, maxVal))
            if node.right:
                st.append((node.right, minVal, node.val))
        return ans



# Solution 2: inorder Traversal
# Time: O(N) | Space: O(N)
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        path = []
        def inorderTraversal(node, path):
            if not node:
                return
            if node.left:
                inorderTraversal(node.left, path)
            path.append(node.val)
            if node.right:
                inorderTraversal(node.right, path)
        
        inorderTraversal(root, path)
        
        tmpMin = math.inf
        
        for i in range(1, len(path)):
            tmpMin = min(tmpMin, path[i] - path[i-1])
        return tmpMin
