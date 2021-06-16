"""
154. Find Minimum in Rotated Sorted Array II
- Hard
- Array, Binary Search
- Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""


# Solution 1: Binary Search
# Time: O(N) | Space: O(1)
# 和 153 不同的是，存在重複的元素，因此無法單靠首元素及末元素來判斷是否 sorted 以及是否 rotated，最壞情況需要遍歷數列，直到數列剩下一或兩個值才能求解
# Avg: O(logN), Worst: O(N)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, l, r):
        if l+1 >= r:
            return min(nums[l], nums[r])
        # 無法確定是否 sorted 是否 rotated，繼續跑下一層 recursive call
        if nums[l] < nums[r]:
            return nums[l]
        mid = (r - l) // 2 + l
        return min(self.helper(nums, l, mid), self.helper(nums, mid+1, r))
