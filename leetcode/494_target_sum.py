"""
494. Target Sum
- Medium
- Array, DP, Backtracking
- Link: https://leetcode.com/problems/target-sum/
"""


# Solution 1: Backtracking + Memorization
# Time: O(NL), where N is the length of nums and L is the range of sum | Space: O(NL)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(curr, nums):
            key = (curr, tuple(nums))

            if key in cache:
                return cache[key]

            if not nums:
                return 1 if curr == target else 0

            res = dfs(curr + nums[0], nums[1:]) + dfs(curr - nums[0], nums[1:])
            cache[key] = res
            return res

        cache = {}
        return dfs(0, nums)


# Solution 2: Recursive (DP) + Memorization
# Time: O(NL), where N is the length of nums and L is the range of sum | Space: O(NL)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, target, index, curr_sum)

    def dp(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]

        # base cases
        if index < 0 and curr_sum == target:
            return 1

        if index < 0:
            return 0

        positive = self.dp(nums, target, index-1, curr_sum + nums[index])
        negative = self.dp(nums, target, index-1, curr_sum - nums[index])

        self.memo[(index, curr_sum)] = positive + negative

        return positive + negative
