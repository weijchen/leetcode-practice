"""
12. Interger to Roman
- Medium
- Math, String
- Link: https://leetcode.com/problems/integer-to-roman/
"""


# Time: O(N)
# Space: O(N)
class Solution:
    def intToRoman(self, num: int) -> str:
        ret = [""] * 4
        numOfK, remain = num // 1000, num % 1000
        for _ in range(numOfK):
            ret[0] += "M"

        ret[1] = self.digitToRoman(remain, 100, "C", "M", "D")
        remain %= 100
        ret[2] = self.digitToRoman(remain, 10, "X", "C", "L")
        remain %= 10
        ret[3] = self.digitToRoman(remain, 1, "I", "X", "V")

        return "".join(ret)

    def digitToRoman(self, num, div, symbol1, symbol2, symbol3) -> str:
        ret = ""
        full, remain = num // div, num % div
        if full == 9:
            ret = "{}{}".format(symbol1, symbol2)
        else:
            toF, notF = full // 5, full % 5
            if notF == 4:
                ret += "{}{}".format(symbol1, symbol3)
            else:
                for _ in range(toF):
                    ret += "{}".format(symbol3)
                for _ in range(notF):
                    ret += "{}".format(symbol1)
        return ret
