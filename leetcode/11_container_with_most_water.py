"""
11. Container With Most Water
- Medium
- Array, Two Pointers
- Link: https://leetcode.com/problems/container-with-most-water/
"""


# Time: O(n)
# Space: O(1)
# Idea: You have two heights H_left and H_right, and H_right < H_left, then we know we have two choices, we want to move one of them. If we move the larger one, we cannot increase the height for the simple reason that we are always limited by the shortest, and we would be decreasing j-i, the width as well.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height)-1

        ret = 0
        while p1 != p2:
            curArea = min(height[p1], height[p2]) * ((p2+1) - (p1+1))
            ret = max(ret, curArea)

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return ret
