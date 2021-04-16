"""
58. Length of Last Word
- Easy
- String
- Link: https://leetcode.com/problems/length-of-last-word/
"""


# Approach 1: Trim
# Time: O(n) | Space: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(self.trim(s).split(' ')[-1])
    
    def trim(self, s: str) -> str:
        l = 0
        r = len(s)-1
        while (l < r) and (s[l] == " " or s[r] == " "):
            if s[l] == " ":
                l += 1
            elif s[r] == " ":
                r -= 1
        return s[l:r+1]


# Approach 2: One-loop Iteration
# Time: O(n) | Space: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p, length = len(s), 0

        while p > 0:
            p -= 1
            # we're in the middle of the last word
            if s[p] != ' ':
                length += 1
            # here is the end of last word
            elif length > 0:
                return length

        return length
