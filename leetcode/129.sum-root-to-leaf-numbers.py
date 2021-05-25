#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: DFS
# Time: O(N) | Space: O(N), worst case -> when the given tree has skewed shape
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = []
        st = [(root, "")]

        while len(st) > 0:
            curNode, curPath = st.pop()
            if self.isLeaf(curNode):
                curPath += "{}".format(curNode.val)
                ans.append(int(curPath))
            else:
                if curNode.left:
                    st.append((curNode.left, curPath + "{}".format(curNode.val)))
                if curNode.right:
                    st.append((curNode.right, curPath + "{}".format(curNode.val)))
        return sum(ans)

    def isLeaf(self, node: TreeNode) -> bool:
        return not node.left and not node.right
# @lc code=end
