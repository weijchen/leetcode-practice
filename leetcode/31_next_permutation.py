"""
31. Next Permutation
- Medium
- Array, Two Pointers
- Link: https://leetcode.com/problems/next-permutation/
"""


# Solution 1: Two Pointers
# Time: O(N) | Space: O(1)
# 須了解特殊解法: swap -> reverse
# 遇到特殊情形時 (數字全部遞減) -> 直接 reverse
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        posToChg = len(nums) - 1
        
        # 1. 尋找 swap 點
        for idx in range(len(nums) - 1, -1, -1):
            posToChg -= 1
            if nums[idx] > nums[idx-1]:
                break
        
        swapPos = posToChg
        for idx in range(posToChg + 1, len(nums)):
            if nums[idx] > nums[posToChg]:
                swapPos += 1
        
        # for continuous ascending nums
        if posToChg == -1:
            nums.reverse()
        else: 
          # 2. in-place reverse
            nums[posToChg], nums[swapPos] = nums[swapPos], nums[posToChg]

            l, r = posToChg + 1, len(nums) - 1

            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

