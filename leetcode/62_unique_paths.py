"""
62. Unique Paths
- Medium
- Array, DP
- Link: https://leetcode.com/problems/unique-paths/
"""


# Solution 1: DP
# Time: O(N * M) | Space: O(N * M), where N and M is the number of Column and Row
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row][col-1] + dp[row-1][col]
        return dp[-1][-1]
