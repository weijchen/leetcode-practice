"""
113. Path Sum II
- Medium
- Tree, DFS
- Link: https://leetcode.com/problems/path-sum-ii/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root: return []
        st = [(root, [root.val], root.val)]
        ret = []
        
        while st:
            node, path, val = st.pop()
            
            if val == targetSum:
                if self.isLeaf(node):
                    ret.append(path)
            
            if node.left:
                st.append((node.left, path + [node.left.val], val + node.left.val))
            
            if node.right:
                st.append((node.right, path + [node.right.val], val + node.right.val))
        
        return ret
        
    
    def isLeaf(self, node: TreeNode) -> bool:
        return not node.left and not node.right
