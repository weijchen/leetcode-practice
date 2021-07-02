"""
15. 3Sum Closest
- Medium
- Array, Two Pointers
- Link: https://leetcode.com/problems/3sum-closest/
"""


# Approach 1: Two Pointers
# Time: O(N^2) | Space: O(logN) to O(N), depending on the implementation of the sorting algorithm
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        dist = float('inf')
        nums.sort()

        for i, num in enumerate(nums):
            remain = nums[i+1:]
            if len(remain) >= 2:
                l, r = 0, len(remain) - 1
                while l < r:
                    _sum = num + remain[l] + remain[r]
                    if abs(target - _sum) < abs(dist):
                        dist = target - _sum

                    if _sum < target:
                        l += 1
                    else:
                        r -= 1
                if dist == 0:
                    break
        return target - dist
