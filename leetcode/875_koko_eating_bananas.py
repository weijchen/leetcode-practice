"""
875. Koko Eating Bananas
- Medium
- Array, Binary Search
- Link: https://leetcode.com/problems/koko-eating-bananas/
"""


# Solution 1: Binary Search
# Time: O(NlogN) | Space: O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(rate):
            totalHour = sum([ceil(p/rate) for p in piles])
            return totalHour <= h

        l, r = 1, max(piles)
        while l < r:
            mid = (r - l) // 2 + l
            if canFinish(mid):
                r = mid
            else:
                l = mid + 1

        return r
