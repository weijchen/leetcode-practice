"""
64. Minimum Path Sum
- Medium
- Array, DP
- Link: https://leetcode.com/problems/minimum-path-sum/
"""


# Solution 1: DP
# Time: O(N * M) | Space: O(N * M), where N and M is the number of Column and Row
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    dp[row][col] = grid[row][col]
                    continue
                dp[row][col] = min(dp[row-1][col] if row-1 >= 0 else float('inf'),
                                   dp[row][col-1] if col-1 >= 0 else float('inf')) + grid[row][col]

        return dp[-1][-1]
