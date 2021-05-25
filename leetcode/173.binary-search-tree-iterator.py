#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: Naive inorder traversal
# Time: O(N) | Space: O(N)
# 時間多花在 inorderTraversal 上 O(N)，為了初始化 traversal list 需花費 O(N) 的時間, 且耗費的是 system stack，next(), hasNext() 為 O(1)
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.traverse = []
        self.cur = 0
        self.inorderTraversal(root)

    def next(self) -> int:
        ret = self.traverse[self.cur]
        self.cur += 1
        return ret

    def hasNext(self) -> bool:
        return self.cur+1 <= len(self.traverse)

    def inorderTraversal(self, node):
        if node.left:
            self.inorderTraversal(node.left)
        self.traverse.append(node.val)
        if node.right:
            self.inorderTraversal(node.right)

# Solution 1: Naive inorder traversal
# Time: O(1) | Space: O(N)
# 進行可控的 inorder traversal，使用自定義的 stack，不耗費系統資源，且 traversal 不是連續性的呼叫，所以只需要 O(1) 的時間複雜度
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.st = []
        self._leftmost_inorder(root)

    # Worst case: skewed left tree -> O(N) 但就算是這種情形，該函數只會被呼叫一次，所以 amortized (avg.) time 為 O(1)
    def _leftmost_inorder(self, root):
        while root:
            self.st.append(root)
            root = root.left

    def next(self) -> int:
        topmost_node = self.st.pop()

        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        return len(self.st) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
