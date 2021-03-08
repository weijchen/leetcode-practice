"""
13. Roman to Integer
- Easy
- Math, String
- Link: https://leetcode.com/problems/roman-to-integer/
"""

# Time: O(1) -> since the question gives a finite set of roman numerals, the time complexity is O(1)
# Space: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        mapTable = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        p = 0
        while p < len(s):
            oneStr, twoStr = s[p: p + 1], s[p: p + 2]
            if twoStr in mapTable.keys():
                ret += mapTable[twoStr]
                p += 2
            else:
                ret += mapTable[oneStr]
                p += 1

        return ret
