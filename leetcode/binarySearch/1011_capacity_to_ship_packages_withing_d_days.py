"""
1011. Capacity To Ship Packages Within D Days
- Medium
- Array, Binary Search, Greedy
- Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""


# Solution 1: Binary Search
# Time: O(NlogN) | Space: O(1)
# boundary: [max(), sum()]
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canFinish(capacity):
            cost = 1
            cur = 0
            for i in weights:
                if cur + i > capacity:
                    cur = 0
                    cost += 1
                cur += i
            return cost <= days

        l, r = max(weights), sum(weights)
        while l < r:
            rate = (r - l) // 2 + l
            if canFinish(rate):
                r = rate
            else:
                l = rate + 1

        return l
