#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
# Solution 1: Array Sorting
# Time: O(NlogN) | Space: O(1)
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        maxGap = 0
        for i in range(len(nums) - 1):
            curGap = nums[i+1] - nums[i]
            maxGap = max(maxGap, curGap)
        return maxGap

# @lc code=end

