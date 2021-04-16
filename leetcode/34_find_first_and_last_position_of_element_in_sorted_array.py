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
        def helper(lo, hi, left):
            found = -1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if target > nums[mid]:
                    lo = mid + 1
                elif target < nums[mid]:
                    hi = mid - 1
                else:
                    if left:
                        found = mid
                        hi = mid - 1
                    else:
                        found = mid
                        lo = mid + 1

            return found
        l = helper(0, len(nums)-1, True)
        r = helper(0, len(nums)-1, False)
        return [l, r]
