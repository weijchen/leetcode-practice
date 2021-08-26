"""
10. Regular Expression Matching
- 難度：Hard
- 狀態：N
- 考點：String, DP, Recursion
- Link：https://leetcode.com/problems/regular-expression-matching/
- 偏好公司 (>= 15)：
- 思路：
"""


# Solution 1: Recursion
# Time: O()
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.isReg(s, p)

    def isReg(self, s, p):
        # base case
        # 1. when the p is empty
        # 2. checkout whether s is empty
        # if both 1 and 2 -> traverse all of the string
        # if not -> can not find the pattern in the string
        if not p:
            return not s

        # whether string still exist and the first element of the pattern is the first element of the string or the dot symbol
        first_match = s and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            # empty the first string in the pattern
            # or, reuse the first string in the pattern
            return (self.isReg(s, p[2:]) or first_match and self.isReg(s[1:], p))
        else:
            return first_match and self.isReg(s[1:], p[1:])
