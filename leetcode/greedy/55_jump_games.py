"""
55. Jump Game
- Medium
- Array, Greedy
- Link: https://leetcode.com/problems/jump-game/
"""


# Solution 1: Greedy (go forward)
# Time: O(N) | O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curMax = 0
        for i, n in enumerate(nums):
            if i > curMax:
                return False
            curMax = max(curMax, i + n)
        return True


# Solution 2: Greedy (go backward)
# Time: O(N) | O(1)
class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal
