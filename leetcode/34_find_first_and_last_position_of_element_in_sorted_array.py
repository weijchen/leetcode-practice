"""
34. Find First and Last Position of Element in Sorted Array
- Medium
- Array, Binary Search
- Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


# Approach 1: Binary Search
# Time: O(logN) | Space: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(l, r, findLow):
            found = -1
            while l <= r:
                mid = (l - r) // 2 + r

                if nums[mid] == target:
                    found = mid
                    if findLow:
                        r = mid - 1
                    else:
                        l = mid + 1
                    
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return found
        
        l = helper(0, len(nums)-1, True)
        r = helper(0, len(nums)-1, False)
        
        return [l, r]

    