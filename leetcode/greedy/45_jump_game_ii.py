"""
45. Jump Game II
- Medium
- Array, Greedy
- Link: https://leetcode.com/problems/jump-game-ii/
"""


# Solution 1: Greedy (go backward)
# Time: O(N^2) | Space: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        count = 0
        while goal != 0:
            remain = nums[:goal]
            cand = []
            for i in range(len(remain))[::-1]:
                if i + remain[i] >= goal:
                    cand.append(i)

            goal = min(cand)
            count += 1

        return count


# Solution 2: Greedy (go forward)
# Time: O(N) | Space: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        current_jump_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_jump_end:
                count += 1
                current_jump_end = farthest

        return count


# Solution 3: Greedy (Two Pointers)
# Time: O(N) | Space: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            furthest = 0

            for i in range(l, r+1):
                furthest = max(furthest, i+nums[i])

            l = r + 1
            r = furthest
            count += 1

        return count
