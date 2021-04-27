"""
75. Sort Colors
- Medium
- Array, Two Pointers, Sort
- Link: https://leetcode.com/problems/sort-colors/
"""


# Approach 1: Built-in function
# Time: O(NlogN) | Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()


# Approach 2: One Pass
# Time: O(N) | Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start, end = 0, len(nums) - 1
        curr = 0

        while curr <= end and start <= end:  # important: curr can not be larger than max boundary
            if nums[curr] == 0:
                nums[curr], nums[start] = nums[start], nums[curr]
                start += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[end] = nums[end], nums[curr]
                end -= 1
            else:
                curr += 1
