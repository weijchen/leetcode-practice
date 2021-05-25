#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
# Solution 1: Math
# Time: O(log(2^31)_26) | Space: O(1)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 26:
            columnNumber, curCol = columnNumber // 26, columnNumber % 26
            if curCol == 0:
                columnNumber -= 1
                curCol = 26
            ans = chr(curCol + 64) + ans
        ans = chr(columnNumber + 64) + ans
        return ans
# @lc code=end

