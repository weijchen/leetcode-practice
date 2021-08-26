"""
121. Best Time to Buy and Sell Stock
- Easy
- Array, DP, Greedy
- Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
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
        tmpMin = prices[0]
        tmpProfit = 0
        
        for price in prices:
            tmpMin = min(tmpMin, price)
            tmpProfit = max(tmpProfit, price - tmpMin)
        return tmpProfit
# @lc code=end

