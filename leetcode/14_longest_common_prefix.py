"""
14 Longest Common Prefix
- Easy
- String
- Link: https://leetcode.com/problems/longest-common-prefix/
"""


# Approach 1: Vertical scanning
# Time: O(S), where S is the sum of all characters in all strings | Space: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if len(strs) == 0:
            return ans
        tmpAns = strs[0]

        for i in range(len(tmpAns) + 1):
            for e in strs[1:]:
                if e[:i] != tmpAns[:i]:
                    return ans
            ans = tmpAns[:i]

        return ans
