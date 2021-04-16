"""
43. Multyply Strings
- Medium
- Math, String
- Link: https://leetcode.com/problems/multiply-strings/
"""


# Time: O(n) | Space: O(1)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.toInt(num1) * self.toInt(num2))

    def toInt(self, num: str) -> int:
        int_num = 0
        for char in num:
            int_num *= 10
            int_num += ord(char) - ord('0')

        return int_num
