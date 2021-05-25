"""
202. Happy Number
- Easy
- Hash Table, Math
- Link: https://leetcode.com/problems/happy-number/
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        curNum = str(n)
        seen = set()

        while curNum != '1':
            tmpNum = str(sum([pow(int(n_str), 2) for n_str in curNum]))
            curNum = tmpNum
            if curNum in seen:
                return False
            seen.add(curNum)
        return True
