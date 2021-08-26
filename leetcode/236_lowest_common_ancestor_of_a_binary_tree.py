"""
236. Lowest Common Ancestor of a Binary Tree
- Medium
- Tree, DFS, Binary Tree
- Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: DFS
# Time: O(N) | Space: O(H)
# 這個方法因為會跑兩次 backtrack，所以效率較差
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def backtrack(node, target, path):
            st = [(node, path)]

            while st:
                n, p = st.pop()
                if n.val == target:
                    return p
                if n.left:
                    st.append((n.left, p + [n.left.val]))
                if n.right:
                    st.append((n.right, p + [n.right.val]))

        p_path = backtrack(root, p.val, [root.val])
        q_path = backtrack(root, q.val, [root.val])

        ret = 0
        length = min(len(p_path), len(q_path))
        for (a, b) in zip(p_path[:length], q_path[:length]):
            if a == b:
                ret = a

        return TreeNode(ret)


# Solution 2: Recursive
# Time: O(N) | Space: O(H)
class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            if mid + left + right >= 2:
                self.ans = current_node

            return mid or left or right

        recurse_tree(root)
        return self.ans


# Solution 3: Recursive
# Time: O(N) | Space: O(H)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left and not right:
            return left
        elif not left and right:
            return right
        return None
