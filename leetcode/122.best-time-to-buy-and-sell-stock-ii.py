#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#   Solution 1: Find peaks and vallies
#   Time: O(N) | Space: O(1)
#   兩個情形：1) 找買點 -> 出現 n < n+1 的情形，取 n 值位置為買點
#           2) 找賣點 -> 出現 m > m+1 的情形，且當下是有買入的，取 m 值位置為賣點
#                       或該值為列表最尾端，且當下是有買入的，取該位置為賣點

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        isHold = False
        ans = 0
        b, s = 0, 0
        curIdx = 0

        while curIdx < len(prices):
            if not isHold:
                b = prices[curIdx]
                if curIdx + 1 < len(prices) and prices[curIdx+1] > b:
                    isHold = True
            else:
                s = prices[curIdx]
                if (curIdx + 1 < len(prices) and prices[curIdx+1] < s) or (curIdx + 1 == len(prices)):
                    profit = s - b
                    ans += profit
                    isHold = False
            curIdx += 1

        return ans

# Solution 2: One pass -> 將連續上升點的值加總即為最後的答案
# Time: O(N) | Space: O(1)

# @lc code=end
