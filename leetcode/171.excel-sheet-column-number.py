#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
# Solution 1: Reverse -> Math
# Time: O(N) | Space: O(1)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        curNum = 0
        for idx, char in enumerate(columnTitle[::-1]):
            toAdd = ord(char)-64
            curNum += toAdd * 26**idx
        return curNum
# @lc code=end

