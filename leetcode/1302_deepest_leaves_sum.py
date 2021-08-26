"""
1302. Deepest Leaves Sum
- Medium
- Tree, DFS
- Link: https://leetcode.com/problems/deepest-leaves-sum/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: DFS + OrderedDict
# Time: O(N * logN), for sorting | Space: O(N)
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ans = []
        if not root:
            return ans

        st = [(0, root)]
        while st:
            level, node = st.pop()
            if self.isLeaf(node):
                ans.append((level, node.val))
            if node.left:
                st.append((level + 1, node.left))
            if node.right:
                st.append((level + 1, node.right))

        ans.sort()
        ret = OrderedDict()
        for level, val in ans:
            if level not in ret:
                ret[level] = [val]
            else:
                ret[level].append(val)
        return sum(list(ret.items())[-1][-1])

    def isLeaf(self, node) -> bool:
        return not node.left and not node.right


# Solution 2: DFS without sorting
# Time: O(N) | Space: O(H), where H is the tree height
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ans = deepest_level = 0
        if not root:
            return ans

        st = [(0, root)]
        while st:
            level, node = st.pop()
            if self.isLeaf(node):
                if level > deepest_level:
                    ans = node.val
                    deepest_level = level
                elif level == deepest_level:
                    ans += node.val
            else:
                if node.left:
                    st.append((level + 1, node.left))
                if node.right:
                    st.append((level + 1, node.right))

        return ans

    def isLeaf(self, node) -> bool:
        return not node.left and not node.right
