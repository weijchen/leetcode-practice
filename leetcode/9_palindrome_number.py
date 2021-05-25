"""
9. Palindrome Number
- Easy
- Math
- Link: https://leetcode.com/problems/palindrome-number/
"""


# Reverse half of the number
# Time: O(log(x)) | Space: O(1)
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


# Solution 2: array check palindrome
# Time: O(N) | Space: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_str, x_length = str(x), len(str(x))

        for i in range(x_length // 2 + 1):
            if x_str[i] != x_str[x_length - i - 1]:
                return False
        return True
