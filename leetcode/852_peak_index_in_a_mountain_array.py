"""
852. Peak Index in a Mountain Array
- Easy
- Array, Binary Search
- Link: https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""


# Solution 1: Binary Search
# Time: O(logN) | Space: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (r - l) // 2 + l
            if arr[mid] > arr[mid+1]:
                r = mid - 1
            else:
                l = mid + 1

        return l
