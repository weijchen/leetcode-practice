"""
35. Search Insert Position
- Easy
- Array, Binary Search
- Link: https://leetcode.com/problems/search-insert-position/
"""

# Time: O(log n)
# Space: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        
        return mid if nums[mid] > target else mid + 1
        
                