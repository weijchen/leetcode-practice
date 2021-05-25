"""
199. Binary Tree Right Side View
- Medium
- Tree, DFS, BFS, Recursion, Queue
- Link: https://leetcode.com/problems/binary-tree-right-side-view/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: BFS
# Time: O(N) | Space: O(N) - skewed tree
# [With List]
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans

        curLevel = [root]

        while curLevel:
            ans.append(curLevel[-1].val)
            nextLevel = []
            for node in curLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            curLevel = nextLevel
        return ans

# [With Deque]
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        if not root: return ans
        
        nextLevel = deque([root,])
        
        while nextLevel:
            curLevel = nextLevel
            nextLevel = deque()
            while curLevel:
                node = curLevel.popleft()
            
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ans.append(node.val)
        return ans
        

# Solution 2: One deque with size measurement
# 計算當下 deque 的長度的同時也限制了 list iteration 的次數
# Time: O(N) | Space: O(N) - skewed tree
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        if not root: return ans
        
        q = deque([root,])
        
        while q:
            level_length = len(q)
            
            for i in range(level_length): # 跑完後會進行下一個 level 的計算
                node = q.popleft()
                
                if i == level_length - 1:
                    ans.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
