#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start

# Solution 1: Use Extra Array
# Time: O(N) | Space: O(N)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = [0] * n

        for i in range(len(nums)):
            a[(i+k) % n] = nums[i]

        nums[:] = a
# @lc code=end
