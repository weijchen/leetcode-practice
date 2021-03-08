"""
9. Palindrome Number
- Easy
- Math
- Link: https://leetcode.com/problems/palindrome-number/
"""


# Time: O(log(x))
# Space: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        revInt = 0
        tmpX = x
        while tmpX != 0:
            revInt *= 10
            tmpX, remain = tmpX // 10, tmpX % 10
            revInt += remain

        return x-revInt == 0
