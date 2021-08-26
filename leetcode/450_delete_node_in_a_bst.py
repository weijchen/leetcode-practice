"""
450. Delete Node in a BST
- Medium
- Tree
- Link: https://leetcode.com/problems/delete-node-in-a-bst/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: InOrder traversal + List to BST
# Time: O(N) | Space: O(N)
def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
    path = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        if node.val != key:
            path.append(node.val)
        traverse(node.right)
    traverse(root)

    newRoot = TreeNode()

    def recover(node, l, r):
        if node:
            if l > r:
                return
            mid = (r - l) // 2 + l
            midVal = path[mid]
            node = TreeNode(midVal)
            node.left = recover(node, l, mid - 1)
            node.right = recover(node, mid + 1, r)
            return node
    return recover(newRoot, 0, len(path)-1)
