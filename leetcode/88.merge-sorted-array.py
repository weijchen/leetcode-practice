#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_l, nums2_l = len(nums1), len(nums2)
        zero_pointer = nums1_l - nums2_l
        if zero_pointer == len(nums1_l): return

        p1, p2 = 0, 0

        while p1 < len(nums1_l) and p2 < len(nums2_l):
            if nums2[p2] <= nums1[p1]:
                nums1[zero_pointer] = nums1[p1]
                nums1[p1] = nums2[p2]
                zero_pointer += 1
                p2 += 1
            p1 += 1

        
# @lc code=end


2 0 2 3 4 6
1 2 6



1 2 3 4 0 0
