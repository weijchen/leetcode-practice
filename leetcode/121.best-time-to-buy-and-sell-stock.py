"""
121. Best Time to Buy and Sell Stock
- Easy
- Array, DP, Greedy
"""

#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# Approach 1: One-pass, Greedy
# Greedy -> 每一步都採用當下看起來最好的選擇
# Time: O(N) | Space: O(1)
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, tmpLow = 0, float('inf')
        for price in prices:
            if price < tmpLow:
                tmpLow = price
            elif price > tmpLow:
                profit = price - tmpLow
                maxProfit = max(profit, maxProfit)
        return maxProfit
# @lc code=end

