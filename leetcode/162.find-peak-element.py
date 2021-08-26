"""
162. Find Peak Element
- Medium
- Array, Binary Search
- Link: https://leetcode.com/problems/find-peak-element/
"""


# Solution 1: Binary Search (Iterative)
# Time: O(logN) | Space: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if (mid-1 < 0 or nums[mid] > nums[mid-1]) and (mid+1 >= len(nums) or nums[mid] > nums[mid+1]):
                return mid
            elif mid-1 >= 0 and nums[mid] < nums[mid-1]:
                r = mid-1
            elif mid+1 < len(nums) and nums[mid] < nums[mid+1]:
                l = mid+1


# Solution 2: Binary Search (With better logics)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
