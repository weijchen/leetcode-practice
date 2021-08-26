"""
322. Coin Change
- Medium
- DP
- Link: https://leetcode.com/problems/coin-change/
- 思路：對於 coin~amount 範圍內的數，計算最小組合的量為何，針對所有 coin 進行遍歷填表
"""


# Solution 1: DP (bottom-up)
# Time: O(S*N) | Space: O(S), where S is the value of amount
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf')] * amount

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[-1] if dp[-1] != float('inf') else -1
