"""
20. Valid Parentheses
- Easy
- String, Stack
- Link: https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        closing = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for _ in s:
            if _ in closing.keys():
                # error handler
                if len(st) == 0: return False
                toPair = st.pop(-1)
                if toPair != closing[_]: return False
            else:
                st.append(_)
        
        return len(st) == 0 and True
