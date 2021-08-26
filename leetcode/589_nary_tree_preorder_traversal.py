"""
589. N-ary Tree Preorder Traversal
- Easy
- BFS, DFS, Tree
- Link: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# Solution: Recursive
# Time: O(N) | Space:O(N)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return ans

        self.helper(root, ans)
        return ans

    def helper(self, node, path):
        if not node:
            return
        path.append(node.val)
        for _ in node.children:
            self.helper(_, path)


# Solution 2: Iterative
# Time: O(N) | Space:O(N)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return ans

        st = [root]

        while st:
            node = st.pop()
            ans.append(node.val)
            if node.children:
                st.extend(node.children[::-1])  # remember to reverse children list

        return ans
