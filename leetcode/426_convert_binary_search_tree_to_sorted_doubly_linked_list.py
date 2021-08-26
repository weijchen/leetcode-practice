"""
426. Convert Binary Search Tree to Sorted Doubly Linked List
- Medium
- Linked List, Stack, Tree, DFS, BST, Binary Tree, Doubly-Linked List
- Link: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


# Solution 1: Inorder Traversal
# Time: O(N) | Space: O(H), the number of recursive calls, which is the height of the given tree
class Solution:
    def __init__(self):
        self.prev = None
        self.last = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.treeToDoublyListHelper(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head

    def treeToDoublyListHelper(self, node):
        if not node:
            return
        self.treeToDoublyListHelper(node.left)
        if self.prev:
            node.left = self.prev
            self.prev.right = node
        else:
            self.head = node
        self.prev = node
        self.treeToDoublyListHelper(node.right)
