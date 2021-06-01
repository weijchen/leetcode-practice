"""
746. Min Cost Climbing Stairs
- Easy
- DP
- Link: https://leetcode.com/problems/min-cost-climbing-stairs/
- 思路 1: min cost to climb to n-th step
        dp(n) = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])
        dp: 是走到該步所需的 cost，非該步的 cost
- 思路 2: min cost before leaving n-th step
        dp(n) = min(dp(n-1), dp(n-2)) + cost[n]
"""

# Solution 1: DP
# Time: O(N) | Space: O(N)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {0: 0, 1: 0}

        n = len(cost)
        for i in range(2, n+1):
            # dp(n) = min(dp(n-1) + cost(n-1), dp(n-2) + cost(n-2))
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]

# Solution 1-1: DP with constant space
# Time: O(N) | Space: O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1, dp2 = 0, 0

        n = len(cost)
        for i in range(2, n+1):
            dp = min(dp1 + cost[i-1], dp2 + cost[i-2])
            dp2, dp1 = dp1, dp

        return dp1
