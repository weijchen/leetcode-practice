"""
1137. N-th Tribonacci Number
- Easy
- DP
- Link: https://leetcode.com/problems/n-th-tribonacci-number/
"""


# Solution 1: DP
# Time: O(N) | Space: O(N)
class Solution:
    def tribonacci(self, n: int) -> int:
        trib = {0: 0, 1: 1, 2: 1}

        if n < 3:
            return trib[n]

        for i in range(3, n+1):
            trib[i] = trib[i-1] + trib[i-2] + trib[i-3]

        return trib[n]


# Solution 1-1: DP with constant space
# Time: O(N) | Space: O(1)
class Solution:
    def tribonacci(self, n: int) -> int:
        trib1, trib2, trib3 = 0, 1, 1
        if n == 0:
            return trib1
        if n == 1 or n == 2:
            return trib2

        for i in range(3, n+1):
            trib = trib1 + trib2 + trib3
            trib1 = trib2
            trib2 = trib3
            trib3 = trib

        return trib3
