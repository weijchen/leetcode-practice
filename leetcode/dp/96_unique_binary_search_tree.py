"""
96. Unique Binary Search Tree
- Medium
- Math, DP, Tree, Binary Search Tree, Binary Tree
- Link: https://leetcode.com/problems/unique-binary-search-trees/
"""


# Solution 1: DP
# Time: O(N^2) | Space: O(N)
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n+1)
        G[0] = 1
        G[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]


# Solution 2: Math (Catalan number)
# Time: O(N) | Space: O(1)
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
