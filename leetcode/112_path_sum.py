"""
112. Path Sum
- Easy
- Tree, DFS
- Link: https://leetcode.com/problems/path-sum/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: BFS
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        return self.bfs(root, targetSum)

    def bfs(self, root: TreeNode, targetSum: int) -> bool:

        cur_l = [[root, root.val]]
        next_l = []

        while cur_l:
            next_l = []
            for path in cur_l:
                node, _sum = path[0], path[1]
                if _sum == targetSum and self.isLeaf(node):
                    return True
                if node.left:
                    next_l.append([node.left, _sum + node.left.val])

                if node.right:
                    next_l.append([node.right, _sum + node.right.val])
            cur_l = next_l

        return False

    def isLeaf(self, root: TreeNode) -> bool:
        return not root.left and not root.right


# Approach 2: DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        st = [(root, root.val)]

        while len(st) > 0:
            curNode, curVal = st.pop()
            if curVal == targetSum and self.isLeaf(curNode):
                return True
            if curNode.left:
                newSum = curVal + curNode.left.val
                st.append((curNode.left, newSum))
            if curNode.right:
                newSum = curVal + curNode.right.val
                st.append((curNode.right, newSum))
        return False

    def isLeaf(self, node: TreeNode) -> bool:
        return not node.left and not node.right
