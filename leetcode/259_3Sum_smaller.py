"""
259. 3Sum Smaller
- Medium
- Array, Two Pointers, Binary Search, Sorting
- Link: https://leetcode.com/problems/3sum-smaller/
"""


# Solution 1: Two Pointers
# Time: O(N^2) | Space: O(1)
class Solution:
    def __init__(self):
        self.ans = 0

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()

        for idx, num in enumerate(nums):
            self.twoSumSmaller(num, nums[idx+1:], target)
        return self.ans

    def twoSumSmaller(self, a, nums,  target):
        l, r = 0, len(nums) - 1

        while l < r:
            _sum = a + nums[l] + nums[r]
            if _sum < target:
                self.ans += (r - l)
                l += 1
            else:
                r -= 1
