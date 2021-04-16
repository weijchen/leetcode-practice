"""
26. Remove Duplicates from Sorted Array
- Easy
- Array, Two Pointers
- Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


# Time: O(n) | Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 0:
            return
        prev = nums[0]
        cur = 1
        while cur < len(nums):
            if nums[cur] == prev:
                nums.pop(cur)
            else:
                prev = nums[cur]
                cur += 1
