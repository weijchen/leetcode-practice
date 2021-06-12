"""
63. Unique Paths II
- Medium
- Array, DP
- Link: https://leetcode.com/problems/unique-paths-ii/
"""


# Solution 1: DP
# Time: O(N * M) | Space: O(N * M), where N and M is the number of Column and Row
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # blocked at begin point
        if obstacleGrid[0][0] == 1:
            return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                # begin point
                if row == 0 and col == 0:
                    dp[row][col] = 1
                    continue
                # obstacle
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[-1][-1]
