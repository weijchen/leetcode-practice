"""
7. Reverse Integer
- Easy
- Math
- Link: https://leetcode.com/problems/reverse-integer/
"""

# Time: O(log(x)) -> roughly log_10(x) digits in x
# Space: O(1)
class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        if neg:
            x = -x

        revInt = 0
        while x != 0:
            revInt *= 10
            x, remain = x // 10,  x % 10
            revInt += remain

        if neg:
            revInt *= -1

        return revInt if revInt >= -pow(2, 31) and revInt <= pow(2, 31)-1 else 0
