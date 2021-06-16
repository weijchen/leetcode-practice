"""
69. Sqrt(x)
- Easy
- Math, Binary  Search
- Link: https://leetcode.com/problems/sqrtx/
"""


# Solution 1-1: Brute Force (for loop)
# Time: O(sqrt(N)) | Space: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        for i in range(x):
            if i * i > x:
                return i - 1
        return 1


# Solution 1-2: Brute Force (while loop)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        cur = 1
        while cur * cur <= x:
            cur += 1
        return cur-1


# Solution 2: Binary Search
# x^(1/2) < x / 2 (by 2x < x^2)
# Time: O(logN) | Space: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 2, x // 2

        while l <= r:
            pivot = l + (r - l) // 2
            num = pivot * pivot
            if num > x:
                r = pivot - 1
            elif num < x:
                l = pivot + 1
            else:
                return pivot
        return r
