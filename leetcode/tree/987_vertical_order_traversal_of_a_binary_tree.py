"""
987. Vertical Order Traversal of a Binary Tree
- Hard
- Hash Table, Tree, DFS, BFS
- Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: DFS + Hash Table
# Time: O(N*logN), for sorting | Space: O(N)
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        cols = {}
        st = [(root, 0, 0)]
        while st:
            node, col, level = st.pop()
            if node.left:
                st.append((node.left, col-1, level+1))
            if node.right:
                st.append((node.right, col+1, level+1))

            if col in cols:
                if level in cols[col]:
                    cols[col][level].append(node.val)
                    cols[col][level].sort()
                else:
                    cols[col][level] = [node.val]
            else:
                cols[col] = {level: [node.val]}

        for k in sorted(list(cols.keys())):
            tmp = []
            for l in sorted(list(cols[k].keys())):
                tmp.extend(cols[k][l])
            ans.append(tmp)

        return ans


# Solution 2: DFS + Hash Table + Ordered Dictionary
# Time: O(N*logN), for sorting | Space: O(N)
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        cols = {}
        st = [(root, 0, 0)]
        while st:
            node, col, level = st.pop()
            ans.append((col, level, node.val))
            if node.left:
                st.append((node.left, col-1, level+1))
            if node.right:
                st.append((node.right, col+1, level+1))

        ans.sort()  # 可以根據 list 內 element 的多個欄位進行排序
        ret = OrderedDict()
        for column, row, value in ans:
            if column in ret:
                ret[column].append(value)
            else:
                ret[column] = [value]
        return ret.values()
