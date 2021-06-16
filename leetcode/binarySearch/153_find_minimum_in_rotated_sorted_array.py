"""
153. Find Minimum in Rotated Sorted Array
- Medium
- Array, Binary Search
- Link: https://leetcode.com/problems/search-insert-position/
"""


# Solution 1: Binary Search
# Time: O(logN) | Space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while nums[l] > nums[r]:
            mid = (r - l) // 2 + l
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]


# Solution 2: Binary Search (by HuaHua)
# Time: O(logN) | Space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
        
    def helper(self, nums, l, r):
        # 若 nums 只包含一個或兩個元素
        if l+1 >= r:
            return min(nums[l], nums[r])
        if nums[l] < nums[r]:
            return nums[l]
        mid = (r - l) // 2 + l
        return min(self.helper(nums, l, mid), self.helper(nums, mid+1, r))
