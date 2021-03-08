"""
125. Valid Palindrome
- Easy
- Two Pointers, String
- Link: https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        p, q = 0, l-1

        while p < q:

            if not s[p].isalnum() or not s[q].isalnum():
                if not s[p].isalnum():
                    p += 1
                if not s[q].isalnum():
                    q -= 1
            else:
                if s[p].lower() != s[q].lower():
                    return False
                else:
                    p += 1
                    q -= 1

        return True
