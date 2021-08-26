"""
42. Trapping Rain Water
- 難度：Hard
- 狀態：N
- 考點：Array, Two Pointers, DP, Stack, Monotonic Stack
- Link：https://leetcode.com/problems/trapping-rain-water/
- 偏好公司 (>= 15)：
- 思路：
"""


# Solution 1: DP
# Time: O(N) | Space: O(N)
# Brute Force 的改良版，利用 O(N) 的空間來儲存左右最高的高度後，再進行整個列表的遍歷
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        ans = 0
        left_height = [0] * len(height)
        right_height = [0] * len(height)

        left_height[0] = height[0]
        for i in range(1, len(height)):
            left_height[i] = max(height[i], left_height[i-1])

        right_height[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            right_height[i] = max(height[i], right_height[i+1])

        for i in range(len(height)):
            ans += (min(left_height[i], right_height[i]) - height[i])

        return ans
