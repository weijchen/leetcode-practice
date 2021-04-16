"""
28. Implement strStr()
- Easy
- String, Two Pointers
- Link: https://leetcode.com/problems/implement-strstr/
"""


# Time: O(n*m), where n is the length of haystack and m is the length of needle | Space: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or haystack == needle:
            return 0
        lengthToMatch = len(needle)

        for i in range(len(haystack) - lengthToMatch+1):  # n
            if haystack[i: i+lengthToMatch] == needle:    # m
                return i
        return -1
