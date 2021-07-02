"""
1283. Find the Smallest Divisor Given a Threshold
- Medium
- Array, Binary Search
- Link: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
"""


# Solution 1: Binary Search
# Time: O(NlogN) | Space: O(1)
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def canFinish(divisor):
            return sum([ceil(num/divisor) for num in nums]) <= threshold

        l, r = 1, max(nums)
        while l < r:
            d = (r - l) // 2 + l
            if canFinish(d):
                r = d
            else:
                l = d + 1

        return r
