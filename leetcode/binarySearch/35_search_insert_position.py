"""
35. Search Insert Position
- Easy
- Array, Binary Search
- Link: https://leetcode.com/problems/search-insert-position/
"""


# Solution 1: Binary Search
# Time: O(log n) | Space: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l
