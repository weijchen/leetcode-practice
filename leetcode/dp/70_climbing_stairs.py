"""
70. Climbing Stairs
- Easy
- DP
- Link: https://leetcode.com/problems/climbing-stairs/
- 思路：要上到第 N 階的樓梯，必須先到 N-1 或 N-2 階，再走 1 或 2 步，因此 S_N = S_N-1 + S_N-2，為費波那契數列
"""


# Solution 1: DP
# Time: O(N) | Space: O(N)n
# with hashtable
class Solution:
    def climbStairs(self, n: int) -> int:
        st = {0: 1, 1: 1}
        if n == 1:
            return st[1]
        for i in range(1, n+1):
            if i == 1:
                continue

            st[i] = st[i-1] + st[i-2]
            if i == n:
                return st[i]


# with array
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        nums = [1, 2]
        for i in range(2, n):
            nums.append(nums[i-1] + nums[i-2])
        return nums[len(nums) - 1]


# with swap
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            second, first = first+second, second
        return second
