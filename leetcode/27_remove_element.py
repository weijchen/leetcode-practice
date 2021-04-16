"""
27. Remove Element
- Easy
- Array, Two Pointers
- Link: https://leetcode.com/problems/remove-element/
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return

        cur = 0

        while cur < len(nums):
            if nums[cur] == val:
                del nums[cur]
            else:
                cur += 1
