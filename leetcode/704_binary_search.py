"""
704. Binary Search
- Easy
- Binary Search
- Link: https://leetcode.com/problems/binary-search/
"""


# Solution 1: Binary Search
# Time: O(logN) | Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l-r) // 2 + r
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
