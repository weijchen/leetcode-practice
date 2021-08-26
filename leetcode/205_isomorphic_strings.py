"""
205. Isomorphic Strings
- Easy
- Hash Table, String
- Link: https://leetcode.com/problems/isomorphic-strings/
"""


# Solution 1: Hash Table
# Time: O(N) | Space: O(N), where N is the length of s and t -> O(1) since N is fixed to 26 characters
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if c1 not in s2t:
                s2t[c1] = c2
            else:
                if c2 != s2t[c1]:
                    return False

            if c2 not in t2s:
                t2s[c2] = c1
            else:
                if c1 != t2s[c2]:
                    return False
        return True
