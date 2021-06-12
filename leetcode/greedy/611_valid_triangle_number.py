"""
611. Valid Triangle Number
- Medium
- Greedy
- Link: https://leetcode.com/problems/valid-triangle-number/
"""


# Solution 1: Greedy
# Time: O(N^2) | Space: O(1)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        nums_rev = nums[::-1]
        for i, a in enumerate(nums_rev):
            l, r = i + 1, len(nums_rev) - 1
            while l < r:
                if nums_rev[l] + nums_rev[r] > a:
                    ans += (r - l)
                    l += 1
                else:
                    r -= 1
        return ans
