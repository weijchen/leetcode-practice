"""
415. Add Strings
- Easy
- String
- Link: https://leetcode.com/problems/add-strings/
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        num1_int = self.toInt(num1)
        num2_int = self.toInt(num2)
        ret = 0
        
        if num1_int == "" and num2_int == "": return ""
        if num1_int: ret += num1_int
        if num2_int: ret += num2_int
            
        return "{}".format(ret)
        
    def toInt(self, ipt: str):
        if len(ipt) == 0: return ""
        base = ord("0")
        val = 0
        multiplier = 1
        while ipt:
            ipt, remain = ipt[:-1], ipt[-1]
            val += (ord(remain) - base) * multiplier
            multiplier *= 10
        return val
        