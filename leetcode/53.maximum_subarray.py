"""
53. Maximum Subarray
- Easy
- DP
- Link: https://leetcode.com/problems/maximum-subarray/
- 解題: 每個迴圈 檢查使用或不使用該數 能產生的最大值為何
"""


# Solution 1: DP
# Time: O(N) | Space: O(1) - O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [nums[0]]
        for idx in range(1, len(nums)):
            _sum = max(nums[idx], nums[idx] + dp[idx - 1])
            dp.append(_sum)

        return max(dp)
